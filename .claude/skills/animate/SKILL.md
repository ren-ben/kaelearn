---
name: animate
description: Make a short manim video (MP4, in the Night Console look) that shows an abstract idea or a specific problem in motion. Examples: a limit settling, epsilon shrinking, a linear map shearing the plane, a phase portrait, an oscillator trading energy. Use it unasked whenever motion would make an idea click better than a static figure (in /exercise, /folio, /ingest or chat), and whenever the student asks for an animation or video.
argument-hint: "[idea or problem]"
---

# Animate

A video earns its place when the idea is a process: something changes, and how it changes is the
point. Examples: epsilon-N games, limits, linear maps, flows, oscillations, a construction built
step by step. A static fact gets a figure, not a video. Make at most one video per artifact unless
the student asks for more.

## Shape: one idea, 30 to 90 seconds

1. `self.title_card(title, subtitle)`.
2. Build the object in steps. One caption line at the top (`Tex`, about 34 pt) says what to look
   at, and changes as the video moves on.
3. Show the change that carries the idea, slowly: 3 to 5 s per move, then `wait` 1 to 2 s so
   the student can think.
4. `self.idea_card(...)`: the idea in one or two sentences.

Silent, with no voice-over. Math goes in `MathTex` or `Tex` (Garamond, through XeLaTeX); plain
words go in `Text`. Use only the inks from `klmanim`:
- the data and the thing to watch: `HI`
- reference lines: `DIM`, dashed
- regions: `INK` at `fill_opacity` of about 0.12
- no red

Kael'thos appears only in the title card.

## Files

- **Belongs to a folio or debrief:** `<artifact-dir>/anims/<slug>.py`. In the `.tex`, write
  `\anim{<slug>}{what to watch for}`, which shows the poster frame; a tap plays the video in
  Obsidian.
- **Standalone** (from chat): `subjects/<s>/anims/<slug>.py`.

Write one scene class per file: `from klmanim import *`, then subclass `KLScene`. The model is
`engine/specimen/anims/heads-and-tails.py`.

## Render, check, publish

1. `python engine/kl.py anim <file.py> --draft` renders fast at 480p and prints a contact sheet
   of 12 frames. Read it and check:
   - nothing is off-frame or overlapping
   - the captions are readable
   - the change is visible
   - the idea card fits

   Fix and repeat until it passes.
2. `python engine/kl.py anim <file.py> --poster 0.6` renders the final 1080p30 video. It writes
   `<slug>.mp4` and the poster `<slug>.png` beside the file. Set `--poster` to the fraction of the
   video that shows the most telling frame.
3. Publish the video: `kl.py publish <slug>.mp4` puts it beside its PDF in the vault, or under
   `Anims/<s>/` for standalone videos. Rebuild and publish the PDF that shows it. Keep each video
   under 3 MB (`publish` refuses bigger: the vault has 1 GB in total); the render prints the size.
4. Embed it in the concept note it explains as `![[<slug>.mp4]]`.
5. Commit and push.

## Manim traps

- A group's updater only runs if the group itself is in the scene. After animating its parts in,
  call `self.add(group)`.
- Use `always_redraw` for anything that depends on a `ValueTracker`. Call `clear_updaters()`
  before fading out.
- Give dots a `z_index` so lines drawn later don't cut through them.
