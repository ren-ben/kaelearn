# Kaelearn

A study system that runs in Claude Code. Kael'thos writes your folios (study PDFs in the AURA-1
Night Console look), turns your Notability notes into Obsidian notes, coaches problems without
giving away answers, and keeps the map of everything you've learned. Start with
`codex/codex.pdf`: the research, and the system you chose.

## Setup

1. Install XeLaTeX (MiKTeX or TeX Live), Python 3.11+ with `pip install numpy pillow`, and Node.
2. Check `kaelearn.json` points at your vault folder (`D:/le vault/Kaelearn`).
3. Connect GitHub:
   ```
   git remote add origin https://github.com/<you>/kaelearn.git
   git push -u origin main
   ```
4. Open Claude Code in this folder. The Kael'thos output style and the push hook load from
   `.claude/`.

## Daily use

- **Before a lecture:** `/pretest ANA sequences`
- **After a lecture:** in Notability, blurt for 5 minutes on a blank page. Export the notes and
  the blurt as PDF and use Save to Files to put them in `Obsidian/le vault/Kaelearn/Inbox`
  (names like `ANA 2026-10-14` and `ANA 2026-10-14 blurt`). Then run `/ingest`.
- **Exercises:** attempt it, then `/exercise` with the problem and your attempt. Talk it
  through; say "debrief" at the end and the session becomes a short PDF in the vault.
- **New topic:** `/folio analysis uniform convergence`, or drag in Skript pages.
- **Weekly:** `/review`, then `/teach <concept>`.
- **Exams:** `/exam mock ANA`, `/exam oral LA`, `/exam board EP1`, `/exam mixed`.

Anki: morning reviews, new cards in the evening, from Kael'thos' suggestions. Make the cards
yourself.
