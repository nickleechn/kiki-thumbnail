#!/usr/bin/env python3
"""Deterministically produce YouTube 16:9 and Rednote 4:3 thumbnails."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:
    raise SystemExit(
        "Pillow is required. Install it with: python3 -m pip install -r requirements.txt"
    ) from exc


LAYOUTS = ("left", "right", "top", "bottom", "center")
EXPECTED_SIZES = {
    "youtube": (1280, 720),
    "rednote": (1200, 900),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create two exact-size thumbnails from one base image: "
            "YouTube 1280x720 and Rednote 1200x900."
        )
    )
    parser.add_argument("--input", required=True, type=Path, help="Generated master image")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--stem", required=True, help="Output filename stem")
    parser.add_argument("--text", required=True, help="YouTube headline")
    parser.add_argument("--rednote-text", help="Optional Rednote headline; defaults to --text")
    parser.add_argument("--layout", choices=LAYOUTS, default="left", help="Default text layout")
    parser.add_argument("--rednote-layout", choices=LAYOUTS, help="Optional 4:3 text layout override")
    parser.add_argument(
        "--align",
        choices=("auto", "left", "center", "right"),
        default="auto",
    )
    parser.add_argument("--font-style", choices=("sans", "serif"), default="sans")
    parser.add_argument("--font", type=Path, help="Optional .ttf/.otf font path")
    parser.add_argument("--font-size", type=int, default=0)
    parser.add_argument("--text-color", default="#FFFFFF")
    parser.add_argument("--stroke-color", default="#111111")
    parser.add_argument("--stroke-width", type=int, default=4)
    parser.add_argument("--highlight", action="append", default=[])
    parser.add_argument("--highlight-color", default="#F20D0D")
    parser.add_argument("--highlight-text-color", default="#FFFFFF")
    parser.add_argument("--overlay", type=float, default=0.42)
    parser.add_argument("--margin", type=int, default=56)
    parser.add_argument("--focus-x", type=float, default=0.5)
    parser.add_argument("--focus-y", type=float, default=0.5)
    parser.add_argument("--rednote-focus-x", type=float)
    parser.add_argument("--rednote-focus-y", type=float)
    parser.add_argument("--format", choices=("png", "jpg"), default="png")
    parser.add_argument("--quality", type=int, default=94)
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing output pair",
    )
    return parser.parse_args()


def build_command(
    args: argparse.Namespace,
    renderer: Path,
    preset: str,
    output: Path,
) -> list[str]:
    is_rednote = preset == "rednote"
    text = args.rednote_text if is_rednote and args.rednote_text else args.text
    layout = args.rednote_layout if is_rednote and args.rednote_layout else args.layout
    focus_x = args.rednote_focus_x if is_rednote and args.rednote_focus_x is not None else args.focus_x
    focus_y = args.rednote_focus_y if is_rednote and args.rednote_focus_y is not None else args.focus_y
    command = [
        sys.executable,
        str(renderer),
        "--input",
        str(args.input),
        "--output",
        str(output),
        "--preset",
        preset,
        "--text",
        text,
        "--layout",
        layout,
        "--align",
        args.align,
        "--font-style",
        args.font_style,
        "--font-size",
        str(args.font_size),
        "--text-color",
        args.text_color,
        "--stroke-color",
        args.stroke_color,
        "--stroke-width",
        str(args.stroke_width),
        "--highlight-color",
        args.highlight_color,
        "--highlight-text-color",
        args.highlight_text_color,
        "--overlay",
        str(args.overlay),
        "--margin",
        str(args.margin),
        "--focus-x",
        str(focus_x),
        "--focus-y",
        str(focus_y),
        "--quality",
        str(args.quality),
    ]
    if args.font:
        command.extend(("--font", str(args.font)))
    for word in args.highlight:
        command.extend(("--highlight", word))
    return command


def main() -> int:
    args = parse_args()
    if not args.input.is_file():
        raise SystemExit(f"Input image not found: {args.input}")
    if not args.stem.strip() or Path(args.stem).name != args.stem:
        raise SystemExit("--stem must be a non-empty filename stem without directories")
    renderer = Path(__file__).with_name("render_thumbnail.py")
    if not renderer.is_file():
        raise SystemExit(f"Renderer not found: {renderer}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "youtube": args.output_dir / f"{args.stem}-youtube.{args.format}",
        "rednote": args.output_dir / f"{args.stem}-rednote.{args.format}",
    }
    existing = [str(output) for output in outputs.values() if output.exists()]
    if existing and not args.overwrite:
        joined = "\n  ".join(existing)
        raise SystemExit(f"Output already exists; pass --overwrite to replace it:\n  {joined}")

    with tempfile.TemporaryDirectory(prefix=".kiki-pair-", dir=args.output_dir) as temp_dir:
        temp_root = Path(temp_dir)
        staged = {
            preset: temp_root / output.name
            for preset, output in outputs.items()
        }
        for preset, output in staged.items():
            subprocess.run(
                build_command(args, renderer, preset, output),
                check=True,
            )
        for preset, output in staged.items():
            with Image.open(output) as image:
                if image.size != EXPECTED_SIZES[preset]:
                    raise SystemExit(
                        f"Unexpected {preset} dimensions: {image.size}; "
                        f"expected {EXPECTED_SIZES[preset]}"
                    )
        for preset, output in outputs.items():
            staged[preset].replace(output)

    print("Created thumbnail pair:")
    print(f"  YouTube 16:9: {outputs['youtube']}")
    print(f"  Rednote 4:3:  {outputs['rednote']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
