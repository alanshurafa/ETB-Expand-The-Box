# PLAN: HTML shells for both course versions (+ complete W-B4)

Planned 2026-06-11 on Fable; executed by delegated agents (Opus/Sonnet) per the token-policy structure. Outcome: both versions open in a browser from a real front door. v2 gets its full W-B4 deliverables; v1 gets an **additive-only** viewing shell.

## §0 — Constraints binding on every executor

- REPO = `/Users/shurafa/Project/ETB-Expand-The-Box`. V2 = `REPO/Digital Expand The Box June 2026`. V1 = `REPO/Digital Expand The Box May 2026`.
- **No git commits** — the orchestrator commits.
- **V1 existing files are frozen.** Executor D adds NEW files only (`index.html`, `Course/` renders, optional `_assets/` if needed); every pre-existing v1 file stays byte-identical. v1 content renders AS-IS, including its known canon bugs — it is the historical May 2026 edition (D adds one neutral banner line on v1 pages: "Archived May 2026 edition — the current course is the June 2026 edition" linking `../Digital%20Expand%20The%20Box%20June%202026/index.html`).
- All new HTML: self-hosted fonts only (`_assets/fonts/fonts.css` at the right relative depth — v2 has it; for v1, link ACROSS to `../Digital Expand The Box June 2026/_assets/fonts/fonts.css` is NOT allowed (versions must be self-contained); instead Executor D copies the `_assets/fonts/` folder into V1 root as a new folder — additive, allowed). Never fonts.googleapis/gstatic.
- No gamification (no scores/streaks/percentages/badges). Completion dots = quiet presence indicators only.
- Works from `file://` — no fetch() of local resources, no absolute paths, %20-encoded relative hrefs.
- localStorage: only `etb_*` keys; consent NEVER stored.
- v2 canon: anything content-bearing follows `V2/Facilitator Resources/Voice and Style Guide.md` (ledger: high drama under Conscious Purpose/Responsible Game; sourcing bright→archiarchy, shadow→patriarchy; matrix build-sense; six EHP positions 0–5). v2 footer block = the Voice Guide standard ("consistent with the spirit of World Copyleft" + not-official-PM line).
- Design system: extract from an existing v2 Atlas page (`Map Atlas/M10 - New Map of Feelings.html`): tokens, paper-grain, EB Garamond/Fraunces/JetBrains Mono, eyebrow labels, reduced-motion, escapeHtml, GROUND NOW pattern where specified.

## §A — Executor A (Opus): v2 build pipeline + front door + Course pages

1. `V2/_build/build.py` (Python 3; try `pip3 install --user markdown`, else built-in minimal md converter; must run offline):
   - RENDER 12 `Days/*.md` → `V2/Course/module-NN.html`, self-contained design-system pages (fonts at `../_assets/fonts/fonts.css`), faithful markdown (headings/tables/blockquotes/images/code blocks).
   - LINK REWRITE in rendered pages: `Days/*.md` links → sibling `module-NN.html`; links to shipping .md files (Practice/, Facilitator Resources/, root docs) unchanged (they resolve via `../`); `../Maps/*.png` unchanged (same depth from Course/ — verify).
   - NAV: prev/next module + breadcrumb to `../index.html` on every Course page.
   - LINK CHECKER (release gate): crawl every internal href/src in all V2 .html and .md → `V2/_build/linkcheck-html.md`; nonzero exit on breakage. Atlas pages matching `M(32|33|35|37|38|39|40|43|44|46|47) - *.html` may be mid-build by Executor B: flag PENDING if absent, don't fail on them.
   - EDITIONS: generate `V2/EXPAND THE BOX v2 — Learner Edition.md` (START HERE + Days 00–11 + Practice/, links path-rewritten, build-stamped) and `V2/EXPAND THE BOX v2 — Operator Edition.md` (README + Docs 00–05 + Facilitator Resources/). Header on both: generated, never hand-edited.
   - Idempotent; build-date stamp.
2. `V2/index.html` — THE front door. Mirrors `START HERE.md` content (adapt, don't invent): what this is, lineage block, how the course runs, first three steps, module list 00–11 → `Course/module-NN.html`, links to Practice/ .md files, `Map%20Atlas/index.html`, `Interactive%20Tools/index.html`, `journal.html`, `ground.html`, Coming Back, LICENSE. Quiet per-module completion-dot row (presence of that module's `etb_*` keys). v2 footer.
3. `V2/Interactive Tools/index.html` — add per-day completion dots; confirm journal.html + ground.html entries exist (add quietly if not). Touch nothing else in that file.
4. RUN build.py; report link-checker verdict.

