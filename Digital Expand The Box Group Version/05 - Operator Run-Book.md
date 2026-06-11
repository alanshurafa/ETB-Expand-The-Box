# 05 — Operator Run-Book

| | |
|---|---|
| **For** | The course operator: the person (or tiny org) who decides to launch a cohort, prices it, stands up the platform, hires the CM, and owns the business layer |
| **When** | Open before anything is announced; work it Step 0 → Step 5 through the first cohort's close |
| **Hierarchy** | **Doc 04 is the law, this is the route.** Where this run-book and [04 - Container and Gatekeeping Protocol.md](04%20-%20Container%20and%20Gatekeeping%20Protocol.md) could ever disagree, Doc 04 wins |
| **Reads alongside** | [02 - Async Delivery Framework.md](02%20-%20Async%20Delivery%20Framework.md) (delivery + reference stack) · [03 - Safety and Facilitation Framework.md](03%20-%20Safety%20and%20Facilitation%20Framework.md) · [CM First-Cohort Run-Book](Facilitator%20Resources/CM%20First-Cohort%20Run-Book.md) (the CM's own sequenced route; this file is the operator's) |

The CM Run-Book sequences the container work; this file sequences everything around it: commerce, platform, staffing, enrollment, the running rhythm, and what happens after Module 11. Each step closes on a *done-when*. Nothing downstream opens until the step above it is closed.

---

## The shape of the launch (one screen)

```
STEP 0  COMMERCE      pricing posture · enrollment terms · refund tree published
STEP 1  PLATFORM      one-origin static shell + private feed · privacy verified
STEP 2  STAFFING      operator/CM delineation · CM contracted within sizing table
                      · backup drilled · witness bench seeded
STEP 3  ENROLLMENT    intake deployed · screening window · pairing · calendar out
        ─────────  Doc 04 §K gate: every box, or no open  ─────────
STEP 4  RUN           weekly operator rhythm · CM holds the container ·
                      Module 5 re-screen · the climb · §L review at close
STEP 5  CONTINUATION  alumni 30/60/90 · Possibility Team conversion ·
                      leavers closed out well · next-cohort decision
```

---

## STEP 0 — Commerce (open content, paid container)

Per ARCHITECTURE decision 8. Get the posture right before any pricing page exists, because every refund and every solo reader's email gets answered out of it.

**The pricing posture.** The content is CC BY-SA and **free forever**: anyone can read every module, study every map, run every tool, today, without paying anyone. What is purchasable is the **held container**: intake screening by a qualified CM, the CM's triage and crisis SLA, partner pairing and re-matching, the private cohort feed, the witness bench, the gated pacing through the climb. A learner pays for being held, not for access. Say it exactly that way on the enrollment page; it is true, and it makes the free path honest instead of a leak.

**The solo track is the honest free path.** Never market against it. The enrollment page links `START HERE.md`'s solo box. Some solo readers become cohort learners when they hit the witness gate; that conversion is earned by the container being real, not by content being withheld.

**Enrollment terms.** Use [Facilitator Resources/Enrollment Terms and Learner Agreement.md](Facilitator%20Resources/Enrollment%20Terms%20and%20Learner%20Agreement.md), the container commerce terms (what is purchased, the four agreements incorporated, the screening as a condition of enrollment, confidentiality and its exceptions, the refund tree). Have it reviewed by a lawyer in your jurisdiction before the first payment is taken; the template flags the clauses that need local review.

**The refund tree (binding, published on the enrollment page):**

| Exit point | Refund |
|---|---|
| Before cohort start (incl. screened-out at intake) | **Full** |
| Within week one (Modules 0–2 window) | **Full minus actual platform costs** |
| After the Module 5 unlock | **Prorated** by modules remaining |
| **Safety-routed exits** (red-flag pause that becomes an exit, screening-based mid-course exit, Doc 03 §O leaver path on CM advice) | **ALWAYS full, at any point.** No learner ever pays for a container that routed them out for their own safety |

