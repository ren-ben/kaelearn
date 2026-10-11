---
name: ingest
description: Process the student's handwritten Notability exports from the vault Inbox (lecture notes, blurts, attempts, review answers) into Obsidian notes. Each note gets a faithful LaTeX transcript with page references to the original, plus a layer of gaps, review questions, card ideas and concept links. Converted PDFs are then deleted from the Inbox. Use at the start of a session when the Inbox has PDFs, or when the student says they exported notes or drops handwritten pages.
---

# Ingest

Inbox: `D:\le vault\Kaelearn\Inbox\`. Names, note formats and the storage rules: `system/vault.md`.

The vault has 1 GB of Sync storage for everything. Handwritten PDFs are big, and their originals
live in Notability anyway, so they never stay in the vault: they come in, get converted, and get
deleted.

1. **List and route.** For each PDF, read the name (`ANA 2026-10-14`, `... blurt`, `... attempt`,
   `REVIEW 2026-W42`, `TEACH ...`). Pair a lecture with its blurt. Route attempts to `/exercise`,
   review answers to `/review` (grading) and teach-backs to `/teach`. The rest of this skill
   covers lecture notes.
2. **Read the handwriting.** Read the PDF pages directly. If the writing is small or dense,
   render it sharper first (`python engine/kl.py look <pdf> --dpi 160`) and read the PNGs. Mark
   anything unreadable as `[?]`; never guess silently.
3. **Transcribe faithfully.** Write the student's own words and structure, as Markdown with
   `$...$` and `$$...$$`. Don't polish, add or reorder. Mark where each section starts in the
   original, as in `### Cauchy sequences *(p. 2)*`, so the student can find it in Notability.
   Describe a sketch in a line. If a sketch carries the idea, crop just that sketch to a JPG
   under 100 KB in `Lectures/<Course>/img/` and embed it. Pull the student's own ideas into
   `> [!idea]` callouts, verbatim.
4. **Blurt comparison.** List what is in the notes but missing or wrong in the blurt: these are
   the **Gaps**. Wrong items in the blurt are worth the most, so say exactly what was wrong.
   With no blurt, skip this and remind the student once that the blurt is the cheapest
   retrieval there is.
5. **Check.** If a statement in the notes is wrong (a missing hypothesis, a sign, a quantifier
   order), note it under **Check** with the reason. Never correct the transcript itself.
6. **Layer.** Write 4 to 8 review questions (retrieval, with collapsed answers; favour why and
   how over what) and at most five card ideas of the types Def, Why and Trigger
   (`system/method.md`), favouring the gaps.
7. **Concepts.** Create or update the concept note for each concept, and its hub. Link the
   lecture note to them and them back to it.
8. **File, then clear the Inbox.** Save the note to `Lectures/<Course>/<name>.md`. Once it is
   written and complete, delete the PDFs it was made from (the lecture and its blurt) from the
   Inbox. Delete only what you converted: keep `_Inbox.md` and anything not processed yet.
9. **Atlas.** New concepts enter at level 1 (next review +7 days). Concepts the blurt nailed
   don't level up yet; a blurt is one retrieval. `kl.py mirror` (it prints the vault size).
   Commit (`ingest: ANA 2026-10-14`) and push.

Reply with the note's name, the gaps in one line each, and tonight's card suggestions.
