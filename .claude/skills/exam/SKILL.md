---
name: exam
description: Exam preparation in four modes. Timed mock exams, oral exam drills, board drills for presenting homework in exercise classes, and cumulative mixed problem sets. Use when an exam or exercise class is coming up, or when the student asks for a mock, an oral drill, board practice or a mixed set.
argument-hint: "[mock | oral | board | mixed] [course]"
---

# Exam

Before the first session for a course, check `system/student.md` for its exam format. If it
isn't there, ask and record it.

## Mock (timed written exam)

1. Build from the Skript, the homework sheets, old exams the student provides, and the
   grimoire. Match the real exam's length, style and time limit. Mix the topics, with no labels.
2. Write `subjects/<s>/exams/<slug>/<slug>.tex` (`\makeheader`, `\problem`, `\answerspace`)
   with the time limit and the points per problem. Write the solutions and the marking scheme
   to `key.md` in the same folder. Never show the key before grading.
3. Build, look, publish. The student writes it under exam conditions and exports it to the
   Inbox as `MOCK <slug>`.
4. Grade strictly against the key, the way the examiner would: points, and where they were lost.
   Errors go to `GRIMOIRE.md`; mastery moves in `ATLAS.md` (a correct transfer counts toward
   level 4). Commit and push.

## Oral

In chat, as the examiner. Adapt the difficulty to the answers. Rotate through: "State ...",
"Prove ...", "Why is ... necessary?", "What if we drop ...?", "Give an example where ... fails",
"How does this connect to ...?". One question at a time, follow-ups on weak answers, no help
during the drill. End with a mark (1 to 5, Austrian scale), with reasons, and the three weakest
points to fix.

## Board

For exercise classes where the student presents at the board. Pick a solved problem from
`subjects/<s>/problems/` (or the student's choice). The student explains it out loud from
memory, typed or as voice-to-text, in about 3 minutes. Then ask what the tutor would ask:
"Why can you assume that?", "What if n = 0?", "Where did you use the hypothesis?". Give feedback
on clarity, the order of ideas and any shaky step.

## Mixed (cumulative set)

A problem set over everything so far, interleaved, with no topic labels and no order by section.
Weight it toward older and weaker material (low levels in `ATLAS.md`, open grimoire entries).
Recognising which method applies is half of each problem. Same build, publish and grading path
as a mock, without the time pressure.
