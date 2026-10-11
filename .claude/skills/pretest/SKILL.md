---
name: pretest
description: Five-minute pretest before a lecture, with three guess-first questions on the next lecture's topic, drawn from the Skript or syllabus. Use when the student says they have a lecture coming up, asks for pre-questions, or names the next lecture's topic.
argument-hint: "[course] [topic]"
---

# Pretest

Guessing before a lecture makes the lecture stick, even when every guess is wrong
(Pan & Carpenter 2023). It takes five minutes.

1. Find the next topic: the student says it, or work it out from the Skript's next section,
   the last ingested lecture note, or the syllabus.
2. Write exactly three questions the lecture will answer:
   - one about the central object ("What should a 'limit' of a function at a point mean, if
     the function isn't even defined there?")
   - one prediction ("Guess the derivative of $x^x$. How would you even start?")
   - one why or what-if ("Why might uniform convergence matter for swapping a limit and an
     integral?")
   They must be answerable by guessing, without the lecture. No definitions to look up.
3. Show them in chat. The student writes guesses on paper or in Notability (in the lecture
   note, so the guesses get ingested with it).
4. Prepend them to `subjects/<s>/pretests.md` under a date heading. During `/ingest`, check
   whether the notes answer them and add any that stayed open to the review questions.
5. Commit and push.

No answers in chat. The lecture answers them.
