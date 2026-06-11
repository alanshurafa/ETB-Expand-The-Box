# Consistency sweep report — v2 post-build (W-consistency)

Scope: `Days/`, `Practice/`, root docs (`START HERE.md`, `README.md`, docs 00–05), `Facilitator Resources/`. Authorities: `Facilitator Resources/Voice and Style Guide.md` (canon ledger) and `Practice/Daily Practice Spine.md` (header lines). Companion report: [`linkcheck-md.md`](linkcheck-md.md).

**Counts: 21 content files changed · 0 broken links (24 allowed-pending left intact) · 18 canon hits fixed (all structured-field "matrix") · 8 footers replaced · ~200 em dashes humanized across 6 files.**

---

## Part A — canon + voice

### A1. Regression greps (high drama, causation, six positions, matrix)

- "Both are gremlin food" / theatrical-high-drama: **zero violations.** Day 07's two "theatrical" hits are inside explicit what-this-is-NOT refutations (allowed). Days 00/01/03 use "theatrical" about practices feeling awkward, unrelated to high drama.
- "sourced from archiarchy/patriarchy": **zero hits** outside the Voice Guide's own correction text.
- "5 positions": **zero hits**; Day 06 teaches "six positions of the EHP map (Position 0 through Position 5)" correctly.
- Matrix in a non-build-leading sense: **18 occurrences fixed.** The carried-forward facilitator files still used the retired v1 "structured field" sense (Doc 02 explicitly retires it in favor of "container"):
  - `Async Partner Pairing Playbook.md` — 12 occurrences → "container"/"pairing" (incl. the defining sentence "The pairing IS the matrix" → "container"; "re-earn matrix trust" → "re-earn the container's trust").
  - `Cohort Feed Templates.md` — 4 occurrences → "container"/"pairing".
  - `CM Leaver Checklist.md` — 1 ("re-earns matrix trust" → "re-earns the container's trust").
  - `Witness Bench Onboarding.md` — 1 ("the matrix you held in your own container" → "the standard you held in your own container").
  - Glossary's Matrix entry already leads with the build sense — no change. All Days/Practice bare-"matrix" hits read correctly against the build sense (StartOver.xyz "matrix codes" are proper nouns, left alone).

### A2. Em-dash density (budget ≤ ~5/1000 words own prose)

Humanized (meaning preserved; quoted scripts untouched):

- `Facilitator Resources/Learning Self-Assessment.md` — 19.9 → 3.4/1000 (61 → 11 dashes). Mandated; Parts 1–2 prose brought into budget, content intact.
- `Days/Day 04 - Feedback, Coaching, Rapid Learning, Experiments.md` — 12.1 → 4.3/1000 (82 → 29; one em-dash chain removed; glossary bullets aligned to the "**Term.** Definition" house style used by Days 05/07).
- `04 - Container and Gatekeeping Protocol.md` — 7.8 → 3.2/1000 (34 → 14).
- `Practice/Daily Practice Spine.md` — 7.6 → 6.1/1000 total; remaining dashes are structural headings/table labels; prose dashes removed. Canonical header-line blocks untouched.
- `Facilitator Resources/Intake Form.md` — 6.0 → 3.1/1000.
- `Facilitator Resources/Cohort Feed Templates.md` — 22.2 → ~2.0/1000 own prose (fenced CM message templates exempt).

Flagged, NOT rewritten (carried-forward v1 prose; bulk rewrite judged unsafe for a sweep — residual for W-B5):
`Referral List.md` (24.1 own), `Reflection and Journal Prompt Bank.md` (20.6), `Solo Centering and Grounding Scripts.md` (15.3 — scripts, largely exempt category), `CM First-Cohort Run-Book.md` (15.4), `Async Partner Pairing Playbook.md` (15.4), `Glossary of PM Distinctions.md` (14.7), `Experiment Bank.md` (13.8), `CM Agreement Templates.md` (10.4), `Voice and Style Guide.md` (authority file, contains spec/quoted material — left alone). `Audio Companion Recording Kit.md` and `Days/Day 06` look high in raw count but are within budget once verbatim scripts are excluded. `LICENSE.md` untouched per scope.

### A3. World Copyleft wording + footers

