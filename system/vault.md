# The vault

Obsidian vault `D:\le vault`, synced to the iPad with Obsidian Sync. Kaelearn writes only
inside `D:\le vault\Kaelearn\`. Read anything else in the vault when it helps (the student
keeps `formula sheets/` and `Literature Notes/` there) and link to it, but never edit outside
`Kaelearn/` without asking.

Principle: the handwriting stays the source, in Notability. Obsidian is the index and the
retrieval layer on top of it, not a typed copy to reread.

## Storage

Obsidian Sync has 1 GB for the whole vault, and about 300 to 400 MB is already used. So:

- **Handwritten PDFs never stay.** They land in the Inbox, get converted, and get deleted. The
  originals live in Notability.
- **Empty the Inbox of what you used.** Every skill that consumes an Inbox file (`/ingest`,
  `/exercise`, `/review`, `/teach`, `/exam`) deletes it once its output is written. Delete only
  what was converted. Keep `_Inbox.md`, which keeps the folder syncing.
- **Small files only.** At most 3 MB per published file (`kl.py publish` refuses bigger ones),
  and JPGs under 100 KB for the rare kept sketch.
- **No needless versions.** Sync keeps a version of every change, so `kl.py publish` skips
  files that haven't changed.
- `kl.py publish` and `kl.py mirror` print the vault size. Above 800 MB, stop adding files and
  tell the student.

## Layout

```
Kaelearn/
  Inbox/                       Notability exports land here (from the iPad: Save to Files)
  Lectures/<Course>/           2026-10-14 ANA.md (img/ for the rare sketch worth keeping)
  Concepts/                    one atomic note per concept: Cauchy sequence.md
  Hubs/                        one per topic: Sequences.md
  Folios/<subject>/            published folio PDFs
  Debriefs/<subject>/          one PDF per exercise session: path, weak points, deep idea, variants
  Anims/<subject>/             standalone manim videos (videos of a folio or debrief sit beside it)
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
| `ANA UE03 attempt` | a homework attempt (for `/exercise`) |
| `REVIEW 2026-W42` | answers to a review sheet |
| `TEACH Cauchy sequence` | a handwritten teach-back |

Course codes are in `system/student.md`. If a name doesn't parse, look at the pages and ask
only when it's still unclear.

## Lecture note

File `Lectures/<Course>/2026-10-14 ANA.md`. The original stays in Notability; the Inbox copy
is deleted after ingest.

```markdown
---
course: ANA
date: 2026-10-14
lecture: 4
topics: [Sequences]
concepts: ["[[Cauchy sequence]]", "[[Bolzano-Weierstrass]]"]
source: Notability, "ANA 2026-10-14"
---
# Analysis 1 · Lecture 4 · 2026-10-14

## Transcript
### Cauchy sequences *(p. 2)*
(the student's words, faithfully, in Markdown with $...$ and $$...$$; unreadable bits as [?])

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
- Folio pages: `![[03-cauchy-sequences.pdf#page=3]]` (the student has pdf-plus installed)
- Callouts: `> [!idea]`, `> [!answer]-` (the `-` collapses)
- Links use file names without paths; keep names unique across the vault
