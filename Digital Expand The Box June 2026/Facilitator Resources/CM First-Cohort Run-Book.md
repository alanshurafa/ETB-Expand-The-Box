# CM First-Cohort Run-Book

| | |
|---|---|
| **For** | A qualified-but-new Community Manager (CM) running their first async Expand the Box cohort |
| **When** | Open at Week 0 (before any learner is enrolled) and work it top to bottom through cohort close |
| **Turns into a path** | What Doc 04 holds as a *bar* (qualifications, checklists, rubrics), this turns into a *sequence* — what you do, in what order |
| **Reads alongside** | `04 - Container and Gatekeeping Protocol.md` (the binding protocol — this run-book operationalizes it) · `03 - Safety and Facilitation Framework.md` Sections F, G, K, L · `02 - Async Delivery Framework.md` Sections C, D, F · `Async Partner Pairing Playbook.md` · `Cohort Feed Templates.md` |

This is not a re-statement of the protocol. Doc 04 is the law; this is the route through it. Where a thing is fully specified elsewhere, this file points to the section and tells you *when* in the sequence to do it — it does not duplicate it. Read the cross-referenced sections; do not assume the one-line pointer is the whole instruction.

Before you start: confirm your own qualifications are met (Doc 04 §J). If your clinical supervisor is not yet named and contracted, and your liability insurance is not in force, you are not ready to open a cohort. Stop here and close those first. Templates for both agreements are in `CM Agreement Templates.md`.

---

## The shape of the run (one screen)

```
WEEK 0      Self-readiness · platform stack · supervisor + backup CM contracted
WEEK 0      Intake opens → screen every applicant (Doc 04 §A) → route green/defer/1:1
WEEK 0–1    Referral packet per learner (Doc 04 §E) · partner matching (Playbook §1)
WEEK 0–1    Partner agreements signed · platforms chosen · pairing tracker built
PRE-LAUNCH  Pre-cohort checklist sign-off (Doc 04 §K) — every box, or no open
─────────────────────────────────────────────────────────────────────────────
MODULES     Per-module cadence: read feed ≤48h · triage every post · tracker check
HIGH WEEKS  Days 5, 6, 7, 9 — extra-vigilance checklist before/during/after
ALWAYS      Backup CM covers any window you're unreachable · red = immediate/15-min
─────────────────────────────────────────────────────────────────────────────
CLOSE       Day 10 closure · pairing close-out · feed gratitude (Feed Templates §7)
POST        Post-cohort review 1–2 weeks after Day 10 (Doc 04 §L) · 1 improvement
```

Everything below expands one band of this strip.

---

## Part 1 — Pre-launch sequence (Week 0 → content opens)

Do these in order. Each step has a *done-when* you can check off. Nothing downstream opens until the step above it is closed.

### Step 1 — Confirm your own readiness (before any learner sees a form)

Doc 04 §J is the bar. Run it on yourself first.

- [ ] Expand the Box (this or equivalent live ETB) completed, plus one further PM training
- [ ] Current mental-health first-aid (or country-recognized equivalent) certification in date
- [ ] Clinical supervisor named, contracted, and reachable for red-flag consultation (agreement template in `CM Agreement Templates.md`; this is the consultation agreement Doc 04 §J requires)
- [ ] Written CM–Operator agreement signed (scope, liability, confidentiality exceptions — template in `CM Agreement Templates.md`)
- [ ] Professional liability insurance in force for your jurisdiction (or you are employed by an entity that carries it)
- [ ] You have re-read Doc 04 §F (triage) and §G (crisis escalation) within the last 30 days

**Done-when:** every box above is checked. If any is open, you are not a qualified CM for this cohort yet (Doc 04 §J — "a cohort run by an underqualified CM is a cohort running without a safety framework"). Close the gap before Step 2.

### Step 2 — Stand up the platform stack

Pick the stack, then test each component against the privacy minimums in Doc 04 §H **before** intake opens — not after learners arrive.

