"""Quarto post-render: make KaTeX JS/CSS/fonts local and version-pinned."""
from pathlib import Path
import os
import shutil

ROOT = Path(__file__).resolve().parents[1]
output = Path(os.environ.get('QUARTO_PROJECT_OUTPUT_DIR', str(ROOT / '_book')))
if not output.is_absolute():
    output = ROOT / output
if (output / 'index.html').exists():
    target = output / 'site_libs' / 'katex-local'
    shutil.copytree(ROOT / 'vendor' / 'katex', target, dirs_exist_ok=True)
    count = 0
    for page in output.rglob('*.html'):
        content = page.read_text()
        relative = os.path.relpath(target, page.parent).replace(os.sep, '/')
        for asset in ['katex.min.js', 'katex.min.css']:
            content = content.replace('https://cdn.jsdelivr.net/npm/katex@latest/dist/' + asset,
                                      relative + '/' + asset)
        page.write_text(content)
        count += 1
    print(f'Local KaTeX assets ready for {count} HTML pages.')