- "the same World Copyleft terms": appears **only in LICENSE.md** (allowed exception). Zero hits elsewhere.
- v1-era footers replaced with the Voice Guide §8 standard v2 footer block (adds "consistent with the spirit of World Copyleft" and the honesty line) on exactly the 8 carried-forward files: `Async Partner Pairing Playbook.md`, `CM Agreement Templates.md`, `CM First-Cohort Run-Book.md`, `Cohort Feed Templates.md`, `Reflection and Journal Prompt Bank.md`, `Solo Centering and Grounding Scripts.md`, `Referral List.md`, `Glossary of PM Distinctions.md`. Every learner-facing md in scope now carries both binding phrases.

### A4. Gamification grep

**Clean.** All streak/badge/score/points hits are negations or teaching content ("no streak to protect", "keeps no score", "A run of Beeps is not a losing streak", Game-2 "keeping score" teaching). Bar-reading and refund percentages untouched.

### A5. "Study the map before reading on"

**Clean.** 0 or 1 per file everywhere; only the Voice Guide (the spec itself) has more.

---

## Part B — cross-references

### B6. Links

Full inventory in [`linkcheck-md.md`](linkcheck-md.md). **467 relative links checked: 443 OK, 24 allowed-pending, 0 broken → 0 fixes needed.** The 24 pending links are exactly the 11 planned Atlas pages (M32, M33, M35, M37, M38, M39, M40, M43, M44, M46, M47) linked from Days 01/03/05/06/07/08/10 — left intact for W-B4. No SPARKS/, ALL ETB MAPS/, Possability Lab, Mini ETB, or bare-.mp4 links found. Two non-link code-path references to `Mini ETB Documents/…Periodic_Table….png` in the Glossary (a non-shipped path) reworded to "a chart from the PM source library (not shipped with this course)". The Voice Guide's mp4 mention sits inside a verbatim canonical script with an explicit v2 handling note — left alone.

### B7. Spine lines

**Pass, no change.** All 12 modules carry the exact canonical line: 00–04 Phase A, 05–11 Phase B, byte-identical to the Spine spec.

### B8. Intensity agreement

One truth established: High = 05/06/07/09; Medium = 02/08; Low = 00/01/03/04/10/11 (per Manifest, Doc 03 §intensity table, Day 00). Fixes:

