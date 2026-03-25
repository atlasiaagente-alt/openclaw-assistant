import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

WHISPER_EXE = r"C:\Users\Gustavo\AppData\Local\Python\pythoncore-3.14-64\Scripts\whisper.exe"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("media_path")
    parser.add_argument("--model", default="base")
    parser.add_argument("--language", default="es")
    args = parser.parse_args()

    media = Path(args.media_path)
    if not media.exists():
        print(f"media not found: {media}", file=sys.stderr)
        sys.exit(2)

    with tempfile.TemporaryDirectory(prefix="whisper-bridge-") as td:
        outdir = Path(td)
        cmd = [
            WHISPER_EXE,
            str(media),
            "--model", args.model,
            "--task", "transcribe",
            "--language", args.language,
            "--output_format", "txt",
            "--output_dir", str(outdir),
            "--fp16", "False",
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        txt_candidates = list(outdir.glob('*.txt'))
        txt_path = txt_candidates[0] if txt_candidates else (outdir / f"{media.stem}.txt")
        if proc.returncode != 0:
            err = (proc.stderr or proc.stdout or "whisper failed").strip()
            print(err, file=sys.stderr)
            sys.exit(proc.returncode)
        if not txt_path.exists():
            debug = '\n'.join([p.name for p in outdir.glob('*')]) or '(empty outdir)'
            print(f"transcript file not produced; outdir contents: {debug}", file=sys.stderr)
            sys.exit(3)
        text = txt_path.read_text(encoding="utf-8", errors="replace").strip()
        print(text)


if __name__ == "__main__":
    main()
