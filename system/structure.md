# Where things go

The repo holds what Kael'thos makes (folios, sheets, problem debriefs, the Atlas). The vault
holds the student's notes (transcripts, concept notes, hubs). Folders are created when first
needed, never in advance.

## Repo

```
kaelearn/
  CLAUDE.md  README.md  ATLAS.md  GRIMOIRE.md  kaelearn.json (vault path)
  system/                 method, voice, design, structure, vault, student
  engine/                 kaelearn.cls, kl.py, fonts/, art/, specimen/
  codex/                  codex.tex, codex.pdf (the study system itself)
  subjects/<subject>/
    folios/NN-slug/       NN-slug.tex, NN-slug.pdf, plate.png, figs/
    problems/             <source>-<id>.md   debriefs from /stuck
    exams/<slug>/         mock exams and cumulative sets (.tex, .pdf, key.md)
    triggers.md           every trigger of the subject, grown by folios and debriefs
    pretests.md           pretest questions, newest first
  review/YYYY-Www/        review-YYYY-Www.tex, review-YYYY-Www.pdf, graded.md
  .claude/                settings, output style, skills, hooks
```

## Subjects

Subject folders follow knowledge, not courses: the analysis lecture and Cummings' book both
feed `analysis/`. The mapping from course to subject is in `system/student.md`. Current
subjects: `analysis`, `linear-algebra`, `physics`, `methods`, `proofs`, `odes`. Add one only
when a body of material doesn't fit any of these, and record it in `student.md` and `ATLAS.md`.

## Names

- kebab-case ASCII: `03-cauchy-sequences`, never spaces or umlauts in repo paths
- folios are numbered per subject, two digits, in the order they were written
- problem debriefs: `<source>-<id>`: `ue03-2.md` (exercise sheet 3, problem 2),
  `cummings-4-12.md`, `udemy-proofs-s5-3.md`
- weeks: ISO, `2026-W42`

## Publishing

`kl.py publish <pdf>` copies into the vault, following the paths:

| Repo | Vault (`D:\le vault\Kaelearn\`) |
|---|---|
| `subjects/<s>/folios/.../x.pdf` | `Folios/<s>/x.pdf` |
| `subjects/<s>/exams/.../x.pdf` | `Exams/<s>/x.pdf` |
| `review/.../review-2026-W42.pdf` | `Reviews/review-2026-W42.pdf` |
| `codex/codex.pdf` | `codex.pdf` |
| `ATLAS.md`, `GRIMOIRE.md` | `Atlas.md`, `Grimoire.md` (every publish, or `kl.py mirror`) |

Give every PDF that goes to the vault a unique, readable name.

## Git

After every finished artifact: build, look, publish, update the Atlas, commit, push. Commit
subjects look like `folio: analysis 03 cauchy sequences`, `ingest: ANA 2026-10-14`,
`review: 2026-W42 graded`, `stuck: ue03-2 debrief`. The Stop hook blocks the end of a turn
while changes are uncommitted or unpushed.
