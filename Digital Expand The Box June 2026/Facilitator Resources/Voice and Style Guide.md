# Voice and Style Guide

*The binding voice, style, and canon-control document for every contributor (human or AI) writing or revising any file in Expand the Box v2.*

---

## How to use this guide

Read this before drafting. Run the checks in the final section before submitting. Every rule here is checkable: where a rule can drift silently, this guide gives the exact string to search for. The humanizer pass that closes each module runs these same checks.

Two scopes apply throughout:

- **Your own prose** must follow every rule in sections 2–5.
- **Verbatim quotes** from the canonical scripts (section 7) and the canonical wordings in the ledger (section 6) are exempt from the style budgets. Quote them exactly, including their punctuation. Do not "improve" a canonical script to satisfy a style rule.

---

## 1. The voice — six rules, verbatim from v1

These six bullets are the drafter voice spec from v1 `01 - Course Architecture and Pedagogy.md` ("How sub-agent drafters should write"). They carry forward into v2 unchanged. Each bullet is quoted verbatim, followed by what it means in practice.

> **Voice.** Direct, distinction-rich, occasionally blunt. Closer to Callahan than to a corporate L&D writer. Use PM's own vocabulary — "box," "thoughtware," "liquid state," "gremlin food," "is-glue," "bright principles." Do not soften these into "limiting beliefs," "growth zones" or "values."

In practice: when a PM term exists, use it. Softening a PM term into the vocabulary of another modality is itself a Box move (the Glossary says this in its own header). If you catch yourself writing "limiting beliefs," "comfort zone," "inner work journey," or "core values" where the course means Box, thoughtware, or bright principles, the paragraph needs rewriting, not a synonym. Blunt is allowed; cruel is not. The voice respects the learner enough to say the hard sentence plainly.

> **Density.** Each paragraph should carry weight. If a paragraph could be cut without the module losing anything, cut it.

In practice: the cut test is real. Read each paragraph and ask what the module loses without it. "It provides transition" is not weight. Transitions in this course are structural (headings, the locked module template), not prose filler. A 350-line module where every paragraph survives the cut test beats a 500-line module that reads smoothly.

> **Verbs.** Prefer concrete verbs (*notice, name, drop, ground, declare, ask, listen, withdraw*) over abstract ones (*explore, engage with, work on, process*).

In practice: instructions name the physical action. "Stand. Say the sentence out loud. Notice what your jaw does." Exception: *process* is canonical PM vocabulary in exactly one context, the expressing-vs-processing distinction and the EHP. Everywhere else it is an abstract verb and stays banned ("process your feelings about the week" is banned; "run the unmixing restatement" is the fix).

> **No motivational filler.** The course is for learners who are already in. Do not pep-talk them.

In practice: no "You've got this!", no "Congratulations on making it this far!", no "This is where it gets exciting." The red-pill ceremony already handled motivation; the learner chose. Encouragement in this course takes exactly one form: accurate information about what to expect ("The first 5 minutes often feel like nothing. Stay.").

> **Cite where the distinction comes from when useful.** The 19 numbered videos and the Sparks are named in source-citation footnotes where a learner might want to verify a distinction. The course does not pretend to be original — it is a faithful re-presentation of an existing body of work.

In practice: cite Sparks by number, name source videos through the Video Manifest (never as bare `.mp4` filenames in learner-facing text), and let the learner trace any distinction back to PM source material. Modesty about originality is part of the voice.

> **Safety is always specific.** Generic "take care of yourself" is not safety. Naming the exact next step (e.g. "if you start dissociating, stop the audio, stand up, put one hand on the wall, name three things you can see") is safety.

In practice: every safety callout names a trigger signal, a physical action, and a next decision. If a safety sentence could appear in any wellness newsletter, it is not a safety sentence. Check: search your draft for "be gentle with yourself", "take care of yourself", "listen to your body" standing alone. Each hit must be replaced with a specific signal and a specific action.

---

## 2. The em-dash budget

v1 measured 17–24 em dashes per 1000 words in every module. That density is a machine signature, and it buries the dashes that matter.

**The budget: at most 5 em dashes per 1000 words of your own prose, and at most one per paragraph.** Quoted canonical scripts and ledger wordings are exempt and do not count toward the budget.

How to check (run from the course root):

```
python3 -c "import sys; t=open(sys.argv[1],encoding='utf-8').read(); w=len(t.split()); d=t.count('—'); print(f'{d} em dashes / {w} words = {1000*d/w:.1f} per 1000')" "Days/<file>.md"
```

If the number is above 5, substitute. The four substitution moves, in order of preference:

