# ETB v2 Architecture — Locked Build Plan

Drafted 2026-06-10 from `_build/AUDIT.md` (11-dimension adversarially-verified audit of v1). v1 at `../Digital Expand The Box/` is the template and is **never modified**. Everything below is built in this folder (`Digital Expand The Box v2/`).

---

## 0. Vision

v2 is the same course taught better: a **practice container, not a content library**. Five moves define it: (1) a real front door and HTML delivery shell; (2) one evolving daily practice spine wired into every module; (3) a retrieval layer inside the no-quiz stance; (4) the safety/canon patches; (5) the operator/commerce/continuation layer that lets a real person launch a cohort — plus a sanctioned solo path for the license-guaranteed reader. The teaching content, safety spine, voice, and tool engineering of v1 carry forward largely intact (see AUDIT §2 KEEP).

## 1. The eight decisions (locked)

1. **Video: text-first.** Every module is declared complete without video. Source videos become optional enrichment listed in a `Video Manifest.md` (filename → status → where-to-get placeholder for the operator). No bare `.mp4` references anywhere in the learner path. A new **Audio Companion Recording Kit** collects every practice script with tone/timing notes so an operator can record guided audio in an afternoon (we ship scripts, not audio).
2. **Hosting: self-hosted static shell.** `index.html` front door + `Course/module-NN.html` pages rendered from the markdown sources + the existing tool HTML — all one origin, works from any static server or file host. A `_build/build.py` pipeline renders md→HTML, rewrites links, runs the link checker, and generates the concat editions. Markdown stays the canonical source.
3. **Solo track: sanctioned, gates intact.** Solo readers get full access to Low/Medium modules. High modules offer two named paths: (a) **recruit-a-witness** (7-line agreement; a friend qualifies), or (b) **defer-list** (read the teaching, do locator-level practices, defer EHP/Demon work until witnessed). "Reading this without a cohort?" boxes in Start Here and Day 5/6/7/9 consent blocks. The structural partner gate is preserved — the path to satisfy it broadens.
4. **Maps: hand-drawn renders canonical.** The May-2026 bare-name clean renders are the course maps (owner's explicit direction). Infographic variants are *referenced* in the Source Inventory as optional study posters, never embedded or copied. v2 inherits the four photo-slot maps (M01/M08/M10/M27) until their regeneration lands (parked external task); the manifest flags them.
5. **Tools: two systems, named by function, unified in navigation.** Map Atlas = **"Study the map"**; Interactive Tools = **"Run the practice."** Module pages present both as buttons at the moment of use; learners never see "two systems." Fixes: one shared per-visit consent component (never persisted), Atlas M12 gated like the Day 6 walker, `journal.html` (local-only progress + export/import of all `etb_*` keys), standalone `ground.html`, completion dots on both indexes.
6. **Daily spine: one evolving sit, 5–10 min.** Phase A (Modules 0–4): Beep! Book morning capture (3–5 min). Phase B (Module 5 on): the Feelings Form bar-reading folds INTO the same sit (~8–10 min total). Module 8 adds one completion-loop line item to the Form — no new practice. One anchor, evolving content, honoring the "one experiment at a time" bandwidth rule. Spec lives in `Practice/Daily Practice Spine.md`; every module header names the current phase.
7. **Retrieval line: generation yes, grading no.** Codified in Doc 01: free recall, teach-back, self-explanation, perform-the-outcome — in. Answer-checking, scoring, right/wrong feedback — out, forever. Implementation: 5-min free-recall warm-up opening every module flow; partner teach-backs scheduled at Modules 3/6/9 (sourced from the "How to explain it verbally" scripts); per-module "Close the loop" self-check on the existing three-word scale; the Atlas flip-cards ARE the unscored recall deck (recall-prompt framing added to the Atlas index).
8. **Commerce: open content, paid container.** The content is CC BY-SA and free forever. The purchasable offering is the **held container**: screening, CM, partner pairing, cohort feed, witness bench. Enrollment Terms + refund tree are written for the container. The solo track is the honest free path.

## 2. Folder structure

Copied folders keep v1 names so relative links survive. New items marked ★.

```
Digital Expand The Box v2/
├── index.html                                ★ THE front door (shell home)
├── README.md                                 operator orientation (learners → index.html)
├── LICENSE.md                                copied, unchanged
├── START HERE.md                             un-prefixed (front-door fix) — rewritten
├── 00 - Course Manifest.md                   ★ what-lives-where + map registry + video manifest pointer
├── 01 - Course Architecture and Pedagogy.md  v2: retrieval line, spine spec, sittings, shipped-format specs
├── 02 - Async Delivery Framework.md          v2: reference platform stack, solo mode, tool slots
├── 03 - Safety and Facilitation Framework.md v2: unified consent spec, exit ramps, bereavement screen
├── 04 - Container and Gatekeeping Protocol.md v2: witness-recruitment protocol, 18+, CM cap
├── 05 - Operator Run-Book.md                 ★ commerce Step 0, platform stack, CM sizing, launch sequence
├── Course/                                   ★ rendered HTML module pages (module-00.html … module-11.html)
├── Days/                                     Day 00 ★ · Days 01–10 rewritten · Day 11 ★  (md sources)
├── Practice/                                 ★ Daily Practice Spine · Beep Book Guide · Feelings Form ·
│                                               Coming Back (re-entry) · My Map Book
├── Maps/                                     M01–M29 copied + ★ M30–M52 new clean renders
├── Map Atlas/                                29 copied+fixed + ★ ~21 new tools + index
├── Map Notes/                                29 cards copied+updated + ★ new cards for M30+
├── Interactive Tools/                        copied + consent fix + ★ journal.html, ground.html
├── Facilitator Resources/                    10 copied+updated + ★ safety pack, ops pack, exemplars,
│                                               Voice & Style Guide, Video Manifest, Audio Recording Kit
├── _build/                                   AUDIT.md · ARCHITECTURE.md · build.py · linkcheck report
└── EXPAND THE BOX v2 — Learner Edition.md    ★ generated; + Operator Edition.md
```

## 3. Module map (12 modules)

Every module gets: free-recall warm-up (5 min, prior module) · explicit **Sitting 1/2/3** markers (cognitive-load fix; files stay whole) · daily-spine phase named in header · "Study the map / Run the practice" buttons · solo-reader box where flagged · tool links at moment of use · videos-are-enrichment note · Close-the-loop self-check · copyleft footer.

| Module | Base | Fixes (from AUDIT §3) | Adds (maps ★new) |
|---|---|---|---|
| **00 Start Here & Getting Your Container** ★ | v1 START HERE + Day-0 material | front-door format; "where this work comes from" lineage block | ★M30 Welcome map · container-acquisition decision tree (cohort/recruit/solo) · 7-line partner agreement · printable schedule+tracker w/ pause beats · Beep! Book install (spine Phase A) |
| **01 Orientation, New Context, Radical Responsibility** | Day 01 | em-dash budget; slot re-timing | ★M31 Red Pill Blue Pill (ceremony visual) · ★M32 Responsibility & Culture · Screen-4 variant note |
| **02 Thoughtware, Thoughtmaps, Box** | Day 02 | Medium partner check-in header fix | matrix vocabulary seeded (one paragraph, consistent definition) |
| **03 Liquid State, Center-Ground-Bubble, Five Bodies** | Day 03 | "it works either way" rephrase | Script 3 named as standing daily practice · teach-back #1 · ★M46 Map of Matrix + ★M51 Building your Matrix (matrix-building half-section) |
| **04 Feedback, Coaching, Rapid Learning, Experiments** | Day 04 | — | Beep! Book upgraded (Go!/Beep!/Shift! grammar onto existing Phase-A habit) · per-Spark citations |
| **05 Feelings vs Emotions, Old Map, Numbness Bar** | Day 05 | M05→M07 pointer fix; mid-course re-screen checkbox | ★M33 Feelings vs Emotions · ★M34 Purpose of Feelings · ★M35 Sensations · ★M36 Feelings Form installed as daily instrument (spine Phase B) · ★M37 Fear Capacity (annex) · solo box |
| **06 Mixed Emotions & EHP** | Day 06 | 40% hard-stop restated at point of use; "5 positions"→0–5 wording | ★M38 Spaceholding Twins (witness annex) · ★M39 Optional Healing Process · ★M40 EHP Learnings · teach-back #2 · solo box; consolidation rep in the 6→7 pause |
| **07 Low Drama, Gremlin, Responsible Game** | Day 07 | **CRITICAL high-drama rewrite** (responsibility axis; delete "both are gremlin food"; fix Glossary mirror); "heaviest stretch" line corrected | ★M41 Responsible Story · ★M47 Map of 3 Games (Responsible Game grounding) · proper high-drama teaching ¶s · Screen-4 note · solo box |
| **08 Listening, Speaking, Communication** | Day 08 | Medium header fix | ★M42 Possibility Speaking · ★M43 Letting Your Heart Speak · feedback round repeated (practice-quality) · Screen-4 note · low-demand beat scheduled after |
| **09 Ego States, Problem Ownership, Learning Spiral** | Day 09 | — | teach-back #3 · solo box |
| **10 Map of Possibility, Bright/Shadow, Is-Glue, 3 Powers** | Day 10 | **bright/shadow causation fix** (all mirrors); matrix unified | ★M44 Linear & Nonlinear · ★M45 Nonlinear/Possibility Story · ★M52 Culture: Patriarchy→Archiarchy · M21 visual fill (M46/M47 "adjacent, not dedicated") · per-Spark citations · Screen-4 note |
| **11 Continuation: 90-Day Container & Possibility Team** ★ | Day 10 §90-day + new | Referral List "invitation-only" claim fixed | ★M48 Treasure Map · ★M49 Possibility Team (conversion guide) · ★M50 StartOver.xyz resources · My Map Book exchange close · stopping-well path · advanced-horizons pointers (Lab material, 99 advanced Sparks) · alumni 30/60/90 touchpoints |

## 4. New map registry (M30–M52) — REVISED after visual classification (2026-06-10)

Every candidate source was visually classified (clean digital hand-drawn render vs framed photo vs infographic). **Only SHIPPED maps are copied, embedded, and given Atlas tools + cards.** Deferred/excluded maps' *teachings* still ship text-first where the module map calls for them.

**SHIPPED (11 — clean renders, copy from `ALL ETB MAPS/<folder>/<folder>.png`):**
M32 Map of Responsibility and Culture · M33 Feelings vs Emotions · M35 Map of Feelings Sensations · M37 Fear Capacity Feelings Form · M38 EHP Spaceholding Twins · M39 Map of Optional Healing Process · M40 EHP Learnings · M43 Letting Your Heart Speak · M44 Linear and Nonlinear · M46 Map of Matrix · M47 Map of 3 Games. All 11 get Atlas tools + Map Note cards + module embeds.

**DEFERRED (10 — source is a framed photo; image NOT embedded; teaching ships text-first; listed in the manifest's redraw queue alongside v1's M01/M08/M10/M27):**
M30 Welcome to Expand the Box · M31 Red Pill Blue Pill Choice · M34 Purpose of Feelings · M36 The Feelings Form (the daily instrument ships as a markdown form in `Practice/Feelings Form.md`; the map joins the redraw queue) · M41 Responsible Story · M42 Possibility Speaking · M45 Nonlinear Story and Possibility Story · M48 Treasure Map · M49 Possibility Team · M50 StartOver XYZ Resources.

**EXCLUDED (2 — NotebookLM-watermarked infographics; owner's standing rule: infographics are not course maps):**
M51 Building your Matrix · M52 Map of Culture Patriarchy→Archiarchy. Referenced in the Source Inventory as optional study material only; matrix-building teaches from M46, the culture teaching ships prose-only.

Module-map implications: Module 00 ships imageless (as v1 START HERE does today) · Module 01 embeds M32 only · Module 05 embeds M33/M35/M37 · Module 06 embeds M38/M39/M40 · Module 07 embeds M47 · Module 08 embeds M43 · Module 10 embeds M44/M46 (M21 fill = M46/M47, "adjacent, not dedicated") · Module 11 ships text-first with no new images. Where §3's table names a deferred ★map, build the teaching, skip the embed, and note the pending image in the manifest. Build verifies each SHIPPED source exists before copying; any miss → flagged in manifest, never silently skipped.

## 5. Cross-cutting specs

- **Unified consent component:** one shared JS block (template-stamped into every gated tool): per-visit, never persisted to localStorage, day-specific items injected, `inert` gating, GROUND-NOW always reachable. Atlas M12's embodiment converts to a description + link to the gated Day 6 walker.
- **Voice & Style Guide** (`Facilitator Resources/`): Doc 01's six bullets + em-dash budget (≤5/1000 words, one per paragraph) + signature-word caps + banned-AI-pattern list + canonical-phrasing ledger (each Glossary distinction annotated with source + canonical wording — the control that catches drift like the high-drama bug) + voice-anchor appendix (verbatim v1 scripts). Every module agent works under it; a humanizer pass closes each module.
- **Safety artifact pack:** Screen-4 variant column in Experiment Bank · partner emergency card · 18+ intake line · bereavement/rupture Y/N intake question · safety-plan template · next-morning three-question check on High days · stopping-well half-page + CM leaver checklist · France line → 3114.
- **Ops artifact pack:** Enrollment Terms + Learner Agreement (container commerce) · pricing/refund Step 0 · reference platform stack (named picks + privacy verification table) · CM sizing table (first-cohort cap 8–12, hours/week bands) · deployable intake form · cohort calendar template · anonymized assessment collection flow · witness-bench onboarding note.
- **Build pipeline (`_build/build.py`):** md→HTML rendering (Atlas design system, self-contained CSS), nav (prev/next, breadcrumbs), link rewriting, **link checker as release gate** (zero broken internal links), generated Learner + Operator editions, manifest generation. Python 3.13, `markdown` package (install if absent).
- **Measurement:** completion-by-module pull list in Doc 05 (operator-facing only); no-name self-assessment submission flow; explicitly no learner-facing gamification.

## 6. Build order (5 workflows, sequential gates)

- **W-B1 Copy + skeleton:** scripted copy of Maps/Atlas/Tools/Cards/Resources from v1; copy M30–M52 source PNGs; verify counts + integrity. Then tool-fix agents: consent component, M12 gate, journal.html, ground.html, label/font cleanups.
- **W-B2 Modules:** 13 Day files (00–11) written in parallel from v1 templates + this doc + AUDIT fix/add lists; then a consistency pass (voice guide + canon ledger + cross-module references).
- **W-B3 Frameworks + packs** (parallel with W-B2): README, START HERE, Manifest, Docs 01–05, Practice/ pack, safety pack, ops pack, exemplars, Voice Guide, Video Manifest, Audio Kit.
- **W-B4 Atlas + cards + shell** (after W-B2): ~21 new Atlas tools (M10 template, content from new modules) · new Map Note cards · Atlas index regrouped · build.py + index.html + Course/ pages rendered · journal/completion wiring.
- **W-B5 QC + release:** link checker (gate) · canon-bug regression greps (high drama, bright/shadow, matrix, consent persistence) · browser QC sample · coverage matrix walk · concat editions · source-integrity check (v1 + ALL ETB MAPS untouched) · delivery report.

## 7. Out of scope (named so nobody re-litigates)

Producing/hosting actual video or audio (kits ship instead) · platform implementation (reference stack documented, not deployed) · advanced-tier teaching (stellating, intimacy offers, Fear Club, Distilling Destiny — horizons pointers only) · embedding infographic variants · regenerating the four photo-slot maps (external task; manifest flags them) · payment processing specifics beyond the terms/refund tree.
