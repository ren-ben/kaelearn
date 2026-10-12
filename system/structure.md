# Where things go

The repo holds what Kael'thos makes (folios, sheets, session debriefs, the Atlas). The vault
holds the student's notes (transcripts, concept notes, hubs). Folders are created when first
needed, never in advance.

## Repo

```
kaelearn/
  CLAUDE.md  README.md  ATLAS.md  GRIMOIRE.md  kaelearn.json (vault path)
  system/                 method, voice, design, structure, vault, student
  engine/                 kaelearn.cls, kl.py, klmanim.py, fonts/, art/, specimen/
  codex/                  codex.tex, codex.pdf (the study system itself)
  subjects/<subject>/
    folios/NN-slug/       NN-slug.tex, NN-slug.pdf, plate.png, figs/, anims/
    debriefs/DATE-slug/   DATE-slug.tex, .pdf, key.md   session debriefs from /exercise
    anims/                <slug>.py, .mp4, .png   standalone videos (inside a folio or debrief: its anims/)
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
- debriefs: `YYYY-MM-DD-<slug>`, with the slug from the session's sources: `2026-10-16-ue03`
  (exercise sheet 3), `2026-10-18-cummings-4`, `2026-10-20-ue03-cummings-4`
- weeks: ISO, `2026-W42`

## Publishing

`kl.py publish <pdf>` copies into the vault, following the paths:

| Repo | Vault (`D:\le vault\Kaelearn\`) |
|---|---|
| `subjects/<s>/folios/.../x.pdf` | `Folios/<s>/x.pdf` |
| `subjects/<s>/debriefs/.../x.pdf` | `Debriefs/<s>/x.pdf` |
| `subjects/<s>/anims/x.mp4` | `Anims/<s>/x.mp4` (a video inside a folio or debrief lands beside its PDF) |
| `subjects/<s>/exams/.../x.pdf` | `Exams/<s>/x.pdf` |
| `review/.../review-2026-W42.pdf` | `Reviews/review-2026-W42.pdf` |
| `codex/codex.pdf` | `codex.pdf` |
| `engine/specimen/x` | `Specimens/x` (reference debrief and videos, plus a hand-made `Videos.md`) |
| `ATLAS.md`, `GRIMOIRE.md` | `Atlas.md`, `Grimoire.md` (every publish, or `kl.py mirror`) |

Give every PDF that goes to the vault a unique, readable name.

## Git

After every finished artifact: build, look, publish, update the Atlas, commit, push. Commit
subjects look like `folio: analysis 03 cauchy sequences`, `ingest: ANA 2026-10-14`,
`review: 2026-W42 graded`, `exercise: ANA UE03 debrief`. The Stop hook blocks the end of a turn
while changes are uncommitted or unpushed.
