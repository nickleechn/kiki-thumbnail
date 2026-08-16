---
name: kiki-thumbnail
description: "Create polished, high-impact thumbnail pairs in the Kiki reference style: a dominant human or object, a lean attention-grabbing headline, a minimal low-detail background, optional subject-over-text depth, strong contrast, and restrained arrows or word highlights. Use when Codex needs to design, generate, revise, or export thumbnails for YouTube and Rednote; produce deterministic 16:9 landscape and 3:4 portrait variants from one generated master; turn a video title, script, or concept into thumbnail options; incorporate a presenter photo; or match the visual language in this skill's reference images."
---

# Kiki Thumbnail

Create a platform-ready thumbnail pair that communicates one idea at a glance. Use the bundled references for visual direction, the built-in `image_gen` tool for the scene, and `scripts/process_variants.py` for exact headline text and deterministic sizing.

## Skill summary

- Turn a video title, script, concept, or presenter photo into one coordinated thumbnail pair.
- Use one dominant focal group, a lean attention-grabbing hook, a muted minimalist palette, and restrained visual emphasis.
- Preserve presenter identity, complete heads, natural gestures, and every meaningful object a subject points at, holds, presents, or looks toward.
- Generate loose base art, then add exact typography and crop deterministically with the bundled fonts and Python processor.
- Deliver YouTube at 1280×720 and Rednote at 1080×1440, inspecting each output independently for legibility and crop safety.

## Workflow

1. Gather the minimum inputs.
   - Require a video idea, title, or short summary.
   - Treat headline copy, brand colors, presenter photos, and must-use objects as optional.
   - If the thumbnail must depict a specific person and no usable photo is supplied, ask for one. Otherwise proceed with a suitable generic subject.
2. Read `reference/style-guide.md` and `reference/colour-palettes.md`, then inspect 1–3 relevant images in `reference/` with `view_image`.
   - Choose references by composition, not by the identity of their subjects.
   - Never copy a reference pixel-for-pixel or reuse its people, logos, characters, or headline.
3. Define one visual promise.
   - Draft three hooks, each 2–5 words, and prefer 2–4 words when the meaning stays clear. For Chinese, target 4–10 Chinese characters.
   - Select the shortest truthful option with the strongest concrete benefit, warning, opinion, or curiosity gap.
   - Make the hook complement rather than repeat the video title. Do not use a full sentence, subtitle, or filler words.
   - Keep the promise truthful to the video.
4. Pick one layout recipe from `reference/style-guide.md`.
   - Use one dominant subject or object.
   - Select one named palette from `reference/colour-palettes.md`. Use one calm base, one dark ink, and one optional muted accent.
   - Prefer a solid neutral, a very soft tonal gradient, or a heavily muted contextual environment. Keep background detail and contrast low.
   - Reserve a clean text zone and keep the lower-right corner visually quiet for YouTube's duration badge.
   - Treat anything the subject points at, holds up, presents, or looks toward as a hero object. Preserve its recognizable shape, cover, material, and important identifying details; simplify only the nonessential surroundings.
   - Prefer a depth overlap when a presenter is prominent: let a shoulder, arm, hand, or edge of the hair sit in front of part of the headline while the text stays readable.
   - Use at most one emphasis device: arrow, underline, circle, or highlighted word.
5. Generate the base art with the built-in `image_gen` tool.
   - Classify the request as `ads-marketing` or `photorealistic-natural`.
   - Label every input image by role. Use the presenter photo as an identity reference and the selected thumbnails only as style/composition references.
   - Ask for one square or near-square master composition that is safe for both a 16:9 landscape crop and a 3:4 portrait crop. Keep the subject, face, hero object, and gesture inside the central 45% of the frame with generous background on every side.
   - Keep the entire head, hair outline, ears, and chin inside the crop-safe region with at least 8% of the master height as breathing room above the hair.
   - Request no generated headline, captions, unrelated lettering, watermarks, borders, or duration badge in the base. Preserve user-supplied visual details on a gesture-targeted object through a labeled reference or deterministic overlay.
   - Keep skin, hands, food, products, and gesture-targeted objects believable. Preserve the visual line between a pointing hand or gaze and its target. Avoid plastic retouching and overstuffed collage layouts.
6. Add the exact headline and always export both platform variants.
   - Run `scripts/process_variants.py` with the generated base.
   - Produce YouTube at 1280×720 (16:9 landscape) and Rednote at 1080×1440 (3:4 portrait).
   - Use separate Rednote crop focus or text layout overrides when the portrait frame would clip the subject or headline. Default Rednote text to the top region.
   - Use the bundled `font/GoogleSansFlex-ExtraBold.ttf` by default. Use `font/Newsreader-ExtraBold.ttf` only for an editorial or warning concept.
   - When an aligned transparent presenter layer is available, pass it with `--foreground` so the renderer places headline text behind the person deterministically.
   - Highlight no more than one key word unless the user requests otherwise.
