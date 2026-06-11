# 04 — Container and Gatekeeping Protocol

This is the operating protocol that turns the safety intentions in `03 - Safety and Facilitation Framework.md` and the structural intentions in `02 - Async Delivery Framework.md` into concrete mechanisms.

**Audience.** The Community Manager (CM). Every action in this document is something the CM (or the platform standing in for them) does. Learners see only the outputs: the intake form, the referral packet, the welcome message.

**Status.** This protocol is **required**. A cohort run without it is not running with the safety framework. It is running with the safety framework's intentions. This document is the law; [05 - Operator Run-Book.md](05%20-%20Operator%20Run-Book.md) and the [CM First-Cohort Run-Book](Facilitator%20Resources/CM%20First-Cohort%20Run-Book.md) are the routes through it.

Section letters A–L match v1. v2 additions: the intake lines in §A.1, §B.2 (witness recruitment), the §D re-screen line, §K.2 (the cohort cap), and §M (solo boundary).

---

## A. Intake screening (before access opens)

Every prospective learner completes the intake **before** content access is granted. This is the gate, not a suggestion. **The deployable form is [`Facilitator Resources/Intake Form.md`](Facilitator%20Resources/Intake%20Form.md)** — operators deploy that artifact rather than re-assembling the screens from this prose; this section remains the binding spec the form implements. The intake takes ~12 minutes and has three parts: identity & cadence, screening questions, and acknowledgments.

The prospective learner has already met the plain-language self-screen (Doc 03 §A) on the enrollment page; the intake form repeats it in one line: *"This course asks real things of your attention and your feelings. If you are in crisis, newly bereaved, or mid-rupture, the right move is usually 'later, with support', and the form below checks this with you properly."*

### A.1 Identity, cadence and referral routing

Required fields (used to generate the per-learner referral packet; see Section E):

- Name and preferred name
- **Confirmation of age 18 or over** *(the course is built and screened for adults; under 18 → no enrollment, no exceptions, with an honest sentence about why)*
- Email (for cohort comms)
- Country and state/province (for region-appropriate crisis line; France: 3114)
- Time zone and weekly availability windows (for partner matching)
- Primary language for partner exchange
- Are you currently working with a therapist, coach, or psychiatrist? *(Y/N; not the name, just the existence)*
- Do you have someone (a friend, family member, or professional) you would call if you were in distress? *(Y/N; short text optional)*
- **In the last 60 days, has someone close to you died, or has a major part of your life come apart (separation, job loss, eviction, serious diagnosis)?** *(Y/N. Y → 1:1 CM consult before access; stretched cadence is the default offer. Routing, not denial; spec in Doc 03 §A.)*

### A.2 The five screens (gate questions)

