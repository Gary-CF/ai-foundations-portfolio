"""Build both formats without reusing format-specific cross-reference caches."""
from pathlib import Path
import os
import shutil
import subprocess

root = Path(__file__).resolve().parents[1]
quarto = os.environ.get('QUARTO_BIN', 'quarto')
for fmt in ['pdf', 'html']:
    shutil.rmtree(root / '.quarto', ignore_errors=True)
    for ext in ['aux', 'toc', 'out', 'lof', 'lot']:
        (root / ('index.' + ext)).unlink(missing_ok=True)
    cmd = [quarto, 'render', '--to', fmt]
    if fmt == 'pdf':
        cmd += ['--output-dir', '_pdf']
    subprocess.run(cmd, cwd=root, check=True)
