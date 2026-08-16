# Kiki thumbnail style guide

Use the images beside this file as compositional references. Borrow their visual logic, not their specific people, artwork, logos, or wording.

## Shared visual DNA

- Communicate one idea in under a second.
- Use one dominant human face, body, or held object.
- Limit the hook to 2–6 words in very large type.
- Balance the subject and headline across the frame; avoid filling every region.
- Prefer a controlled or simplified background with strong subject separation.
- Use white, black, or deep navy type plus one accent color.
- Use only one markup device: an arrow, underline, circle, check, or word box.
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
- Repeat or softly blur related objects in the background to establish abundance or proof.
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
- Prefer tension and specificity: `NEVER DO THIS`, `REACT TO NOTHING`, `STARTED SOONER`.
- Avoid vague filler such as `MY NEW VIDEO`, `YOU NEED THIS`, or a full sentence copied from the title.
- Put the strongest word first or isolate it with the accent color.
- Keep punctuation minimal. One period can make an opinion feel deliberate.
- Render text after image generation so spelling stays exact.

## Platform pair and finish

- YouTube canvas: 1280×720, 16:9.
- Rednote canvas: 1080×1440, portrait 3:4.
- Generate one loose square or near-square master, then crop and typeset each platform deterministically with `scripts/process_variants.py`.
- Keep faces, hands, hero objects, and gestures inside the master image's central 45% with usable background on every side so the landscape and portrait crops preserve the idea.
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
