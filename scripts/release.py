#!/usr/bin/env python3
"""Build isolated Quarto books; publish verified PDFs after page review.
Python standard library only. No Git commit, push, or website deployment.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'scripts/books.json'
QUARTO = os.environ.get('QUARTO_BIN', 'quarto')
SKIP = {'.git', '.quarto', '_book', '_pdf', '_draft', '.release-build',
        '_freeze', '__pycache__', 'site_libs', 'preview', 'archive', '.venv', 'node_modules'}
GENERATED = {'.zip', '.html', '.aux', '.log', '.out', '.toc', '.lof', '.lot',
             '.fls', '.fdb_latexmk', '.quarto_ipynb'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inside(base, relative):
    p = Path(relative)
    target = (base / p).resolve()
    if p.is_absolute() or '..' in p.parts or not target.is_relative_to(base.resolve()):
        raise RuntimeError(f'Path outside project: {relative}')
    return target


def registry():
    rows = json.loads(REGISTRY.read_text())
    for key in ('id', 'path', 'destination'):
        values = [r[key] for r in rows]
        if len(values) != len(set(values)):
            raise RuntimeError(f'Duplicate book {key}')
    for r in rows:
        inside(ROOT, r['path']); inside(ROOT, r['destination'])
        if not re.fullmatch(r'[a-z0-9-]+', r['id']):
            raise RuntimeError('Invalid book id')
        if Path(r['output']).name != r['output'] or not r['output'].endswith('.pdf'):
            raise RuntimeError('Invalid PDF output name')
    return rows


def sources(rows):
    result = {}
    for row in rows:
        project = inside(ROOT, row['path'])
        for p in sorted(project.rglob('*')):
            rel = p.relative_to(project)
            if not p.is_file() or any(x in SKIP for x in rel.parts):
                continue
            if p.is_symlink():
                raise RuntimeError(f'Symlink requires explicit handling: {p}')
            if 'Zone.Identifier' in p.name or p.suffix in GENERATED or p.name.endswith('.synctex.gz'):
                continue
            # Keep genuine PDF image assets; exclude old book PDFs at project root.
            if p.suffix == '.pdf' and len(rel.parts) == 1:
                continue
            if p.suffix == '.tex' and len(rel.parts) == 1:
                continue
            result[str(p.relative_to(ROOT))] = sha(p)
    for p in [REGISTRY, ROOT / 'scripts/release.py']:
        result[str(p.relative_to(ROOT))] = sha(p)
    return result


def preflight(rows):
    errors = []
    for row in rows:
        project = inside(ROOT, row['path'])
        config = project / '_quarto.yml'
        if not config.exists():
            errors.append(f'Missing {config}'); continue
        text = config.read_text()
        refs = re.findall(r'^\s*-\s+[\"\']?([^\n\"\']+\.qmd)[\"\']?\s*$', text, re.M)
        for ref in refs:
            if '*' not in ref and not inside(project, ref).is_file():
                errors.append(f'{row["id"]}: missing {ref}')
        m = re.search(r'^\s*output-file:\s*[\"\']?([^\n\"\']+)', text, re.M)
        output = m.group(1).strip() if m else ''
        if output.removesuffix('.pdf') + '.pdf' != row['output']:
            errors.append(f'{row["id"]}: output-file disagrees with books.json')
        if not (project / '_quarto-pdf.yml').exists():
            errors.append(f'{row["id"]}: missing PDF profile')
        qmds = [p for p in project.rglob('*.qmd') if not any(x in SKIP for x in p.relative_to(project).parts)]
        for p in qmds:
            for target in re.findall(r'!\[[^\]]*\]\(([^\s)]+)', p.read_text()):
                if '://' not in target and not (p.parent / target).exists():
                    errors.append(f'Missing image: {p.relative_to(ROOT)} -> {target}')
        print(f'{row["id"]}: {len(qmds)} QMD sources, {row["destination"]}')
    ledger = ROOT / 'machine-learning-foundations/deep-learning-statistical-learning-toolbox/source-ledger.json'
    if ledger.exists() and any('excerpt' in x for x in json.loads(ledger.read_text()).get('paragraphs', [])):
        errors.append('Public deep-learning ledger still contains transcript excerpts')
    if errors:
        raise RuntimeError('\n'.join(errors))
    print('Source/configuration preflight passed; this is not a render or page review.')


def command(args, cwd, log):
    with log.open('w') as stream:
        subprocess.run(args, cwd=cwd, stdout=stream, stderr=subprocess.STDOUT, check=True)


def check_log(path):
    text = path.read_text(errors='replace')
    if re.search(r'Missing character|undefined references|Reference .* undefined|Unable to resolve crossref|ERROR:', text, re.I):
        raise RuntimeError(f'Readability error: {path}')


def check_pdf(pdf, log):
    text = subprocess.check_output(['pdftotext', str(pdf), '-'], text=True)
    fonts = subprocess.check_output(['pdffonts', str(pdf)], text=True)
    info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
    if len(re.findall(r'[\u4e00-\u9fff]', text)) < 100:
        raise RuntimeError(f'Chinese text extraction failed: {pdf}')
    cjk = [line for line in fonts.splitlines()[2:] if re.search(r'CJK|Fandol', line, re.I)]
    flags = [re.search(r'\s+(yes|no)\s+(?:yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$', line) for line in cjk]
    if not cjk or any(not flag or flag[1] != 'yes' for flag in flags):
        raise RuntimeError(f'Chinese font embedding failed: {pdf}')
    explicit_unicode = all(flag[2] == 'yes' for flag in flags)
    if not explicit_unicode:
        # pdffonts uni=no means no explicit ToUnicode map, not failed extraction.
        print(f'NOTE: {pdf.name}: Chinese extraction passed, but some fonts have no explicit ToUnicode map; inspect copy/search in your PDF reader.')
    check_log(log)
    return {'sha256': sha(pdf), 'pages': int(re.search(r'Pages:\s+(\d+)', info)[1]),
            'explicit_cjk_unicode': explicit_unicode,
            'chinese_characters': len(re.findall(r'[\u4e00-\u9fff]', text))}


def build(rows, selected):
    preflight(rows)
    for tool in [QUARTO, 'pdftotext', 'pdffonts', 'pdfinfo']:
        if not shutil.which(tool):
            raise RuntimeError(f'Missing command: {tool}')
    base = ROOT / '.release-build'; base.mkdir(exist_ok=True)
    run = Path(tempfile.mkdtemp(prefix='run-', dir=base))
    initial = sources(rows)
    snapshot = run / 'source'
    for rel, digest in initial.items():
        dest = snapshot / rel; dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, dest)
        if sha(dest) != digest:
            raise RuntimeError('Sources changed while copying; rebuild.')
    manifest = {'schema': 2, 'sources': initial, 'books': {},
                'quarto': subprocess.check_output([QUARTO, '--version'], text=True).strip()}
    print(f'Fresh build: {run}', flush=True)
    for row in selected:
        name = row['id']
        # Separate copies prevent stale cross-reference and intermediate HTML reuse.
        for fmt, out in [('pdf', '_pdf'), ('html', '_book')]:
            project = run / 'work' / fmt / row['path']
            shutil.copytree(snapshot / row['path'], project)
            log = run / f'{name}-{fmt}.log'
            print(f'{name}: {fmt}', flush=True)
            command([QUARTO, 'render', '--to', fmt, '--output-dir', out, '--debug'], project, log)
            check_log(log)
            if fmt == 'pdf':
                for texlog in project.glob('*.log'):
                    check_log(texlog)
                pdf = project / out / row['output']
                result = check_pdf(pdf, log)
                result.update(artifact=str(pdf.relative_to(run)), destination=row['destination'])
            else:
                if not (project / out / 'index.html').exists():
                    raise RuntimeError(f'Missing HTML entry for {name}')
                result['html'] = str((project / out).relative_to(run))
        manifest['books'][name] = result
    if sources(rows) != initial:
        raise RuntimeError('Sources changed during build; rebuild.')
    (run / 'complete.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    if len(selected) == len(rows):
        print(f'Build complete. Review PDF pages and HTML, then:\npython3 scripts/release.py --publish {run}')
    else:
        print('Selected-book diagnostic build complete. Full seven-book build is required for --publish.')


def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, suffix='.tmp', delete=False) as stream:
        temp = Path(stream.name); stream.write(data)
    try:
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def publish(rows, run):
    run = run.resolve()
    if not run.is_relative_to((ROOT / '.release-build').resolve()):
        raise RuntimeError('Publish requires a run inside this repository .release-build/')
    manifest = json.loads((run / 'complete.json').read_text())
    expected = {r['id']: r for r in rows}
    if manifest.get('schema') != 2 or set(manifest['books']) != set(expected) or sources(rows) != manifest['sources']:
        raise RuntimeError('Incomplete/old build or changed sources; rebuild all seven books.')
    verified = []
    for name, entry in manifest['books'].items():
        if entry['destination'] != expected[name]['destination']:
            raise RuntimeError(f'Unexpected destination for {name}')
        pdf = inside(run, entry['artifact'])
        actual = check_pdf(pdf, run / f'{name}-pdf.log')
        if actual['sha256'] != entry['sha256'] or actual['pages'] != entry['pages']:
            raise RuntimeError(f'Artifact changed: {pdf}')
        verified.append((expected[name], entry, pdf.read_bytes()))
    # Validate ALL books before replacing ANY published PDF.
    for row, entry, data in verified:
        atomic_write(inside(ROOT, row['destination']), data)
        # Retain the old probability-statistics public URL as a compatibility copy.
        if row.get('legacy_destination'):
            atomic_write(inside(ROOT, row['legacy_destination']), data)
        print(f'{entry["pages"]} pages  {row["destination"]}')
    output = {'schema': 2, 'quarto': manifest['quarto'], 'sources': manifest['sources'],
              'books': {k: {x: v[x] for x in ('destination', 'sha256', 'pages', 'explicit_cjk_unicode', 'chinese_characters')} for k, v in manifest['books'].items()}}
    atomic_write(ROOT / 'pdfs/manifest.json', (json.dumps(output, ensure_ascii=False, indent=2) + '\n').encode())
    readme = ROOT / 'README.md'
    text = readme.read_text()
    for row in rows:
        marker = f'<!-- pdf:{row["id"]} -->'
        pattern = re.escape(marker) + r'.*?<!-- /pdf -->'
        text = re.sub(pattern, marker + f'[阅读]({row["destination"]})<!-- /pdf -->', text)
    atomic_write(readme, text.encode())
    print('Local PDFs, manifest and README updated. No commit, push or website deployment was performed.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true', help='Fast source/configuration checks; no rendering')
    mode.add_argument('--publish', type=Path, help='Publish a FULL completed run after visual review')
    parser.add_argument('--book', action='append', help='Build/check only this registry id; repeat as needed')
    args = parser.parse_args()
    rows = registry()
    wanted = set(args.book or [r['id'] for r in rows])
    unknown = wanted - {r['id'] for r in rows}
    if unknown: parser.error(f'Unknown book ids: {sorted(unknown)}')
    if args.publish and args.book: parser.error('--publish requires all books; omit --book')
    selected = [r for r in rows if r['id'] in wanted]
    if args.check: preflight(selected)
    elif args.publish: publish(rows, args.publish)
    else: build(rows, selected)


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, OSError, subprocess.CalledProcessError, ValueError) as exc:
        raise SystemExit(f'ERROR: {exc}')
