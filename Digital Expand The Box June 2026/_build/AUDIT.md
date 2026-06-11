# ETB v2 Master Audit Report

Synthesized 2026-06-10 from 11 dimension audits (pedagogy, coverage, safety, journey, ops, tools, voice, structure, practice, sources, best-practices research), each adversarially verified. Refuted findings dropped; adjusted severities applied. Unless noted, v1 paths are relative to `_PM Possability Manangement/Digital Expand The Box/`; source-library paths are under `_PM Possability Manangement/`.

Headline: v1's teaching content, safety architecture, and voice are strong and carry forward largely intact. Rebuild work concentrates in five places: delivery (no HTML shell, unresolved video), wiring (practice instruments, tools, and daily scripts exist but are unreachable from the learner path), the business/continuation layer, a small set of canon bugs, and retrieval pedagogy.

Note: the best-practices research audit evaluated the older `ETB_Day1_Packet`, not the v1 course; verification refuted its headline claims (partner architecture, safety container, and Module-0 functions all exist in the course). Its survivors fold into pedagogy/practice; two salvaged ideas appear in ADD.

---

## 1. Executive summary — 10 highest-leverage v2 improvements (ranked)

1. **Build an HTML course shell + build pipeline** (markdown as source, rendered pages, one front door, working links, manifest, link checker, generated editions) — the learner path currently runs through raw .md files and dead links.
2. **Wire the practice layer into the learner path**: Beep! Book from Day 1, the daily Bar Reading promoted to a standing Feelings Form, Solo Centering Scripts as explicit flow steps — converts a content library into a practice container using assets v1 already wrote.
3. **Gate Atlas M12's do-it-now EHP and unify consent** into one shared per-visit component (Day 2 currently persists survival-layer consent forever) — the one open hole in an otherwise excellent safety stack.
4. **Fix the canon bugs across all mirrors**: high drama mistaught as "theatrical... both are gremlin food" while the course's own M20.png shows HIGH DRAMA under Conscious Purpose; bright/shadow causation reversed in Day 10; matrix defined three conflicting ways.
5. **Add a retrieval layer inside the no-quiz stance**: module-opening free recall of the prior map, scheduled partner teach-backs (the Map Notes' "How to explain it verbally" paragraphs are built for this, never used), and a close-the-loop outcome self-check per module.
6. **Ship the commerce and operator layer**: enrollment terms/refund policy, a tested reference platform stack, a binding CM cohort cap with hours model, and an Operator Run-Book — v1 can keep a cohort safe but cannot launch one.
7. **Resolve video delivery**: declare modules text-first with videos as enrichment plus a filename-to-URL manifest (or produce/license a new set); kill the Day-1 dead end of bare .mp4 filenames nobody can play.
8. **Build the sanctioned solo/cohort-less pathway**: Day 0 "getting your container" decision tree, recruit-a-witness protocol, per-module solo-safety defer list, "reading this without a cohort?" boxes — the CC BY-SA license guarantees this audience.
9. **Close the exits and continuation**: "Coming back" re-entry page, a held stopping path, Possibility Team conversion guide (fix the Referral List's wrong "invitation-only" claim), StartOver.xyz in What's Next, and a low-demand beat between Days 8 and 9.
10. **Mine the source library**: fill the M21 image gap (Map of Matrix / Map of 3 Games clean PNGs sit ready), embed the four cohort-provenance maps and the Feelings Form map, document ALL ETB MAPS in the Source Inventory, cite Sparks by number.

---

## 2. KEEP — what v1 does well that v2 must copy forward

**Safety spine (nearly verbatim)**
- Five-screen intake with thresholds, actions, routing-not-denial; Screen 4 (coercive environment) is rare and excellent — `04 - Container and Gatekeeping Protocol.md` §A.2.
- Triage rubric with response windows + three worked ambiguous-post examples — `04` §F; `CM First-Cohort Run-Book.md` Part 2. Backup-CM drill (tested 15-min red-flag coverage) — Part 5.
- Per-module consent on High days with day-specific items, skip-override removed — Days 5/6/7/9; `03` §C.
- Day 6 EHP containment (solo scope cap, stop cues, witness-overflow script) and all scope carve-outs (EHP vs trauma, gremlin naming vs GT, Demon as locator only) — Days 06/07/09.
- Module-specific predicted failure modes in every safety callout; `Referral List.md` (crisis lines first, screen-to-section map, quarterly verification).

**Pedagogy and practice**
- Performance-based prerequisite chains and 10-second readiness checks gating High modules — `01 - Course Architecture and Pedagogy.md`; `Learning Self-Assessment.md` Part 2.
- Experiment discipline: what / by-when / what-I-will-notice, one at a time, capture within ten minutes, failed experiments are Beeps — `Days/Day 04`; `Experiment Bank.md` (83 items).
- Beep!/Shift!/Go! taught as content; the Beep! Book concept (engineering log, not journal).
- Inline micro-practices with "what to expect" calibration and named drift signals; "Common misunderstandings" refutation blocks after every map — lock both into the v2 template.
- Day 8 partner exchange (timed roles, scripted response format, roadblock self-monitoring) — the strongest single practice design in v1.
- Day 10's 90-day container (two practices, 30/60/90 calendar check-ins, standing witness, named next gameworld).
- Learning Self-Assessment: three-word scale, baseline/Day-10 delta, anonymized aggregate feeding revision.
- The no-gamification/no-quiz stance (`02` §J) as a load-bearing constraint all v2 fixes must respect.

**Operations**
- Run-Book pattern (sequenced steps, done-when criteria) as the template for v2 ops docs; Pairing Playbook (matching priority, mechanical SLA triggers, verbatim CM scripts, ghost/rematch/witness-bench) verbatim; Cohort Feed Templates (prompts, good-vs-drift exemplars, metadata-only triage log); CM Agreement Templates incl. §11.2; the "Doc 04 is the law, the Run-Book is the route" hierarchy.

**Content, voice, structure**
- Concept-to-source coverage matrix (27/27) — `00 - Source Inventory...` §C; extend, don't replace.
- Complete entry-level canon: four-feelings ecosystem, full communication stack, gameworld as first-class entry concept, Day 7's six-reactivities tool routing, the ~140-term Glossary.
- The drafter voice spec (`01`) and the verbal scripts as anchors (red-pill ceremony, four-level sentence, Day 6 EHP and witness-overflow scripts, 60-second grounding) — copy verbatim. World Copyleft footer + LICENSE honesty about not being official PM.
- Single-canonical-home pattern (each map taught once, inline, satellites point back); the locked 14-section Day template; START HERE's content (right front door, wrong format).
- Tool engineering as the v2 quality bar: unified design system, per-visit consent with `inert` gating (Day 7), GROUND NOW in all 29 Atlas tools, privacy-first localStorage, escapeHtml, real a11y.
- Clean-PNG map pipeline (Maps/M01–M29 byte-identical to ALL ETB MAPS renders) — extend to the 33 unused maps.

---

## 3. FIX — confirmed weaknesses by dimension (critical first)

### Voice / canon accuracy
- **CRITICAL — High drama mistaught and self-contradicted.** Day 07 defines high drama as "theatrical, staged... contained" then says "Both are gremlin food"; canon and the course's own `Maps/M20.png` put HIGH DRAMA under Conscious Purpose / Responsible Game. Fix: rewrite on the responsibility axis, delete "Both are gremlin food," cross-link to Day 10's M20, and fix every mirror (Day 07 lines 51/95-103/385, `Glossary of PM Distinctions.md` lines 355-357 + High drama entry, concat).
- **MAJOR — Bright/shadow sourcing direction reversed.** Day 10 lines 112-114 vs the correct line 116. Fix: "the class whose sourcing generates archiarchy/patriarchy" in Day 10, Map Note M21, Atlas M21, both Glossary entries, concat.
- **MAJOR — Em-dash density 17-24 per 1000 words in every module.** Fix: style-guide budget (≤5/1000, one per paragraph) plus a humanizer pass.
- Minor: rotate the template incantations ("Study the map before reading on" ×27) and cap signature words; one superlative claim per module; soften "the same World Copyleft terms" to "consistent with the spirit of"; reconcile the EHP "5 positions" wording with the six taught positions (0-5).

### Tools
- **CRITICAL — Atlas M12 is an ungated side door into the EHP** while the Day 6 walker enforces a structural consent gate the suite advertises as "not optional." Fix: same gate + trauma carve-out on M12, or convert its embodiment to a description linking the gated day tool. (M09/M11/M27/M29 verified locator-level; no gate needed.)
- **MAJOR — Day 2 persists survival-layer consent forever** (`etb_day02_survival_consent`). Fix: one shared consent component, re-armed every visit, never persisted.
- **MAJOR — Both tool systems invisible to the delivery flow** (zero mentions in Docs 02/03/04; zero Day-file links to Interactive Tools/). Fix: tool slot in Doc 02 §B's artifact list, header row per Day, links at the moment of use; rename by function ("Study the map" / "Run the practice").
- **MAJOR — No export or progress view for 46 localStorage keys**; one browser-data clear destroys 30 days of practice records the course references back to. Fix: local-only `journal.html` (completion dots, journal view, export/import), per-tool export, indicators on both indexes.
- **MAJOR — HTML tools link to raw .md files** (folds into the structure fix).
- Minor: Atlas interaction monotony (make map geometry clickable where it pays); duplicated ~700-line design system with consent-logic drift (template + shared source emitting standalone files); stale "Prototype v0.1" labels; Google Fonts CDN call (EU/GDPR exposure) — self-host WOFF2.

### Structure / delivery
- **CRITICAL — Markdown as delivery; no learner shell.** START HERE has zero internal links; HTML pages link raw .md; relative paths break on every platform Doc 02 §G names. Fix: render all learner-facing pages as HTML from .md sources, extending the Atlas design system.
- **MAJOR — Front door fails**: the internal audit doc sorts above START HERE (both "00 -"). Fix: one un-prefixed entry point; operator docs into their own subfolder; never reuse a prefix.
- **MAJOR — Doc 01 describes a Map Note template that no longer exists** post-v1.7; README sends contributors to it. Fix: spec the shipped formats; defer to a single "what lives where" table.
- **MAJOR — The concat is broken by construction**: all 161 broken links in the tree, mixed audiences, hand-rebuilt with no script. Fix: two generated, path-rewritten, build-stamped editions — or drop it once the shell exists.
- **MAJOR — Pointer errors and private-path leaks**: Day 05 line 223 cites M05 for the M07 practice; Days 07/10 cite `Possability Lab...`/`SPARKS/...` paths that don't ship; headers cite bare .mp4 filenames. Fix: learner files reference only shipped paths; fix M05→M07; automated link checker as release gate.
- Minor: one map split across three folders (collapse to unified per-map pages); "Day" vs "module" naming, URL-hostile filenames, desktop.ini shipping; no next/prev or breadcrumbs anywhere.

### Ops / business layer
- **CRITICAL — No commerce or enrollment-terms layer.** Two safety paths reference "cohort terms" that exist nowhere. Fix: Enrollment Terms & Learner Agreement template + Run-Book "Step 0" (pricing, payments, refund tree).
- **MAJOR — No reference platform stack** (Doc 02 §G is a menu with no pick; manual gating already documented in Run-Book Part 4). Fix: one named, tested stack with per-component privacy verification and tracker columns.
- **MAJOR — Continuation thin and partly wrong**: Possibility Team gets two sentences and `Referral List.md` line 276 mislabels it invitation-only; operator contact ends 2 weeks post-course; StartOver.xyz only in legal text. Fix: PT conversion guide, operator 30/60/90 alumni touchpoints, StartOver.xyz in What's Next.
- **MAJOR — No operator run-book, CM workload model, or cohort cap**; CM overload is the likeliest safety failure. Fix: binding first-cohort cap (e.g. 8-12), hours/week bands per phase, Operator Run-Book delineating operator vs CM, added to the §K gate.
- **MAJOR — Video delivery unresolved**: required orientation videos don't exist; lectures are private recordings (18 of 19, slot 08 missing) cited by local filename with no streaming location. Fix: see Open Question 1; either way remove dead references and ship a manifest.
- **MAJOR — Measurement plumbing missing**: no collection mechanism for the anonymized self-assessment aggregate; no completion/drop-off metric in the §L review. Fix: no-name submission flow; add completion-by-module to the §L pull list (operator-facing, no gamification conflict).
- Minor: witness-bench recruitment undefined (and empty for cohort one); no deployable intake form (operators re-assemble the suicidality screen from prose); no cohort calendar template.

### Practice
- **CRITICAL — The Solo Centering and Grounding Scripts are orphaned.** Script 2 ("Run this before every module. Every single one."), the daily Script 3, and post-High Script 5 are linked from zero Day files — the root cause of the daily-spine gap. Fix: Script 2 as step 0 of every flow; Script 3 named on Day 3 as the standing daily practice; Scripts 5/9 as High-day closers; the file in START HERE's checklist.
- **MAJOR — No daily practice before Day 10**; every Day 1-9 experiment is run-once. Fix: a minimal daily anchor from Day 1 built from existing assets, honoring the "one experiment at a time" bandwidth rule (see Open Question 6).
- **MAJOR — The daily feelings instrument exists but is never promoted.** Day 5's Per-Feeling Bar Reading is the Feelings Form in all but name, scheduled once. Fix: name it, run it every morning Day 5 onward, log it in the Beep! Book, re-read at Days 6/7/10 (the 30-day trend as evidence the Numbness Bar moved). Dedicated map exists: `ALL ETB MAPS/The Feelings Form/`.
- **MAJOR — Beep! Book starts Day 4, then dropped** (zero mentions Days 5-10; Days 1-3 captures have no destination). Fix: book starts Day 1; Day 4 upgrades it with the Go!/Beep!/Shift! grammar; every later capture instruction names it; Day 10's daily catches write into it.
- **MAJOR — Solo experiment reps never re-invoked** (exchange-layer recurrence exists and is good). Fix: each module's experiment uses the Day 4 format and includes one callback rep to a prior instrument.
- Minor: Days 5-9 experiments don't model the Day 4 format; practice visibility folds into the Beep! Book fix (plain dated grid + one weekly "what got skipped, and what does the skip say about my Box?" prompt — data, not reward).

### Safety
- **MAJOR — Screen-4 low-stakes experiment variants promised, never built per-day** (Day 8's live completion conversation and Day 10's declaration unmarked). Fix: Screen-4 variant column in `Experiment Bank.md` + one-line notes on Days 1/7/8/10 with a discreet learner-facing cue.
- **MAJOR — No pathway for the cohort-less reader** despite CC BY-SA. Fix: three-sentence "Reading this without a cohort?" boxes in START HERE and the Day 5/6/9 consent blocks (Low/Medium fine; no EHP or Demon work without a live witness; findahelpline.com).
- **MAJOR — Intake never asks about bereavement or active rupture** though Doc 03 §A and Day 6 both gate on the 60-day rule. Fix: one Y/N question in §A.1 routing to a CM consult, stretched-cadence default.
- **MAJOR — CM load unquantified** (shared with ops).
- Minor: mid-course re-screen checkbox in the Day 5 unlock; learner-facing "stopping well" half-page + leaver wellbeing check; rephrase Day 3's "it works either way"; restate the 40% hard stop inside the Day 6 script at the point of use; France crisis line → 3114 (24/7 national); plain-language pre-course self-screen (current wording uses skills the course itself teaches); surface the Medium-day partner check-in in the Day 2/8 headers (which currently say the opposite).

### Journey
- **MAJOR — No-video dead end** is learner-facing: no text says the written module is self-sufficient even though Doc 02 §B declares it canonical. Fix: per-module "videos are enrichment" statement + the manifest.
- **MAJOR — Solo learner cannot obtain the container** the course hard-gates on (folds into the solo pathway; the "truly solo" track must be a defer-list, not a workaround).
- **MAJOR — No learner-facing re-entry path**, and the Playbook makes silent absence sticky (no chasing past twice; returners re-earn via the witness bench). Fix: "Coming back" one-pager (3+/7+/30+ day tiers, anti-binge, return framed as a rep), linked from START HERE and High-day headers.
- **MAJOR — The back-half climb is under-cushioned**: Days 5-9 stack four High modules plus a heavy Medium, word counts peak in the same stretch, the pause architecture stops at Day 7, and Day 7's consent check says the heaviest stretch is over with Days 8-9 ahead. Fix: name Days 5-9 as the climb in START HERE; recommended low-demand beat between Days 8 and 9; correct Day 7's line.
- Minor: tools discoverability (header rows; GROUND NOW named on High days); ship the "delivery schedule" Day 7 dangles (printable tracker with pause beats marked).
- Dropped (refuted): the 30-50% time-budget claim — the arithmetic misattributed whole-file word counts to single steps. A narrow slot-timing slip survives under pedagogy.

### Pedagogy
- **MAJOR — No verbal/conceptual retrieval anywhere.** Procedural recall is real, but no module schedules teach-back, map redraw before Day 10, or vocabulary recall; the Map Notes' teach-back asset is never used. Fix: 5-minute free-recall warm-up on the prior module in every flow; partner teach-back scheduled 3 times (Days 3/6/9); both framed as verified-in-lived-experience, not quizzes.
- **MAJOR — Practice-quality feedback ends at Day 4.** Exchanges go witnessing-only, the CM never sees content, call demos reach volunteers only — while Doc 01 names intellectual swallowing as the fatal failure mode and the High block starts right after. Fix: repeat the feedback round at Day 8; learner-facing worked exemplars (extend the CM-facing good/drift feed posts); 15 minutes of the mid-course call as opt-in calibration.
- Minor: per-module "Close the loop (5 min)" outcome self-check on the existing three-word scale; honest re-timing of the few slipping slots (Day 1 practice, Day 10 reading) plus a core-vs-optional statement per map representation; a 15-minute recall-based consolidation wired into the existing Day 6→7 pause.

### Coverage
- **MAJOR — Matrix-building never taught; "matrix" defined three conflicting ways** (README's build sense, Doc 02's "structured field," the Glossary's Patriarchy-only sense, plus a dangling "See Day 01" pointer). Fix: half-section matrix-building teaching on Day 3 or 4; Glossary entry leads with the build sense; align Doc 02. Assets ready: `Mini ETB Documents/120725/Building your Matrix.png` + Matrix video; `ALL ETB MAPS/Map of Matrix/`.
- Minor: M21's "closest maps" sentence references unshipped maps (fix by embedding them — see ADD); StartOver.xyz absent from Day 10's What's Next; one-sentence "horizons" pointers naming advanced-tier material (stellating, intimacy offers, Fear Club, Distilling Destiny) as held-container work; linear vs nonlinear possibility vocabulary (one paragraph + glossary line); the patriarchy→archiarchy culture map taught prose-only with its image unused.

### Sources
- **MAJOR — ALL ETB MAPS absent from the Source Inventory** though Maps/M01-M29 are byte-identical copies from it; 33 more clean maps sit undiscoverable. Fix: full inventory section (61 folders; clean PNG + Infographic BEST + photos each; 28 used / 33 unused), regenerated from a scripted, date-stamped listing.
- **MAJOR — Sparks mined generically**: one verbatim quote, zero per-Spark citations despite Doc 01's footnote promise; 99 advanced letter-coded Sparks uninventoried. Fix: per-Spark citations (Days 4 and 10 especially); correct the count to 258 + 99 + 7.
- **MAJOR — M21 ships no map image** while clean renders of the two named-closest maps sit ready. Fix: embed `Map of Matrix.png` and/or `Map of 3 Games.png` with an "adjacent, not dedicated" caveat.
- Minor: four cohort-provenance maps unused where their concepts are day titles or ceremonies (see ADD); the 8 Possability Lab PDFs never embedded; two Mini ETB videos never referenced and three cited-but-never-linked; small count drift in the inventory.

---

## 4. ADD — new content and systems, ranked by teaching value

"Clean PNG ✓" = a ready bare-name render exists in `_PM Possability Manangement/ALL ETB MAPS/<folder>/` (most also have a June-2026 "Infographic BEST" variant). The 28 maps v1 uses came from this pipeline, so embedding is zero-cost.

1. **Daily practice spine + the Feelings Form** (clean PNG ✓ `The Feelings Form/`; companion `Fear Capacity Feelings Form/` ✓): Beep! Book from Day 1 with a Morning Page grid; Bar Reading promoted to a named daily instrument at Day 5; Scripts 2/3/5/9 wired into flows. Sources: `Days/Day 05`; `Solo Centering and Grounding Scripts.md`; `Experiment Bank.md` #3/#28/#32/#83.
2. **Retrieval layer**: free-recall warm-ups, 3 scheduled teach-backs using the Map Notes' "How to explain it verbally" paragraphs, close-the-loop self-checks, and an unscored distinction-recall deck from the Map Notes' key-distinction blocks + Glossary.
3. **Guided audio for every practice script** (red-pill ceremony, center/cord/bubble, low-intensity feelings, solo EHP, ego-state locator, declaration, 60-second grounding) — cheapest high-impact addition; scripts already written. Sources: Days 03/05/06/09/10; Doc 03 §D.
4. **Matrix-building mini-teaching + unified Glossary entry** (clean PNG ✓ `Map of Matrix/`; `Building your Matrix.png` + Matrix video in `Mini ETB Documents/120725/`).
5. **M21 visual fill / Map of 3 Games teaching** (clean PNGs ✓ `Map of Matrix/`, `Map of 3 Games/`) — repairs the only missing map slot; optionally grounds Day 7's "Responsible Game" and Day 10's gameworld work.
6. **A proper 2-3 paragraph high-drama teaching** on Day 7 or 10 (responsibility axis; `Maps/M20.png` already shows it) — companion to the critical voice fix.
7. **Cohort-provenance map embeds** (all clean PNG ✓, all drawn live in the source cohort): `Feelings vs Emotions/` → Day 5 (the title concept has no map); `Red Pill Blue Pill Choice/` → Day 1 ceremony; `Map of Responsibility and Culture/` → Day 1; `Welcome to Expand the Box/` → START HERE (currently imageless).
8. **Module visual enrichment from unused clean renders** (all ✓): Days 5-6 — `Purpose of Feelings/`, `Map of Feelings Sensations/`, `Map of Optional Healing Process/`, `Emotional Healing Process Learnings/`, `EHP Spaceholding Twins/` (→ Doc 03 / Day 6 witness annex). Days 7-8 — `Responsible Story/`, `Possibility Speaking/`, `Letting Your Heart Speak/`. Day 10 — `Map of Culture from Patriarchy to Archiarchy.png` (Mini ETB), `Linear and Nonlinear/`, `Nonlinear Story and Possibility Story/`, `Treasure Map/`, `Possibility Team/`, `StartOver XYZ Resources/`, `Map_of_Creating.pdf` (Lab), plus the linear/nonlinear vocabulary paragraph.
9. **Spark integration**: per-Spark citations in Days 4 and 10; optional Spark-of-the-day per module (one-page distinctions with built-in experiments — shaped for async); the 99 advanced Sparks as a post-course track. Source: `SPARKS/`.
10. **Worked exemplars pack**: annotated strong-vs-drifting partner exchange, filled Beep! Book page, completed experiment capture, sample unmixing restatement — extend the CM-facing good/drift feed exemplars into learner-facing models. Sources: Day 04 criteria; `Cohort Feed Templates.md` §3-4.
11. **Day 0 "Getting your container"** (enrollment in learner voice, partner-acquisition decision tree incl. recruit-a-friend on the 7-line agreement, calendaring ritual) **+ printable schedule/tracker** (repairs Day 7's dangling "delivery schedule" reference).
12. **"Coming back" re-entry one-pager** linked from START HERE and High-day headers.
13. **Safety artifact pack**: Screen-4 variant column; solo-reader boxes; partner-facing "If your partner is in trouble" card (from Doc 03 §F + Day 6's witness script); 18+ line in intake; safety-plan template for Screen-1 routings; next-morning three-question check on High days; "stopping well" section + CM leaver checklist.
14. **Ops artifact pack**: Enrollment Terms + pricing/refund Step 0; reference platform stack guide; Operator Run-Book + CM sizing table; deployable intake form; cohort calendar template; anonymized assessment collection flow; witness-bench onboarding note; Possibility-Team conversion guide (clean PNG ✓ `Possibility Team/`).
15. **Tool additions**: local-only `journal.html` (progress + export/import for all etb_* keys); partner-exchange helper (prompt + timer + listener reply script); standalone bookmarkable `ground.html`; completion dots on both indexes; print/export on High-day logs and Atlas reflections; self-hosted fonts.
16. **Build system**: machine-readable course manifest generating start page/navigators/editions; "what lives where" concept→artifact table; automated link checker as release gate; video manifest; generated Learner + Operator editions; printable 29-map glossary index.
17. **Voice & Style Guide** (Doc 01's six bullets + em-dash budget + signature-word caps + banned-AI-pattern list + voice-anchor appendix; humanizer pass per module) **+ canonical-phrasing ledger** (each glossary distinction annotated with source and canonical wording — the control that would have caught the high-drama drift) **+ a learner-facing "Where this work comes from" block** in START HERE.
18. **Salvage from the best-practices research** (vendor completion stats are directional, not precise): "My Map Book" running completion artifact (one distinction-in-your-own-words + lived example per module, exchanged at Day 10 — retrieval and reflection in one; replaces certificates); progress-keyed messaging engine (completion triggers, recall-question drips, day-4/7 invitations, one-click "pausing intentionally") for self-paced operation.

---

## 5. OPEN QUESTIONS — design forks the architect must decide

1. **Video strategy.** Produce/license a v2 video set (orientation kit + hosting; scripts liftable from the modules) or restructure text-first with videos optional? The sources are private cohort recordings outside the CC grant, one slot missing. Gates every module flow, the manifest, and Doc 02 §B.
2. **Hosting/platform.** Self-hosted static HTML shell vs commercial platform? Decides High-module gating implementation, localStorage journal viability (origin-scoped — all tools must serve from one origin), font/GDPR posture, and where the cohort feed lives.
3. **Solo track scope.** Advisory-only defer list vs fully sanctioned solo mode with recruit-a-witness and self-generated referral packet? The deeper version serves the license-guaranteed audience but weakens a partner gate Doc 02 calls structural safety.
4. **Map visual style.** Keep the May-2026 minimal hand-drawn-emulation renders (what v1 ships), upgrade to the June-2026 "Infographic BEST" batch (60 of 61 folders; clearly the owner's current direction), or layer both (map to teach, infographic to review)? One global decision before any map page is built.
5. **Tool architecture.** Two systems renamed by function ("Study the map" / "Run the practice" — the tools verdict) vs collapse into unified per-map pages (the structure proposal)? Affects the build template, the manifest, and 52 files.
6. **Daily spine size.** One minimal standing anchor (honoring the Experiment Bank's "one experiment at a time; two compete for noticing bandwidth" rule) vs the phased accumulating 5→15 min stack? Auditor and verifier disagree; the answer defines every Day header.
7. **Retrieval vs the no-quiz line.** Free recall, teach-back, and perform-the-outcome checks are clearly inside Doc 02 §J; an unscored deck probably is; answer-checking probably isn't. Where does v2 write the line so contributors don't re-litigate it?
8. **Commerce posture.** Open content free with the paid offering being the held container (CM, screening, pairing, feed), or course access itself priced? Enrollment terms, the refund tree, and the solo-track framing all depend on this.

---

*Build order follows the executive summary: shell and pipeline first (everything else lands inside it), then safety/canon patches (small, high-stakes), then wiring (practice, tools, retrieval), then the business/continuation layer, then source-library enrichment. Every FIX cites the v1 file to change; every ADD cites the source asset.*
