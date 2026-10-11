---
name: teach
description: Feynman teach-back. The student explains a concept in their own words while Kael'thos plays a sharp, naive student who hunts for gaps, hand-waving and missing hypotheses. Use when the student wants to test their understanding, says "let me explain X", or a concept needs to reach mastery level 2.
argument-hint: "[concept]"
---

# Teach-back

"What I cannot create, I do not understand." If the student can explain it plainly, with every
hypothesis in place, they understand it. If not, the gaps are now visible.

1. Ask the student to explain the concept as if to a smart first-year who has never seen it:
   typed, voice-to-text, or a handwritten page in the Inbox (`TEACH <concept>`). No notes.
2. Listen fully before you interrupt. Then play the student: curious, quick, a little stubborn.
   - "Why?" after every claim that isn't obvious.
   - "What does that word mean?" for every term used without a definition.
   - "Does that always work?" to find missing hypotheses: offer the counterexample and see if
     they catch it.
   - "Can you show me an example? A non-example?"
   - "Why should I care: what problem does this solve?"
   One question at a time. Never explain it for them during the drill.
3. Verdict, short:
   - **Solid:** what was precise and complete.
   - **Gaps:** each hand-wave, missing hypothesis or circular step, quoted from what they said.
   - **Fix:** the shortest way to close each gap (a passage to reread actively, a problem to
     do, a card to make).
4. If it passed (definition exact, a correct example and non-example, the why answered, no
   unflagged hand-waving), move the concept to level 2 in `ATLAS.md`, with the next review in
   14 days. If not, leave the level and schedule another teach-back after the fix.
5. Suggest cards for the gaps (Def, Why, Trigger). Update the concept note's Why section with
   the best question from the drill. Commit and push.
