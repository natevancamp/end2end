# Assets

GitHub pushes from the agent go through a text-only API, so the binary logo files
are stored here as base64 text. `build.py` reads a real `.png` from the repo root
if one is present, and otherwise falls back to the matching `.b64` file here.

To turn these back into PNG files locally:

```bash
python3 - <<'PY'
import base64, pathlib
for p in pathlib.Path('assets').glob('*.b64'):
    pathlib.Path(p.stem).write_bytes(base64.b64decode(p.read_text()))
PY
```
