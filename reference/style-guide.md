# Kiki thumbnail style guide

Use the images beside this file as compositional references. Borrow their visual logic, not their specific people, artwork, logos, or wording.

## Shared visual DNA

- Communicate one idea in under a second.
- Use one dominant human face, body, or held object.
- Limit the hook to 2–5 words in very large type; prefer 2–4 words. For Chinese, target 4–10 Chinese characters.
- Balance the subject and headline across the frame; avoid filling every region.
- Make the background color minimalistic: one calm base color or two closely related tones, plus one optional accent.
- Prefer a solid neutral, soft tonal gradient, or heavily muted contextual environment with strong subject separation.
- Use white, black, or deep navy type plus one accent color.
- Prefer a subtle depth overlap: place part of the headline behind a shoulder, arm, hand, or hair edge when the words remain immediately readable.
- Use only one markup device: an arrow, underline, circle, check, or word box.
- Treat anything the subject points at, holds, presents, or looks toward as essential content, not background detail.
- Keep the lower-right corner low priority because YouTube overlays the duration there.
- Do not include a duration badge in generated output.

## Layout recipes

### 1. Direct warning

References: `IMG_4883.png`, `IMG_4060.png`

- Put a waist-up or full-body subject on the right.
- Put a 3–5 word warning or regret hook on the left.
- Use bold sans-serif for modern/self-improvement topics or bold serif for a more editorial warning.
- Use one red arrow or one red word box.
- Keep the background neutral and lightly textured.

### 2. Show and tell

Reference: `IMG_0324.png`

- Put the presenter on one side holding the hero object near the center.
- If proof objects are necessary, use a small, softly blurred group in one area rather than filling the background.
- Use a short conversational hook and a simple arrow aimed at the hero object.
- Keep the object large enough to understand at phone size.

### 3. Editorial statement

References: `IMG_0029.png`, `IMG_0379.png`

- Center or slightly offset a strong portrait.
- Put a declarative statement across the top or lower third.
- Use white all-caps type with a dark shadow over a restrained environment.
- Let the expression and posture carry the emotion; avoid extra icons and props.

### 4. Beginner explainer

Reference: `IMG_9475.png`

- Use a light gray or off-white field.
- Put the headline across the top and highlight one key phrase in yellow.
- Arrange a few muted topic icons as a progression.
- Place the presenter or tool in the lower half, looking or pointing toward the outcome.
- Use one bright arrow to connect cause and result.

### 5. Warm editorial collage

Reference: `WPoKkr_WED8.jpg`

- Use a warm, pale neutral background and a dark navy headline.
- Put a friendly presenter on one side and one coherent supporting visual group on the other.
- Use a loose hand-drawn underline or flourish as the only accent.
- Keep the overall feeling calm and intentional rather than urgent.

## Headline rules

- Write the thumbnail hook after understanding the video's actual payoff.
- Draft three hooks, then choose the shortest truthful option that creates the strongest curiosity, benefit, warning, or opinion.
- Use 2–5 words and prefer 2–4. For Chinese, target 4–10 Chinese characters.
- Prefer tension and specificity: `NEVER DO THIS`, `REACT TO NOTHING`, `STARTED SOONER`.
- Avoid vague filler such as `MY NEW VIDEO`, `YOU NEED THIS`, conjunction-heavy copy, subtitles, or a full sentence copied from the title.
- Put the strongest word first or isolate it with the accent color.
- Keep punctuation minimal. One period can make an opinion feel deliberate.
- Render text after image generation so spelling stays exact.

## Background color rules

- Select a named palette from `colour-palettes.md` and keep its assigned base, ink, and optional accent roles.
- Start with one restrained base: off-white, light gray, warm beige, muted pastel, deep navy, or charcoal.
- Use no more than two closely related base tones and one optional accent color across the thumbnail.
- A solid field or very soft tonal gradient is the default. Never use rainbow gradients, busy patterns, or multiple unrelated bright color blocks.
- When a real setting is essential, reduce its saturation, detail, and contrast so it reads as context rather than a second focal point.
- Let the subject, headline, and single accent create contrast. Do not add decorative props or icons merely to fill empty space.

