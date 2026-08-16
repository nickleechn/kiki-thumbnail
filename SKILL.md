---
name: kiki-thumbnail
description: "Create polished, high-impact YouTube thumbnails in the Kiki reference style: a dominant human or object, short curiosity-driven headline, clean 16:9 composition, strong contrast, and restrained arrows or word highlights. Use when Codex needs to design, generate, revise, or export a YouTube thumbnail; turn a video title, script, or concept into thumbnail options; incorporate a presenter photo; or match the visual language in this skill's reference images."
---

# Kiki Thumbnail

Create a YouTube-ready thumbnail that communicates one idea at a glance. Use the bundled references for visual direction, the built-in `image_gen` tool for the scene, and `scripts/render_thumbnail.py` for exact headline text and final sizing.

## Workflow

1. Gather the minimum inputs.
   - Require a video idea, title, or short summary.
   - Treat headline copy, brand colors, presenter photos, and must-use objects as optional.
   - If the thumbnail must depict a specific person and no usable photo is supplied, ask for one. Otherwise proceed with a suitable generic subject.
2. Read `reference/style-guide.md` and inspect 1–3 relevant images in `reference/` with `view_image`.
   - Choose references by composition, not by the identity of their subjects.
   - Never copy a reference pixel-for-pixel or reuse its people, logos, characters, or headline.
3. Define one visual promise.
   - Write a 2–6 word hook that complements rather than repeats the video title.
   - Prefer a concrete benefit, warning, opinion, or curiosity gap.
   - Keep the promise truthful to the video.
4. Pick one layout recipe from `reference/style-guide.md`.
   - Use one dominant subject or object.
   - Reserve a clean text zone and keep the lower-right corner visually quiet for YouTube's duration badge.
   - Use at most one emphasis device: arrow, underline, circle, or highlighted word.
5. Generate the base art with the built-in `image_gen` tool.
   - Classify the request as `ads-marketing` or `photorealistic-natural`.
   - Label every input image by role. Use the presenter photo as an identity reference and the selected thumbnails only as style/composition references.
   - Ask for a 16:9 YouTube-thumbnail base with deliberate negative space for the headline.
   - Request no words, letters, captions, logos, watermarks, borders, or duration badge in the generated base.
   - Keep skin, hands, food, and products believable. Avoid plastic retouching and overstuffed collage layouts.
6. Add the exact headline and export at 1280×720.
   - Run `scripts/render_thumbnail.py` with the generated base.
   - Use sans-serif type by default. Use serif only for an editorial or warning concept.
   - Highlight no more than one key word unless the user requests otherwise.
7. Inspect the final image with `view_image`.
   - Check spelling verbatim.
   - Check legibility at roughly 10% scale.
   - Confirm one clear focal point, adequate contrast, unclipped faces/text, and an unobstructed lower-right corner.
   - Make one targeted revision at a time.
8. Deliver the final workspace path, the final image-generation prompt, and the exact headline.

## Image-generation prompt

Use this structure and omit unused lines:

```text
Use case: ads-marketing
Asset type: YouTube thumbnail base image
Primary request: <single visual idea tied to the video>
Input images: <Image 1: presenter identity reference; Image 2..N: composition/style references>
Scene/backdrop: <simple setting or controlled background>
Subject: <one dominant person or object, expression/pose/action>
Style/medium: polished photorealistic editorial thumbnail
Composition/framing: 16:9; <subject placement>; clean negative space on <text side>; bold silhouette; lower-right corner quiet
Lighting/mood: bright subject separation, believable skin and material texture
Color palette: restrained neutrals plus one accent color
Constraints: no text, letters, captions, logos, watermark, border, or duration badge; do not reproduce reference identities or copyrighted characters; keep anatomy natural
Avoid: clutter, tiny props, generic stock-photo staging, exaggerated HDR, excessive glow
```

## Exact-text renderer

Use the bundled Python runtime when available; any Python with Pillow 10+ also works.

```bash
python3 scripts/render_thumbnail.py \
  --input output/base.png \
  --output output/thumbnail.png \
  --text "I WISH I STARTED SOONER" \
  --layout left \
  --highlight SOONER \
  --highlight-color "#F20D0D" \
  --focus-x 0.72
```

Use `--font-style serif` for the editorial-warning recipe. Use `--overlay 0` only when the base already provides strong text contrast. Run `python3 scripts/render_thumbnail.py --help` for all options.

## Output rules

- Export exactly 1280×720 in PNG or high-quality JPEG.
- Keep essential content at least 48 px from the edges.
- Default to one final thumbnail. Generate separate variants only when requested or when testing meaningfully different hooks.
- Do not bake a duration badge into the image; YouTube adds it in the interface.
- Preserve a supplied person's identity. Do not fabricate or imitate a real person who was not provided for the thumbnail.
