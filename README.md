# Kaelearn

A study system that runs in Claude Code. Kael'thos writes your folios (study PDFs in the AURA-1
Night Console look), turns your Notability notes into Obsidian notes, coaches problems without
giving away answers, and keeps the map of everything you've learned. Start with
`codex/codex.pdf`: the research, and the system you chose.

## Setup

1. Install XeLaTeX (MiKTeX or TeX Live), Python 3.11+ with `pip install numpy pillow manim boto3`,
   and Node.
2. Check `kaelearn.json` points at your vault folder (`D:/le vault/Kaelearn`).
3. Connect GitHub:
   ```
   git remote add origin https://github.com/<you>/kaelearn.git
   git push -u origin main
   ```
4. Videos live in Cloudflare R2, never in the vault (10 GB free, about 5000 videos). In the
   Cloudflare dashboard: open R2 and enable it (a card is needed, the free tier costs $0), create
   the bucket `kaelearn-anims`, connect the custom domain `anims.amygdala-inc.org` under its
   Settings, and make an API token with Object Read & Write on that bucket. Copy
   `.env.example` to `.env` and fill it in. With your own bucket and domain, change them in
   `kaelearn.json`.
   The repo is public, so turn on the hook that refuses to commit `.env`:
   ```
   git config core.hooksPath .githooks
   ```
5. Open Claude Code in this folder. The Kael'thos output style and the push hook load from
   `.claude/`.

## Course codes

Commands, file names and commits name a course by its code.

| Code | Course | Subject folder |
|---|---|---|
| EP1 | Experimentalphysik 1 | `physics` |
| RM | Physikalische Rechenmethoden | `methods` |
| LA | Lineare Algebra 1 | `linear-algebra` |
| ANA | Analysis 1 | `analysis` |
| FUS | Forschung und Studium | none |
| CUM | Cummings, *Real Analysis* (self-study) | `analysis` |
| PRF | Udemy proofs course | `proofs` |
| ODE | Udemy differential equations course | `odes` |

Homework sheets are `UE03` (exercise sheet 3), so `ANA UE03/2` is problem 2 of Analysis sheet 3.
Add new courses in `system/student.md` and here.

## Daily use

- **Before a lecture:** `/pretest ANA sequences`
- **After a lecture:** blurt. On a blank Notability page, write down everything you remember
  from the lecture for 5 minutes, without looking at your notes. Recalling it is the practice,
  and whatever you can't produce is a gap you would otherwise never notice. Export the notes
  and the blurt as PDF and use Save to Files to put them in `Obsidian/le vault/Kaelearn/Inbox`
  (names like `ANA 2026-10-14` and `ANA 2026-10-14 blurt`). Then run `/ingest`: it compares
  the blurt with the notes and lists the gaps.
- **Exercises:** attempt it, then `/exercise` with the problem and your attempt. Talk it
  through; say "debrief" at the end and the session becomes a short PDF in the vault.
- **Videos:** Kael'thos makes short manim videos when motion helps, or on request with
  `/animate <idea>`. They stream from `anims.amygdala-inc.org`. On the iPad, watch them
  embedded in the concept note in Obsidian, or tap the frame in a PDF. To try it, open
  `Kaelearn/Specimens/Videos.md`.
- **New topic:** `/folio analysis uniform convergence`, or drag in Skript pages.
- **Weekly:** `/review`, then `/teach <concept>`.
- **Exams:** `/exam mock ANA`, `/exam oral LA`, `/exam board EP1`, `/exam mixed`.

Anki: morning reviews, new cards in the evening, from Kael'thos' suggestions. Make the cards
yourself.