**Done-when:** posture written on the enrollment page in the terms' words · terms legal-reviewed and published · refund tree published verbatim · payment rail chosen and tested (specifics are out of scope by design; any invoicing or checkout tool works, since it touches no learner course data).

---

## STEP 1 — Platform (the reference stack, stood up and verified)

Stand up the stack from Doc 02 §F. The operator does this; the CM verifies the parts they will live in.

1. **The one-origin static shell:** `index.html` + `Course/` pages + Map Atlas + Interactive Tools served from one origin (any static host; GitHub Pages works; even `file://` works for a single learner). Run the link checker; click GROUND NOW from three gated tools; confirm the journal sees test records from both an Atlas page and a Day tool (that proves one-origin).
2. **The private cohort feed:** Discourse private category (reference pick) or Signal group (cohorts ≤8). Configure: closed membership, author-deletable posts, CM hide rights, no public indexing.
3. **CM 1:1 channel + partner-channel list** published (Signal reference pick; the §H-compliant list verbatim from Doc 04).
4. **Privacy verification:** walk Doc 02 §F's per-component privacy table against your actual stack, component by component. Open devtools on three course pages and confirm **zero external requests** (fonts self-hosted, no analytics). Load a gated tool twice and confirm the consent block re-arms (nothing persisted). This is also a §K gate line.

**Done-when:** every row of the privacy table verified against the real stack · link checker green · consent re-arm confirmed · gating procedure agreed with the CM (who releases High-module links, per Doc 04 §D).

---

## STEP 2 — Staffing (the operator/CM line, the sizing table, the bench)

### Operator vs CM delineation

| Concern | Operator owns | CM owns |
|---|---|---|
| Commerce, terms, refunds | ✔ (executes refund tree) | flags safety-routed exits |
| Platform standing up + costs | ✔ | verifies privacy minimums in daily use |
| Marketing, enrollment page | ✔ | never |
| Intake screening + thresholds | never | ✔ (Doc 04 §A) |
| Pairing, tracker, triage, SLAs | never | ✔ (Doc 04 §B–§G) |
| High-module gating + re-screen | never | ✔ (Doc 04 §D) |
| Calendar + cadence holds | publishes template | holds pause beats per learner |
| Incident response | informed, factually | ✔ runs it (Doc 03 §L) |
| Post-cohort review | receives + acts on it | conducts it (Doc 04 §L) |
| Alumni touchpoints (Step 5) | ✔ sends them | hands off open threads at close |

The operator never sees screening answers, triage content, or anything in the 1:1 channel. The CM never handles money. One person wearing both hats (common for a first cohort) keeps the hats separate on paper anyway: the §L review will ask which hat each hour belonged to.

### CM sizing table (binding; cap from Doc 04 §K.2)

**First cohort: 8–12 learners, one CM. Hard cap.** Hours bands one qualified CM should expect (and be paid for):

| Phase | CM hours/week |
|---|---|
| Pre-launch (screening, consults, packets, pairing, drills), ~2 weeks | 8–12 |
| Modules 0–4 | 4–6 |
| **Modules 5–9 (the climb):** daily feed reads at 24h, High-week DMs to every learner, unlock verifications, the Module 5 re-screen, pause-beat holds | **8–12** |
| Modules 10–11 + wind-down (closure exchanges, leaver checklists, §L review) | 3–5 |

Budget roughly 140–180 CM hours across a default-cadence first cohort, weighted toward the climb. If your candidate CM can not protect the climb-phase hours, you do not have a CM yet. Contract via [CM Agreement Templates](Facilitator%20Resources/CM%20Agreement%20Templates.md) (CM–Operator + clinical-supervisor consultation agreements; legal review required).

### Backup CM and the bench

