#!/usr/bin/env python3
# python rename_frames.py <source_dir> <dest_dir>
import sys, pathlib, shutil
src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(sys.argv[2])
dst.mkdir(parents=True, exist_ok=True)
# png/jpg のみを対象、mtime（古い→新しい）でソート
files = sorted([p for p in src.iterdir() if p.is_file() and p.suffix.lower() in ('.png','.jpg')], key=lambda p: p.stat().st_mtime)
for i, f in enumerate(files, start=1):
    dst_path = dst / f"frame{i:04d}{f.suffix.lower()}"
    shutil.copy2(f, dst_path)
    print(f"{f} -> {dst_path}")