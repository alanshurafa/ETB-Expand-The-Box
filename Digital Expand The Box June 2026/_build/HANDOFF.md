# ETB v2 Build — HANDOFF

Updated 2026-06-10 (build session 2, macOS). Note: the prior session's HANDOFF.md (referenced from the Windows machine, `C:\Users\alan\...`) never synced to Drive; this file recreates it. Resume sequence for any new session: read this file, then `_build/AUDIT.md`, then `_build/ARCHITECTURE.md` (the locked plan). v1 (`../Digital Expand The Box/`) and all source folders are READ-ONLY.

## Build-order status (ARCHITECTURE §6)

- [x] **W-B1 Copy + skeleton — COMPLETE (2026-06-10)**
  - Copied from v1 (byte-verified, desktop.ini excluded): Maps/ (28), Map Atlas/ (30), Map Notes/ (29), Interactive Tools/ (23 html), Facilitator Resources/ (10), LICENSE.md.
  - 11 new shipped map renders copied from `ALL ETB MAPS/<folder>/<folder>.png` → Maps/: M32 Responsibility & Culture, M33 Feelings vs Emotions, M35 Feelings Sensations, M37 Fear Capacity Feelings Form, M38 EHP Spaceholding Twins, M39 Optional Healing Process, M40 EHP Learnings (source folder: "Emotional Healing Process Learnings"), M43 Letting Your Heart Speak, M44 Linear and Nonlinear, M46 Map of Matrix, M47 Map of 3 Games. Maps/ now has 39 PNGs.
  - Tool fixes done: Day 2 box-inventory consent no longer persisted (per-visit, memory only); Atlas M12 solo-EHP embodiment converted to description + link to gated Day 6 walker (trauma carve-out retained); GROUND NOW now visible from the gate screen on Day 5/7/9 tools; consent audit table in session log — Day 6/7/9 pattern confirmed per-visit + inert.
  - New tools: `Interactive Tools/journal.html` (local-only progress/journal/export-import of all etb_* keys, consent keys excluded; tested) and `Interactive Tools/ground.html` (standalone 60-second grounding, zero storage; tested).
  - Fonts self-hosted: `_assets/fonts/fonts.css` + 23 variable WOFF2 slices (Fraunces with SOFT/WONK axes, EB Garamond ital, JetBrains Mono); all 55 HTML files rewritten to relative links, zero fonts.googleapis/gstatic references remain. Stale "Prototype v0.1" labels → "Practice suite · v2.0" (12 files).
  - Created empty: Days/, Practice/, Course/.

- [ ] **W-B2 Modules** — 13 Day files (Days/Day 00–11) per ARCHITECTURE §3 + consistency pass. IN PROGRESS this session.
- [ ] **W-B3 Frameworks + packs** — README, START HERE, Manifest, Docs 01–05, Practice/ pack, safety/ops/exemplar packs, Voice & Style Guide, Video Manifest, Audio Kit. IN PROGRESS this session (runs with W-B2; Voice Guide + Spine spec are written FIRST — every module agent works under them).
- [ ] **W-B4 Atlas + cards + shell** — 11 new Atlas tools + cards (shipped maps only), Atlas index regrouped, `_build/build.py`, index.html, Course/ rendered pages, journal/completion wiring.
- [ ] **W-B5 QC + release** — link checker gate, canon regression greps (high drama / bright-shadow / matrix / consent persistence), browser QC, coverage matrix, concat editions, source-integrity check, delivery report.

## Conventions locked during W-B1
- Module md filenames stay v1-style `Days/Day NN - <title>.md` (per ARCHITECTURE §2 tree); learner-facing naming inside content and rendered pages is "Module NN" (`Course/module-NN.html`).
- New HTML must link `_assets/fonts/fonts.css` (relative), never Google Fonts CDN.
- Consent is per-visit, in-memory only — no etb_*consent* localStorage keys may ever be written (journal.html enforces on import).
- Deferred/excluded maps (ARCHITECTURE §4): teaching ships text-first, no embed; manifest carries the redraw queue (M30/M31/M34/M36/M41/M42/M45/M48/M49/M50 + v1 photo slots M01/M08/M10/M27).