- **Backup CM:** named, accepted in writing, platform access granted, referral packets in hand, and **drilled** per the [CM First-Cohort Run-Book](Facilitator%20Resources/CM%20First-Cohort%20Run-Book.md) Part 5 (the 15-minute red-flag SLA must survive the CM sleeping). A backup without access and a passed drill is not a backup.
- **Witness bench:** 2–3 people (alumni when they exist; recruited witnesses per Doc 04 §B.2 for a first cohort) onboarded with the witness annex + Module 6 witness script + Partner Emergency Card, available for cadence mismatches and re-matches (onboarding note in the Facilitator Resources ops pack).

**Done-when:** CM contracted, qualified per Doc 04 §J, sized within the table · backup drilled and passed · bench of ≥2 onboarded · delineation table initialed by both hats.

---

## STEP 3 — Enrollment (intake → screening → pairing → calendar)

1. **Deploy the intake form:** [Facilitator Resources/Intake Form.md](Facilitator%20Resources/Intake%20Form.md) onto whatever form tool meets Doc 04 §H (or run it as a document the CM walks each applicant through, which is slower and fine at first-cohort size). The form implements Doc 04 §A exactly: 18+ line, bereavement/rupture question, five screens, acknowledgments including the terms.
2. **Screening window:** open intake 3–4 weeks before start; the CM screens applicant-by-applicant (never batched on a first cohort), routes green / 1:1 consult / defer-with-resources per Doc 04 §A. The operator sees only counts, never answers. Stop at 12 green enrollments (the cap); run a waitlist rather than a 13th seat.
3. **Pairing:** the CM matches per the [Async Partner Pairing Playbook](Facilitator%20Resources/Async%20Partner%20Pairing%20Playbook.md) (cadence first, time zone within 6h, language, no close ties), sends welcome packets, collects signed 7-line agreements, builds the tracker.
4. **Cohort calendar:** publish from the calendar template. Module 00's printable schedule is the learner-facing artifact; the operator's copy adds the screening window, start date, the **integration pause after Module 6**, the **rest day between Modules 8 and 9**, the optional mid-course call (after Module 6) and close call (after Module 11), and the §L review date. The pause beats go on the calendar before enrollment closes, so nobody negotiates them later.

**Done-when:** the Doc 04 §K.1 gate is met: every box checked, including cap, packets, signed agreements, drilled backup, published terms. If any box is open, the start date moves. The gate is the gate.

---

## STEP 4 — Run (cohort open → Module 11 close)

The CM holds the container per their own run-book. The operator's standing rhythm, weekly:

1. **Hours + load check (10 min):** CM reports hours against the Step 2 sizing bands and any SLA misses. Hours trending above band during the climb is the early-warning light for the likeliest safety failure (Doc 04 §K.2); respond with scope relief (operator absorbs ops tasks), never with silent CM overtime.
2. **Feed posture, not feed content:** the operator does not read the feed. The CM reports counts only: posts triaged, flags by color (per the **triage SLA in Doc 04 §F**: green none / yellow ≤24h / red immediate), re-matches, unlocks released. Templates the CM runs on: [Cohort Feed Templates](Facilitator%20Resources/Cohort%20Feed%20Templates.md).
3. **Cadence + commerce touchpoints:** refunds executed per the Step 0 tree within 5 business days of any exit; safety-routed exits refunded full, same week, no review needed.
4. **The climb (Modules 5–9):** operator's only jobs are protecting CM hours, honoring the calendar's pause beats, and not scheduling anything (calls, announcements, surveys) inside the Module 6 integration pause.

**At close: the review and the two measurements (operator-facing only, never learner-facing).**

