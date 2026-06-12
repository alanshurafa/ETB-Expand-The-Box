# WORK ORDER: Redraw the four photo-slot maps (M01 · M08 · M10 · M27)

Authored 2026-06-11 on Fable from the owner's instruction. Status: **PARKED — awaiting Codex** (owner wants OpenAI Codex to do the drawing; not installed on this Mac as of 2026-06-11). Executable by Codex CLI or any image-capable agent; an SVG-authoring fallback route is documented in §5. A future Claude session resuming this: read this whole file, then verify the source photos yourself before drawing anything.

## §1 — The problem

Four course maps are framed **photographs** (flipcharts taped to walls/brick, inside a digital frame with a typeset title) instead of clean digital renders like the other 36 maps. Owner's words: "They're just pictures inside the map." They must be redrawn and inserted into **all existing ETB course editions**.

| Slot | Map | Current file (all 3 editions) | Best source photo (Drive, READ-ONLY) |
|---|---|---|---|
| M01 | New Context (the chain) — "the context map" | `Maps/M01.png` (1600×2200 framed photo) | `ALL ETB MAPS/New Context Chain/New Context Chain.png` (+ 2 cohort .jpg alternates) |
| M08 | The Old Map of Feelings | `Maps/M08.png` | `ALL ETB MAPS/Old Map of Feelings/Old Map of Feelings.png` (+ "ETB Online January 2026" + "NY October 2025" .jpg alternates) |
| M10 | The New Map of Feelings | `Maps/M10.png` | `ALL ETB MAPS/New Map of Feelings/New Map of Feelings.png` (+ 2 cohort .jpg alternates) |
| M27 | Your Gremlin | `Maps/M27.png` | `ALL ETB MAPS/Your Gremlin/Your Gremlin.png` (+ 2 cohort .jpg alternates) |

Drive base: `/Users/shurafa/Library/CloudStorage/GoogleDrive-shurafa@gmail.com/My Drive/__shurafa@gmail.com/_PM Possability Manangement/`. **Do NOT use any "Infographic" variant as a source of style** — infographics are excluded from course maps by standing owner rule; use them only to cross-check hard-to-read words.

## §2 — Target style (match the 36 existing clean renders)

Reference exemplars in the repo: `Maps/M07.png`, `Maps/M20.png`, `Maps/M33.png` (open them first). The house style is **minimal hand-drawn emulation**: clean ivory/white paper background (no photo, no frame-in-frame, no wall, no tape), marker-style hand lettering and line work, the source chart's own palette (typically blue/red/green marker on white), the map title drawn as part of the chart (as the source charts do), no watermarks, no NotebookLM/AI-tool branding, no gradients/3D/stock-infographic styling. Output: **PNG, 1024×1536** (the clean-render standard; the four current photo files are 1600×2200 — the replacement adopts the render standard).

## §3 — Content spec per map (verify against source photos before drawing — transcriptions below are starters, not gospel)

**M01 · New Context Chain** — a vertical chain of boxed/lettered stages connected by downward arrows: NEW CONTEXT → NEW THOUGHTMAPS → NEW OPTIONS → NEW CHOICES (annotated: conscious / unconscious) → NEW BEHAVIOUR → NEW RESULTS. A red funnel/cone overlays the chain narrowing from top-right down to an ellipse around NEW RESULTS, with crossed-circle marks at top and beside NEW THOUGHTMAPS, and a red "METHOD: 1) 2) ..." note at right. Canon check: must agree with the M01 Atlas page's distinctions (the chain runs context→results; you intervene at context, not at results).

