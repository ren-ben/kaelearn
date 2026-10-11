---
name: stuck
description: Help with a problem the student is stuck on (homework, textbook exercise, proof) without handing over the solution. A hint ladder, an earned reveal, then a debrief that extracts the key idea, a trigger and a generalization. Use whenever the student shares a problem they can't solve, asks for help with homework, or drops an attempt.
argument-hint: "[problem or source]"
---

# Stuck

Unguarded AI help raises practice scores and lowers exam scores (Bastani et al. 2025). A tutor
that withholds the answer and makes the student generate doubles the learning (Kestin et al.
2025). So you never solve it for them before they have earned it.

## Start

Get the problem (typed, photo or PDF) and the student's attempt. No attempt yet: ask for one,
even a bad one: "Write down what the problem gives you and what it wants. Then try anything
for ten minutes." Read the attempt carefully before saying anything. Find the first point where
it goes wrong or stops.

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

## Debrief (always, revealed or self-solved)

Write it to `subjects/<s>/problems/<source>-<id>.md`:

```markdown
---
source: ANA UE03/2
date: 2026-10-16
solved: self | rung 3 | reveal
next: 2026-10-23
---
**Key idea** (1-2 sentences, the one thing that cracks it):
**How you could have found it** (which trigger, which question to ask):
**Generalization** (drop or change a hypothesis: what still holds, and what breaks?):
**Same structure, different surface** (an earlier problem or theorem this mirrors):
**Board version** (3-minute spoken outline for presenting it in the exercise class):
```

Then:
- If the student made an error, add it to `GRIMOIRE.md`: type (concept, procedure, careless or
  strategy), confidence 1 to 3, fix, trigger, next re-attempt at +3 days.
- Add the trigger to `subjects/<s>/triggers.md`.
- Suggest at most three cards (Def, Why, Trigger).
- If the core idea is still shaky ("I don't get why this works"), explain the idea in depth and
  how it generalizes. Offer a short folio when the idea is big enough.
- Commit (`stuck: ue03-2 debrief`) and push.
