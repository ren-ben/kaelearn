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

Every video has to make sense on its own, with no PDF beside it. It is also always placed in
context: an `\anim` panel in the PDF, or an embed in the concept note.

1. `self.title_card(title, subtitle)`.
2. `self.question_card(...)`: the question the video answers, stated in full (the claim, the
   problem, the definitions it needs). A viewer who has only seen this card knows what to watch
   for.
3. Build the object in steps. `self.play(self.say(...), ...)` sets the caption line at the top.
   Each caption explains the step: what is happening and why it matters, not just a label.
4. Show the change that carries the idea, slowly: 3 to 5 s per move, then `wait` 1 to 2 s so
   the student can think.
5. `self.idea_card(...)`: the answer in one or two sentences.

**Motion is smooth.** Every move eases in and out (manim's default `smooth`). Nothing snaps,
teleports, pops in or out, or starts and stops at full speed.
- A quantity that has to be a whole number (an index, a count) glides to each new value: animate
  a second `ValueTracker` for its position alongside the first, as `heads-and-tails.py` does with
  ε and N.
- To bring an object back to a start point, fade it out and a new one in. Never `move_to` it
  between frames.
- Run caption changes during a motion (`added_anims=[self.say(...)]`), not in a dead pause
  between two motions.

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

## 3D

For surfaces, fields in space, gradients, divergence and curl, or thermodynamic state surfaces,
subclass `KLScene3D`. The model is `engine/specimen/anims/uphill.py`.
- Build with `kl_axes3d(...)` and `kl_surface(ax, f, x_range, y_range)`. The surface is shaded
  by height from `LOW` to `HI`.
- Captions and cards stay flat on the screen by themselves. Anything else that should stay flat
  goes through `self.pin(...)`.
- Set the camera with `set_camera_orientation(phi=60-70°, theta=...)`. For depth, use
  `self.orbit(degrees, run_time)`, a slow eased swing. Never use ambient camera rotation: it
  starts and stops with a jerk, and `kl.py anim` refuses scenes that use it. Every other camera
  change is a `move_camera(...)`, which eases by default.
- **One layer at a time.** Flat objects (arrows, rings, curves) always draw on top of every 3D
  face, so a map stacked under a surface ends up over it. For a map or a field, move the camera
  straight above (`move_camera(phi=0, theta=-90°, zoom≈0.8)`), fade the surface to about 0.3,
  and draw the field there. Fade the field out before tilting back to the side.
- 3D renders slowly (about 6 minutes for a minute of video at 1080p). Get the draft right first,
  and for videos over 30 s, check a denser contact sheet as well.

## Render, check, publish

1. `python engine/kl.py anim <file.py> --draft` renders fast at 480p and prints a contact sheet
   of 12 frames. Read it and check:
   - nothing is off-frame or overlapping
   - the captions are readable
   - the change is visible
   - the idea card fits
   - no `motion:` warnings. The render flags any motion that starts or stops abruptly, at its
     timestamp. It only sees motion that covers a lot of the frame, so slow or small moves still
     depend on the rules above.

   Fix and repeat until it passes.
2. `python engine/kl.py anim <file.py> --poster 0.6` renders the final 1080p30 video. It writes
   `<slug>.mp4` and the poster `<slug>.png` beside the file. Set `--poster` to the fraction of the
   video that shows the most telling frame.
3. Publish the video: `kl.py publish <slug>.mp4` puts it beside its PDF in the vault, or under
   `Anims/<s>/` for standalone videos. Rebuild and publish the PDF that shows it. Keep each video
   under 3 MB (`publish` refuses bigger: the vault has 1 GB in total). `kl.py anim` re-encodes a
   render that comes out too big, and prints the final size.
4. Embed it in the concept note it explains as `![[<slug>.mp4]]`.
5. Commit and push.

## Manim traps

- A group's updater only runs if the group itself is in the scene. After animating its parts in,
  call `self.add(group)`.
- Use `always_redraw` for anything that depends on a `ValueTracker`. Call `clear_updaters()`
  before fading out.
- Give dots a `z_index` so lines drawn later don't cut through them.
- In 3D, never `Transform` a pinned text into another: the new letters come out unpinned and
  vanish. Never crossfade two captions either, because the overlap reads as ghost letters. Fade
  the old one out, then the new one in (`say` does this).
