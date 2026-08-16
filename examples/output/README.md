# Example Outputs

This folder is the intended location for paired YouTube + Rednote renders.

## How to populate

1. Generate a master:
   ```bash
   # via Codex image_gen or any image model — keep it square ~1024–1280px
   # Keep face/hero object inside central 45%, 8% headroom above hair
   ```

2. Render both variants:
   ```bash
   python scripts/process_variants.py \
     --input master.png --output-dir examples/output --stem demo-warning \
     --text "NEVER DO THIS" --highlight "NEVER" --layout left \
     --rednote-text "NEVER DO THIS" --rednote-layout top \
     --font-style sans --overlay 0.42
   ```

3. Expected pair:
   - `demo-warning-youtube.png`  — 1280×720 (16:9)
   - `demo-warning-rednote.png`  — 1080×1440 (3:4)

## Checklist (zoom to ~10% / 128×72)

- [ ] Both crops show the full head/hair outline (no top crop)
- [ ] Headline readable, spelling exact, lower-right quiet
- [ ] One accent only (arrow / box / underline)

> Until real renders are added, this README stands in. Add 1 ideal pair per layout recipe (01–08) when ready.