Each screen has a specific question, a threshold, and an action. The CM (or the platform's intake logic) applies the threshold and routes accordingly. **The learner is told that "no" or "I'd rather not say" routes them to a 1:1 CM conversation, not to automatic denial.**

#### Screen 1 — Suicidality

**Question.** In the past 30 days, have any of the following been true for you?
- You wished you were dead, or wished you could go to sleep and not wake up
- You had thoughts about killing yourself
- You made a plan
- You intended to act on it

**Thresholds and actions.**
- Any current plan, intent, attempt, or active suicidal ideation → **No course access at this time.** CM sends crisis-line numbers and the licensed-clinician portion of the referral list, and offers a re-application path: "the course will be available to you when a clinician confirms you are stable enough for thoughtware work."
- Passive ideation (wishing you weren't here, no plan) → **CM 1:1 consult required before access.** Requires confirmation that the learner has clinician or coach support. High modules (5, 6, 7, 9) require explicit confirmation from that support person before the learner unlocks them.
- None of the above → continue.

#### Screen 2 — Trauma & dissociation

**Question.** In the past 6 months, have you experienced any of the following: flashbacks, lost time, feeling outside your body, inability to function after emotional work, intrusive memories that disrupted your day?

**Thresholds and actions.**
- Monthly or more frequent, OR any lost time, OR any hospitalization for these → **Defer enrollment unless a trauma-qualified clinician (TF-CBT, EMDR, somatic, or equivalent) confirms participation in writing.** Course runs on stretched cadence (Doc 02 §K). High modules require the same explicit confirmation from the clinician.
- Less frequent, no lost time, currently in care → CM 1:1 consult; proceed with stretched cadence recommended.
- None of the above → continue.

This gate protects the learner from using PM distinctions to bypass trauma care. PM is *precise* that emotional healing process work (in scope) is distinct from trauma processing (out of scope). A learner with unresolved trauma who treats this course as a substitute for trauma care will get hurt.

#### Screen 3 — Active addiction / compulsive behavior

**Question.** In the past 90 days, have any of the following felt out of your control to a degree that is affecting your life: alcohol, drugs (including cannabis), self-harm, restricting/bingeing food, gambling, sexual behavior, screens/scrolling?

**Thresholds and actions.**
- Currently uncontrolled, OR less than 90 days sobriety from severe addiction → **Defer or require active professional support (12-step sponsor + meeting attendance, or treating clinician).** No High modules without an explicit support plan in writing.
- Compulsive but not "out of control," currently in active recovery support → continue with CM 1:1 consult.
- None of the above → continue.

#### Screen 4 — Coercive or unsafe environment

**Question.** Is there anyone in your household, intimate relationship, workplace, visa status, custody arrangement, or financial life where speaking directly, setting a boundary, or shifting how you behave could put your safety, housing, children, or income at risk?

**Thresholds and actions.**
- Yes, any of the above → **Course access proceeds, but no direct-confrontation experiments with that person.** CM provides domestic-violence and legal resources (region-appropriate) at enrollment. Between-module experiments are substituted with low-stakes variants (e.g., the "single-word context shift" experiment instead of the "dangerous conversation" experiment). The learner is told this is not because they cannot handle the work but because the course refuses to create risk in their actual life.
- No → continue.

This screen is one of the most important and the most often missed in thoughtware courses. A learner inspired by Day 1's "radical responsibility" content can run an experiment that costs them their housing if the course has not asked them this question.

*v2 implementation note: the substitutions are no longer improvised. Every experiment in the [Experiment Bank](Facilitator%20Resources/Experiment%20Bank.md) has a lower-stakes variant column, and Modules 1, 7, 8 and 10 carry the discreet learner-facing cue. Spec: Doc 03 §Q.*

#### Screen 5 — Mania, psychosis, spiritual emergency

**Question.** In the past 12 months, have you experienced any of the following: manic episodes, psychosis, hearing or seeing things others did not, severe paranoia, psychiatric hospitalization, major changes to psychiatric medication?

**Thresholds and actions.**
- Yes, any of the above → **Defer access unless the prescribing clinician confirms participation in writing.** Archetypal and ego-state material (especially Module 9) can amplify these states. The course is not equipped to hold this.
- Recovered, no episodes in the past 12 months, stable on medication, in care → CM 1:1 consult; proceed.
- None of the above → continue.

### A.3 Acknowledgments

Learner clicks/initials each:

- I understand this course is not therapy, coaching, or psychiatric care.
- I have received the referral packet for my region.
- I agree to the four working agreements (Doc 03 §B).
- I will pair with a partner before Module 1.
- I will use the grounding script and pause practices as instructed.
- I will contact the CM if anything in my life changes that makes the course inappropriate for me.
- I have read the Enrollment Terms, including the refund tree ([Facilitator Resources/Enrollment Terms and Learner Agreement.md](Facilitator%20Resources/Enrollment%20Terms%20and%20Learner%20Agreement.md)).

Access opens after the screens are passed and acknowledgments are completed. Not before.

---

## B. The witness layer

### B.1 The partner agreement

When the CM matches two learners, both receive and acknowledge the **partner agreement** before exchanges begin. It is 7 lines:

> 1. I will respond to my partner's voice message within 24 hours, even if briefly.
> 2. I will not advise, fix, or diagnose. I will witness.
> 3. I will hold what my partner shares in confidence.
> 4. **If my partner tells me they may harm themselves or someone else, I will ask: "Are you in immediate danger right now?" If yes, I will contact local emergency or crisis services AND the CM immediately. I will not wait for course protocol.**
> 5. If I become unable to be in the partnership, I will tell the CM within 48 hours so a re-match happens.
> 6. I will not use what my partner shares in any other context.
> 7. I will not enter a sexual, financial, or professional relationship with my partner during the course.

A learner who will not acknowledge item 4 is not eligible for partner pairing and therefore not eligible for the course.

### B.2 WITNESS-RECRUITMENT PROTOCOL (v2: the recruit-a-witness path, formalized)

A reader without a cohort can satisfy the High-module witness gate by recruiting their own witness. **A friend qualifies.** This is a sanctioned path, not a loophole; the protocol below is what makes it real.

**The instrument is the same 7-line agreement** (B.1), adapted: "partner" reads "the person I am witnessing," item 1's 24-hour SLA applies during agreed practice windows rather than continuously, and item 5's re-match line becomes "I will say so plainly before the next High module, so the work pauses rather than running unwitnessed." Item 4 is unchanged and remains the eligibility line: **no acknowledged item 4, no witness role.**

**Scope.** The recruited witness holds the High-module witness role: reachable before/during/after Modules 5, 6, 7 and 9, present (live or in the message thread) for the witnessed practices, and the recipient of the post-module debrief. They are not obliged to take the course, do the exchanges of Modules 1–4 and 8–11, or hold anything course-long.

**What the witness reads before the first High module** (under an hour, total):

1. **The witness annex**: Doc 03 §F (when the learner calls, what witnessing is and is not, the immediate-danger protocol).
2. **The Module 6 witness script**, including the witness-overflow script, verbatim, for material that exceeds scope.
3. **The Partner Emergency Card** (Facilitator Resources safety pack): the one-page "if the person you are witnessing is in trouble" card, kept where they can reach it in thirty seconds.

**Who is disqualified from the witness role:**

- Anyone under 18.
- Anyone the learner flagged (or would flag) under Screen 4 (the person whose presence in the learner's life carries the safety/housing/income risk), and anyone whose own relationship to the learner is the live subject of the work.
- Anyone currently in acute crisis themselves, or who cannot honestly take on item 4.
- Anyone in a dependency or authority entanglement with the learner that the witness role would strain (therapist-of, employee-of, minor child of; the role needs a peer, not a hierarchy).

Spouses and close friends, explicitly **allowed** here (unlike cohort pairing): the recruited witness is scoped to witnessing, not to a course-long mutual exchange, and the learner with no cohort has no matching pool. The narrowed scope is the safeguard.

**Inside a cohort,** witness recruitment also covers the witness-bench: alumni or recruited witnesses the CM keeps on hand for cadence mismatches and re-matches (onboarding note in the Facilitator Resources ops pack; sequencing in Doc 05 Step 2).

---

## C. Pairing tracker (CM-side, no content logged)

The CM maintains a simple per-module tracker. **It logs only that exchanges happened, never what was said.** Fields per module per pair:

| Field | Example |
|---|---|
| Pair ID | P-07 |
| Module | 5 |
| A sent message? | Yes — 2026-02-12 |
| B replied? | Yes — 2026-02-13 |
| Within SLA (24h)? | Yes |
| Missed SLA? | — |
| CM action | None |

Tracker lives in a private spreadsheet (Notion, Airtable, Excel) accessible only to the CM and their supervisor.

**Trigger rules.**
- Missed SLA twice in one module → CM DMs both partners with the standard "I noticed the cadence dropped. Is the pairing still working?" message.
- Missed SLA in two consecutive modules → CM offers a re-match.
- One partner has not initiated any exchange in 6 days → CM offers the silent partner a re-match.

These triggers are mechanical so the CM does not have to remember to act.

---

## D. High-module unlock checklist

A learner cannot start Modules 5, 6, 7, or 9 (High intensity) until all of the following are confirmed:

- [ ] Partner agreement signed by both partners (or witness agreement signed, §B.2)
- [ ] Partner/witness has been responsive (no missed SLA on the prior module)
- [ ] Learner has confirmed: "My partner is reachable today and tomorrow"
- [ ] Learner has confirmed: "I have 90 uninterrupted minutes ahead of me"
- [ ] Learner has confirmed: "I am not in acute crisis or under the influence right now"
- [ ] Learner has read the consent prompt (Doc 03 §I) for this module
- [ ] If Screen 1 (suicidality) or Screen 5 (mania) applied at enrollment: clinician confirmation on file for this module
- [ ] **At the Module 5 unlock only, the mid-course re-screen checkbox (v2):** the learner confirms *"Nothing has changed since my intake that would change my screening answers — no new loss, rupture, substance pattern, or safety risk. If something has changed, I have messaged the CM instead of ticking this box."* A message instead of a tick is routing, not denial: usually a short consult, sometimes a cadence change, rarely a pause.

The reference platform is a static shell with no server logic, so this gate is **procedural**: the CM verifies the checklist per learner and releases the module link (sequenced in the run-books). Where an operator's platform can gate programmatically, it should. **Skip-after-24-hours-override is removed** — the prior framework's allowance for an informed override is retracted. If a learner cannot meet the gate, they wait. The course will still be there.

---

## E. The referral packet (per-learner)

Generated at enrollment from the learner's Section A.1 inputs. It contains:

1. **One crisis line for the learner's country** (with phone, text, web, whichever is region-appropriate). Listed *first*, not buried. France: **3114** (national, 24/7).
2. **A short list of licensed mental health professionals** in the learner's region: minimally a directory link (Psychology Today, Therapy Den, region equivalent) and one or two PM-friendly clinicians where known. If the learner indicated they already have a clinician, this section is brief.
3. **PM-aware coaches** in the learner's language, with rates and availability.
4. **Local domestic violence and legal resources** *if* Screen 4 returned yes.
5. **The not-therapy disclaimer**: one short paragraph.

The packet is generated as a PDF the learner downloads and is also kept on the platform for future access. The CM verifies the packet exists for the learner before access opens.

---

## F. CM triage rubric (cohort feed + DMs)

Every cohort-feed post and every learner DM is classified by the CM into one of three flags, with a defined response window. The CM does this in their head as they read; classifications go in the action log. Worked ambiguous-post examples for calibration live in the [CM First-Cohort Run-Book](Facilitator%20Resources/CM%20First-Cohort%20Run-Book.md) Part 2.

| Flag | What it looks like | Response window | CM action |
|---|---|---|---|
| **Green** | Normal reflection, processing, "this is hard," frustration with a concept, ordinary doubts | No action required | Acknowledgment optional |
| **Yellow** | Stuck feeling for >24 hrs · increased numbing reported · partner-conflict surfacing · learner expressing they are over their head but functional · life stressor compounding the work | **CM DM within 24 hours.** "I noticed X — how are you doing? Want a quick voice call this week?" Offer pause, slower cadence, or 1:1 referral. | Document in action log |
| **Red** | Suicidal ideation (any) · imminent harm to self or others · disclosure of abuse in progress · psychotic break or dissociative state in progress · medical emergency | **Same day, immediate.** Crisis-line numbers within the first message. Direct hand-off to clinician or emergency services. The CM does not "discuss" red flags — they refer. | Document; debrief with supervisor; review module |

The 24-hour SLA in Doc 03 §G is for green and yellow flags. **Red is immediate**: not within 24 hours, not next business day, not "as soon as the CM is available." The CM ensures a backup contact exists for any window when they themselves may be unreachable.

---

## G. Crisis escalation flow

A specific sequence when a Red flag arrives.

```
1. CM acknowledges receipt within 15 minutes of seeing the message.
   "I see you. I'm here. Are you safe right now?"

2. If learner is in immediate physical danger:
   → CM gives crisis-line number for learner's country in the message.
   → CM asks: "Will you call them now, or do you want me to stay on with you while you call?"
   → CM stays in the conversation until learner confirms they have connected with crisis services
     OR until 90 minutes have passed and CM contacts a designated backup
     (a licensed clinician on the CM's emergency contact list, agreed in advance).

3. If learner is not in immediate physical danger but red-flagged:
   → CM connects learner with one of: PM-aware coach (if learner has one),
     learner's existing clinician (if they consent), or the licensed-clinician
     list from their referral packet.
   → CM follows up within 24 hours to confirm connection happened.

4. Course access:
   → CM pauses learner's cohort access until the learner and their clinician
     agree it is appropriate to resume.
   → Pause is framed as care, not punishment. A safety-routed exit refunds in
     full (Doc 05 Step 0).

5. Documentation:
   → CM logs the exchange (date, summary of action, learner consent
     for any disclosure made).
   → CM debriefs with their supervisor within 72 hours.
```

The CM does not provide clinical care at any step. The CM's job is to stay present, hand off, and document.

---

## H. Platform privacy minimums

The course operator selects a platform stack (reference stack: Doc 02 §F). Every component must meet these minimums **before** the cohort opens:

| Component | Minimum |
|---|---|
| Voice-message tool | Private 1:1 thread; no automatic AI transcription; no public forwarding; user can delete messages; end-to-end encryption preferred (Signal is the reference pick) |
| Document hosting | Access-controlled or fully open by design (the v2 static shell is public content; learner *data* never touches it: all records are browser-local) |
| Cohort feed | Closed to the cohort; not visible externally; posts deletable by author; CM can hide posts |
| 1:1 CM channel | Private; CM logs metadata only; content of messages not shared with anyone unless one of the confidentiality exceptions applies (Doc 03 §K) |
| Interactive tools | One origin; localStorage only; no analytics, no CDN calls, fonts self-hosted; **consent never persisted** (Doc 03 §I) |
| Live integration calls (if held) | Recording requires explicit consent from every participant **per call**. Personal check-ins, demos, and shares are **never recorded.** Recording is permitted only for teaching segments and Q&A, and only if all participants have agreed in that call. |

If any component cannot meet the minimum, the operator either replaces the component or runs the cohort smaller and tighter (e.g., cohort feed becomes a shared doc the CM moderates manually).

---

## I. Cadence + partner-cadence mismatch protocol

Doc 02 §K lists cadence variants. The protocol fills in what happens when paired partners get out of sync.

- Each learner declares their cadence at enrollment (Default / Compressed / Stretched / Pulsed).
- Partners are matched on compatible cadence.
- If partners drift more than **one module apart** for **4+ consecutive days**, the CM intervenes:
  - First: ask both whether the mismatch is workable for them (sometimes it is).
  - If not: offer a **witness partner** (a third learner, a witness-bench member, or the CM themselves for a single exchange) so the slower learner is not left without a witness before their next High module.
  - If chronic: re-match the faster learner to a new partner. The slower learner keeps the existing partner once they catch up, or is re-matched also.
- **High modules do not unlock when partners are mismatched.** Either the faster learner waits, or a witness partner is assigned, or the faster learner re-matches. No exceptions.

---

## J. CM qualifications (the real bar)

Doc 02 §I points here. Given the responsibilities in this document, the CM must:

- Have personally completed an Expand the Box training (this course or equivalent live ETB) **and** at least one further PM training
- Hold current basic first aid / mental health first aid training (or equivalent country-recognized program)
- Have a named clinical supervisor or licensed mental-health professional they consult for case-by-case judgment (paid, not a friend)
- Have a written CM agreement with the course operator covering scope, liability, and the confidentiality exceptions (templates: [CM Agreement Templates](Facilitator%20Resources/CM%20Agreement%20Templates.md))
- Carry appropriate professional liability insurance for educator/coach roles in their jurisdiction (or be employed by an entity that does)

The CM is not a PM trainer. The CM is also not a casual community moderator. The role sits between, and the qualifications must match the responsibilities. A cohort run by an underqualified CM is a cohort running without a safety framework, regardless of how strong the documents look.

---

## K. The launch gate

### K.1 Pre-cohort checklist

The CM signs off on this checklist before content access opens for any cohort.

- [ ] Every enrolled learner has passed intake screening (Section A, including the 18+ line and the bereavement question) and acknowledged consent
- [ ] **Cohort size is within the binding cap (§K.2): 8–12 for a first cohort**
- [ ] Every learner has a region-specific referral packet on file (Section E)
- [ ] Every learner has been paired with a partner
- [ ] Both partners in each pair have signed the partner agreement (Section B)
- [ ] Pairing tracker is set up (Section C)
- [ ] CM qualifications are met (Section J)
- [ ] Backup CM contact is identified, has accepted the role, has platform access, and has been drilled
- [ ] Platform stack meets privacy minimums (Section H), including the tools' no-persistence consent check
- [ ] Cohort feed rules are posted and pinned
- [ ] Enrollment terms and refund tree are published and acknowledged (Doc 05 Step 0)
- [ ] Incident response and crisis escalation playbook (Sections F, G) is reviewed by CM in the past 30 days

If any item is unchecked, the cohort does not open.

### K.2 The first-cohort cap (binding)

**A first cohort is 8–12 learners. This is a cap, not a target band to negotiate.** The rationale is arithmetic, not caution: one CM carries the triage SLA (every post read ≤48h, ≤24h in High windows; red = 15 minutes), the pairing tracker, the High-week check-in DMs, and the unlock verifications. Above ~12 learners those duties exceed what one qualified person can hold during the Modules 5–9 climb, and CM overload is the likeliest safety failure in the whole design. Below 8, a single dropout can strand a partner with no re-match pool.

Subsequent cohorts may move within 8–16 **only** after a completed post-cohort review (§L) shows the CM's actual hours stayed within the sizing bands in Doc 05 Step 2, and never above 16 per CM. Two CMs do not double the cap; they run two cohorts.

---

## L. Post-cohort review

After the cohort closes, the CM conducts a private review (1–2 weeks after the Module 11 close):

- Anonymized read-through of the action log: how many green / yellow / red flags, distributed by module
- Identified content patterns: where did multiple learners get stuck, ungrounded, or overwhelmed?
- Partner pairing outcomes: matches that worked, matches that needed re-matching, any patterns
- Completion-by-module and the anonymized self-assessment aggregate (operator pull list and collection flow: Doc 05 Step 4)
- CM actual hours per phase, against the Doc 05 sizing table (this is what future cap decisions stand on; §K.2)
- One concrete improvement proposed for the next cohort

The review is shared with the course operator and the CM's supervisor. Patterns recur across cohorts; the review is how the course improves.

---

## M. Solo readers: the boundary

Solo mode is sanctioned (Doc 02 §G; Doc 03 §P) and this protocol does not govern solo readers: there is no CM, no intake, no SLA to enforce. What this document contributes is the boundary: **the High-module witness gate applies to everyone.** A solo reader satisfies it through §B.2 (recruit-a-witness) or honors the defer-list. There is no third path, and no course artifact may describe one. The defer-list is a boundary, not a workaround to be engineered around; the course states this before the climb, not after.

---

<sub>🄯 **World Copyleft 2026** · *Expand the Box (Digital)* · licensed **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**, consistent with the spirit of World Copyleft · re-presents Possibility Management thoughtware originated by Clinton Callahan & the Possibility Management community · this course is an independent re-presentation, **not an official Possibility Management training** · please share, share-alike · Powered by Possibility Management ([possibilitymanagement.org](https://possibilitymanagement.org)) · full terms: `LICENSE.md` in the course root</sub>