1. **New sentence.** Most em dashes are splice points between two complete thoughts. Give each its own sentence. *"The bar drops over time — not in one practice"* becomes *"The bar drops over time. Not in one practice."* This is the v1 voice anyway: short declaratives.
2. **Comma.** When the second half is a light continuation, a comma carries it.
3. **Colon.** When the second half explains or delivers the first, use a colon. One colon per paragraph, too.
4. **Parentheses.** For genuine asides only. If the aside survives the density cut test, parentheses; if not, delete it.

Never substitute with a semicolon chain or by keeping the dash and hoping. And never write an em-dash chain (two or more in one sentence); that pattern is also on the banned list in section 5.

---

## 3. Signature-word caps and incantation rotation

### 3.1 Signature-word caps

v1's voice has signature words. Used sparingly they are the voice; repeated every page they become a tic. Measured counts across the ten v1 Day files (~67,000 words) and the resulting per-module caps:

| Signature word / phrase | v1 count | Cap per module file |
|---|---|---|
| "load-bearing" | 13 | 1 |
| "on purpose" | 35 | 2 |
| "structural" / "structurally" | 32 | 3 (safety carve-outs first claim) |
| "lands" / "landed" (as a metaphor for understanding) | 49 | 3 |
| "the rep" / "reps compound" | 18 | 2 |
| "That is data." / "is data" | 11 | 1 |
| "the move" (meaning: the action to take) | 23 | 2 |
| "in your body" | 35 | 3 (practice scripts exempt) |

Check any of these with `grep -o -i -w "<phrase>" "Days/<file>.md" | wc -l`. The caps apply to teaching prose; verbatim canonical scripts are exempt as always.

### 3.2 Incantation rotation

"Study the map before reading on" appeared 27 times in v1: once per map, every map, every module. The instruction is right; the incantation must rotate. **Use the original at most once per module file.** For all other maps in the file, use one of these approved variants (or write your own that passes the six voice rules):

1. "Study the map before reading on." *(the original; once per module, maximum)*
2. "Stop here and take the map in. Shape first, labels second."
3. "Give the map a full minute before the words."
4. "Look at the map until you could redraw it with your eyes closed. Then continue."
5. "The map first. The text below assumes you have seen it."
6. "Before the prose: the image. Notice what is drawn, and what is not."

Check: `grep -c "Study the map before reading on" "Days/<file>.md"` must return 0 or 1 per file.

---

## 4. One superlative per module

v1 leaned on superlative claims: "the single most common error," "the most useful kind," "the strongest practice," "the most direct piece of inner work." Each claim is individually fine. Stacked, they cancel each other.

**Rule: each module file gets at most ONE superlative claim** ("the most…", "the single most…", "the strongest…", "the deepest…", "the #1…"). Choose the one claim the module genuinely stands behind and delete or demote the rest ("a common error," "among the most useful," "one of the strongest").

Check: `grep -o -i "the single most\|the most [a-z]*\b\|the strongest\|the deepest" "Days/<file>.md" | wc -l` and read each hit. Comparative restatements ("more useful than," "stronger than the alternative") do not count.

---

## 5. Banned AI patterns

These patterns mark machine-generated prose. They are banned in all v2 files. The humanizer pass greps for them; any hit must be rewritten.

| # | Pattern | What to search for | The fix |
|---|---|---|---|
| 1 | **"It's not X, it's Y" scaffold** and variants ("This isn't about X. It's about Y.", "not because X but because Y" stacked more than once per file) | `grep -n "It's not\|It isn't\|This isn't about\|is not about" <file>` and read each hit | State Y directly. If the X-contrast genuinely teaches (PM does use real contrasts: feeling vs emotion), make it a named distinction with both sides defined, not a rhetorical flourish. |
| 2 | **Rule-of-three overuse** (triplet lists as default rhythm: "clear, concise, and compelling") | read-aloud pass; if three consecutive sentences each contain a triplet, rewrite two | Vary list lengths. Two items and four items exist. |
| 3 | **"Here's the thing"** and cousins ("Here's the kicker", "Let that sink in", "Read that again") | `grep -ni "here's the thing\|here's the kicker\|let that sink in\|read that again" <file>` | Delete. Say the thing. |
| 4 | **Bold-led bullet walls** (five+ consecutive bullets each opening with a bolded phrase and a colon) | visual scan; `grep -c "^- \*\*" <file>` as a smoke test (>10 hits in teaching prose warrants a look) | Tables for genuinely parallel data (v1 uses these well); prose for argument; bullets only when the items are truly a list. Note: the locked module template's "Core PM concepts" and "Glossary additions" sections legitimately use bold-led bullets; the ban targets teaching prose. |
| 5 | **Em-dash chains** (two or more em dashes in one sentence) | covered by section 2's budget; additionally `grep -n "—.*—" <file>` | Restructure the sentence. |
| 6 | **Class words**: delve, tapestry, landscape (figurative), deep dive, unpack, embark, elevate, foster, leverage, robust, seamless, holistic, transformative journey, "in today's world", "at the end of the day", game-changer, supercharge | `grep -niw "delve\|tapestry\|unpack\|embark\|leverage\|robust\|seamless\|holistic\|game-changer\|supercharge" <file>` and `grep -ni "deep dive\|in today's world\|at the end of the day\|transformative journey" <file>` | Replace with a concrete verb or delete. **Two named exemptions:** *journey* is allowed only inside the canonical EHP sentence ("a moment-to-moment, non-linear discovery journey of healing"), and *navigate* is allowed only for EHP/witness navigation (Positions 2–4), where it is PM's own term. *Unlock* is allowed only for the unlock checklist, which is course vocabulary. |
| 7 | **Hedging openers**: "It's worth noting that", "It's important to remember", "Keep in mind that" | `grep -ni "worth noting\|important to remember\|keep in mind that" <file>` | If it is worth noting, note it. Delete the scaffold. |

