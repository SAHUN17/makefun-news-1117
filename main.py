#!/usr/bin/env python3
"""news-image-20261117 entry: publish the day's news poster to /output/entry.png.

The image is a committed asset (entry.png beside this file); this program checks
it against the bounty's limits and copies it where the judge reads it.
"""

import os
import shutil
from pathlib import Path

ENTRY_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def image_kind(data: bytes) -> str:
    """The bounty accepts a PNG or a JPEG under the name entry.png."""
    if data.startswith(PNG_MAGIC):
        return "png"
    if data.startswith(JPEG_MAGIC):
        return "jpeg"
    raise ValueError("entry.png is neither a PNG nor a JPEG by its first bytes")


def source_path() -> Path:
    """The bundled image that sits beside this program."""
    return Path(__file__).resolve().parent / ENTRY_NAME


def png_size(data: bytes) -> tuple[int, int]:
    """Width and height from the PNG's IHDR chunk, which follows the 8-byte magic."""
    if len(data) < 24:
        raise ValueError("PNG is shorter than its header")
    return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")


def check_source(path: Path) -> tuple[int, int]:
    """Refuse anything the scorer's gate would refuse, and report the image size."""
    if not path.is_file():
        raise FileNotFoundError(f"{path} is missing")
    data = path.read_bytes()
    kind = image_kind(data)
    width = height = 0
    if len(data) > MAX_BYTES:
        raise ValueError(f"{path} is {len(data)} bytes, over the {MAX_BYTES}-byte cap")
    if kind == "png":
        width, height = png_size(data)
        if width > MAX_SIDE or height > MAX_SIDE:
            raise ValueError(f"{path} is {width}x{height}, over the {MAX_SIDE}px cap")
    return width, height


def publish(out_dir: Path) -> Path:
    """Copy the image into the output directory and return the destination."""
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / ENTRY_NAME
    shutil.copyfile(source_path(), dest)
    if dest.read_bytes() != source_path().read_bytes():
        raise IOError(f"{dest} does not match the bundled image")
    return dest


def main() -> int:
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    width, height = check_source(source_path())
    dest = publish(out_dir)
    print(f"{dest} ({width}x{height}, {dest.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())