- [ ] Document hosting: access-controlled, not publicly indexed, deletion-on-request supported
- [ ] Cohort feed: closed to the cohort, not externally visible, author can delete, CM can hide
- [ ] 1:1 CM channel: private, metadata-only logging
- [ ] Voice-message tool the partners will use meets §H (you don't pick it for them, but you publish the acceptable list: Telegram / WhatsApp E2EE / Voxer / Signal — never Discord servers, group chats, or anything that auto-transcribes)
- [ ] The private spreadsheet that will hold the pairing tracker (Doc 04 §C) and triage log (Feed Templates §5) exists, and only you and your supervisor can open it

**Done-when:** every component passes §H, or you've replaced it / shrunk the cohort per §H's fallback ("cohort feed becomes a shared doc the CM moderates manually").

### Step 3 — Open intake and screen every applicant

Intake is the gate, not a survey (Doc 04 §A). Every prospective learner completes the 12-minute form before content access is even discussed.

For each applicant:

- [ ] Identity, cadence, region, language, availability captured (Doc 04 §A.1) — you need region and language to generate the referral packet, and cadence + time-zone window to match partners
- [ ] The five screens applied with their thresholds (Doc 04 §A.2): suicidality · trauma & dissociation · addiction · coercive environment · mania/psychosis
- [ ] Each applicant routed to exactly one of three outcomes:
  - **Green → continue.** All five screens returned "none of the above" (or the explicitly-allowed in-care variants).
  - **1:1 consult required → book it before access.** Any screen hit a "CM 1:1 consult" threshold, or the applicant answered "I'd rather not say." Remember the learner-facing framing: "no" or "rather not say" routes to a conversation, **not** automatic denial.
  - **Defer → no access now, re-application path given.** Any screen hit a defer/clinician-confirmation threshold (e.g., current suicidal plan/intent; monthly-or-more dissociation or lost time; uncontrolled addiction; mania/psychosis in past 12 months). Send the relevant referral-list portion and the re-application language from Doc 04 §A.2.
- [ ] Coercive-environment "yes" (Screen 4) flagged on the learner's record now — it changes their referral packet (adds DV/legal resources) and substitutes their between-module experiments with low-stakes variants (Doc 04 §A.2, Screen 4)
- [ ] Acknowledgments completed (Doc 04 §A.3 — six initials, including "this is not therapy" and "I will pair before Day 1")

**Done-when:** every applicant is green-with-acknowledgments, scheduled for a 1:1, or deferred-with-resources. No one moves to matching until they are green and acknowledged.

> First-cohort note. Do the screening yourself, slowly, applicant by applicant. Do not batch it or delegate the threshold judgment to a form's auto-logic on your first run — you want to feel where the thresholds bite before you trust automation with them.

### Step 4 — Generate the referral packet per learner

For every green/acknowledged learner, generate the packet from their §A.1 inputs (Doc 04 §E). This is region-specific; a generic packet is not the artifact.

- [ ] Crisis line for the learner's country, listed **first**
- [ ] Licensed-clinician directory link for their region (brief if they already have a clinician)
- [ ] PM-aware coaches in their language, with rates
- [ ] DV + legal resources **only if** Screen 4 returned yes
- [ ] Not-therapy disclaimer paragraph
- [ ] Packet saved as the learner's downloadable PDF **and** kept on the platform

**Done-when:** a packet exists and is verified for every enrolled learner (Doc 04 §K bullet 2). The template list lives in `Referral List.md`; the per-learner packet is what you actually generate and confirm.

### Step 5 — Match partners

Matching happens before content opens (Doc 04 §A.1 routing feeds this; full method in `Async Partner Pairing Playbook.md` §1). Cadence first, time-zone within 6h, shared language, no close ties.

- [ ] Every learner matched (odd cohort: you bridge the leftover learner for week one only — Playbook §1, "Solo learners")
- [ ] Welcome email sent to each pair (Playbook §2), partner agreement (Doc 04 §B) attached, referral packet re-attached
- [ ] Both partners in each pair have replied "signed" to the 7-line partner agreement — **a learner who will not acknowledge item 4 (immediate-danger protocol) is not eligible** (Doc 04 §B)
- [ ] Each pair has chosen a §H-compliant platform and confirmed it to you
- [ ] Pairing tracker rows created for every pair (Doc 04 §C — metadata only, never content)

**Done-when:** every learner has a signed partner and a platform. Silent or unsigned pairings are not "almost ready" — they are not ready (Playbook §1).

### Step 6 — Pre-cohort checklist sign-off (the gate to open)

This is Doc 04 §K, verbatim in intent. You personally sign it. If any line is unchecked, the cohort does not open.

- [ ] Every enrolled learner passed intake and acknowledged consent (Step 3)
- [ ] Every learner has a region-specific referral packet on file (Step 4)
- [ ] Every learner is paired (Step 5)
- [ ] Both partners in each pair signed the partner agreement (Step 5)
- [ ] Pairing tracker is set up (Step 2 + Step 5)
- [ ] CM qualifications are met (Step 1)
- [ ] **Backup CM contact is identified and has accepted the role, with platform access and the crisis protocol in hand** (see Part 4 — this is the line new CMs most often leave half-done)
- [ ] Platform stack meets privacy minimums (Step 2)
- [ ] Cohort feed rules posted and pinned (Feed Templates §1 welcome post)
- [ ] Crisis escalation playbook (Doc 04 §F, §G) reviewed by you in the past 30 days (Step 1)

**Done-when:** all ten checked. Open content access. Not before (Doc 04 §K — "if any item is unchecked, the cohort does not open").

---

## Part 2 — Per-module CM cadence (Day 1 → Day 10)

The rhythm repeats every module. Doc 02 §A is the learner's week; this is *yours*.

### The standing weekly loop (every module)

1. **Post the module's feed prompt** at module start (Feed Templates §2 — one or two sentences, signal not story).
2. **Read every cohort-feed post within 48 hours.** No exceptions (Doc 03 §K). On High-module weeks, tighten to 24h for the mid-course check-in window (Feed Templates §6).
3. **Triage every post and DM** into green/yellow/red the moment you read it (Doc 04 §F). Log metadata only (Feed Templates §5).
4. **Check the pairing tracker** against its mechanical triggers (Doc 04 §C): missed SLA twice in one module → DM both; missed in two consecutive modules → offer re-match; one partner silent 6 days → offer the responsive partner a re-match. The triggers do the remembering for you; verbatim DM language is in Playbook §4.
5. **Answer routine DMs within 24h** (Doc 03 §G). Red flags are not routine — see Part 3.
6. **Hold the feed narrow.** Redirect drift (confessional, advice, theory debate) privately using the verbatim language in Feed Templates §4.

That is the whole per-module job in calm water. Most weeks are calm water. The triage rubric is what you reach for when a post is *not* obviously calm.

### Applying the triage rubric — what the three flags mean

Straight from Doc 04 §F. Hold these definitions exactly; the response window is the load-bearing part.

| Flag | Looks like | Window | Your action |
|---|---|---|---|
| **Green** | Normal reflection, "this is hard," frustration with a concept, ordinary doubt | None required | Acknowledgment optional |
| **Yellow** | Stuck feeling >24h · increased numbing reported · partner conflict surfacing · "over my head but functional" · a life stressor compounding the work | **DM within 24h** | Offer voice call, pause, slower cadence, or 1:1 referral; log it |
| **Red** | Suicidal ideation (any) · imminent harm to self/others · abuse in progress · psychotic/dissociative state in progress · medical emergency | **Same day, immediate** | Crisis-line numbers in the first message; hand off to clinician/emergency; do not "discuss" — refer (Part 3); log; debrief supervisor |

When uncertain between two flags, **classify up** (treat a maybe-yellow as yellow, a maybe-red as red) and let the conversation tell you. The course losing nothing to caution is fine; a missed red is not.

### Worked examples — ambiguous feed posts and how to classify + respond

These are the posts that don't sort themselves. Use them to calibrate your eye on the first cohort. Each shows the post, the call, the reasoning, and the move.

**Worked example A — "I've gone numb again" (Day 5).**

> *Post:* "Day 5. Honestly I came in wanting to feel more and this module I just went flat. Watched the whole thing from behind glass. Couldn't find a single feeling under the Numbness Bar. Kind of done with trying."

- **Call: Yellow.** Increased numbing reported + "kind of done" reads as deflation, not crisis. There is no harm indicator. But "went flat / behind glass" is the dissociation-adjacent language Doc 03 §D names, so it is past green.
- **Why not green:** "behind glass" and "watched from outside" are on Doc 03 §D's grounding-trigger list; numbness deepening across a High module is a yellow stuck-state signal, not ordinary doubt.
- **Why not red:** no suicidal ideation, no harm, no psychotic/dissociative state *in progress at the moment of writing* — they wrote a coherent reflection. If the next reply contained "and I don't see the point of any of it anymore," it crosses to red.
- **Move:** DM within 24h. "Saw your Day 5 post — going flat behind glass is exactly the Numbness Bar doing its job, not you failing the module. Before you decide you're done, two things: run the 60-second grounding script at the top of the file, and tell me — is the flatness only in the module, or has it been in your week too? Want a short voice call this week?" Offer pause/stretched cadence. Log Yellow. If "in my week too" comes back with lost time or not-functioning, re-triage toward defer-and-refer.

**Worked example B — the dark-but-completed past (Day 7).**

> *Post:* "Day 7. Caught my Persecutor clean for the first time. The move: I tear people down in meetings so I feel less small. Reminds me of a year a while back when I genuinely wanted to not be here anymore — glad that's behind me. Gremlin ate well off the meetings though."

- **Call: Yellow, with a same-day soft touch.** This is mostly a *good* Day 7 post — specific, self-located, gremlin-aware. But it contains a past suicidality disclosure ("wanted to not be here anymore"), explicitly framed as resolved ("glad that's behind me").
- **Why not red:** the ideation is reported in the past tense and self-framed as over. Red is for ideation that is *current or active* (Doc 04 §F). Treating every historical mention as red would punish honesty and teach learners not to disclose.
- **Why not plain green:** a suicidality mention — even past-tense — gets a private acknowledgment and a quiet check that "behind me" is actually behind them. You verify; you don't assume.
- **Move:** Acknowledge the Day 7 work *in the feed* if you'd normally acknowledge (keep it about the Persecutor catch — never surface the suicidality reference publicly). Then DM, same day, light: "Strong catch on the Persecutor today. You named something from a harder time too — I'm not making it a big thing, just checking: is that genuinely in the rear-view, and do you have someone in your life you'd reach for if it ever came back?" If the answer wobbles ("mostly… some days…"), you're now in yellow-trending-red: send the referral packet's clinician section and ask the Doc 03 §H pause question. Log it with the historical-disclosure note.

**Worked example C — the experiment that's about to cost something real (Day 1 / Day 2).**

> *Post:* "Radical responsibility landed hard. I've decided I'm done being a victim about my marriage — going to confront my husband this weekend and tell him everything that's wrong, no filter. Box has been running this for 15 years and I'm DONE."

- **Call: Yellow → check the intake flag immediately.** The post itself is energized, not in crisis. The risk is the *experiment*: a no-filter confrontation inspired by Day 1's responsibility content is exactly the move Doc 04 §A (Screen 4) and §72-style coercion logic exist to catch.
- **First action before responding:** check this learner's record for a Screen 4 (coercive/unsafe environment) flag. If Screen 4 returned **yes**, this is closer to red-adjacent — a course-inspired experiment is heading toward the exact risk the screen was meant to prevent, and you intervene firmly. If Screen 4 was clean, it's a yellow coaching-the-container moment.
- **Why not green:** Day 1 is explicitly the module that can send a fired-up learner into a real-life action that costs them (Doc 04 §A, Screen 4 note — "a learner inspired by Day 1's radical-responsibility content can run an experiment that costs them their housing"). The feed naming an imminent high-stakes confrontation is a structural yellow regardless of charge.
- **Move:** DM within 24h (same day if Screen 4 = yes). "Big landing — and I want to slow one thing down. Radical responsibility is a stance about *your* creating, not a green light for a no-filter confrontation. The course's experiments are deliberately small reps, not life-altering moves (that's by design). Before this weekend, let's talk: what's the smallest true version of what you want to say? If there's any way this conversation could put your safety, housing, or finances at risk, we substitute a low-stakes experiment — that's not me doubting you, it's the course refusing to create risk in your actual life." Point to the between-module experiment's small-rep framing. If Screen 4 = yes, also re-send the DV/legal resources from their packet. Log Yellow (or Red if Screen 4 = yes and risk is concrete).

The pattern across all three: **the flag is set by risk and state, not by emotional intensity.** A hot post about catching the Box is green-to-yellow; a calm post naming an imminent real-world risk is yellow-to-red. Intensity is the work (Doc 03 §M); risk is what you triage.

---

## Part 3 — When a Red flag arrives (the immediate path)

Red is not a 24-hour item. It is **immediate on detection, first response within 15 minutes** of you (or your named backup) seeing it, with crisis-line numbers in that first message (Doc 03 §G, Doc 04 §F). Run Doc 04 §G's sequence exactly:

1. **Acknowledge within 15 minutes.** "I see you. I'm here. Are you safe right now?"
2. **If immediate physical danger:** crisis-line number for their country in the message; ask "Will you call them now, or do you want me to stay on while you call?"; stay in the thread until they've connected with crisis services **or** 90 minutes pass and you contact your designated backup clinician.
3. **If red-flagged but not in immediate danger:** connect them to a PM-aware coach (if they have one), their existing clinician (with consent), or the licensed-clinician list from their packet; follow up within 24h to confirm the connection happened.
4. **Pause their cohort access** until they and their clinician agree it's appropriate to resume. Frame as care, not punishment.
5. **Document** (date, action, learner consent for any disclosure) and **debrief your supervisor within 72 hours.**

You do not provide clinical care at any step. Stay present, hand off, document (Doc 04 §G). The referral language template in Doc 03 §H is the words to use. If a partner is the one who surfaces the red flag, they follow the buddy immediate-danger protocol (Doc 03 §F) and relay to you — they are the relay, not the clinician (Playbook §9, scenario 5).

---

## Part 4 — High-module weeks (Days 5, 6, 7, 9): extra vigilance

High modules directly engage the emotional body, drama patterns, the gremlin, and ego states (Doc 03 §C). They are where material the learner hasn't seen before surfaces. Run this extra checklist *around* each High module, on top of the standing weekly loop.

### Before the module unlocks (per learner)

Verify the unlock checklist (Doc 04 §D) is satisfied — gate it programmatically where the platform can, manually where it can't:

- [ ] Partner agreement signed by both
- [ ] Partner was responsive on the prior module (no missed SLA)
- [ ] Learner confirmed: "My partner is reachable today and tomorrow" — and this is the *result of an actual exchange* 24–48h ahead (Playbook §7 script), not an assertion in their head
- [ ] Learner confirmed: "I have 90 uninterrupted minutes ahead of me"
- [ ] Learner confirmed: "I am not in acute crisis or under the influence right now"
- [ ] Learner has read this module's consent prompt (Doc 03 §I)
- [ ] **If Screen 1 (suicidality) or Screen 5 (mania) applied at enrollment: clinician confirmation is on file for *this* module** (Doc 04 §D — per-module, not once)
- [ ] Partners are not cadence-mismatched (Doc 04 §I — High modules do not unlock when partners are >1 module apart; either the faster waits, a witness partner is assigned per Playbook §6, or re-match)

**The skip-after-24h override is gone** (Doc 03 §C, Doc 04 §D). If a learner can't meet the gate, they wait. The course will still be there.

### During the High-module window

- [ ] Read the feed at **24h, not 48h**, for the duration of the window (the cohort is at higher charge)
- [ ] Send the lightweight High-week check-in DM to every learner ("how's it landing? anything to flag?") — no reply required (Doc 02 §F, "High-intensity weeks")
- [ ] Between Day 5 and Day 6 specifically, post the mid-course "what's alive" pause prompt (Feed Templates §6); read replies within 24h; any "too fast" triggers a cadence DM, any partner-related answer triggers a tracker check
- [ ] Watch for the Day-specific surfaces:
  - **Day 5 (Feelings vs Emotions / Numbness Bar):** numbness deepening, "behind glass," a learner naming emotions (story-attached, past) where the module asks for feelings (present, located) — the partner gently re-scopes and points to you (Playbook §3, Day 5 example)
  - **Day 6 (Mixed Emotions / Emotional Healing Process):** the most demanding module; async partner-reply latency can stretch its calendar time (Doc 02 §A) — make sure no learner is mid-process and waiting days for a witness
  - **Day 7 (Low Drama / Gremlin Food):** historical disclosures surfacing as learners catch Persecutor/Victim/Rescuer moves (Worked example B); drama patterns can route present feeling through old material
  - **Day 9 (Ego States):** archetypal and ego-state material can amplify mania/psychosis/dissociation (Doc 04 §A, Screen 5; Doc 01 §"Box layers") — this is the module the clinician-confirmation gate most protects

### After the module

- [ ] Confirm the required partner debrief happened (tracker shows the exchange — content stays private) (Doc 03 §C)
- [ ] Any learner who went quiet across a High module gets a direct check-in DM, not a wait-and-see

---

## Part 5 — Backup-CM handoff (how the 15-minute crisis SLA survives you being unreachable)

You will sleep, travel, lose signal, and have hours off. The red-flag SLA does not pause for any of that (Doc 03 §G — "the CM ensures a named backup with accepted role + platform access + crisis protocol covers any window when the CM is unreachable"). This is the procedure new CMs most often under-build. Build it before launch (it is a line on the §K gate).

### Who the backup is

- A specific named person who has **accepted the role** — not "someone I'll call." Ideally a fellow qualified CM, a PM-aware coach, or your clinical supervisor acting in a coverage capacity. The backup must themselves meet enough of the Doc 04 §J floor to hold a red flag: mental-health first aid, the ability to refer without flinching, and access to the crisis protocol.
- The backup is named on your enrollment paperwork and the platform privacy setup (Doc 04 §H lists the 1:1 channel; the backup needs read access to it for coverage windows).

### What the backup has, before they're ever needed

- [ ] **Accepted the role in writing** (a coverage clause in the CM–Operator agreement, or a short separate note)
- [ ] **Platform access** to the 1:1 CM channel and the cohort feed (so they can see and respond)
- [ ] **The crisis escalation flow** (Doc 04 §G) and **triage rubric** (Doc 04 §F) in hand
- [ ] **The current pairing tracker + triage log location** (read access) so they know the cohort's state
- [ ] **The referral packets** for the cohort's regions (so they can drop a region-correct crisis line into a first message)
- [ ] **Your supervisor's contact** as the 90-minute escalation point (Doc 04 §G step 2)

### How coverage is triggered

1. **Planned absence** (sleep window, travel, a known offline block): you tell the backup the window in advance and post nothing learner-facing — coverage is silent. If you run a cohort across incompatible time zones, name the nightly window the backup owns.
2. **Unplanned unreachability:** define the trip-wire in advance. The standard is — if a learner's red-flag message sits unacknowledged for **10 minutes**, the platform/learner routing (or the backup's own feed-watch) escalates to the backup, who then owns the 15-minute first-response SLA. The 5-minute buffer between the 10-minute trip-wire and the 15-minute SLA is deliberate.
3. **The backup runs Doc 04 §G exactly as you would** — acknowledge ≤15 min, crisis line in the first message, stay present, hand off, document. They log it in the shared triage log so the record is continuous.
4. **Hand-back:** when you're reachable again, the backup briefs you on anything that moved; you debrief your supervisor within 72h on any red flag the backup handled (Doc 04 §G step 5 — the debrief is yours even if the backup ran the call).