---

## 6. CANONICAL-PHRASING LEDGER

This ledger is the canon control. Every major distinction has exactly one canonical wording, with its source. When a module, Map Note, Atlas tool, glossary entry, or feed template states one of these distinctions, it states it in words compatible with the ledger. This is the control that would have caught the v1 high-drama drift before it shipped.

**Three entries below are CORRECTIONS of confirmed v1 bugs.** They are flagged ⚠ CORRECTION and stated unmistakably. Where v1 text (including the copied v2 `Facilitator Resources/Glossary of PM Distinctions.md`, until its fix lands) contradicts this ledger, **the ledger wins.**

### 6.1 The three corrections

#### ⚠ CORRECTION 1 — HIGH DRAMA

**Canonical:** High drama sits under **Conscious Purpose**, in the **Responsible Game**; the course's own map Map 20 (`Maps/M20.png`) places it there. **High drama is taking radical responsibility at gameworld scale**: consciously sourcing bright principles to hold and shift what happens in a whole field of commitment — a team, a family, a culture, a gameworld. Low drama is unconscious purpose at kitchen scale; high drama is conscious purpose at world scale. High drama is the *destination* of the drama work, not a variant of the disease.

**What v1 got wrong:** v1 Day 07 (lines ~51, ~95–103, ~385) and the Glossary (lines ~355–357) defined high drama as "theatrical, staged, often productive drama — a surgeon in an emergency, a trainer holding a charged moment, an actor in a play" and then claimed **"Both are gremlin food."**

**That sentence is FALSE and is banned.** High drama is NOT theatrical, staged performance. High drama is NOT gremlin food. Only low drama feeds the Gremlin. The v1 wording also contradicted the course's own Map 20 map, which shows HIGH DRAMA under Conscious Purpose.

**Regression check (must return zero hits in every v2 file):**
```
grep -rn "Both are gremlin food" .
grep -rni "high drama.*theatrical\|theatrical.*high drama" .
```

#### ⚠ CORRECTION 2 — BRIGHT AND SHADOW PRINCIPLES (causation direction)

**Canonical:** The causation runs from principle to culture. **Sourcing bright principles generates archiarchy. Sourcing shadow principles generates patriarchy.** The principle is upstream; the culture is downstream. Bright principles are the class of principles whose sourcing generates archiarchy (love, integrity, possibility, courage, presence, clarity…). Shadow principles are the class whose sourcing generates patriarchy (domination, manipulation, control, deception, scarcity, righteousness…). Bright is not "good" and shadow is not "evil": bright is generative of consciousness, shadow is destructive of consciousness, and shadow has domains (the surgeon sources control during the operation). *The shadow you cannot name owns you.*

**What v1 got wrong:** v1 Day 10 lines ~112–114 said bright principles "are sourced **from** archiarchy" and shadow principles "are sourced **from** patriarchy". The arrow ran backwards, making culture the source of principles. Line ~116 of the same file had it right ("Archiarchy is created by sourcing from bright principles; patriarchy is created by sourcing from shadow"). Line ~116's direction is canon. Never write "sourced from archiarchy/patriarchy" about a principle class.

**Regression check (must return zero hits):**
```
grep -rni "sourced from archiarchy\|sourced from patriarchy" .
```

#### ⚠ CORRECTION 3 — MATRIX (one definition, build sense leads)

