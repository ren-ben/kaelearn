# Design: the Night Console

The student picked this look on 2026-10-11 from three rendered directions. It is the AURA-1
dashboard turned into paper: phosphor ink on charcoal, LED-dot frames with pixel title strips,
dithered plates for scenery, and Kael'thos as a phosphor hologram. All of it lives in
`engine/kaelearn.cls`; the reference document is `engine/specimen/specimen.tex`.

## Rules

- **Readable over dither.** Text sits on solid charcoal and stays crisp. Dither belongs to plates
  and figure fills only, never behind text.
- **Two inks.** Charcoal `#121212` (never pure black) and phosphor `#C5BCAB`, plus their greys.
  The one exception is red, and only for the wax seal on a folio's keystone theorem.
- **Kael'thos comes from the rig.** Use the PNGs in `engine/art/` (exported from the locked AURA-1
  rig). Never draw a cat. He never stands in front of a dithered sky: plates and he are separate.
- **4:3 pages** (210 x 280 mm), fitted to the 13-inch iPad. The wide right margin holds his asides
  and the student's handwriting.

## Palette (class colour names)

| Name | Hex | Use |
|---|---|---|
| `klpage` | `#121212` | the page |
| `klink` | `#C5BCAB` | body text |
| `klhi` | `#E6E0D4` | headings, emphasis, plotted data |
| `kldim` | `#8A8376` | labels, captions, asides, German terms |
| `kllow` | `#4C4741` | LED dots and rules |
| `klfaint` | `#1B1A18` | quiet fills |
| `klseal` | `#8E2B22` | wax only |

## Type

| Role | Face | Command |
|---|---|---|
| Body | EB Garamond Medium | default |
| Math | Garamond-Math | default |
| Part titles, "Why?" | UnifrakturMaguntia | `\goth` |
| Subheads, asides, German terms, captions | IM Fell English | `\fell`, `\de{}` |
| Labels, title strips, running head | Silkscreen | `\pix{}` |
| Numbers (page, problem, folio) | Tektur | `\tek` |
| Metadata values | Geist Mono | `\mono` |

## Components

```latex
\documentclass{kaelearn}
\subject{Analysis I}  \folio{03}  \title{Cauchy\\Sequences}  \shorttitle{Cauchy sequences}
\subtitle{One line on what this buys you.}  \sources{Cummings ch.~4 · Skript §2.3}
\readtime{2 min view · 14 min folio}  \filed{2026-10-11}
\plate{plate.png}{Zeno's nave}  \kael{reading}       % cover art: engine/art/<pose>.png
\begin{document}
\makecover                          % folios; sheets use \makeheader instead
\section{The trouble with limits}   % "PART I" label + Fraktur title
\opening{T}{o prove} that...        % small-caps opening words of a part
\aside{One lore line, at most one per page.}
\begin{twominute} ... \end{twominute}        % always first, readable in under 2 minutes
\begin{guessfirst} \begin{enumerate}\item ...\end{enumerate} \end{guessfirst}
\begin{terms} \term{Cauchy sequence}{Cauchy-Folge}{one-line meaning} \end{terms}
\begin{definition}{Name}{German name} ... \end{definition}
\begin{theorem}{Name}{German name} ... \end{theorem}
\begin{keystone}{Name}{German name} ... \end{keystone}   % once per folio, gets the wax seal
\begin{example}{Name} ... \end{example}
\begin{panel}{Kind}{name}{German name} ... \end{panel}   % any other framed block
\begin{panel}[unbreakable]{Kind}{name}{} ... \end{panel}  % [options]: keeps a short panel whole
\begin{proof} ... \end{proof}
\why{The question?}{The answer, two to five sentences.}
\begin{triggers} \trigger{You see this}{reach for that} \end{triggers}
\marginkael{delighted}               % a pose in the margin, at most one per folio
\begin{deck} \card{Def}{front}{back} \card{Why}{..}{..} \card{Trigger}{..}{..} \end{deck}
\problem[Cummings 4.12] Statement.  \answerspace{60mm}   % sheets: an LED-dot grid to write on
\problemparts                        % before \begin{document}: sections read "Problem 01" (debriefs)
\end{document}
```

Poses in `engine/art/`: `reading` (cover default), `curious`, `proud`, `delighted`, `serene`,
`questioning`, `cameo`, `peek`, `keeper` (hourglass: timed exams), `wave`, `asleep`.

## Figures

Real figures, never ASCII. TikZ and pgfplots inside the document, so the fonts and inks match:
`\begin{axis}[klplot, ...]`. Fill regions with `pattern={dither25}` or `pattern={dither50}` and
`pattern color=klink` for the 1-bit look. Data goes in `klhi`; reference lines go in `kldim`,
dashed. For heavy numerics (ODE solutions, phase portraits), compute the data in Python, write it
to a `.dat` file in the folio's `figs/` folder, and plot it with `\addplot table`. Caption with
`\plotcaption{...}`: say what to see, not what the axes are. Labels placed outside the axis
(`clip=false`) need room: set `width=.88\linewidth` on that axis, or the build warns about overfull lines.

## Plates

Each folio gets a dithered cover plate: `python engine/kl.py plate <scene> <folio-dir>/plate.png`.

| Scene | Fits |
|---|---|
| `nave` | sequences, limits, series, convergence (arches shrinking toward a limit) |
| `horizon` | the Codex, general, anything about infinity or completeness |
| `orrery` | mechanics, gravitation, oscillations, conics |
| `field` | ODEs, flows, vector fields, Rechenmethoden |
| `lattice` | linear algebra, vector spaces, linear maps |

To add a scene: a function in `engine/kl.py` that returns greys in [0, 1] for a (w, h) grid.
Register it in `SCENES` and keep it scenery only, without text or a cat.

## Folio anatomy (in this order)

1. Cover (`\makecover`)
2. Part I opens with the problem the topic solves, in his voice, half a page at most
3. `twominute`: the whole topic, readable in under 2 minutes
4. `guessfirst`: 2 or 3 questions to answer before reading on
5. `terms`: English, Deutsch, one line each
6. Parts: definitions, theorems (one `keystone`), a figure wherever one helps, a proof or proof
   idea, `\why` questions (at least two per folio)
7. `triggers` for the topic
8. `deck`: at most five cards, of the types Def, Why and Trigger (see `system/method.md`)

Aim for 4 to 8 pages. Sheets (reviews, exams, problem sets, debriefs) use `\makeheader`, `\problem`
and `\answerspace`, with no cover.

## Debrief anatomy

The record of an `/exercise` session; the reference is `engine/specimen/debrief.tex` and the
full order is in the skill. `\problemparts`, `\folio{Debrief}`, `\makeheader`, then the
session panel, one section per problem, the triggers and the deck. The variants come last, on
a page of their own with answer grids that fill it, so the student can redo them in Notability.
Short panels (the problem, weak points, the deep idea) take `[unbreakable]` so they never split
across a page break. About 2 pages per problem, plus the redo page.

## Check every render

After `kl.py build`, run `kl.py look <pdf>` and read the contact sheet. Check for overflowing
boxes, figures stranded on half-empty pages, misplaced margin notes and missing glyphs (the build
warns). Fix them before you publish.