**M08 · The Old Map of Feelings** — title + the framing lines: "GOOD/POSITIVE vs BAD/NEGATIVE" (struck through as taught) and the quoted belief **"IT'S NOT OKAY TO FEEL."** Four quadrants (ANGER, SADNESS, JOY, FEAR), each filled with the conditioned negative beliefs in marker scrawl (ANGER: out of control, dangerous, violent, chaos, uncivilized, immature, savage, not professional, crazy, loud, intense, BAD negative, lacks discipline, power over, manipulation, not okay, "women are crazy" … SADNESS: weak, "men don't cry," unprofessional, feminine, brings others down, not fun, something is wrong, party pooper, never-ending black hole, can't do anything, mopey, needy, childish, keep it to yourself, not okay … JOY: ridiculous, childish, not real, "who do you think you are?", creates jealousy, lousy, crazy, must be on drugs, not realistic, naive, not serious, cannot lead, parasite, annoying, don't have enough, work to do, irresponsible, fool, selfish, things are so bad out there, not okay … FEAR: weak, small, deer in the headlights, has no place, lack of courage, can be controlled through fear, insecure, unconfident, unprofessional, can't trust, not credible, unreliable, wild, crazy, unpredictable, hysterical, contagious, stress, can't function, chicken, can't take chances, cannot lead, panic, blocks, not okay, wrong, BAD negative). Canon check: this is the **conditioned** map — the beliefs render as quoted conditioning, matching Module 05's teaching.

**M10 · The New Map of Feelings** — title + the header line: "FEELINGS ARE NATURAL SOURCES OF ENERGY AND INFORMATION to create…". Four quadrants with each feeling's purpose/asked-for actions (ANGER: set boundaries, say no, physical presence, choose, raise voice, energy, take space, chop wood, clarity, take a stand, take action, move, assertiveness, protect, commitment … SADNESS: what is essential, empathy, softness, slow, preciousness of love, share tenderly, accept what is, closure, grieving, cry, tension release, rest, cleanse, let go … JOY: bond, play, celebrate, collaboration, uplift, explore, engagement, invitations … FEAR: get prepared, plan ahead, list, frequently notice danger, sense the edge, negotiate intimacy, sense where you are, invention, possibility, potential, what's next). Canon check: must agree with Module 05 + the M10 Atlas flip-cards (four feelings, each neutral information + energy with asked-for actions).

**M27 · Your Gremlin** — the gremlin figure drawn large (the source's green line-drawn creature: horned/grinning, ribbed torso), with the text blocks: "YOUR GREMLIN — the King or Queen of your Underworld. And it owns your life." · "…is currently on a low drama gremlin feast." · "TYPE 1 / TYPE 2" · "Gremlin transformation — prologue, chapter 0, chapter 1." Canon check: matches the M27 Atlas page (gremlin food = drama, righteousness, being right/victim/special; you HAVE a gremlin, you are not your gremlin; the war on the gremlin is itself gremlin food).

## §4 — Insertion checklist (after the four PNGs exist)

1. Replace `Maps/M01.png`, `Maps/M08.png`, `Maps/M10.png`, `Maps/M27.png` in ALL THREE editions of the repo `~/Project/ETB-Expand-The-Box/`: `Digital Expand The Box May 2026/` (owner explicitly authorized touching the archive's four map images — images only, nothing else), `Digital Expand The Box June 2026/`, `Digital Expand The Box Group Version/`.
2. Also drop each new render as the bare-name PNG back into its `ALL ETB MAPS/<folder>/` on Drive? **NO — Drive library is read-only. Instead** place copies under `_build/redrawn-maps/` in the repo and note in the manifest that the library's bare-name files remain the photos.
3. Update `00 - Course Manifest.md` (June + Group Version): M01/M08/M10/M27 move from "photo-slot regeneration pending" to "clean render (redrawn 20XX-XX-XX)".
4. Check the M01/M08/M10/M27 Atlas pages + Map Note cards for alt text describing the old image; update alt text to describe the redrawn chart (current alt texts don't mention photos — verify anyway).
5. Run `_build/build.py` in June + Group Version (link gate must pass); spot-open the four Atlas pages and the Maps index in a browser.
6. Commit + push (one commit, message notes the four slots closed); update `_build/HANDOFF.md`.

## §5 — Fallback route (no Codex)

Any capable agent can: author each map as an SVG in the §2 style (hand-drawn-emulation: slight line jitter, marker-weight strokes, hand-lettering font or drawn paths), render SVG→PNG at 1024×1536 via headless Chrome (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --headless --screenshot=... --window-size=1024,1536 file.svg`), and proceed from §4. Quality bar: side-by-side with M07/M20/M33 it should read as the same family.
