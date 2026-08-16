# Recommended colour palettes

Use these muted palettes for thumbnail backgrounds, headline ink, and restrained highlights. The hex values are sampled from the supplied palette references.

## Selection rules

- Use one named palette per thumbnail.
- Use no more than three colours in the final composition: one light base, one dark ink, and one optional muted accent.
- Let the base occupy roughly 75–85% of the colour field. Keep the accent below roughly 10%.
- Prefer a solid base or a very soft gradient between adjacent swatches from the same palette.
- Keep saturation at or below these samples. Do not brighten them into neon or candy colours.
- Use `#222529` or `#353A40` as shared dark ink when a palette contains only pale swatches.
- Preserve strong headline contrast. Do not place pale text over a pale background.

## Soft Sand

Warm, calm, and editorial. Use for lifestyle, wellness, reflective advice, food, and approachable explainers.

| Role | Recommended colour |
| --- | --- |
| Base | `#F4ECE1` |
| Alternate base | `#EDEDEA` |
| Supporting tone | `#E1D6CB` |
| Muted accent | `#D1BEB1` |
| Dark ink | `#222529` |

Reference swatches: `#EDEDEA`, `#D5CDC3`, `#F4ECE1`, `#E1D6CB`, `#D1BEB1`.

## Light Steel

Neutral, modern, and precise. Use for technology, business, productivity, tutorials, and serious commentary.

| Role | Recommended colour |
| --- | --- |
| Base | `#F8F9FA` |
| Alternate base | `#EAECEF` |
| Supporting tone | `#CFD4DA` |
| Muted accent | `#6E757C` |
| Dark ink | `#222529` |

Reference swatches: `#F8F9FA`, `#EAECEF`, `#DFE2E6`, `#CFD4DA`, `#AFB5BC`, `#6E757C`, `#4B5057`, `#353A40`, `#222529`.

## Blue Serenity

Soft, optimistic, and trustworthy. Use for learning, calm self-improvement, planning, software, and thoughtful guidance.

| Role | Recommended colour |
| --- | --- |
| Base | `#EEF2FA` |
| Alternate base | `#E4EAFB` |
| Supporting tone | `#CFDBFA` |
| Muted accent | `#B0C3FA` |
| Dark ink | `#353A40` |

Reference swatches: `#EEF2FA`, `#E4EAFB`, `#D9E3FA`, `#CFDBFA`, `#C5D3FB`, `#BACCFA`, `#B0C3FA`.

## Soft Lavender

Gentle, creative, and contemporary. Use for personal stories, beauty, design, emotional topics, and softer opinion pieces.

| Role | Recommended colour |
| --- | --- |
| Base | `#FBEBF9` |
| Alternate base | `#DFE2FD` |
| Supporting tone | `#EBD4D7` |
| Muted accent | `#909AAD` |
| Dark ink | `#353A40` |

Reference swatches: `#909AAD`, `#C9C1D2`, `#EBD4D7`, `#FBEBF9`, `#DFE2FD`.

## Midnight Ink

High-contrast, low-light editorial. Use for urgent warnings, night scenes, authority statements, and serious explainers where light palettes wash out.

| Role | Recommended colour |
| --- | --- |
| Base | `#0F1419` |
| Alternate base | `#1A222C` |
| Supporting tone | `#2A3441` |
| Muted accent | `#8A9BB0` |
| Dark ink | `#F0F2F5` |
| Accent highlight | `#E53935` |

Reference swatches: `#0F1419`, `#1A222C`, `#2A3441`, `#3A4A5E`, `#8A9BB0`, `#F0F2F5`, `#E53935`.

> When using Midnight Ink, place light ink `#F0F2F5` over the dark base — do not place `#222529` over `#0F1419`.

## Contrast & accessibility

- Aim for **WCAG AA ≥ 4.5:1** for headline text. Check quickly: `python scripts/lint_headline.py --check-contrast "#F0F2F5" "#0F1419"` (or use WebAIM contrast checker).
- If a sampled background is mid-tone (~`#6E757C`–`#909AAD`), add the directional dark overlay (`--overlay 0.42` default) or switch ink to `#FFFFFF` with `#111111` stroke.
- Keep the single accent below ~10% of pixels; never rely on color alone to convey meaning — pair it with scale or placement.

## Prompt language

Describe the chosen palette by name and hex role values. Add: `muted, low-chroma, minimalist colour treatment; no neon tones; no unrelated bright colour blocks`.
