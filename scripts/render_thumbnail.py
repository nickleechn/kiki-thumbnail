#!/usr/bin/env python3
"""Crop a base image to a platform preset and render exact thumbnail text."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from PIL import Image, ImageColor, ImageDraw, ImageFont
except ImportError as exc:
    raise SystemExit(
        "Pillow is required. Install it with: python3 -m pip install -r requirements.txt"
    ) from exc


PRESETS = {
    "youtube": (1280, 720),
    "rednote": (1080, 1440),
}
FONT_CANDIDATES = {
    "sans": [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
    ],
    "serif": [
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
        "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf",
    ],
}
CJK_FONT_CANDIDATES = {
    "sans": [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    ],
    "serif": [
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc",
        "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create an exact-text thumbnail using a deterministic platform preset."
    )
    parser.add_argument("--input", required=True, type=Path, help="Base image path")
    parser.add_argument("--output", required=True, type=Path, help="PNG or JPEG output path")
    parser.add_argument(
        "--preset",
        choices=tuple(PRESETS),
        default="youtube",
        help="youtube=1280x720; rednote=1080x1440 portrait",
    )
    parser.add_argument("--text", required=True, help="Headline text; use \\n for forced breaks")
    parser.add_argument(
        "--layout",
        choices=("left", "right", "top", "bottom", "center"),
        default="left",
        help="Headline region",
    )
    parser.add_argument(
        "--align",
        choices=("auto", "left", "center", "right"),
        default="auto",
        help="Text alignment inside the headline region",
    )
    parser.add_argument("--font-style", choices=("sans", "serif"), default="sans")
    parser.add_argument("--font", type=Path, help="Optional .ttf/.otf font path")
    parser.add_argument("--font-size", type=int, default=0, help="0 chooses the largest fitting size")
    parser.add_argument("--text-color", default="#FFFFFF")
    parser.add_argument("--stroke-color", default="#111111")
    parser.add_argument("--stroke-width", type=int, default=4)
    parser.add_argument(
        "--highlight",
        action="append",
        default=[],
        help="Word to place in a color box; repeat for multiple words",
    )
    parser.add_argument("--highlight-color", default="#F20D0D")
    parser.add_argument("--highlight-text-color", default="#FFFFFF")
    parser.add_argument("--overlay", type=float, default=0.42, help="Directional black overlay, 0 to 0.85")
    parser.add_argument("--margin", type=int, default=56)
    parser.add_argument("--focus-x", type=float, default=0.5, help="Horizontal crop focus, 0 to 1")
    parser.add_argument("--focus-y", type=float, default=0.5, help="Vertical crop focus, 0 to 1")
    parser.add_argument("--quality", type=int, default=94, help="JPEG quality")
    return parser.parse_args()


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def cover_crop(
    image: Image.Image,
    canvas: tuple[int, int],
    focus_x: float,
    focus_y: float,
) -> Image.Image:
    target_w, target_h = canvas
    scale = max(target_w / image.width, target_h / image.height)
    resized = image.resize(
        (round(image.width * scale), round(image.height * scale)),
        Image.Resampling.LANCZOS,
    )
    extra_x = resized.width - target_w
    extra_y = resized.height - target_h
    left = round(extra_x * clamp(focus_x, 0.0, 1.0))
    top = round(extra_y * clamp(focus_y, 0.0, 1.0))
    return resized.crop((left, top, left + target_w, top + target_h)).convert("RGBA")


def add_overlay(image: Image.Image, layout: str, strength: float) -> Image.Image:
    strength = clamp(strength, 0.0, 0.85)
    if strength == 0:
        return image
    width, height = image.size
    alpha = Image.new("L", image.size)
    pixels = alpha.load()
    peak = round(255 * strength)
    for y in range(height):
        for x in range(width):
            if layout == "left":
                factor = clamp(1 - x / (width * 0.68), 0, 1)
            elif layout == "right":
                factor = clamp((x - width * 0.32) / (width * 0.68), 0, 1)
            elif layout == "top":
                factor = clamp(1 - y / (height * 0.62), 0, 1)
            elif layout == "bottom":
                factor = clamp((y - height * 0.38) / (height * 0.62), 0, 1)
            else:
                factor = 0.55
            pixels[x, y] = round(peak * factor)
    shade = Image.new("RGBA", image.size, (0, 0, 0, 0))
    shade.putalpha(alpha)
    return Image.alpha_composite(image, shade)


def contains_cjk(text: str) -> bool:
    ranges = (
        (0x3040, 0x30FF),
        (0x3400, 0x4DBF),
        (0x4E00, 0x9FFF),
        (0xAC00, 0xD7AF),
        (0xF900, 0xFAFF),
    )
    return any(any(start <= ord(char) <= end for start, end in ranges) for char in text)


def find_font(
    style: str,
    custom: Path | None,
    size: int,
    text: str,
) -> ImageFont.FreeTypeFont:
    if custom:
        candidates = [str(custom)]
    elif contains_cjk(text):
        candidates = CJK_FONT_CANDIDATES[style] + FONT_CANDIDATES[style]
    else:
        candidates = FONT_CANDIDATES[style]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    raise SystemExit("No suitable font found. Pass a font file with --font /path/to/font.ttf")


def normalize_token(token: str) -> str:
    return re.sub(r"[^\w'-]", "", token, flags=re.UNICODE).casefold()


def line_width(draw: ImageDraw.ImageDraw, words: list[str], font: ImageFont.FreeTypeFont) -> float:
    if not words:
        return 0
    return sum(draw.textlength(word, font=font) for word in words) + draw.textlength(" ", font=font) * (len(words) - 1)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[list[str]]:
    lines: list[list[str]] = []
    for paragraph in text.replace("\\n", "\n").splitlines() or [""]:
        words = paragraph.split()
        if not words:
            lines.append([])
            continue
        current: list[str] = []
        for word in words:
            candidate = current + [word]
            if current and line_width(draw, candidate, font) > max_width:
                lines.append(current)
                current = [word]
            else:
                current = candidate
        lines.append(current)
    return lines


def text_region(
    layout: str,
    margin: int,
    canvas: tuple[int, int],
) -> tuple[int, int, int, int]:
    width, height = canvas
    if layout == "left":
        return margin, margin, round(width * 0.48) - margin, height - 2 * margin
    if layout == "right":
        x = round(width * 0.52)
        return x, margin, width - x - margin, height - 2 * margin
    if layout == "top":
        return margin, margin, width - 2 * margin, round(height * 0.46) - margin
    if layout == "bottom":
        y = round(height * 0.54)
        return margin, y, width - 2 * margin, height - y - margin
    return margin, margin, width - 2 * margin, height - 2 * margin


def fit_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    style: str,
    custom_font: Path | None,
    max_width: int,
    max_height: int,
    requested_size: int,
) -> tuple[ImageFont.FreeTypeFont, list[list[str]], int]:
    sizes = [requested_size] if requested_size > 0 else list(range(132, 43, -2))
    for size in sizes:
        font = find_font(style, custom_font, size, text)
        lines = wrap_text(draw, text, font, max_width)
        bbox = draw.textbbox((0, 0), "Ag", font=font, stroke_width=0)
        line_height = bbox[3] - bbox[1]
        gap = max(8, round(size * 0.12))
        total_height = len(lines) * line_height + max(0, len(lines) - 1) * gap
        if total_height <= max_height and all(line_width(draw, line, font) <= max_width for line in lines):
            return font, lines, gap
    raise SystemExit("Headline does not fit. Shorten --text, choose another layout, or reduce --font-size.")


def draw_headline(image: Image.Image, args: argparse.Namespace) -> None:
    draw = ImageDraw.Draw(image)
    region_x, region_y, region_w, region_h = text_region(
        args.layout,
        args.margin,
        image.size,
    )
    font, lines, line_gap = fit_text(
        draw,
        args.text,
        args.font_style,
        args.font,
        region_w,
        region_h,
        args.font_size,
    )
    bbox = draw.textbbox((0, 0), "Ag", font=font, stroke_width=0)
    line_height = bbox[3] - bbox[1]
    total_height = len(lines) * line_height + max(0, len(lines) - 1) * line_gap
    if args.layout == "top":
        y = region_y
    elif args.layout == "bottom":
        y = region_y + region_h - total_height
    else:
        y = region_y + (region_h - total_height) / 2

    align = args.align
    if align == "auto":
        align = "center" if args.layout in ("top", "bottom", "center") else "left"
    highlighted = {normalize_token(word) for phrase in args.highlight for word in phrase.split()}
    text_color = ImageColor.getrgb(args.text_color)
    stroke_color = ImageColor.getrgb(args.stroke_color)
    highlight_color = ImageColor.getrgb(args.highlight_color)
    highlight_text_color = ImageColor.getrgb(args.highlight_text_color)
    space_width = draw.textlength(" ", font=font)

    for words in lines:
        width = line_width(draw, words, font)
        if align == "center":
            x = region_x + (region_w - width) / 2
        elif align == "right":
            x = region_x + region_w - width
        else:
            x = region_x
        for word in words:
            word_width = draw.textlength(word, font=font)
            is_highlighted = normalize_token(word) in highlighted
            if is_highlighted:
                pad_x = max(10, round(font.size * 0.10))
                pad_y = max(6, round(font.size * 0.05))
                draw.rounded_rectangle(
                    (x - pad_x, y - pad_y, x + word_width + pad_x, y + line_height + pad_y),
                    radius=max(8, round(font.size * 0.08)),
                    fill=highlight_color,
                )
            color = highlight_text_color if is_highlighted else text_color
            draw.text(
                (x, y - bbox[1]),
                word,
                font=font,
                fill=color,
                stroke_width=args.stroke_width if not is_highlighted else 0,
                stroke_fill=stroke_color,
            )
            x += word_width + space_width
        y += line_height + line_gap


def save_image(image: Image.Image, output: Path, quality: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    suffix = output.suffix.lower()
    if suffix in (".jpg", ".jpeg"):
        image.convert("RGB").save(output, quality=round(clamp(quality, 1, 100)), optimize=True)
    elif suffix == ".png":
        image.save(output, optimize=True)
    else:
        raise SystemExit("Output must end in .png, .jpg, or .jpeg")


def main() -> int:
    args = parse_args()
    canvas = PRESETS[args.preset]
    if not args.input.is_file():
        raise SystemExit(f"Input image not found: {args.input}")
    max_margin = min(canvas) // 3 - 1
    if args.margin < 0 or args.margin > max_margin:
        raise SystemExit(f"--margin must be between 0 and {max_margin}")
    base = cover_crop(Image.open(args.input), canvas, args.focus_x, args.focus_y)
    base = add_overlay(base, args.layout, args.overlay)
    draw_headline(base, args)
    save_image(base, args.output, args.quality)
    print(f"Wrote {args.output} ({canvas[0]}x{canvas[1]}, {args.preset})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
