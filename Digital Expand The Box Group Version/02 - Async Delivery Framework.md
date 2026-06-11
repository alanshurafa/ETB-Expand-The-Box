# 02 — Async Delivery Framework

This document is the **operational manual** for delivering Expand the Box as a self-paced asynchronous online course. A community manager, course operator, or solo cohort steward reads it in full before opening a cohort. The launch sequence that uses it lives in [05 - Operator Run-Book.md](05%20-%20Operator%20Run-Book.md); the binding safety protocol it serves is [04 - Container and Gatekeeping Protocol.md](04%20-%20Container%20and%20Gatekeeping%20Protocol.md).

The course works without a live facilitator on every module. It does **not** work without structure. The structure is here.

---

## A. The learner's module cycle

A learner moves through one module per **~3 days**. The rhythm per module:

| Cycle day | Action | Time |
|---|---|---|
| 1 | Read the module (Sitting 1, then 2–3 with real breaks) + solo embodied practice | 60–120 min total across sittings |
| 1 or 2 | Record partner check-in (voice message) | 5–10 min |
| 2–3 | Run the between-module experiment in real life | no scheduled time; it rides ordinary life |
| 3 | Listen to partner's reply; record reflection back; journal; one line to the cohort feed | 25–30 min |
| every day | The daily spine sit (Phase A or B per module header) | 5–10 min |

Total active time: ~2 hours on Low modules, ~3–3.5 on High (5, 6, 7, 9); each module header carries its own honest estimate, which is authoritative. Async partner-reply latency (24h SLA) can stretch a High module's calendar time, especially Module 6.

Twelve modules at ~3 days ≈ **~35 days** end to end, including the integration pause after Module 6 and the rest day between Modules 8 and 9. Compressed (~25 days) and stretched (~60–70) both work as long as the rhythm of *recall → content → practice → experiment → reflection* and the two pause beats are preserved. The pause beats are not compressible.

---

## B. Module artifacts (what the learner actually receives)

Each module delivers, in order:

1. **The written module file** (`Days/Day NN - ….md`, rendered as `Course/module-NN.html` in the shell). The single canonical source for the module. **Every module is complete without video** (see §E below).
2. **The daily-spine instruction** in the header: which phase the morning sit is in, linked to the binding spec ([Practice/Daily Practice Spine.md](Practice/Daily%20Practice%20Spine.md)).
3. **THE TOOL SLOT.** Every module names its two interactive surfaces at the moment of use, as buttons in the flow:
   - **"Study the map"** → the module's Map Atlas pages (interactive walk-through of each map taught).
   - **"Run the practice"** → the module's Interactive Tools suite (the practice instrument for that module).
   - Standing utilities, every module: **[the journal](Interactive%20Tools/journal.html)** (local-only progress view, export/import of all `etb_*` records) and **[ground.html](Interactive%20Tools/ground.html)** (the 60-second grounding script, bookmarkable, one tap).
   - The Manifest §1 table registers which pages and tools belong to which module. Learners never see "two systems"; they see two buttons.
