# Atlas

The map of everything learned. Kael'thos keeps it current (`/atlas`); it is mirrored into the
vault as `Atlas.md`.

Levels: **0** unseen · **1** met · **2** understood · **3** retrieved · **4** owned.
`Next` is the next review date. The rules are in `system/method.md`.

## The Dozen

Twelve open questions you carry around (Feynman's habit, via Rota). Every new theorem or trick
gets tested against them.

*Not chosen yet. Kael'thos asks in the first session.*

## Due

| What | When |
|---|---|
| Grimoire re-attempts: 7 entries from ANA UE01 | 2026-10-15 |
| Debrief variants: ANA UE01, 8 problems (`Debriefs/analysis/2026-10-12-ue01.pdf`, last pages) | 2026-10-19 |
| First review of the 10 concepts met in ANA UE01 | 2026-10-19 |
| First review of the 14 rigid-body concepts (EP1, folios physics 01 and 02) | 2026-11-16 |

## Analysis

Analysis 1 (ANA) · Cummings, *Real Analysis*.

```mermaid
flowchart LR
  subgraph RN[Real numbers]
    F[Field] --> AV[Absolute value] --> PN[p-norm]
  end
  subgraph FN[Functions]
    IP[Image and preimage]
    INJ[Injective function] --> INV[Inverse function]
    SUR[Surjective function] --> INV
    INJ --> SM[Strictly monotone function]
  end
  IP --> SUR
```

| Concept | Level | Next | Folio | Last evidence |
|---|---|---|---|---|
| [[Field]] | 1 | 2026-10-19 | | 2026-10-12 ANA UE01/1: checked $\mathbb{Z}_2$, one case argued by an instance |
| [[Absolute value]] | 1 | 2026-10-19 | | 2026-10-12 ANA UE01/2: (a) clean, (b) key step unproved |
| [[p-norm]] | 1 | 2026-10-19 | | 2026-10-12 ANA UE01/3: sets right, inclusions from the sketch |
| [[Image and preimage]] | 1 | 2026-10-19 | | 2026-10-12 ANA UE01/4: all eight right; arrows in (a) mistyped |
| [[Injective function]] | 1 | 2026-10-19 | | 2026-10-12 ANA UE01/5: all verdicts right |
| [[Surjective function]] | 1 | 2026-10-19 | | 2026-10-12 ANA UE01/5: verdicts right; reversed inequality in 5c |
| [[Inverse function]] | 1 | 2026-10-19 | | 2026-10-12 ANA UE01/5b: $f_2^{-1}=f_2$, with $f^{-1}
eq 1/f$ noted |
| [[Strictly monotone function]] | 1 | 2026-10-19 | | 2026-10-12 ANA UE01/6: right structure, wrong reason cited |

Homework solved on paper counts as "met". Level 2 needs a teach-back or a clean self-explanation.

## Linear algebra

Lineare Algebra 1 (LA).

*No concepts yet.*

## Physics

Experimentalphysik 1 (EP1).

```mermaid
flowchart LR
  subgraph RB[Rigid bodies]
    COM[Centre of mass] --> RBD[Rigid body]
    RBD --> AV[Angular velocity]
    TQ[Torque] --> AM[Angular momentum]
    AV --> AM
    AV --> MI[Moment of inertia]
    MI --> PAT[Parallel-axis theorem]
    AM --> IT[Inertia tensor]
    MI --> IT
    IT --> PA[Principal axes]
    AV --> ROL[Rolling]
    PAT --> ROL
    PAT --> PP[Physical pendulum]
    TQ --> PP
    AM --> PRE[Precession]
    AV --> IC[Instantaneous centre of rotation]
    IC --> ROL
    MI --> EM[Effective mass]
    EM --> ROL
  end
```

| Concept | Level | Next | Folio | Last evidence |
|---|---|---|---|---|
| [[Rigid body]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] | 2026-11-09 EP1 notes + folio 01 |
| [[Angular velocity]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] | 2026-11-09 EP1 notes: $\vec v_i = \vec v_s+\vec\omega\times\vec r_{si}$ written down |
| [[Centre of mass]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] · [[02-drehen-im-bild.pdf]] | 2026-11-09 EP1 notes: gravity torque $= M\vec R_s\times\vec g$, stability stated |
| [[Torque]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] | 2026-11-09 EP1 notes + folio 01 |
| [[Moment of inertia]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] | 2026-11-09 EP1 notes: cylinder $I_{zz} = \frac12MR^2$ computed |
| [[Parallel-axis theorem]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] | 2026-11-09 folio 01 |
| [[Angular momentum]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] | 2026-11-09 EP1 notes + folio 01 |
| [[Inertia tensor]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] | 2026-11-09 EP1 notes: derived; sign slip in $L_1$ (fixed in folio) |
| [[Principal axes]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] | 2026-11-09 folio 01 |
| [[Rolling]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] | 2026-11-09 folio 01 + video |
| [[Physical pendulum]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] | 2026-11-09 folio 01 |
| [[Precession]] | 1 | 2026-11-16 | [[01-starrer-koerper.pdf]] | 2026-11-09 folio 01 |
| [[Instantaneous centre of rotation]] | 1 | 2026-11-16 | [[02-drehen-im-bild.pdf]] | 2026-11-09 folio 02 |
| [[Effective mass]] | 1 | 2026-11-16 | [[02-drehen-im-bild.pdf]] | 2026-11-09 folio 02 |

## Methods

Physikalische Rechenmethoden (RM).

*No concepts yet.*

## Proofs

Udemy proofs course (PRF), and the proofs met in analysis and linear algebra.

```mermaid
flowchart LR
  IMP[Implication] --> IND[Mathematical induction]
```

| Concept | Level | Next | Folio | Last evidence |
|---|---|---|---|---|
| [[Implication]] | 1 | 2026-10-19 | | 2026-10-12 ANA UE01/7: $A\Rightarrow B$ right; converse refuted with part of $A$ |
| [[Mathematical induction]] | 1 | 2026-10-19 | | 2026-10-12 ANA UE01/8: correct; step opened with the goal |

## ODEs

Udemy differential equations course (ODE).

*No concepts yet.*