**Canonical, primary sense (use this everywhere by default):** **Your matrix is the energetic structure you build, through practice, that determines how much consciousness you can hold.** Distinctions, feelings at higher intensity, responsibility at larger scale: each requires matrix to hold it. Matrix is built through conscious practice: reps, feelings work, holding attention, taking on responsibility slightly beyond current capacity. Thoughtware upgrades install onto matrix; without enough matrix, an upgrade has nowhere to live.

**Two secondary senses exist and must be explicitly marked as secondary whenever used:**
- *Cultural-matrix sense:* "the matrix" as the default cultural cosmology a person is raised inside (in most learners' case, patriarchy). Always written with a qualifier ("the cultural matrix," "the patriarchal matrix"), never bare "matrix."
- *Structured-field sense* (delivery docs): a deliberately structured learning field. Avoid where possible; say "container" or "holding context" instead.

**What v1 got wrong:** v1 defined matrix three conflicting ways (README's build sense, Doc 02's "structured field," the Glossary's patriarchy-only sense) with a dangling "See Day 01" pointer. v2 uses one definition, the build sense, everywhere; the Glossary entry leads with it.

**Check:** every occurrence of the bare word "matrix" in a learner-facing file must read correctly against the build sense: `grep -rniw "matrix" Days/ Practice/ "Map Notes"/ | grep -vi "cultural matrix\|patriarchal matrix\|matrix-code"`.

#### Minor wording fix — EHP positions

The EHP has **six positions, numbered 0 through 5**. v1 wrote "5 positions (Position 0 through Position 5)", which miscounts. Canonical wording: "the six positions of the EHP map (Position 0 through Position 5)". Check: `grep -rn "5 positions" .` must return zero hits.

### 6.2 The ledger

Each entry: term, canonical wording (quote-ready; use these words or words plainly compatible with them), source. Source "Glossary" = `Facilitator Resources/Glossary of PM Distinctions.md` (post-fix v2 edition).

| Term | Canonical wording | Source |
|---|---|---|
| **Context** | The invisible source-frame that determines what actions, meanings, choices, and results are even available. Upstream of mindset, beliefs, and intentions. The leftmost link of the chain. | Glossary; Day 01 |
| **Content** | What is happening inside the context — topic, facts, words. Same content in two contexts means two different things. | Glossary; Day 01 |
| **The chain** | new context → new thoughtware → new thoughtmaps → new options → new choices → new behavior → new results. The arrow runs left to right only. | Day 01; Glossary |
| **Thoughtware** | What you think *with* — the internal architecture that determines which thoughts are available. Distinct from the content (opinions, beliefs) that runs on it. | Glossary; Day 02 |
| **Thoughtmap** | A specific cognitive map used to navigate. The map is not the territory; a tool, not a doctrine. | Glossary; Day 02 |
| **Box** | The survival-and-protection thoughtware you assembled in childhood. What kept you alive then. Not the enemy. *You have a Box; you are not your Box.* | Glossary; Day 02 |
| **Being** | What you actually are, prior to the Box. You have a Box. You have a Gremlin. You are neither. You are Being, which has both. | Glossary |
| **Disidentification** | The move from *I am this* to *I have this*. The grammatical shift is the energetic shift. Not destruction. | Glossary; Day 02 |
| **Is-glue / is-glue dissolver** | The verb *to be* + a noun, fusing a transient perception to a permanent identity. The dissolver restores provisional status without softening the perception. | Glossary; Map Note Map 22 |
| **Liquid state** | The temporary condition in which solid thoughtware loosens and new thoughtware can be installed. Transformative only inside a holding context. | Glossary; Day 03 |
| **Holding context** | The structural conditions inside which a liquid state becomes transformative rather than merely spectacular. | Glossary; Day 03 |
| **Five bodies** | Intellectual, emotional, physical, energetic, archetypal. The intellectual body is the loudest for most modern adults; the other four run on emergency power. | Glossary; Day 03 |
| **Center** | The energetic location in your body from which your choices, will, and authority come. Not a metaphor. | Glossary; Day 03 |
| **Grounding cord** | An energetic line declared — by intention, not visualisation — from your center to the centre of the earth. Discharge and stability. Not protection. | Glossary; Day 03 |
| **Bubble** | An arm's-length energetic sphere declared around you. A distinction, not a protection. Clarifies what is yours and what is not. | Glossary; Day 03 |
| **Golden cube** | A portable, declared creative workspace. Workspace, not refuge. | Glossary; Day 03 |
| **Feeling** | A present-time archetypal energy in the emotional body. One of four: anger, sadness, fear, joy. 3–5 minutes at full intensity, then it passes. Informational. Clean. | Glossary; Day 05 |
| **Emotion** | A past-time, mixed, story-laden state. A feeling that was not allowed to move, got stored, and now runs on autopilot. Longer than five minutes. | Glossary; Day 05 |
| **Four feelings** | Anger, sadness, fear, joy. Four. Not five. Not eight. "Love" is not a feeling; "frustration," "overwhelm," "stress" are stories about mixed emotions. | Glossary; Day 05 |
| **The four asked-for actions** | Anger says make a boundary. Sadness says let this go. Fear says prepare. Joy says more of this. | Day 05 |
| **5-minute test** | If it is still happening after five minutes, you are in an emotion, not a clean feeling. | Glossary; Day 05 |
| **Numbness Bar** | A threshold in the emotional body below which feelings do not register. Installed in childhood as protection. Intelligent then. Obsolete now. Lowers through repeated low-intensity work. | Glossary; Day 05 |
| **Old Map of Feelings** | The patriarchal-paradigm map: feelings sorted into good and bad, three of four forbidden, the fourth diluted. The numbness is the load-bearing mechanism. | Glossary; Day 05 |
| **Mixed emotion** | A stored state that is part feeling, part memory, part story — two or three feelings tangled with the past event that froze them. The default adult condition. | Glossary; Day 06 |
| **Unmixing** | Naming the component feelings of a mixed emotion, one at a time, so each can move through. Anger as anger. Sadness as sadness. Fear as fear. Not all at once. | Glossary; Day 06 |
| **EHP** | The structured PM practice for completing a stored emotion so its energy returns. Six positions, numbered 0 through 5. Non-linear; no script — a moment-to-moment discovery journey. Requires a witness beyond small material. NOT for trauma. | Glossary; Day 06 |
| **Expressing vs processing** | Expressing acts a feeling out at a person and creates damage; processing completes a stored emotion with a witness in a held container. Different practices. Different rooms. | Glossary; Day 06 |
| **Witness** | (1) The inner location feedback is sourced from — observed without verdict. (2) The person holding space during an EHP. Does not fix, advise, narrate, or "send love." The witness's energy of being present is the medicine. | Glossary; Days 04/06 |
| **Low drama** | The daily-life, sub-threshold kind of drama. Low not because the stakes are low but because it operates below the threshold of noticing. Produces gremlin food. | Glossary; Day 07 |
| **High drama** | See ⚠ CORRECTION 1. Radical responsibility at gameworld scale, under Conscious Purpose, in the Responsible Game (map Map 20). NOT theatrical performance. NOT gremlin food. | Map 20; v2 canon |
| **Low Drama Triangle** | Persecutor, Victim, Rescuer: three positions of one Box-pattern, one machine, three costumes, producing gremlin food. | Glossary; Day 07 |
| **Gremlin** | The part of you that wants gremlin food. Hungrier than the Box, more cunning, louder. You have a Gremlin. You are not your Gremlin. | Glossary; Day 07 |
| **Gremlin food** | What drama is actually for. Being right. Being wronged. Being special. Being misunderstood. The uncomfortable one is usually the most operational. | Glossary; Day 07 |
| **Responsible Game** | What is left when you decline drama. Simpler. Less stimulating. Feels less alive at first because the Gremlin is starving. Sourced from Adult and bright principles. | Glossary; Day 07 |
| **Feedback (PM)** | Information about *how a person was* when they did what they did. Sourced from the witness. Past-oriented. Given only inside a consenting transformational container. | Glossary; Day 04 |
| **Criticism / Advice** | Same sentence shape, different source: criticism from the Gremlin (wants the other smaller), advice from the Rescuer (wants its own discomfort to stop). | Glossary; Day 04 |
| **Coaching (PM)** | Future-oriented offer of possibilities the client could try. Does not solve the client's problem. | Glossary; Day 04 |
| **Beep · Shift · Go** | The rapid-learning loop. Go: act. Beep!: information that something did not work — a design specification, not a verdict. Shift: change one specific thing. Go again. | Glossary; Day 04 |
| **Beep! Book** | A literal notebook. Engineering log, not journal. Date-stamped reps. | Glossary; Day 04 |
| **Experiment** | Small, specific, time-bounded test of new thoughtware: *what I will do / by when / what I will notice*. One at a time. Reps compound; insight does not install thoughtware. | Glossary; Day 04; Experiment Bank |
| **4 Listenings / Possibility Listening** | Four stances a listener can occupy; the fourth is the vacuum — zero resistance, no nodding, no fixing. Serves emergence, not accuracy. | Glossary; Day 08 |
| **Completion loop** | The five-step discipline that closes a communication so it leaves no residue. Step 5 — naming complete, out loud — is the PM-distinctive piece. | Glossary; Day 08 |
| **Energetic debt** | The accumulated weight of incomplete communications. Gremlin food. Paid down by completion loops, including retroactive ones. | Glossary; Day 08 |
| **Ego states** | Five, not three: Parent, Child, Adult, Gremlin, Demon. A state, not a personality. PM names the Gremlin and Demon on purpose. | Glossary; Day 09 |
| **Demon** | The ego state with the capacity for real harm. Not a metaphor. The work is not to integrate the Demon; the work is to *know* it. Locator only in this course. | Glossary; Day 09 |
| **Problem ownership** | Whose problem is this? My problem / the other person's problem / explicitly contracted shared. There is no "we" in responsibility. | Glossary; Day 09 |
| **Levels of responsibility** | Child (someone else is responsible) · adolescent (rebellion, frame intact) · adult (I do my share) · radical (I am at cause; author of the next move, not of your past). | Glossary; Day 01 |
| **Red pill / blue pill** | The metaphor for choosing whether to actually be in the work. If a learner cannot honestly say the red-pill sentence, that is not a problem — it is data. | Glossary; Day 01 |
| **Gameworld** | A field of human commitment: context, purpose, rules of engagement. Bounded, ruled, chosen. Entered by choice; closed consciously. | Glossary; Day 01 |
| **Matrix** | See ⚠ CORRECTION 3. Build sense leads, everywhere. | v2 canon |
| **Bright / shadow principles** | See ⚠ CORRECTION 2. Sourcing bright generates archiarchy; sourcing shadow generates patriarchy. | Day 10 (line ~116 sense); v2 canon |
| **Sourcing** | The act of acting from a principle. There is no neutral action. *What is sourcing this action right now?* — asked per-action, not per-life. | Glossary; Day 10 |
| **Map of Possibility** | Possibility is not a list of options the world hands you; possibility is a space you enter on purpose. Entered by three keys held simultaneously: held context, liquid state, dangerous question. | Glossary; Day 10 |
| **The Three Powers** | Choosing (own the choice) · Asking Dangerous Questions · Declaring. Sequential, not parallel — declarations that skip the foundation collapse. | Glossary; Day 10 |
| **Declaration** | A speech act that brings a new context into being. Not a promise, not an opinion, not a wish. Only holds when sourced from a bright principle. | Glossary; Day 10 |
| **Learning Spiral** | Try → notice → name → adjust → try again. The slow outer loop; Beep · Shift · Go is the fast inner loop. Not linear self-improvement. | Glossary; Days 04/09 |
| **Archiarchy / Patriarchy** | Archiarchy: the culture generated by sourcing bright principles — distributed authority, conscious relating, creating rather than dominating. Patriarchy: the culture generated by sourcing shadow principles — hierarchical, fear-based, control-oriented, built on numbness. Structural descriptions, not moral indictments. | Glossary; Day 10; v2 causation per CORRECTION 2 |

When in doubt about a term not listed here, the post-fix Glossary is the source of truth; this ledger overrides it only where a CORRECTION applies.

---

## 7. Voice-anchor appendix

The scripts below are the course's verbal canon. **Copy verbatim, never paraphrase.** When a v2 file needs one of these, paste it exactly, including punctuation, em dashes, italics, and line breaks. These quotes are exempt from every style budget in this guide. They are also your calibration: read one aloud before drafting and match its register.

### 7.1 The red-pill ceremony script (v1 Day 01, embodied practice)

> **Script.**
>
> Stand up. Both feet on the floor. Shoulders down. Hands loose at your sides.
>
> Take three breaths, exhale longer than inhale. Audible exhale.
>
> Now, out loud: *"In the next 30 days I am going to do this course."* Say it.
>
> Notice what your body did when you said that. Did you tighten? Did you brace? Did you brighten? Whatever it did, that's information.
>
> Now, out loud: *"I can stop at any time. I can pause at any time. I can put it down at any time. Nothing makes me do this."*
>
> Notice what your body did *that* time.
>
> Now, the choice. Two options. Speak each one out loud, in order, and notice which one your body recognizes as true.
>
> *"Blue pill. I'm not doing this. The course is interesting but I'm not actually in it. I'll watch the videos when I get to them. I won't pair with anyone. I won't run the experiments. I'm a tourist."*
>
> Pause. Notice.
>
> *"Red pill. I am in this. For the next 30 days I am the author of what this becomes for me. I will pair with my partner. I will run the experiments. I will use the safety practices when I need them. I will not pretend to be in if I am not. I am in."*
>
> Pause. Notice.
>
> Choose. Say the chosen sentence one more time, alone, in the room you are in, with your body present.
>
> Sit down. Write the date and your chosen sentence on a piece of paper. Put it where you will see it during this course.

And its closing paragraph, also canonical:

> If you cannot honestly say the red-pill sentence right now — that is not a problem. That is data. The course is not for everyone right now. Pause. Talk to the community manager. The course will still be here in three months.

### 7.2 The four-level sentence (v1 Day 01, companion practice)

> **Companion practice — the four-level sentence (~10 min).** This is the solo version of the Day 1 "Four Levels" interactive tool — the levels-of-responsibility map, done in your body instead of on the screen. Run it after watching `02 - New Responsibility & Culture.mp4`. Stand, both feet on the floor, shoulders down, three breaths with the exhale longer than the inhale. Pick **one real sentence you actually said recently** — to a partner, a boss, a kid, yourself — something with a charge on it: *"You never listen." "I can't deal with this right now." "Fine, I'll just do it myself."* Write it down so it doesn't drift. You will say that one sentence four times — once from each level — and notice what your body does each time. **Child (90 sec):** speak it as pure blame; someone did this to you, it isn't fair. Notice your chest, your jaw, where the weight sits — the suffering posture. Return to neutral. **Adolescent (90 sec):** the same sentence as defiance — *watch me, I'll do the opposite.* Feel the charge of rebelling, and notice you are still aimed *at* someone. Return to neutral. **Adult (90 sec):** the same sentence from "my ability to create results — I keep my agreements." The voice goes plainer; notice the weight come off the chest. Return to neutral. **Radical (3 min):** the same sentence one last time, from "I am at cause — I am the author of what this becomes." Not *I caused it* — the author of the next move. Notice what becomes available that was invisible from child or adolescent, and that the posture is the least dramatic of the four. Stay an extra minute. Sit and write three lines: *which level was my body's home stance on that sentence; which level felt unfamiliar in my body; what became possible only from radical that was invisible from child.*

*(v2 note: the video reference in this script is handled per the text-first decision. The module file points to the Video Manifest, and the script runs with or without the video.)*

### 7.3 The Day 6 small solo EHP script (v1 Day 06, embodied practice)

> **Script.**
>
> **Position 0 — Set foundation (5 min).**
> Sit. Both feet on the floor. Center. Drop a grounding cord into the earth. Set a bubble at arm's-length. Imagine a golden cube around the bubble — the container of this practice. Three breaths, exhale longer than inhale.
>
> Name out loud one bright principle you are sourcing from. (Examples: clarity, presence, integrity, gentleness, truth.) One word.
>
> **Position 1 — Make contact with yourself (3 min).**
> One hand on chest, one on belly. Speak to yourself by name: *"[Name], what can I do for you?"* Wait. Listen. (If the answer is "stop the practice" — stop. That is a valid completion.)
>
> Name the small stored emotion you have chosen, plainly: *"I have a stored emotion about [X]."* One sentence. No story yet.
>
> **Position 2 — Navigate to liquid state (5–8 min).**
> Close your eyes. Locate the stored emotion in your body. Where exactly? Heart? Throat? Belly? Bones? Specific.
>
> Let the sensation get *bigger*. Not the story — the sensation. If a sound wants to come (a sigh, a hum, a soft groan, even a single word), let it. Sound moves emotion faster than language.
>
> Stay until you feel a softening — a "yes, I am with this" quality. That is liquid state. If you cannot find it in 5 minutes, ground and end here. The bar may still be high today. Try again another day.
>
> **Position 3 — Unmix (8–12 min).**
> Eyes closed: of the four feelings — anger, sadness, fear, joy — **which two or three are in this mixed emotion?** Name them out loud. *"In this I have some anger and some sadness."* Whatever is true.
>
> Pick *one* of them. The one that wants to move first. Let it take more space. Anger as anger — jaw setting, arms wanting to push, bones solid. Sadness as sadness — chest softening, throat thickening, tears if they come. Fear as fear — skin prickling, breath shallow, attention sharpening.
>
> 3 to 5 minutes. **One feeling at a time.** No story. If the mind tries to explain "this is because of…" — set the explanation down and return to the sensation.
>
> If a second feeling rises behind the first, let it move. Same way. 3 to 5 minutes.
>
> If a memory of the original event surfaces, register but do not narrate it. *"I see myself at seven, in the kitchen."* That is enough. Stay with the feeling, not the storyboard.
>
> **Position 4 — Closing (5–7 min).**
> When the body has softened and the breath deepened, begin to close. Open eyes. Name three things you can see. Drink water. One hand on the chair, one foot pressed to the floor. You are here, in this room, now.
>
> If a new decision arrived (an old *"I will never need anyone"* becoming *"I can let myself be witnessed now"*) — write it down, one sentence, present tense.
>
> Out loud: *"Thank you, [Name]. We will continue when ready."* The container is closing.
>
> **Position 5 — Cleanup (3 min).**
> The golden cube dissolves. The bubble softens. The grounding cord remains. Stand. Walk three steps. Drink water. Notice the temperature of the room. You are back.
>
> In your notebook, fast, no editing: *Mixed emotion · component feelings · what moved · what didn't · any new decision · how my body feels right now.*

### 7.4 The witness-overflow script (v1 Day 06, partner exchange)

For when a partner names material that exceeds the exchange's scope:

> If your partner names material that exceeds the module's scope (trauma surfacing, ideation, intent to act on the original event in their adult life) — gently say so. *"What you are describing is bigger than this exchange can hold. I am glad you told me. I am also asking you to message the CM today, and if there is a clinician you work with, them too. I am still with you. And I am being honest about the limits of what I can do here."* Then continue witnessing. The honesty is part of the witnessing.

### 7.5 The 60-second universal grounding script (v1 Doc 03 §D / Solo Scripts #1)

> **Grounding (60 seconds).**
>
> 1. Stop whatever you were doing in the module. Close the video or the document.
> 2. Stand up. Both feet on the floor. Knees soft.
> 3. Breathe out longer than you breathe in, three times. Audible exhale is fine.
> 4. Name three things you can see in the room.
> 5. Name one thing you can hear.
> 6. Place one hand on your sternum, the other on your belly. Notice that your body is here.
> 7. When you have come back, decide: continue, pause for 10 minutes, or stop the module for today.

---

## 8. The standard World Copyleft footer block

Every learner-facing markdown file ends with this footer, exactly:

```
<sub>🄯 **World Copyleft 2026** · *Expand the Box (Digital)* · licensed **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**, consistent with the spirit of World Copyleft · re-presents Possibility Management thoughtware originated by Clinton Callahan & the Possibility Management community · this course is an independent re-presentation, **not an official Possibility Management training** · please share, share-alike · Powered by Possibility Management ([possibilitymanagement.org](https://possibilitymanagement.org)) · full terms: `LICENSE.md` in the course root</sub>
```

Two binding wording rules inside it:

1. **"consistent with the spirit of World Copyleft"**, never "the same World Copyleft terms." World Copyleft is PM's own license concept; CC BY-SA 4.0 is a different instrument that honors its spirit. Claiming identity overstates. Check: `grep -rn "same World Copyleft terms" .` must return zero hits.
2. **The honesty line stays in.** "Not an official Possibility Management training" appears in every footer, not only in LICENSE.md. The course's standing rests on being honest about what it is. Check: `grep -L "not an official Possibility Management training" Days/*.md` lists any module missing it.

---

## 9. Pre-flight checklist (run before submitting any file)

```
# 1. Em-dash density (target ≤ 5.0)
python3 -c "import sys; t=open(sys.argv[1],encoding='utf-8').read(); w=len(t.split()); d=t.count('—'); print(f'{1000*d/w:.1f} per 1000')" <file>

# 2. Canon regressions (all must be silent)
grep -n "Both are gremlin food" <file>
grep -ni "sourced from archiarchy\|sourced from patriarchy" <file>
grep -n "5 positions" <file>
grep -n "same World Copyleft terms" <file>

# 3. Banned patterns (all must be silent or justified)
grep -ni "here's the thing\|let that sink in\|worth noting\|important to remember" <file>
grep -niw "delve\|tapestry\|unpack\|embark\|leverage\|robust\|seamless\|holistic" <file>
grep -n "—.*—" <file>

# 4. Incantation rotation (0 or 1)
grep -c "Study the map before reading on" <file>

# 5. Signature caps (compare against the table in §3.1)
grep -o -i -w "load-bearing" <file> | wc -l

# 6. Footer present and correct
grep -c "consistent with the spirit of World Copyleft" <file>
grep -c "not an official Possibility Management training" <file>
```

A file that passes all six blocks is style-clean. The humanizer pass still reads it aloud once: greps catch patterns, not tone.

---

<sub>🄯 **World Copyleft 2026** · *Expand the Box (Digital)* · licensed **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**, consistent with the spirit of World Copyleft · re-presents Possibility Management thoughtware originated by Clinton Callahan & the Possibility Management community · this course is an independent re-presentation, **not an official Possibility Management training** · please share, share-alike · Powered by Possibility Management ([possibilitymanagement.org](https://possibilitymanagement.org)) · full terms: `LICENSE.md` in the course root</sub>