## §B — Executor B (Opus): v2 Atlas — 11 new pages + index regroup

1. Build 11 pages in `V2/Map Atlas/` with EXACTLY these filenames (module links already point at them):
   `M32 - Map of Responsibility and Culture.html` · `M33 - Feelings vs Emotions.html` · `M35 - Map of Feelings Sensations.html` · `M37 - Fear Capacity Feelings Form.html` · `M38 - EHP Spaceholding Twins.html` · `M39 - Map of Optional Healing Process.html` · `M40 - EHP Learnings.html` · `M43 - Letting Your Heart Speak.html` · `M44 - Linear and Nonlinear.html` · `M46 - Map of Matrix.html` · `M47 - Map of 3 Games.html`
2. METHOD (token-efficient, audit-sanctioned): template-stamp, don't hand-copy. Read `M10 - New Map of Feelings.html` once as the structural template; write generator `V2/_build/gen_atlas.py` (template + per-map CONTENT dict); emit 11 standalone files; spot-fix what can't parameterize. Generator stays in repo.
3. Per page: header label "Study the map"; `../Maps/MXX.png` with alt text; 3–5 key distinctions (ledger-compliant); 6–10 flip-cards (generate-then-flip recall framing, no scoring); common-misunderstandings block; one reflection prompt saving to `etb_atlas_MXX`; GROUND NOW + 60-second modal identical to the suite's; v2 footer.
4. Content sources (v2 modules): M32←Day 01; M33/M35/M37←Day 05; M38/M39/M40←Day 06; M47←Day 07; M43←Day 08; M44/M46←Day 10 (M46 also Day 03 matrix-building).
5. SAFETY: M38/M39/M40 are locator/study level ONLY — no do-it-now EHP steps; route practice impulses to `../Interactive%20Tools/Day%2006/ehp-walker.html` with the trauma carve-out (copy the approved wording pattern from the fixed M12 page).
6. Regroup `V2/Map Atlas/index.html`: module-grouped sections 01→10 including the 11 new pages; M21 slot notes "no dedicated map; M46/M47 adjacent"; completion dots from `etb_atlas_*` presence; keep all 29 existing entries; "Study the map" + recall-deck framing.

## §C — Executor C (Opus): v2 Map Note cards — verbal teach-back layer

1. All 29 existing cards in `V2/Map Notes/`: add `## How to explain it verbally` — one spoken-voice paragraph (60–110 words) a learner says aloud to teach the map from memory + one-line "If you only remember one thing". Ledger-compliant (M13/M20 high drama; M21 bright/shadow — already canon-fixed, extend don't regress; M12 six positions 0–5). Replace footers with the v2 block. Change nothing else.
2. Create 11 NEW cards (same format + verbal section), names matching §B's M-numbers with `.md`. Image `../Maps/MXX.png`; pointer block links the teaching module in `../Days/` and the Atlas page in `../Map%20Atlas/` (%20-encoded). M38/M39/M40: study-level only, practice routes to the gated Day 6 walker.
3. Verify: 40 cards; canon greps silent; em-dash budget; links resolve (Atlas pages may land in parallel — treat §B filenames as resolving).

## §D — Executor D (Sonnet): v1 additive viewing shell

1. ADDITIVE ONLY. Copy `V2/_assets/fonts/` → `V1/_assets/fonts/` (new folder).
2. Write `V1/index.html`: archived-edition front door in the same design system: title, the archive banner (§0), the v1 README/START HERE orientation summarized faithfully (render v1's actual words where possible), links: rendered `Course/day-NN.html` pages (below), `00 - START HERE (Learner Welcome).md`, `Interactive%20Tools/index.html`, `Map%20Atlas/index.html`, `LICENSE.md`. v1's own footer wording (it is the archive — do not impose v2 footer language on v1 content).
3. Render v1's 10 Day files + START HERE → `V1/Course/day-NN.html` + `V1/Course/start-here.html` (simple faithful md→HTML; a small `V1/Course/_render_v1.py` kept beside them is fine, or reuse stdlib approach; NO edits to source .md). Same nav pattern (prev/next, breadcrumb to ../index.html). Render content verbatim — v1's known bugs stay (archive).
4. Verify: every pre-existing v1 file byte-identical (`git status` must show only ADDED paths under V1); all new links resolve; no external font calls.

## §E — Orchestrator close-out (after A–D)

Run `build.py` (fresh, post-Atlas) → link gate must pass with zero PENDING; canon regression greps over new HTML; `git add -A`, commit, push; update `_build/HANDOFF.md` (W-B4 complete + v1 shell noted); report to user with file:// links to both front doors. W-B5 (full QC + delivery report) remains a separate phase.
