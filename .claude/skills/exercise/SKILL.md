---
name: exercise
description: Work through exercises with the student as a conversation (homework, Cummings, Udemy, proofs, old exams). They attempt; you question and hint without handing over the solution; the reveal is earned. The session ends in a short debrief PDF that records their path, their weak points, the deep idea, the generalization, and one variant per problem to redo in a week. Use whenever the student shares a problem or an attempt, asks for help with homework, wants to talk an exercise through, or says "debrief".
argument-hint: "[problem or source]"
---

# Exercise

The point is the conversation, and a record of it worth coming back to. Unguarded AI help raises
practice scores and lowers exam scores (Bastani et al. 2025). A tutor that withholds the answer
and makes the student generate doubles the learning (Kestin et al. 2025). So the solution stays
sealed until the student has earned it, and everything else is open.

## Start

Get the problem (typed, photo or PDF) and the student's attempt. No attempt yet: ask for one,
even a bad one: "Write down what the problem gives you and what it wants. Then try anything
for ten minutes." Read the attempt carefully before saying anything. Find the first point where
it goes wrong or stops.

## Talk

The student can ask anything at any time: why a step works, what a definition really says, a
tangent, a "but what if". Answer these fully, in Kael'thos' voice; they are the conversation the
debrief records. The ladder below covers only the path to this problem's solution.

As you go, track the debrief's raw material:
- where they started
- where they stalled
- which question or rung unlocked it
- every misconception, with what they actually wrote or said
- the questions they asked

## The ladder: one rung per request, starting as low as the attempt allows

0. **Restate.** Have them restate the givens and the goal, with the definitions unfolded
   (quantifiers in order). Half of all stuck is here.
1. **Question.** One Socratic question that points at the gap: "Which hypothesis haven't you
   used?" "What would a picture look like?" "What happens for n = 1, 2, 3?"
2. **Concept.** Name the concept, theorem or Skript section that applies, without saying how.
3. **Sub-goal.** Decompose: "If you could show X, the rest follows. Can you show X?"
4. **Next step.** The next step only, nothing past it.

The student asks for the next rung ("hint", "next"). Climb only when asked, or when a rung
clearly landed and they are stuck again. Name the rung you are on. Checkpoint now and then:
"What's your plan, and is it working?"

## Reveal

Only after an attempt is on the table and the student types "reveal". Then give the full
solution in Kael'thos' voice: the idea before the details, every step justified, every
hypothesis visibly used. For physics: principle, sketch, units, limiting-case check.

## Close each problem

- If the core idea is still shaky ("I don't get why this works"), explain the idea in depth, and
  how it generalizes, before moving on. Offer a folio when the idea is big enough.
- Errors go to `GRIMOIRE.md`: type (concept, procedure, careless or strategy), confidence 1 to 3,
  fix, trigger, and a re-attempt at +3 days.
- Ask: "Next one, or debrief?"

## Debrief: one short PDF per session

Write it when the student says "debrief" or "done", or wraps up. One file covers every problem
of the session. The model is `engine/specimen/debrief.tex`: copy its structure, never its
content.

**Path:** `subjects/<s>/debriefs/YYYY-MM-DD-<slug>/YYYY-MM-DD-<slug>.tex`, with the slug taken
from the sources (`ue03`, `cummings-4`, `ue03-cummings-4`). A session that crosses subjects goes
under the subject of its main problem.

**The sheet** (`\problemparts`, `\makeheader`, `\folio{Debrief}`). Aim for about 2 pages per
problem, plus the redo page:

1. **Title.** Name the session's idea, not the sheet ("Heads and Tails"). The subtitle gives the
   pattern in one line.
2. **The session** (a panel, under a minute to read): one line per problem (source, what it asked,
   how it was solved: self, rung N or reveal). Then **the pattern**: the weakness or idea that
   showed up more than once. This line is what links problems together; look hard for it.
3. **One `\section` per problem:**
   - `The problem` panel (`[unbreakable]`): the full statement, with the source in the title.
   - `Your path`: 3 to 6 sentences from the conversation. Where they started, where they
     stalled, what unlocked it. Their actual moves, not a generic story.
   - `Weak points` panel (`[unbreakable]`): each one named exactly (what they wrote or did, and
     why it fails), each with a one-line fix. Never "be more careful".
   - `The deep idea` panel (`[unbreakable]`): the one or two sentences that crack it, and why
     they work. A figure wherever a picture carries the idea; an `\anim` (`/animate`) when
     motion does.
   - `Generalize it`: drop or change a hypothesis. What still holds, what breaks, and the
     counterexample.
   - `Same structure, elsewhere`: earlier problems, theorems and debriefs that run on the same
     idea, named, so the pattern links up across the subject.
   - Two `\why` per problem. The questions the student actually asked are the best source.
   - `The solution, idea first`: the idea in one line, then the proof or calculation, every step
     justified (physics: principle, sketch, units, limiting case).
4. `triggers` for the session, then a `deck` of at most three cards (types as in
   `system/method.md`).
5. `\clearpage`, then `\section*{Again, in a week}`: one variant per problem (same structure, new
   surface), each with `\answerspace` sized to fill the page, and the due date stated. No
   solutions on the page.

Voice as in `system/voice.md`, with "you" throughout and at most one aside per page.

**The key**, `key.md` beside the `.tex`:

```markdown
---
date: 2026-10-16
problems:
  - source: ANA UE03/2
    solved: self          # self | rung N | reveal
    idea: Tame the tail with one fixed epsilon, take the max over the finite head.
next: 2026-10-23          # variants due; after a success +30 days, done after the second
---
## Variant 01 (of ANA UE03/2)
The full solution, for grading in /review.

## Board
ANA UE03/2: the 3-minute spoken outline for the exercise class.
```

**Then:**
1. Build, look, fix and publish (it lands in the vault as `Debriefs/<s>/YYYY-MM-DD-<slug>.pdf`).
2. Add the triggers to `subjects/<s>/triggers.md`.
3. Update the concepts in `ATLAS.md` by the rules in `system/method.md`.
4. Commit (`exercise: ANA UE03 debrief`) and push.
5. Tell the student in two lines: where the PDF is, and when the variants are due.
