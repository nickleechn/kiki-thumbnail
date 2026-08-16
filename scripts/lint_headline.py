#!/usr/bin/env python3
"""Lint thumbnail headlines for length, filler, contrast, and palette rules."""

from __future__ import annotations
import argparse
import re
import sys

BANNED_PHRASES = [
    "my new video",
    "you need this",
    "like and subscribe",
    "click here",
]

def check_length(text: str) -> list[str]:
    issues: list[str] = []
    # Count words (Latin) or characters (CJK)
    cjk = any(0x4E00 <= ord(c) <= 0x9FFF for c in text)
    if cjk:
        chars = len(text.replace(" ", "").replace("\n", ""))
        if chars < 4 or chars > 10:
            issues.append(f"CJK length {chars} chars — target 4–10 (text: {text!r})")
    else:
        words = [w for w in re.split(r"\s+", text.strip()) if w]
        n = len(words)
        if n < 2 or n > 5:
            issues.append(f"Word count {n} — prefer 2–5 words (target 2–4): {text!r}")
        if " and " in text.lower() or " & " in text:
            issues.append("Avoid conjunctions like 'and'/'&' in thumbnail hooks")
    if len(text) > 40:
        issues.append("Headline likely too long for phone legibility (>40 chars)")
    return issues

def check_filler(text: str) -> list[str]:
    low = text.lower()
    issues: list[str] = []
    for phrase in BANNED_PHRASES:
        if phrase in low:
            issues.append(f"Avoid vague filler: {phrase!r}")
    if text.strip().endswith(".") and text.count(".") > 1:
        issues.append("Keep punctuation minimal — at most one period")
    if re.search(r"[.!?]{2,}", text):
        issues.append("Avoid repeated punctuation (!! / ??)")
    return issues

def hex_to_rgb(h: str) -> tuple[int,int,int]:
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c*2 for c in h)
    return int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)

def luminance(rgb: tuple[int,int,int]) -> float:
    def lin(c: int) -> float:
        c = c/255
        return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
    r,g,b = rgb
    return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)

def contrast_ratio(a: str, b: str) -> float:
    la, lb = luminance(hex_to_rgb(a)), luminance(hex_to_rgb(b))
    lighter, darker = max(la,lb), min(la,lb)
    return (lighter+0.05)/(darker+0.05)

def main() -> int:
    p = argparse.ArgumentParser(description="Lint thumbnail headlines and colors")
    p.add_argument("--text", help="Headline to lint")
    p.add_argument("--check-contrast", nargs=2, metavar=("FG","BG"), help="Check WCAG contrast between two hex colors")
    p.add_argument("--palette", choices=["soft-sand","light-steel","blue-serenity","soft-lavender","midnight-ink"], help="Validate palette name")
    args = p.parse_args()

    ok = True
    if args.check_contrast:
        fg, bg = args.check_contrast
        try:
            ratio = contrast_ratio(fg, bg)
            status = "PASS" if ratio >= 4.5 else "FAIL"
            print(f"Contrast {fg} on {bg}: {ratio:.2f}:1 — {status} (WCAG AA needs ≥4.5:1)")
            if ratio < 4.5:
                ok = False
                print("  Hint: try #FFFFFF on #1A222C, or add --overlay 0.42 in render_thumbnail.py")
        except Exception as e:
            print(f"Invalid hex: {e}")
            ok = False

    if args.text is not None:
        issues = check_length(args.text) + check_filler(args.text)
        if issues:
            print(f"Headline: {args.text!r}")
            for iss in issues:
                print(f"  ⚠ {iss}")
            ok = False
        else:
            print(f"Headline OK: {args.text!r} — 2–5 words, no filler detected")

    if not args.text and not args.check_contrast and not args.palette:
        p.print_help()
        return 2

    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