### Test it once, before Day 1

Send the backup a drill message ("this is a test — walk me through your first three actions if a red flag arrives in your window"). If they can't name *acknowledge ≤15 min → region crisis line in first message → stay until connected or 90-min supervisor escalation*, they are not ready, and your §K gate is not actually met.

> The single most common first-cohort failure mode is treating the backup as a formality — a name on a form with no access and no drill. A backup without platform access cannot meet a 15-minute SLA. Build the access and run the drill, or you do not have a backup.

---

## Part 6 — Cohort close and post-cohort review

### Closing the cohort (Day 10 → close)

- [ ] Day 10 closure exchange happens between partners (Playbook §8 — explicit closure, not fade)
- [ ] Opt-in continuation message sent to each partner separately (Playbook §8) — item 7 ends with the cohort; flag it
- [ ] Feed gratitude prompts posted (Feed Templates §7): partner-to-partner, then partner-to-cohort; announce the feed's read-only archive date
- [ ] Learners reminded how to access materials post-cohort (Doc 02 §F, "Closure")
- [ ] Any learner whose access was paused mid-cohort (red flag) is closed out per their own clinician timeline, not the cohort calendar

### The post-cohort review (1–2 weeks after Day 10)

This is Doc 04 §L — a private review you conduct, then share with the operator and your supervisor. Pull from the triage log (Feed Templates §5) and pairing tracker (Doc 04 §C), both anonymized.

