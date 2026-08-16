---
name: kiki-thumbnail
description: "Create polished, high-impact thumbnail pairs in the Kiki reference style: a dominant human or object, short curiosity-driven headline, strong contrast, and restrained arrows or word highlights. Use when Codex needs to design, generate, revise, or export thumbnails for YouTube and Rednote; produce deterministic 16:9 landscape and 3:4 portrait variants from one generated master; turn a video title, script, or concept into thumbnail options; incorporate a presenter photo; or match the visual language in this skill's reference images."
---

# Kiki Thumbnail

Create a platform-ready thumbnail pair that communicates one idea at a glance. Use the bundled references for visual direction, the built-in `image_gen` tool for the scene, and `scripts/process_variants.py` for exact headline text and deterministic sizing.

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
   - Ask for one square or near-square master composition that is safe for both a 16:9 landscape crop and a 3:4 portrait crop. Keep the subject, face, hero object, and gesture inside the central 45% of the frame with generous background on every side.
   - Request no words, letters, captions, logos, watermarks, borders, or duration badge in the generated base.
   - Keep skin, hands, food, and products believable. Avoid plastic retouching and overstuffed collage layouts.
6. Add the exact headline and always export both platform variants.
   - Run `scripts/process_variants.py` with the generated base.
   - Produce YouTube at 1280×720 (16:9 landscape) and Rednote at 1080×1440 (3:4 portrait).
   - Use separate Rednote crop focus or text layout overrides when the portrait frame would clip the subject or headline. Default Rednote text to the top region.
   - Use sans-serif type by default. Use serif only for an editorial or warning concept.
   - Highlight no more than one key word unless the user requests otherwise.
7. Inspect both final images with `view_image`.
   - Check spelling verbatim.
   - Check legibility at roughly 10% scale.
   - Confirm one clear focal point, adequate contrast, unclipped faces/text, and an unobstructed lower-right corner.
   - Make one targeted revision at a time.
8. Deliver both final workspace paths, the final image-generation prompt, and the exact headline or platform-specific headlines.

## Image-generation prompt

Use this structure and omit unused lines:

```text
Use case: ads-marketing
Asset type: cross-platform thumbnail master image
Primary request: <single visual idea tied to the video>
Input images: <Image 1: presenter identity reference; Image 2..N: composition/style references>
Scene/backdrop: <simple setting or controlled background>
Subject: <one dominant person or object, expression/pose/action>
Style/medium: polished photorealistic editorial thumbnail
Composition/framing: square or near-square master safe for both 16:9 landscape and 3:4 portrait crops; essential subject and gesture inside central 45%; generous background on every side; clean negative space around the subject; bold silhouette
Lighting/mood: bright subject separation, believable skin and material texture
Color palette: restrained neutrals plus one accent color
Constraints: no text, letters, captions, logos, watermark, border, or duration badge; do not reproduce reference identities or copyrighted characters; keep anatomy natural
Avoid: clutter, tiny props, generic stock-photo staging, exaggerated HDR, excessive glow
```

## Deterministic two-variant processor

Use the bundled Python runtime when available; any Python with Pillow 10+ also works.

```bash
python3 scripts/process_variants.py \
  --input output/base.png \
  --output-dir output \
  --stem my-video \
  --text "I WISH I STARTED SOONER" \
  --layout left \
  --rednote-layout top \
  --highlight SOONER \
  --highlight-color "#F20D0D" \
  --focus-x 0.72 \
  --rednote-focus-x 0.66
```

This command must create `output/my-video-youtube.png` and `output/my-video-rednote.png`. Use `--rednote-text` when Rednote needs a different hook. Use `--font-style serif` for the editorial-warning recipe. Use `--overlay 0` only when the base already provides strong text contrast. Run `python3 scripts/process_variants.py --help` for all options. Use `scripts/render_thumbnail.py --preset <youtube|rednote>` only for targeted single-output revisions.

The processor stages and dimension-checks both files before publishing the pair. It refuses to replace existing outputs unless `--overwrite` is supplied.

The renderer automatically selects an available CJK font when a headline contains Chinese, Japanese, or Korean characters. Pass `--font /path/to/font.ttf` only when a specific brand font is required.

## Output rules

- Always export two files from every generation: YouTube at exactly 1280×720 and Rednote at exactly 1080×1440.
- Keep essential content at least 48 px from the edges.
- Treat the two aspect ratios as one thumbnail pair, not as optional creative variants.
- Do not bake a duration badge into the image; YouTube adds it in the interface.
- Preserve a supplied person's identity. Do not fabricate or imitate a real person who was not provided for the thumbnail.
