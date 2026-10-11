---
name: folio
description: Write a Kaelearn folio, the Night Console PDF that teaches one topic (overview, guess-first questions, terms EN/DE, concepts with why-questions, real figures, triggers, card suggestions). Use when the student asks to learn or explain a topic, drops Skript or textbook pages to turn into a study PDF, or asks for "a folio" or "a PDF on X".
argument-hint: "[subject] [topic]"
---

# Folio

1. **Sources.** Gather what the topic rests on: dropped pages, the Skript, Cummings, the
   student's lecture notes in `D:\le vault\Kaelearn\Lectures\`, and existing concept notes.
   Follow the course's notation and the Skript's order, so the folio matches the lecture.
2. **Place.** Use `subjects/<subject>/folios/NN-slug/` with the next free NN for that
   subject (`system/structure.md`). Make the plate:
   `python engine/kl.py plate <scene> subjects/<s>/folios/NN-slug/plate.png`
   (scenes in `system/design.md`).
3. **Write** `NN-slug.tex`, starting from `engine/specimen/specimen.tex`:
   - anatomy and components exactly as in `system/design.md`
   - voice as in `system/voice.md`: open with the problem the topic solves
   - pedagogy as in `system/method.md`. `twominute` must be readable in under 2 minutes.
     `guessfirst` asks questions the folio later answers. At least two `\why` questions. One
     `keystone`. The triggers, and a deck of at most five cards of the types Def, Why and Trigger.
   - figures wherever a picture explains faster than words: pgfplots or TikZ, never ASCII
   - correctness first: check every statement, hypothesis and computation. If a proof is
     sketched, say so.
4. **Build and look.** `python engine/kl.py build <tex>`, then `python engine/kl.py look <pdf>`.
   Read the sheet and fix overflow, stranded figures and missing glyphs. Rebuild until clean.
5. **Publish.** `python engine/kl.py publish <pdf>`.
6. **Atlas and notes.** Add the topic's concepts to `ATLAS.md` (level 1, next review +7 days,
   unless the student already had them). Link the folio there. Add the triggers to
   `subjects/<s>/triggers.md`. Create or update the concept notes and the hub in the vault
   (`system/vault.md`), and `kl.py mirror`.
7. **Commit and push.** Commit as `folio: <subject> NN <slug>`, then push.

Reply with the path of the PDF, one sentence on what the folio teaches, and where to start
(the 2-minute view).