4. **Map Note cards** for the maps introduced.
5. **The partner prompt** (inside the module file's exchange section).
6. **The experiment card** (inside the module file, Day-4 format).
7. **Reflection prompts.**

Everything ships as text/HTML from one folder. Nothing requires an account, a server round-trip, or a video player.

---

## C. Pairing partners

### Pairing as the witness strand of the container

The course's container is woven from several strands: the learner's declared context (the red-pill commitment), the four working agreements, the body practices, the daily spine, the cohort boundary, the CM's gatekeeping, and the **partner pairing**. (v1 called this structure "the training matrix"; v2 reserves *matrix* for the build sense per the ledger and calls this the **container**.)

The pairing is the witness strand: a structured place to speak the learner's material out loud, a witness who listens without advising, a presence that interrupts isolation on the High modules. What the partner does **not** hold: the learner's safety container, clinical care, commitment, or responsibility for their own state. The partner agreement (Doc 04 §B) is signed before any exchange; a learner without a live pairing (or recruited witness, §K below) cannot unlock High modules.

### C.1 Matching rules

- **Match before Module 1.** Late enrollers are matched before content access opens.
- **Match on cadence first, content preference second.** Compatible daily windows beat philosophical fit.
- **Avoid pre-existing close ties** for cohort pairing. If unavoidable in a small cohort, name the dynamic and add a witness partner. (The recruit-a-witness path for solo readers deliberately uses a friend; the difference is scope: a recruited witness holds the High-module witness role only, not the full course-long exchange. Doc 04 §B2.)
- **Re-match by Module 4 if it is not working.** Silent partnerships are worse than swapped ones.

### C.2 Voice-message exchanges (default mode)

Voice carries tone, breath, and the texture of the emotional body; text strips it. The platform must meet the privacy minimums in Doc 04 §H: private 1:1 thread, no automatic AI transcription, no public forwarding, deletion option, end-to-end encryption preferred (Signal is the reference pick). Public servers, group chats, and auto-summarizing platforms do not qualify.

Default shape per module: A records 3–8 min on the partner prompt → B replies within 24 hours, 3–8 min: *what I heard · what I noticed in myself · one question I'm leaving with you*. Partners do not advise, fix, diagnose, or pretend to feel what they do not feel. Module 8 teaches the listening formally; until then the "we're learning this" frame covers clumsy exchanges.

### C.3 Scheduled async calls (alternative)

A 30-minute scheduled call substitutes: ~10 minutes each, uninterrupted, the other witnessing.

---

## D. The cohort feed

One shared private space; learners post a line or two after each module: what landed, what is sticking sideways, optionally a question or a witness offer. Not posted: long confessionals (the partner exchange holds those), other people's stories, advice (CM redirects, verbatim language in [Cohort Feed Templates](Facilitator%20Resources/Cohort%20Feed%20Templates.md) §4).

Moderation: CM reads every post within 48 hours (24 during High windows), triages each against Doc 04 §F (yellow = DM within 24h; red = immediate, crisis numbers in the first message), and keeps the feed narrow.

---

## E. Video posture (text-first, declared)

**Every module is complete without video.** The written module is the canonical teaching; source videos are optional enrichment. The operator-facing registry of what exists and where to get it is [`Facilitator Resources/Video Manifest.md`](Facilitator%20Resources/Video%20Manifest.md). Binding rule: **no bare video filename appears anywhere in the learner path**; learner-facing text says "optional enrichment: see the Video Manifest" and nothing more specific. The [Audio Companion Recording Kit](Facilitator%20Resources/Audio%20Companion%20Recording%20Kit.md) gives an operator the scripts and tone notes to record guided audio for every practice script in an afternoon; the course ships scripts, not recordings.

---

## F. REFERENCE PLATFORM STACK (the named pick)

v1 offered a platform menu with no pick; that gap is closed. Per ARCHITECTURE decision 2, the reference stack is:

**1. The self-hosted static shell — one origin.** `index.html` (the front door) + `Course/module-NN.html` pages + the Map Atlas + the Interactive Tools, all served from **one origin**. Any static host works; **GitHub Pages works** since the repo is public; even `file://` works for a single learner. One origin is not cosmetic: the tools' localStorage records and the journal's export view are origin-scoped, so splitting the tools across hosts silently splits the learner's records.

**2. The cohort feed — a private space off the shell.** Reference pick: a **Discourse private category** (closed to the cohort, author-deletable posts, CM can hide, not externally visible). Lighter alternative: a **Signal group** (E2EE, but no post-hiding and weaker triage ergonomics; acceptable for cohorts ≤8). Either must pass Doc 04 §H before launch.

**3. Partner channel — partners choose** from the §H-compliant list (Signal reference pick).

**4. Gating — manual, per the Run-Book.** The static shell has no server logic, so High-module gating is procedural: the CM verifies the Doc 04 §D unlock checklist per learner and releases the module link (the Run-Book sequences this). The consent components inside the gated tools enforce the per-visit consent layer regardless.

### Per-component privacy table

| Component | Where data lives | What the operator can see | External calls |
|---|---|---|---|
| Static shell (pages, Atlas, tools) | learner's browser only; all `etb_*` keys are **localStorage, never transmitted** | nothing | **zero** — fonts self-hosted in `_assets/fonts/`, no CDN, no analytics, no trackers |
| `journal.html` export | a file the learner saves locally | nothing | zero |
| Cohort feed (Discourse private category) | the Discourse instance | posts (metadata-only triage log) | per instance; self-host or EU host for GDPR posture |
| Partner channel (Signal) | the partners' devices, E2EE | nothing (tracker logs *that* exchanges happened, never content) | Signal infrastructure |
| 1:1 CM channel | per chosen tool (Signal reference) | message content, logged metadata-only | per tool |
| Consent (all gated tools) | **nowhere — per-visit, never persisted** | nothing | zero |

Verification before launch is Step 1 of the [Operator Run-Book](05%20-%20Operator%20Run-Book.md). The v1 platform menu survives as Appendix A, marked *alternatives*.

### F.2 The Telegram reference configuration (community scale)

The §F stack runs a held cohort. When the shape is a community of up to ~100 people doing the work together at their own pace, the reference configuration adds Telegram alongside the static shell, not in place of it: the course pages, Atlas, and tools still serve from one origin (GitHub Pages works), and Telegram becomes the coordination space. The full model is [06 - Group and Community Framework.md](06%20-%20Group%20and%20Community%20Framework.md); this is the platform-layer summary.

**v1 runs bot-less:** conventions and templates only, no custom software. A private Telegram group in **forum/Topics mode**, joined by invite plus a pinned self-screen acknowledgment. The topic map:

| Topic | Holds |
|---|---|
| 📍 **Start Here** (pinned) | course links, the self-screen, the crisis card, how the community works |
| 🔥 **Stake Board** | experiments posted in the Day-4 format, before they run |
| ✅ **Loop Closings** | what happened, what was noticed (or merged into the Stake Board as replies; operator's choice) |
| 🤝 **Witness Board** | structured ask/offer posts for witnesses, with the qualification path stated |
| 🧭 **Pod Directory** | find and form pods, which then run as their own small private Telegram groups |
| 📚 **Module rooms 00–11** | questions and shares per module, **Low/Medium content only** |
| 🚨 **Ground & SOS** (pinned) | the `ground.html` link, crisis lines, "this group is not a crisis service, here is who is" |
| 🕯 **Space Holder line** | the DM route to a Space Holder |

**Privacy line, stated in Start Here:** a private group is still on Telegram's servers, so members share at the depth they choose; the Beep! Book stays private by default and a stake is chosen exposure; practice data stays in the browser (the `journal.html` export is the only copy that leaves the device). The High-work-never-over-text law (Doc 06 §B) governs every topic: the module rooms and boards coordinate the work and celebrate it, while the EHP and Demon-locator practices happen live on a call inside a dyad or pod, never in any topic. Telegram must still pass the Doc 04 §H minimums for the partner channel; the deployment checklist and the pinned-post texts live in the [Telegram Community Operator Guide](Facilitator%20Resources/Telegram%20Community%20Operator%20Guide.md).

**Enabler:** the course must be URL-addressable for the Telegram links, so the operator enables GitHub Pages on the (already public) repo, a one-time step needing the owner's go-ahead. **Deferred (spec only):** a Telegram bot for stake templates, witness matching, and Wave reminders is a later, separate build; v1 needs none of it.

---

## G. SOLO MODE (sanctioned, gates intact)

The license guarantees readers without a cohort; the course holds a real path for them instead of pretending they do not exist. Per ARCHITECTURE decision 3:

**What solo readers can do, fully:** all Low and Medium modules; the daily spine; the Atlas and the tools; the journal; the experiments (Screen-4 self-check applies, see Doc 03); the self-assessment.

**What stays gated, and the two named paths through the gate.** The High modules (5, 6, 7, 9) keep the witness requirement. The structural partner gate is preserved; what broadens is the path to satisfy it:

- **(a) Recruit-a-witness.** A friend qualifies. The instrument is the 7-line agreement; the protocol (who qualifies, what the witness reads, what disqualifies) is Doc 04 §B2. With a recruited witness, the High modules open as designed.
- **(b) Defer-list.** Without a witness, the solo reader reads the High teaching in full, runs the locator-level practices (bar readings, drama detection, ego-state location), and **defers the witnessed practices** (the EHP and Demon-adjacent work) until a witness exists. The module files mark exactly which practices defer.

**Why the gate holds even solo:** the EHP's witness is not ceremony; it is the containment mechanism for material that can exceed what a person alone can re-ground from. A course that waives that for convenience is not safer for being more accessible.

"Reading this without a cohort?" boxes appear in `START HERE.md` and in the Module 5/6/7/9 consent blocks, with [findahelpline.com](https://findahelpline.com) named as the no-cohort referral floor. Solo readers have no CM and no SLA; the boxes say so plainly.

---

## H. Optional live integration calls

Two optional live calls per cohort, unchanged from v1: **mid-course after Module 6** (placed after the heaviest module, before Module 7; integration and a breath, not a warm-up; 15 minutes may run as opt-in feedback calibration per Doc 01) and **end-of-course after Module 11** (declarations round, gratitude, what's-next). Recording rules per Doc 04 §H: personal shares never recorded; teaching segments only with per-call consent from everyone.

### The pause architecture (built into the cadence, not optional)

- **After Module 6:** at least one full low-demand day. No new content; ground, sleep, journal, partner check-in, and the 15-minute recall consolidation rep. CMs hold this even on compressed cadence.
- **Between Modules 8 and 9:** one scheduled rest day. Module 8 is as demanding as the High modules for many learners; Module 9 opens ego-state material. The rest day is on the printable schedule from Module 00.

---

## I. The community manager role

The CM is the **container caretaker**, not the teacher. Responsibilities (pre-cohort matching and packets, per-module feed triage and tracker checks, High-week vigilance, closure, the referral list, never therapy) are unchanged from v1 and sequenced in the two run-books. The binding qualification bar is Doc 04 §J; the **binding first-cohort cap (8–12 learners) and the hours model** live in Doc 04 §K2 and the [Operator Run-Book](05%20-%20Operator%20Run-Book.md) Step 2. A CM holding more than the cap is the likeliest safety failure in the whole design; the cap is part of the launch gate.

---

## J. The referral pathway

Every learner receives a per-learner referral packet generated from intake (country, region, language): crisis line first, licensed-clinician directory, PM-aware coaches, DV/legal resources if Screen 4 returned yes, the not-therapy disclaimer. Generated and acknowledged before content access opens; the CM verifies. Template: [Facilitator Resources/Referral List.md](Facilitator%20Resources/Referral%20List.md). France's national line is **3114** (24/7).

---

## K. Cadence variants

| Variant | Pace | Notes |
|---|---|---|
| **Default** | ~3 days/module, ~35 days | Best for most learners |
| **Compressed** | ~2 days/module, ~25 days | Only with real bandwidth; the two pause beats still apply |
| **Stretched** | 4–6 days/module, 40–70 days | Default offer for screen-flagged and bereavement-flagged learners |
| **Pulsed** | modules in bursts with week-long breaks | CM keeps pairings alive at re-entry |

Pace is the learner's; the CM aligns the partner. Mismatch protocol: Doc 04 §I.

---

## L. What this framework deliberately leaves out

- **Gamification, badges, streaks, completion certificates.** They feed the Gremlin's appetite for approval and completion points. PM does not reward compliance.
- **Quizzes and answer-checking.** PM is verified in lived experience. The retrieval layer (free recall, teach-backs, flip-card recall) lives entirely on the generation side of **the retrieval line in Doc 01**, which defines exactly what is allowed and what never will be. Contributors read that section before proposing anything recall-shaped.
- **Discussion forums for "questions about PM."** The feed stays narrow.
- **An app, accounts, analytics.** A folder of pages is enough, and the privacy table in §F is only honest because of it.

---

## Appendix A — platform menu (alternatives, not the pick)

The v1 menu, kept for operators with existing infrastructure. Any combination of (Teachable / Podia / Kajabi / Notion / Circle) for content + (Telegram / WhatsApp E2EE / Voxer / Signal) for partner voice + (closed forum / moderated shared doc) for the feed can work **if** every component passes Doc 04 §H and the tools still serve from one origin. Commercial platforms that re-host the HTML tools on their own domains split localStorage from the Atlas; test the journal before committing. The reference stack in §F exists because every one of these alternatives has failed at least one of those checks somewhere.

---

<sub>🄯 **World Copyleft 2026** · *Expand the Box (Digital)* · licensed **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**, consistent with the spirit of World Copyleft · re-presents Possibility Management thoughtware originated by Clinton Callahan & the Possibility Management community · this course is an independent re-presentation, **not an official Possibility Management training** · please share, share-alike · Powered by Possibility Management ([possibilitymanagement.org](https://possibilitymanagement.org)) · full terms: `LICENSE.md` in the course root</sub>
