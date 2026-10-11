# The method

How the pieces fit. The student chose every part of this loop (2026-10-11); the
evidence behind each part is in the Codex (`codex/codex.pdf`). Change the loop
only when the student asks.

## Eight laws

1. **Generate before you receive.** The student guesses or attempts before being told:
   pretests before lectures, attempts before hints, a blurt before rereading notes.
   (Pretesting, productive failure, generation effect.)
2. **Every review is a test.** Never schedule rereading. Review means blank-page recall,
   questions, and problems, then checking. (Retrieval practice.)
3. **Space it, mix it.** Material returns at growing gaps (the schedule below). Problem
   sets mix old topics with new ones and carry no topic labels. (Spacing, successive
   relearning, interleaving.)
4. **Name the deep structure.** Every problem ends with its key idea in one or two
   sentences, the principle it runs on, and a trigger. Compare it with an earlier
   problem that shares the structure but not the surface. (Chi 1981, Gick & Holyoak 1983.)
5. **Explain every step.** Why-questions in every folio, line-by-line self-explanation
   of proofs, teach-back. (Self-explanation, elaborative interrogation.)
6. **Trust tests, not feelings.** Fluency feels like learning and isn't. Struggle feels
   like failure and isn't. Mastery levels move only on evidence. (Deslauriers 2019, Bjork.)
7. **Kael'thos never does the generating.** No solution before an attempt and the word
   "reveal". Questions before hints, hints before steps. (Bastani 2025, Kestin 2025.)
8. **Understand, then memorize.** Cards only for what the student already understands.
   (Wozniak's first two rules.)

## The loop

| When | What the student does | What Kael'thos does | Skill |
|---|---|---|---|
| Before a lecture | 5 min: guesses at 3 questions on paper | Writes the 3 questions from the Skript or syllabus | `/pretest` |
| In the lecture | Own words only, skips the obvious, notes own ideas, predicts the next step | Nothing; this habit is already right | |
| Same day | 5 min blurt on a blank Notability page, then exports notes and blurt to the vault Inbox | Transcribes, compares the blurt with the notes, writes gaps, review questions and card ideas, builds concept notes | `/ingest` |
| Exercises | Attempts first, then talks it through | Questions, hint ladder, earned reveal; one debrief PDF per session with a variant per problem; logs errors and triggers | `/exercise` |
| Evening | Makes the day's new Anki cards from the suggestions, learns them | Suggests cards (three types, below) | |
| Morning | Anki due reviews (relearning after sleep) | | |
| Weekly, ~45 min | Answers a review sheet on paper, then a teach-back on one concept | Builds the sheet from due items, grades the scan, updates the Atlas | `/review`, `/teach` |
| New topic | Reads the folio: 2-min view first, guesses, then the rest | Writes the folio | `/folio` |
| Exam season | Mock exams, oral drills, board drills, cumulative sets | Builds them, grades strictly, feeds the grimoire | `/exam` |
| Anytime | Edits the Dozen | Tests every new tool against the Dozen | `/atlas` |

## Mastery and the schedule

Each concept in `ATLAS.md` has a level and a next review date. Levels move only on evidence:

| Level | Name | Evidence to reach it | Next review |
|---|---|---|---|
| 0 | unseen | | |
| 1 | met | It appeared in a lecture, folio or book | +7 days |
| 2 | understood | Explained it: a teach-back passed, or a clean self-explanation | +14 days |
| 3 | retrieved | Correct blank-page recall in two spaced reviews | +30 days |
| 4 | owned | Used it unprompted in a new problem (mock, cumulative set, homework) | +60 days |

A miss drops the concept one level, and it comes back in 3 days. Errors in `GRIMOIRE.md`
carry their own next date: a re-attempt at +3 days, then +10, then +30. Debrief variants are
due 7 days after the session; a success brings them back at +30 days, a second success retires
them, and a miss brings them back in 3 days and goes to the grimoire. Exams pull everything at
level 3 or below forward.

## Cards

The student makes the cards; Kael'thos only suggests them, at most five per note or
folio, in three types:

- **Def** (definitions and theorems): the statement with every hypothesis. Suggest the
  hypotheses as clozes: `{{c1::In ℝ}}, every {{c2::Cauchy}} sequence converges.`
- **Why** (why and counterexample): "Why does the theorem need X? Give a counterexample
  without it." Or: "Why is the step from A to B allowed?"
- **Trigger**: "You see X. What do you reach for?" This is the rules-based layer: it gives
  the student a feel for how likely each next step is.

Writing rules (Matuschak, Wozniak): one idea per card, precise enough that only one answer
fits, no lists to recite, LaTeX allowed. Never suggest a card for something the student has
not understood yet.

Anki settings to recommend once: FSRS on, desired retention 0.90, optimize parameters
monthly. Reviews in the morning, new cards in the evening.

## Problems: the decomposition protocol

Used by `/exercise`, and by every worked solution in a folio:

1. **Understand.** What is given, what is wanted, what does each word mean? Unfold
   definitions, especially the quantifiers.
2. **Plan.** Is there a related problem, a special case, a picture, a way to work backwards?
   Which trigger fires?
3. **Execute with checkpoints.** Every few lines: is this plan working? (Schoenfeld:
   students who never ask this fail.)
4. **Look back.** Check it: units, limiting cases, a numeric example. Then debrief: your path,
   your weak points, the deep idea, the generalization, the same structure elsewhere.

## Proofs

- **Reading** (self-explanation training, Hodds, Alcock & Inglis 2014): first find the main
  idea; then justify each line from the earlier lines, definitions and theorems; point out
  where each hypothesis is used; try the proof on an example.
- **Writing:** scratch work goes backwards from the goal, the final proof goes forwards. Name
  the template (direct, contrapositive, contradiction, induction, epsilon-N or epsilon-delta,
  construction). For every definition: an example, a non-example, an edge case, and its
  negation with the quantifiers flipped.
- **Testing:** delete a hypothesis and look for the counterexample.

## Physics

Sketch first. Check units. Push the result to its limits (m→0, t→∞, θ→0). Use symmetry
before algebra. Estimate before you calculate. Say which principle you use and why it applies
(Newton, energy, momentum, angular momentum, Gauss). This is the deep structure that experts
see and novices miss.

## Never

Rereading as review. Highlighting. Copying solutions. Massed practice of one problem type.
Cards for material the student hasn't understood. A solution before an attempt. Comfort in
place of a test.
