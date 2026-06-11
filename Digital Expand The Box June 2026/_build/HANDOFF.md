# ETB v2 Build — HANDOFF

Updated 2026-06-11 (build session 2, macOS). Resume sequence for any new session: read this file, then `_build/AUDIT.md`, then `_build/ARCHITECTURE.md` (the locked plan).

## THE BUILD NOW LIVES ON GITHUB (2026-06-11)

- Repo: https://github.com/alanshurafa/ETB-Expand-The-Box (public). Clone OUTSIDE any cloud-synced folder: Mac `~/Project/ETB-Expand-The-Box`, PC `C:\Projects\ETB-Expand-The-Box` (`gh repo clone alanshurafa/ETB-Expand-The-Box`). Pull before working, commit+push at every phase boundary — GitHub replaces Google Drive sync for the course (the old Drive copies are frozen snapshots with relocation notices).
- v1 = `../Digital Expand The Box May 2026/` (frozen, tagged `v1-may-2026`, READ-ONLY). v2 = this folder, `Digital Expand The Box June 2026/`.
- The source library (ALL ETB MAPS, SPARKS, books, Possability Lab, Mini ETB) stays on Google Drive only, READ-ONLY, at `.../My Drive/__shurafa@gmail.com/_PM Possability Manangement/` — needed for Spark citations and any future map work; build from a machine with Drive mounted when a task touches it.

## Build-order status (ARCHITECTURE §6)

- [x] **W-B1 Copy + skeleton — COMPLETE (2026-06-10)**
  - Copied from v1 (byte-verified, desktop.ini excluded): Maps/ (28), Map Atlas/ (30), Map Notes/ (29), Interactive Tools/ (23 html), Facilitator Resources/ (10), LICENSE.md.
  - 11 new shipped map renders copied from `ALL ETB MAPS/<folder>/<folder>.png` → Maps/: M32 Responsibility & Culture, M33 Feelings vs Emotions, M35 Feelings Sensations, M37 Fear Capacity Feelings Form, M38 EHP Spaceholding Twins, M39 Optional Healing Process, M40 EHP Learnings (source folder: "Emotional Healing Process Learnings"), M43 Letting Your Heart Speak, M44 Linear and Nonlinear, M46 Map of Matrix, M47 Map of 3 Games. Maps/ now has 39 PNGs.
  - Tool fixes done: Day 2 box-inventory consent no longer persisted (per-visit, memory only); Atlas M12 solo-EHP embodiment converted to description + link to gated Day 6 walker (trauma carve-out retained); GROUND NOW now visible from the gate screen on Day 5/7/9 tools; consent audit table in session log — Day 6/7/9 pattern confirmed per-visit + inert.
  - New tools: `Interactive Tools/journal.html` (local-only progress/journal/export-import of all etb_* keys, consent keys excluded; tested) and `Interactive Tools/ground.html` (standalone 60-second grounding, zero storage; tested).
  - Fonts self-hosted: `_assets/fonts/fonts.css` + 23 variable WOFF2 slices (Fraunces with SOFT/WONK axes, EB Garamond ital, JetBrains Mono); all 55 HTML files rewritten to relative links, zero fonts.googleapis/gstatic references remain. Stale "Prototype v0.1" labels → "Practice suite · v2.0" (12 files).
  - Created empty: Days/, Practice/, Course/.

- [x] **W-B2 Modules — COMPLETE (2026-06-11).** 12 module files (Days/Day 00–11; learner-facing naming "Module NN"). Critical canon fixes landed and grep-verified: Day 07 high drama rewritten on the responsibility axis ("Both are gremlin food" deleted), Day 10 bright/shadow causation corrected, matrix unified to the build sense, EHP "six positions (0–5)" everywhere. Day 10's 90-day/continuation content moved to the new Day 11. Spark citations verified per-number (`_build/sparks-index.md`).
- [x] **W-B3 Frameworks + packs — COMPLETE (2026-06-11).** Voice & Style Guide (canonical-phrasing ledger = the canon control) + Daily Practice Spine written first, binding on all writers. Then: START HERE, README, 00 Course Manifest, Docs 01–05 (05 = new Operator Run-Book), Practice/ pack (Beep Book Guide, Feelings Form, Coming Back, My Map Book), safety pack (Experiment Bank Screen-4 variant lines, Referral List fixes incl. PT=open + France 3114, Partner Emergency Card, Intake Form, CM Leaver Checklist), ops pack (Enrollment Terms, Cohort Calendar, Witness Bench Onboarding, PT Conversion Guide, Self-Assessment collection flow), Worked Exemplars Pack, Video Manifest, Audio Companion Recording Kit, Glossary canon fixes. Consistency sweep done: 467 links verified, 0 broken, 24 intentionally pending on the 11 W-B4 Atlas pages (`_build/consistency-report.md`, `_build/linkcheck-md.md`).
- [ ] **W-B4 Atlas + cards + shell** — 11 new Atlas tools + cards (shipped maps only), Atlas index regrouped, `_build/build.py`, index.html, Course/ rendered pages, journal/completion wiring. MUST-DOS from the sweep: (1) add "How to explain it verbally" sections to Map Note cards — 0 of 29 currently have them while Days 03/06/09 teach-backs reference them; (2) new Atlas filenames must match the 24 pending links byte-exactly (list in linkcheck-md.md); (3) v2 footers on all cards.
- [ ] **W-B5 QC + release** — link checker gate, canon regression greps (high drama / bright-shadow / matrix / consent persistence), browser QC, coverage matrix, concat editions, source-integrity check, delivery report.

## Conventions locked during W-B1
- Module md filenames stay v1-style `Days/Day NN - <title>.md` (per ARCHITECTURE §2 tree); learner-facing naming inside content and rendered pages is "Module NN" (`Course/module-NN.html`).
- New HTML must link `_assets/fonts/fonts.css` (relative), never Google Fonts CDN.
- Consent is per-visit, in-memory only — no etb_*consent* localStorage keys may ever be written (journal.html enforces on import).
- Deferred/excluded maps (ARCHITECTURE §4): teaching ships text-first, no embed; manifest carries the redraw queue (M30/M31/M34/M36/M41/M42/M45/M48/M49/M50 + v1 photo slots M01/M08/M10/M27).
