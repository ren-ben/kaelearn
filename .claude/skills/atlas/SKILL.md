---
name: atlas
description: Maintain ATLAS.md, the map of everything learned (subjects, concept maps in Mermaid, mastery levels, review dates, the Dozen), and its vault mirror and hubs. Use when the student asks for the map, an overview of what they know, what's due, or to edit the Dozen, and after any work that changes mastery.
---

# Atlas

`ATLAS.md` is the state of the student's knowledge and the source of truth for mastery and
review dates. Every other skill updates it; this skill tidies it and answers questions about it.

## Shape

- **The Dozen:** the student's twelve open questions (Feynman, via Rota). Test every new
  theorem or trick against them. When one moves, say so and note the date.
- **Due:** concepts and grimoire entries due in the next 7 days, refreshed on every update.
- **Per subject:** a Mermaid `flowchart LR` concept map (prerequisite → concept; at most about
  25 nodes per map, so split by hub when it grows), then a table: Concept (a `[[wikilink]]` to
  the concept note) | Level 0-4 | Next | Folio | Last evidence.
- Links are Obsidian wikilinks, because the file is read in the vault (as `Atlas.md`).

## Doing it

1. Read `ATLAS.md`, `GRIMOIRE.md` and the latest debriefs and graded reviews.
2. Apply the level and schedule rules in `system/method.md`. Never raise a level without
   evidence: the date and what happened go in "Last evidence".
3. Keep each Mermaid map readable: group with subgraphs by hub, and keep edges only for real
   prerequisites (you need A to state or prove B).
4. Sync the hubs in the vault, so each hub lists its concepts in order.
5. `python engine/kl.py mirror`, commit (`atlas: ...`), push.

When asked "what do I know" or "where am I": answer from the Atlas in a few lines (strong,
shaky, due), and offer the next best action.
