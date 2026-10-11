---
name: review
description: The weekly review ritual. Build a ~45-minute retrieval sheet (blank-page recall prompts plus interleaved, unlabeled problems, including old topics coming due), and later grade the student's handwritten answers and update mastery in the Atlas. Use when the student asks for their weekly review, when reviews are due, or when a REVIEW export appears in the Inbox.
argument-hint: "[build | grade]"
---

# Review

Every review is a test, never a reread (`system/method.md`).

## Build

1. **Collect what's due** by today + 2 days:
   - concepts in `ATLAS.md` whose `next` date has passed
   - `GRIMOIRE.md` entries due for a re-attempt
   - problem debriefs with a due `next:` date
   - this week's lecture gaps (the **Gaps** in this week's lecture notes)
2. **Write the sheet** at `review/YYYY-Www/review-YYYY-Www.tex` (`\makeheader`, `\problem`, `\answerspace`):
   - **Recall** (about 15 min): 4 to 8 blank-page prompts. "State and prove ...", "Why does ...
     need ...", "Draw the picture behind ...". No hints on the sheet.
   - **Problems** (about 25 min): 4 to 6 problems, interleaved, with no topic labels and no
     section order. At least two from older material, and at least one where the method has to
     be recognised (same structure, new surface). Use fresh problems, not copies of solved ones.
   - **Grimoire** (about 5 min): due re-attempts, reworded.
   - Last line: "If one of your Dozen moved this week, write one sentence about it."
3. **Build, look, publish.** Commit and push.
4. Tell the student: answer on paper or in Notability (import the PDF), no notes, timer on, then
   export to the Inbox as `REVIEW YYYY-Www`.

## Grade

1. Read the scan. Grade each item strictly: correct, partly (say exactly what was missing) or wrong.
2. Write `review/YYYY-Www/graded.md`: the per-item verdict, the gist of the right answer, and
   the misconception behind each miss.
3. Update `ATLAS.md` by the rules in `system/method.md`: a correct recall moves a concept toward
   level 3 (it needs two spaced successes), a correct transfer problem toward level 4. A miss
   drops one level, with the next review in 3 days. New errors go to `GRIMOIRE.md`, with
   confidence (confident errors are the most valuable ones to fix).
4. `kl.py mirror`, commit (`review: YYYY-Www graded`), push.
5. Reply in three lines: what's solid, what slipped, what's due next week.