- **§L review:** the CM conducts it 1–2 weeks after Module 11 (Doc 04 §L); the operator receives it and owns the one-improvement implementation before the next cohort.
- **Completion-by-module pull list:** from the CM's tracker metadata (never content), per module: started / completed / paused / exited. This is drop-off telemetry for course revision. It is never published to learners, never framed as a leaderboard, and never carries names into the review (pair IDs suffice).
- **Anonymized self-assessment collection:** invite every learner (finishers and leavers) to submit their [Learning Self-Assessment](Facilitator%20Resources/Learning%20Self-Assessment.md) baseline→close deltas through a **no-name channel**: a form with no identity fields, or paper photographed and sent to a collection address the CM does not run. The aggregate (not individual rows) feeds the §L review's learning-axis section.

**Done-when:** Module 11 closure ran (closure exchanges, feed gratitude, archive date announced) · all refund obligations cleared · §L review delivered with both measurements folded in · one improvement named and scheduled.

---

## STEP 5 — Continuation (the 90 days after)

The course ends; the container hands off rather than evaporating. Module 11 sets up the learner's 90-day container; this step is the operator's side of it.

**Alumni touchpoints at 30/60/90 days** (operator sends; scripted, short, no reply required; one message each):

> **Day 30:** "A month since the cohort closed. One question, from the course, not from marketing: is the morning sit still alive, in either phase? If it lapsed, [Coming Back](Practice/Coming%20Back.md) is the page that was built for exactly this. Nothing to report back. This is a witness message, not a survey."
>
> **Day 60:** "Two months. The 90-day container you declared in Module 11 is two-thirds run. One prompt for the Beep! Book: *what experiment am I in the middle of right now?* If the honest answer is 'none,' that is data, and Module 11's treasure-map section is the re-entry point."
>
> **Day 90:** "The 90-day container closes about now. Close it consciously, the way the course taught: name what got built, thank your witness, declare what is next. If 'what is next' includes holding this work with others, the Possibility Team guide is the door: [Possibility Team Conversion Guide](Facilitator%20Resources/Possibility%20Team%20Conversion%20Guide.md)."

**Possibility Team conversion:** the learner-facing guide lives in Module 11; the operator/CM-facing conversion guide is [Facilitator Resources/Possibility Team Conversion Guide.md](Facilitator%20Resources/Possibility%20Team%20Conversion%20Guide.md). Possibility Teams are open to start, not invitation-only (this corrects a v1 error). The operator's role is pointing, not running: alumni teams are theirs, not a product.

**Leavers:** anyone who exited mid-course was closed out at exit via the stopping-well path and CM Leaver Checklist (Doc 03 §O), including the ~2-week wellbeing check. At Step 5 they receive the same 30/60/90 messages **only if** they opted in at exit; the Leaver Checklist records the choice.

**Next-cohort decision:** only after the §L review is delivered. Cap movement follows Doc 04 §K.2 (8–16 ceiling, evidence-based, never above 16 per CM).

**Done-when:** three touchpoints scheduled at close (calendar or scheduler, written before the cohort ends) · leaver opt-ins recorded · PT guide linked in the Day-90 message · next-cohort decision minuted with the §L review attached.

---

## Pin these (operator edition)

- **Doc 04 is the law; this is the route.** When in doubt mid-run, the answer is in Doc 04, not in your judgment of the moment.
- **The container is the product.** The content was free yesterday and stays free tomorrow; nobody bought pages, they bought being held. Every commerce decision flows from that sentence.
- **Safety-routed exits always refund in full.** Unconditionally. The one commerce rule with no judgment call in it.
- **Protect the climb.** CM hours, pause beats, no operator noise between Modules 5 and 9.
- **You never read the feed.** Counts, not content. The delineation table is what makes the confidentiality promises true.

---

<sub>🄯 **World Copyleft 2026** · *Expand the Box (Digital)* · licensed **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**, consistent with the spirit of World Copyleft · re-presents Possibility Management thoughtware originated by Clinton Callahan & the Possibility Management community · this course is an independent re-presentation, **not an official Possibility Management training** · please share, share-alike · Powered by Possibility Management ([possibilitymanagement.org](https://possibilitymanagement.org)) · full terms: `LICENSE.md` in the course root</sub>