- [ ] **Flag distribution:** how many green / yellow / red, by module. Where did the charge cluster?
- [ ] **Content patterns:** where did multiple learners get stuck, ungrounded, or overwhelmed? (A pattern on one module = revise that module before the next cohort — Doc 03 §L step 5)
- [ ] **Pairing outcomes:** which matches worked, which needed re-matching, any pattern (cadence mismatch? time-zone? a recurring drift point?)
- [ ] **Learning-axis signal:** fold in the anonymized aggregate from `Learning Self-Assessment.md` — the baseline→Day-10 deltas and the per-HIGH-module readiness self-checks. Where learners report a distinction "not yet landed" at Day 10, or repeatedly flag a readiness gap before a High module, that is a content signal, not a learner failure. (See that file's closing note on how the aggregate feeds this review.)
- [ ] **One concrete improvement** proposed for the next cohort. One. Specific. Implementable.

Share with the operator and supervisor. Patterns recur across cohorts; the review is how the course improves (Doc 04 §L). It is also where your first cohort stops being a one-off and becomes the first data point in a system that compounds.

---

## First-cohort reminders (pin these)

- **The gate is the gate.** Intake screening, partner signing, the §K checklist, the High-module unlock — none of these is a suggestion you can soften when a keen applicant pushes. The protocol is required (Doc 04 status note).
- **Classify up when unsure.** Maybe-yellow → yellow. Maybe-red → red. Caution costs minutes; a missed red costs more.
- **Refer without flinching** (Doc 03 §K). Wanting to "help first" before referring is how a CM contributes to harm.
- **You are not the teacher and not a therapist** (Doc 02 §F, Doc 03 §M). You keep the container intact. The modules teach; clinicians treat; you triage, hand off, and document.
- **Metadata only, always.** The tracker and the log record *that* something happened and *what you did* — never what was said (Doc 04 §C, Feed Templates §5). Confidentiality holds except the three exceptions (Doc 03 §K).
- **The backup is real or you have no backup.** Access + drill, before Day 1.

---

<sub>🄯 **World Copyleft 2026** · *Expand the Box (Digital)* · licensed **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)** · re-presents Possibility Management thoughtware originated by Clinton Callahan & the Possibility Management community · please share, share-alike · Powered by Possibility Management ([possibilitymanagement.org](https://possibilitymanagement.org)) · full terms: `LICENSE.md` in the course root</sub>
