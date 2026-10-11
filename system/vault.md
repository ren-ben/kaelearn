# The vault

Obsidian vault `D:\le vault`, synced to the iPad with Obsidian Sync. Kaelearn writes only
inside `D:\le vault\Kaelearn\`. Read anything else in the vault when it helps (the student
keeps `formula sheets/` and `Literature Notes/` there) and link to it, but never edit outside
`Kaelearn/` without asking.

Principle: the handwriting stays the source. Obsidian is the index and the retrieval layer on
top of it, not a typed copy to reread.

## Layout

```
Kaelearn/
  Inbox/                       Notability exports land here (from the iPad: Save to Files)
  Lectures/<Course>/           2026-10-14 ANA.md, plus pdf/2026-10-14 ANA.pdf
  Concepts/                    one atomic note per concept: Cauchy sequence.md
  Hubs/                        one per topic: Sequences.md
  Folios/<subject>/            published folio PDFs
  Reviews/  Exams/<subject>/   published sheets
  Atlas.md  Grimoire.md        mirrors of the repo files (never edit these here)
  codex.pdf
```

## Inbox names

The student names Notability notes like this, and the exported PDFs keep the names:

| Name | Is |
|---|---|
| `ANA 2026-10-14` | lecture notes (course code, date) |
| `ANA 2026-10-14 blurt` | the blurt for that lecture |
| `ANA UE03 attempt` | a homework attempt (for `/stuck`) |
| `REVIEW 2026-W42` | answers to a review sheet |
| `TEACH Cauchy sequence` | a handwritten teach-back |

Course codes are in `system/student.md`. If a name doesn't parse, look at the pages and ask
only when it's still unclear.

## Lecture note

File `Lectures/<Course>/2026-10-14 ANA.md`; the original goes to `Lectures/<Course>/pdf/`.

```markdown
---
course: ANA
date: 2026-10-14
lecture: 4
topics: [Sequences]
concepts: ["[[Cauchy sequence]]", "[[Bolzano-Weierstrass]]"]
source: "[[2026-10-14 ANA.pdf]]"
---
# Analysis 1 · Lecture 4 · 2026-10-14

## Transcript
### Cauchy sequences
(the student's words, faithfully, in Markdown with $...$ and $$...$$; unreadable bits as [?])

> [!page]- Original, p. 1
> ![[2026-10-14 ANA.pdf#page=1]]

> [!idea] Your idea
> (anything the student wrote that goes beyond the lecture, pulled out verbatim)

## Layer
**Gaps** (in the notes, missing from the blurt): ...
**Check** (anything in the notes that looks wrong, with the reason): ...

### Review questions
1. Question?
   > [!answer]-
   > Answer.

### Cards to make
- Def: ...
- Why: ...
- Trigger: ...
```

Never correct the student's notes silently: put corrections under **Check**.

## Concept note

File `Concepts/Cauchy sequence.md`, named in English. The German name goes in `aliases`, so
both link.

```markdown
---
aliases: [Cauchy-Folge]
hub: "[[Sequences]]"
---
# Cauchy sequence *(Cauchy-Folge)*
**Definition.** $\forall\varepsilon>0\ \exists N\ \forall m,n\ge N: |a_m-a_n|<\varepsilon$.

**Why it exists.** (two or three sentences: the problem it solves)

**Examples / non-examples / edge cases.** ...

**Why?** (two why-questions with collapsed answers)

**Appears in.** [[2026-10-14 ANA]] · Folio [[03-cauchy-sequences.pdf]] · [[ue03-2]]
```

Keep concept notes atomic: one concept each. Update the existing note when a concept comes
back; never duplicate it.

## Hub

File `Hubs/Sequences.md`: a short orientation paragraph, the concepts in a sensible order with
one line each, prerequisites (links to other hubs), the folios, and the open questions. Hubs are
what the graph view clusters around.

## Obsidian specifics

- Math: `$...$` and `$$...$$`
- PDF pages: `![[file.pdf#page=3]]` (the student has pdf-plus installed)
- Callouts: `> [!idea]`, `> [!page]-`, `> [!answer]-` (the `-` collapses)
- Links use file names without paths; keep names unique across the vault