7. Inspect both final images with `view_image`.
   - Check spelling verbatim.
   - Check legibility at roughly 10% scale.
   - Confirm one clear focal point, adequate contrast, an entirely visible head and hair outline, readable text, and an unobstructed lower-right corner.
   - Reject any crop that cuts through the top or sides of a person's head. Adjust platform-specific focus or regenerate the master.
   - Make one targeted revision at a time.
8. Deliver both final workspace paths, the final image-generation prompt, and the exact headline or platform-specific headlines.

## Image-generation prompt

Use this structure and omit unused lines:

```text
Use case: ads-marketing
Asset type: cross-platform thumbnail master image
Primary request: <single visual idea tied to the video>
Input images: <Image 1: presenter identity reference; Image 2: hero-object detail reference when supplied; remaining images: composition/style references>
Scene/backdrop: <minimal low-detail field: solid neutral, soft monochrome gradient, or heavily muted contextual environment>
Subject: <one dominant person or object, expression/pose/action; describe any object being pointed at or presented with enough detail to keep it recognizable>
Style/medium: polished photorealistic editorial thumbnail
Composition/framing: square or near-square master safe for both 16:9 landscape and 3:4 portrait crops; essential subject and gesture inside central 45%; entire head, hair outline, ears, and chin visible; at least 8% master-height breathing room above the hair; generous background on every side; clean negative space around the subject; bold silhouette; allow a shoulder, hand, or hair edge to overlap the future headline zone
Lighting/mood: bright subject separation, believable skin and material texture
Background color: one calm neutral base or two closely related tones; optional single accent only
Color palette: <named palette from reference/colour-palettes.md; one light base, one dark ink, one optional muted accent>
Constraints: no generated headline, captions, watermark, border, or duration badge; do not reproduce reference identities or copyrighted characters; keep anatomy natural; preserve the form, material, and meaningful details of any object the subject points at, holds, presents, or looks toward
Avoid: simplifying or abstracting a gesture-targeted object; busy or multicolor backgrounds, rainbow gradients, repeated patterns, decorative clutter, tiny unrelated props, generic stock-photo staging, exaggerated HDR, excessive glow
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
  --rednote-focus-x 0.66 \
  --foreground output/presenter-cutout.png
```

This command must create `output/my-video-youtube.png` and `output/my-video-rednote.png`. Use `--rednote-text` when Rednote needs a different hook. Use `--font-style serif` for the editorial-warning recipe. Use `--overlay 0` only when the base already provides strong text contrast. Run `python3 scripts/process_variants.py --help` for all options. Use `scripts/render_thumbnail.py --preset <youtube|rednote>` only for targeted single-output revisions.

The processor stages and dimension-checks both files before publishing the pair. It refuses to replace existing outputs unless `--overwrite` is supplied.

The optional `--foreground` file must be a transparent PNG aligned pixel-for-pixel with the uncropped input master. The renderer applies the same platform crop to both files, draws the headline, and then composites the foreground person above the text. Keep every word instantly readable; normally obscure no more than 20% of its letterforms.

The renderer automatically uses the bundled Google Sans Flex ExtraBold for Latin sans-serif headlines and Newsreader ExtraBold for Latin serif headlines. It selects an available CJK system font when a headline contains Chinese, Japanese, or Korean characters. Pass `--font /path/to/font.ttf` only when a specific brand font is required. The bundled fonts and their SIL Open Font License are stored in `font/`.

## Output rules

- Always export two files from every generation: YouTube at exactly 1280×720 and Rednote at exactly 1080×1440.
- Keep the headline to 2–5 words and prefer 2–4; for Chinese, target 4–10 Chinese characters.
- Keep the background minimal: at most two closely related base tones plus one optional accent, with no busy pattern or unrelated bright color blocks.
- Never simplify, blur away, crop out, or replace an object that the subject points at, holds, presents, or looks toward. Keep the gesture and target readable as one visual idea.
- Prefer text-behind-person depth when it improves the composition, but preserve instant word recognition.
- Keep essential content at least 48 px from the edges.
- Never clip the top or sides of a person's head or hair. Use `--focus-y` and `--rednote-focus-y` independently when needed.
- Treat the two aspect ratios as one thumbnail pair, not as optional creative variants.
- Do not bake a duration badge into the image; YouTube adds it in the interface.
- Preserve a supplied person's identity. Do not fabricate or imitate a real person who was not provided for the thumbnail.
