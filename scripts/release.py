#!/usr/bin/env python3
"""Build a fresh working-tree snapshot; publish only that completed, reviewed run.
Uses Python's standard library, Quarto, XeLaTeX/Noto CJK and Poppler.
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
BOOKS = ['convex-optimization-toolbox', 'advanced-optimization-toolbox',
         'stochastic-processes-toolbox', 'probability-statistics']
SKIP = {'.git', '.quarto', '_book', '_pdf', '_draft', '.release-build',
        '_freeze', '__pycache__', 'site_libs'}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def sources():
    result = {}
    for path in (ROOT / 'mathematical-foundations').rglob('*'):
        rel = path.relative_to(ROOT)
        if not path.is_file() or any(part in SKIP for part in rel.parts):
            continue
        if 'Zone.Identifier' in path.name or path.suffix in {'.zip', '.pdf', '.html', '.aux', '.log', '.out', '.toc'}:
            continue
        if path.suffix == '.tex' and 'tex' not in rel.parts:
            continue
        result[str(rel)] = sha(path)
    return result

def command(args, cwd, log):
    with log.open('w') as stream:
        subprocess.run(args, cwd=cwd, stdout=stream, stderr=subprocess.STDOUT, check=True)

def check_pdf(pdf, log):
    text = subprocess.check_output(['pdftotext', str(pdf), '-'], text=True)
    fonts = subprocess.check_output(['pdffonts', str(pdf)], text=True)
    info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
    if len(re.findall(r'[\u4e00-\u9fff]', text)) < 100:
        raise RuntimeError(f'Chinese text extraction failed: {pdf}')
    cjk = [line for line in fonts.splitlines() if 'CJK' in line]
    if not cjk or any(not re.search(r'\byes\s+(?:yes|no)\s+yes\b', line) for line in cjk):
        raise RuntimeError(f'CJK font embedding/Unicode mapping failed: {pdf}')
    texlog = pdf.parent.parent / 'index.log'
    logs = log.read_text() + (texlog.read_text(errors='replace') if texlog.exists() else '')
    if re.search(r'Missing character|undefined references|Reference .* undefined|Unable to resolve crossref|ERROR:', logs, re.I):
        raise RuntimeError(f'Readability error in {log}')
    return {'sha256': sha(pdf), 'pages': int(re.search(r'Pages:\s+(\d+)', info)[1])}

def build():
    base = ROOT / '.release-build'
    base.mkdir(exist_ok=True)
    run = Path(tempfile.mkdtemp(prefix='run-', dir=base))
    snapshot = run / 'source'
    initial = sources()
    for rel in initial:
        dest = snapshot / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, dest)
    manifest = {'sources': initial, 'books': {}, 'quarto': subprocess.check_output(['quarto', '--version'], text=True).strip()}
    print(f'Fresh build: {run}', flush=True)
    for name in BOOKS:
        project = snapshot / 'mathematical-foundations' / name
        # Deliberately exercise the default PDF configuration without a profile.
        for fmt, out in [('pdf', '_pdf'), ('html', '_book')]:
            print(f'{name}: {fmt}', flush=True)
            command(['quarto', 'render', '--to', fmt, '--output-dir', out, '--debug'], project, run / f'{name}-{fmt}.log')
        output = 'probability-statistics-notes' if name == 'probability-statistics' else name
        pdf = project / '_pdf' / f'{output}.pdf'
        result = check_pdf(pdf, run / f'{name}-pdf.log')
        result['artifact'] = str(pdf.relative_to(run))
        result['destination'] = ('mathematical-foundations/probability-statistics/probability-statistics-notes.pdf'
                                 if name == 'probability-statistics' else f'pdfs/{name}.pdf')
        manifest['books'][name] = result
    if sources() != initial:
        raise RuntimeError('Sources changed during build; start a new run before publishing.')
    (run / 'complete.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    print(f'Build complete. Inspect pages/logs, then: python3 scripts/release.py --publish {run}', flush=True)

def publish(run):
    run = run.resolve()
    manifest = json.loads((run / 'complete.json').read_text())
    if set(manifest['books']) != set(BOOKS) or sources() != manifest['sources']:
        raise RuntimeError('Incomplete build or changed source snapshot; rebuild first.')
    # Validate all four before replacing any published file.
    for name, entry in manifest['books'].items():
        pdf = (run / entry['artifact']).resolve()
        if not pdf.is_relative_to(run):
            raise RuntimeError('Artifact outside build directory')
        if check_pdf(pdf, run / f'{name}-pdf.log')['sha256'] != entry['sha256']:
            raise RuntimeError(f'Artifact changed: {pdf}')
        expected = ('mathematical-foundations/probability-statistics/probability-statistics-notes.pdf'
                    if name == 'probability-statistics' else f'pdfs/{name}.pdf')
        if entry['destination'] != expected:
            raise RuntimeError('Unexpected publication path')
    for entry in manifest['books'].values():
        dest = ROOT / entry['destination']
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists() or sha(dest) != entry['sha256']:
            with tempfile.NamedTemporaryFile(dir=dest.parent, suffix='.tmp', delete=False) as stream:
                tmp = Path(stream.name)
                stream.write((run / entry['artifact']).read_bytes())
            os.replace(tmp, dest)
        assert sha(dest) == entry['sha256']
        print(f'{entry["pages"]} pages  {entry["sha256"]}  {entry["destination"]}')
    (ROOT / 'pdfs' / 'manifest.json').write_text(json.dumps({
        'quarto': manifest['quarto'], 'sources': manifest['sources'],
        'books': {k: {x: v[x] for x in ('destination', 'sha256', 'pages')} for k, v in manifest['books'].items()}
    }, ensure_ascii=False, indent=2) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publish', type=Path, help='Copy PDFs from a completed run AFTER visual review')
    args = parser.parse_args()
    publish(args.publish) if args.publish else build()