## Typography rules

- Use the bundled Google Sans Flex ExtraBold for the default modern, clean headline style.
- Use the bundled Newsreader ExtraBold for editorial statements and serious warnings.
- Use one typeface per thumbnail. Create emphasis with scale, placement, or one color highlight rather than mixing families.
- Treat these bundled files as Latin fonts; let the renderer choose a compatible system font for Chinese, Japanese, or Korean text.

## Subject and text depth

- Use foreground overlap as the default recommendation for human-led thumbnails when it adds depth.
- Place the text behind a shoulder, arm, hand, or small edge of the hair—not across the eyes or central facial features.
- Keep every word recognizable at a glance; obscure no more than about 20% of any word's letterforms.
- Build the effect with an aligned transparent presenter layer and the renderer's `--foreground` option. Do not bake uncertain AI-generated lettering into the scene.
- Keep the entire head and hair outline visible. Any crop through the top or sides of the head is a failed composition.

## Gesture and hero-object integrity

- Preserve the complete visual relationship between a pointing hand, directed gaze, or presenting pose and its target.
- Keep a targeted book, product, tool, screen, food item, or other object recognizable at phone size. Retain its silhouette, material, orientation, and meaningful visible details.
- Do not blur, flatten, abstract, substitute, crop out, or hide a gesture-targeted object in the name of minimalism.
- Simplify only unrelated surroundings. The person, gesture, and target together form the primary focal group.
- If the target contains user-supplied cover art, packaging, or other exact visual details, use the supplied image as a reference or deterministic overlay rather than asking image generation to recreate it from memory.
- Check both platform crops independently so the pointing direction still lands on the same visible object.

## Platform pair and finish

- YouTube canvas: 1280×720, 16:9.
- Rednote canvas: 1080×1440, portrait 3:4.
- Generate one loose square or near-square master, then crop and typeset each platform deterministically with `scripts/process_variants.py`.
- Keep faces, hands, hero objects, gestures, and their targets inside the master image's central 45% with usable background on every side so the landscape and portrait crops preserve the idea.
- Keep at least 8% of the master height above the person's hair and verify the full head outline independently in both final crops.
- Default the Rednote headline to the top region. Allow a different headline, position, or crop focus for the portrait version; do not stretch or letterbox the image.
- Edge safety: 48 px minimum.
- Subject size: face or hero object should usually occupy 30–55% of the frame.
- Text zone: usually 38–52% of the canvas width.
- Contrast: use a directional dark overlay behind light text when the photo is busy.
- Retouching: keep real skin texture, believable hands, and natural fabric or food detail.
- Final check: zoom out to approximately 128×72. The subject and hook should still read instantly.

## Reference index

| File | Primary lesson |
| --- | --- |
| `WPoKkr_WED8.jpg` | Calm split composition, warm neutral palette, dark navy headline |
| `IMG_4883.png` | Minimal warning hook, serif type, red arrow, right-side portrait |
| `IMG_0324.png` | Presenter plus hero object, repeated background proof, red markup |
| `IMG_0029.png` | Centered authority portrait and oversized lower-third statement |
| `IMG_9475.png` | Beginner explainer, highlighted phrase, icons, progression arrow |
| `IMG_4060.png` | Big left-aligned hook, one red highlight box, full-body subject |
| `IMG_0379.png` | Outdoor portrait with a bold top-line opinion |
| `NsR3rkuLNNs.jpg` | Oversized editorial serif, warm muted scene, and subject-over-text depth |
| `1X2tOUBfo8E.jpg` | Quiet seasonal backdrop with an elegant left-headline/right-portrait split |
| `ZuiqHa3i5oc.jpg` | Split proof composition, curved centered headline, and neutral palette |
| `Mgc6JxAn7WM.jpg` | Headline behind a centered presenter with restrained supporting product cutouts |