- `Days/Day 10` header: **MEDIUM → LOW** (Manifest, Doc 03, and Day 00 all say Low; per the sweep rule, Module 10's header follows the Manifest). Closure-sensitivity prose and check-in recommendation kept.
- `Days/Day 10` safety callout: "Module 10 is Medium intensity" → "Low intensity".
- `Facilitator Resources/Cohort Calendar Template.md`: tags for Modules **01, 03, 04, 10** corrected M → L (02/08 correctly M; 05/06/07/09 correctly H; 00/11 L).

### B9. Teach-backs + rest day

- Teach-backs exist **only** at Modules 3/6/9, consistently shaped (~20 min, partner, maps of the prior 3-module block), and cross-referenced in Manifest/Doc 01/Doc 02/Calendar. One inconsistency fixed: `Days/Day 03` told learners to read the Map Note's "How to explain it verbally" paragraph **before** the teach-back, contradicting Doc 01 ("read after the attempt, not before") and Days 06/09 → Day 03 now reads the card after the attempt.
- Rest day sits between Modules 8 and 9 everywhere (Day 00 tracker row, Day 07 climb note, Day 08 §rest-day, Day 09 opening + unlock item, Calendar day 29, Docs 01/02/03/05). `Days/Day 08` rest-day paragraph now **links Day 00's tracker** ("[Module 0](Day%2000%20-…)") — the link the writer noted missing.

### B10. Consent blocks

**Pass, no change.** Days 05/06/07/09 each carry a day-specific consent check (emotional body / EHP / drama patterns / ego states + Demon) matching Doc 03 §I's spec names, plus the "Reading this without a cohort?" solo box. Day 02's survival-layer consent prose says per-visit, never remembered. Doc 03's named implementing tools match the modules' actual tools.

### B11. Recall warm-ups + Module 10 close

**Pass, no change.** Every module's recall references exactly the prior module (01→00 … 11→10). Module 10 closes with an explicit hand-off section and link to Module 11; its 90-day mentions are forward-pointers only ("you will build the container itself in Module 11") — no container content remains in 10.

### B12. Feelings Form choreography

- Phase B starts Module 5 (header lines + Manifest + Spine) — pass.
- Module 8 completion-loop line item present (Day 08 §spine note, Spine, Manifest) — pass.
- Scale is 0–10 everywhere bars are described (Day 05 micro-practice and glossary, Spine, Feelings Form); no 0–100% bar references found in module prose (the "2%/5% of a feeling" idiom is intensity language, not the bar scale; Feelings Form's one-point-equals-ten-percent equivalence intact) — pass.
- Trend re-reads at 6/7/10: Day 05 promises them, but Days 06/07/10 never sent the learner back to their rows. **Added:** Day 06 (first re-read, two minutes before Sitting 1), Day 07 (second re-read, drama-day rows), Day 10 (reflection prompt 8, the 30-day trend read). Each one or two sentences, in the modules' existing register.

### B13. Map Notes check (report-only — W-B4 owns the cards)

**Verdict: 0 of 29 cards in `Map Notes/` contain a "How to explain it verbally" section.** The cards are slim map-cards (lede · map image · "What it is" · "At a glance" · pointer block) and also still carry the v1-era footer. Days 03/06/09 teach-backs, the Manifest (§teach-back slots), and Doc 01 all instruct learners to read that paragraph. W-B4 must add the section to all 29 cards (or at minimum the 13 cards the teach-backs name: M01–M07, M10, M11, M13, M16, M17, M26) and swap the card footers to the v2 block.

### B14. Day-number/tool alignment

**Pass, no change.** Each module links only `../Interactive%20Tools/Day%20NN/` tools for its own NN; Modules 00 and 11 link only the standing utilities (`journal.html`, `ground.html`), no Day-folder tools.

---

## Change log (file → change → why)

| File | Change | Why |
|---|---|---|
| Facilitator Resources/Async Partner Pairing Playbook.md | v2 footer; 12× structured-field "matrix" → container/pairing | A3; CORRECTION 3 |
| Facilitator Resources/CM Agreement Templates.md | v2 footer | A3 |
| Facilitator Resources/CM First-Cohort Run-Book.md | v2 footer | A3 |
| Facilitator Resources/Cohort Feed Templates.md | v2 footer; 4× "matrix" → container/pairing; own-prose dashes 27→2 | A3; CORRECTION 3; A2 |
| Facilitator Resources/Reflection and Journal Prompt Bank.md | v2 footer | A3 |
| Facilitator Resources/Solo Centering and Grounding Scripts.md | v2 footer | A3 |
| Facilitator Resources/Referral List.md | v2 footer | A3 |
| Facilitator Resources/Glossary of PM Distinctions.md | v2 footer; 2× non-shipped `Mini ETB Documents/` path reworded | A3; B6 |
| Facilitator Resources/CM Leaver Checklist.md | "matrix trust" → "the container's trust" | CORRECTION 3 |
| Facilitator Resources/Witness Bench Onboarding.md | "the matrix you held" → "the standard you held" | CORRECTION 3 |
| Facilitator Resources/Learning Self-Assessment.md | dashes 19.9→3.4/1000, meaning intact | A2 (mandated) |
| Facilitator Resources/Intake Form.md | dashes 6.0→3.1/1000 | A2 |
| Facilitator Resources/Cohort Calendar Template.md | Modules 01/03/04/10 tags M→L | B8 |
| 04 - Container and Gatekeeping Protocol.md | dashes 7.8→3.2/1000 | A2 |
| Practice/Daily Practice Spine.md | 3 prose dashes removed (Phase B step 2) | A2 |
| Days/Day 03 - Liquid State… | teach-back card read moved to after the attempt | B9 |
| Days/Day 04 - Feedback… | dashes 12.1→4.3/1000; glossary bullets to house style; chain removed | A2 |
| Days/Day 06 - Mixed Emotions… | first scheduled row re-read added | B12 |
| Days/Day 07 - Low Drama… | second scheduled row re-read added | B12 |
| Days/Day 08 - Listening… | Day 00 tracker link added in rest-day paragraph | B9 |
| Days/Day 10 - Map of Possibility… | header MEDIUM→LOW; safety prose Medium→Low; trend-read reflection prompt 8 added | B8; B12 |
| _build/linkcheck-md.md | new — full link inventory | B6 |
| _build/consistency-report.md | this file | output |

## Found but judged unsafe to fix (residual for W-B4 / W-B5)

1. **Map Note cards lack "How to explain it verbally" and carry v1 footers** (all 29; Map Notes read-only for this sweep) — W-B4.
2. **Eight carried-forward facilitator files remain over the em-dash budget** (list in A2). Their content was deliberately carried forward; bulk humanization risks meaning drift and belongs in a dedicated pass — W-B5.
3. **The 24 allowed-pending Atlas links** (11 pages) go live only when W-B4 ships the pages; re-run `linkcheck-md` afterward.
4. `Course/` is an empty directory (nothing links into it); confirm with the orchestrator whether it ships or gets dropped at release — W-B5.
