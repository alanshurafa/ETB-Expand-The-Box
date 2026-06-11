# PLAN: Group & Community Delivery (Telegram) — "do it together, at your own pace"

Planned 2026-06-11 on Fable. Status: EXECUTED 2026-06-11 (X1/X2/X3 + sweep complete; link gate 1767 links 0 broken). TARGET WAS: the fork `Digital Expand The Box Group Version/` — the June 2026 edition stays untouched. Executors and file map in §6.

## §1 — What the user asked for

A way for groups to run ETB together: a private Telegram community where everyone has the course; self-paced; people do the rituals and partner experiences by calling on each other; a creative public-accountability mechanism (name what you're doing where others can see it, so you're more likely to do it); group sizes from 2 up to ~100 doing it at the same time.

## §2 — The core design decision: fractal containers, not one big container

The audited safety architecture caps a held cohort at 8–12 because that is what one held container of attention can carry. Scaling to 100 does NOT mean stretching the container; it means nesting them:

| Tier | Size | What it is | Safety container |
|---|---|---|---|
| **Dyad** | 2 | Partner/witness pair | The existing 7-line partner agreement (already shipped) |
| **Pod** | 3–12 | The held group: does rituals together, witnesses each other's High work, runs teach-backs on calls | NEW Pod Charter (extends the 7-line agreement); one Pod Anchor (scheduler/charter-keeper, NOT a facilitator) |
| **Commons** | up to ~100 | The Telegram community: declarations, loop-closings, witness-finding, module rooms, celebration of Beeps | Space Holders (the CM triage rubric adapted; minimum 2; ~1 per 35 members); crisis routing pinned everywhere |

Rules that make this safe: **all High work (EHP, Demon-locator) happens live on a call inside a dyad or pod with a qualified witness — never over text, never in the commons.** The commons is for coordination, declaration, Low/Medium sharing, and finding people. Every existing gate (per-visit consent, readiness checks, witness qualification) transfers unchanged to the pod level. The intake becomes a self-screen + pod-level gate (the deployable Intake Form already exists; pods adopt it; the commons pins the plain-language self-screen and crisis card).

## §3 — The accountability mechanic: "Staking" (Declaring, practiced early)

The course already teaches Declaring as one of the Three Powers (Module 10), and the Day-4 experiment format (what / by-when / what-I-will-notice) is already a complete commitment artifact. The accountability system is those two things made public — no points, no streaks, no leaderboards (the no-gamification line holds; **visibility is the mechanism, not score**):

1. **The Stake Board** (a Telegram topic): you post your experiment in the Day-4 format before you run it. Template provided. Posting = staking your word in front of the community.
2. **Witnessed-by convention:** up to two people reply "Witnessed 🕯" to a stake. They are now the two people you report back to — a named, human hook, not a notification.
3. **Close the loop publicly:** the existing capture-within-ten-minutes discipline becomes a reply to your own stake — what happened, what you noticed. **Failed experiments are posted as Beeps and celebrated as data** (already canon: "failed experiments are Beeps"). The Worked Exemplars Pack gains stake/close/Beep exemplar posts so people see what good looks like.
4. **Sunday skip-read** (already in the Daily Practice Spine): the weekly question — "what got skipped, and what does the skip say about my Box?" — posted as a thread prompt. Optional to answer publicly; the prompt itself is the ritual.
5. **Pod rituals live:** red-pill ceremony, the three teach-backs (Modules 3/6/9), and the Module 8 partner exchange happen on pod calls; the Audio Recording Kit scripts are the call scripts.

## §4 — Rhythm: self-paced AND together

- **Gates stay readiness-based, never calendar-based** (course law, unchanged). Self-paced is the default.
- **Community heartbeat** (the "together" feeling without forced sync): Stake Monday · Loop-close Friday · Skip-read Sunday. People at different modules share the same weekly pulse.
- **Waves (optional):** monthly start dates for people who want true sync; a Wave = a set of pods starting Module 00 the same week, using the existing Cohort Calendar Template. A 100-person launch = one commons + ~8–12 pods in one Wave.
- **Calling on people:** the **Witness Board** topic — structured ask/offer posts ("Seeking a witness for a small EHP, Tue/Wed evenings CET, I've read the witness annex") with the qualification path stated: a witness must have the 7-line/Pod agreement with you + have read the Doc 03 witness annex + Partner Emergency Card. The existing Witness Bench Onboarding generalizes to the commons.

## §5 — Telegram reference configuration (v1 = no bot, conventions + templates only)

Private Telegram group, **forum/Topics mode**, join by invite + pinned self-screen acknowledgment. Topic map:
**📍 Start Here** (pinned: course links, self-screen, crisis card, how this community works) · **🔥 Stake Board** · **✅ Loop Closings** (or merged with stakes as replies — operator's choice) · **🤝 Witness Board** · **🧭 Pod Directory** (find/form pods; pods then run as their own small private TG groups) · **📚 Module rooms 00–11** (questions/shares per module, Low/Medium content only) · **🚨 Ground & SOS** (pinned: ground.html link, crisis lines, "this group is not a crisis service — here is who is") · **🕯 Space Holder line** (DM route).
Privacy stated plainly in Start Here: a private group is still on Telegram's servers; share at the depth you choose; the Beep! Book stays private by default — stakes are chosen exposure; practice data stays in your browser (journal.html export).
**Enabler:** the course must be URL-addressable for Telegram links → enable GitHub Pages on the repo (one-time, needs owner OK; repo is already public). **Deferred (spec only, build later if wanted):** a Telegram bot for stake templates, witness matching, and wave reminders.

## §6 — Execution map (on GO)

| Executor | Model | Writes |
|---|---|---|
| **X1** | Opus | NEW root doc `06 - Group and Community Framework.md` (the §2–§4 model, made canonical: tiers, Staking choreography, safety adaptation, scale table) + EDITS: Doc 02 (Telegram reference config in the platform section), Doc 04 (pod as a recognized container path; Space Holder role; scale table; law otherwise intact), Doc 05 (Run-Book community variant step) |
| **X2** | Opus | NEW Facilitator Resources: `Telegram Community Operator Guide.md` (setup checklist, topic map, pinned-post texts, permissions, Space Holder staffing + triage adaptation, Wave launch sequence) · `Community Message Templates.md` (adapted from Cohort Feed Templates: welcome, stake/close/Beep formats, skip-read, witness ask/offer, wave start) · `Pod Charter.md` (the 3–12 agreement extending the 7-line dyad agreement) + stake/close/Beep exemplars appended to Worked Exemplars Pack |
| **X3** | Opus | NEW learner-facing `Practice/Practicing in a Group.md` (join/form a pod, the Staking choreography, calling on a witness, running rituals on calls, privacy) + EDITS: Module 00 decision tree gains the community-pod path; START HERE one-line + link; 00 Manifest registers all new artifacts |
| **Sweep** | Sonnet | Link gate (build.py), canon greps, consistency of the new cross-references; commit at each boundary |

Disjoint file ownership as listed; no concurrent edits to the same file. After X1–X3 + sweep: rebuild, commit, push, update HANDOFF. Separately, on explicit OK: enable GitHub Pages and swap pinned links to public URLs.

## §7 — Open forks I locked (changeable on request)

1. **Commons ≠ container** (fractal model) rather than one big cohort — this is the safety-preserving reading of "up to 100 together."
2. **Accountability via visibility, not points** — staking/witnessed-by/loop-close instead of streaks or completion races, to stay inside the no-gamification law.
3. **Telegram v1 runs bot-less** (conventions + templates); bot is a later, separate build.
4. **High work never over text** — non-negotiable safety line carried from the audit.
