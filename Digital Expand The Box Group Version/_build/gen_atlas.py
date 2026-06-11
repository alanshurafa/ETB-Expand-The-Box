#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_atlas.py — template-stamp the 11 NEW Map Atlas "Study the map" pages
for ETB v2, plus regroup the Atlas index by course module with quiet
completion dots.

METHOD (PLAN-html-shells.md §B.2): read the structural template once from
"M10 - New Map of Feelings.html", hold it here as TEMPLATE + a per-map
CONTENT dict, and emit 11 standalone files into ../ (the Map Atlas dir).

Binding constraints (§0):
  - self-hosted fonts only (../_assets/fonts/fonts.css). Never googleapis/gstatic.
  - works from file://  — relative %20-encoded hrefs, no fetch() of local files.
  - localStorage: only etb_atlas_MXX keys.
  - no gamification. completion dots = quiet presence indicators only.
  - v2 footer = the Voice-Guide World-Copyleft block.
  - ledger-compliant content (Voice and Style Guide §6): high drama under
    Conscious Purpose / Responsible Game (NOT theatrical, NOT gremlin food);
    sourcing bright -> archiarchy, shadow -> patriarchy (principle upstream);
    matrix = build sense; EHP six positions 0-5.

SAFETY (§B.5): M38/M39/M40 are locator / study level ONLY. No do-it-now EHP
steps. A "carve-out travels with the practice" block routes the practice
impulse to the gated Day 6 walker, pattern copied from the fixed M12 page.

Run from anywhere:  python3 _build/gen_atlas.py
Idempotent.  The generator stays in the repo.
"""

import html
import os
import sys

# ----------------------------------------------------------------------------
# Paths — resolve relative to this file so the script runs from any cwd.
# ----------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
V2_ROOT = os.path.dirname(HERE)                      # .../Digital Expand The Box June 2026
ATLAS_DIR = os.path.join(V2_ROOT, "Map Atlas")
MAPS_DIR = os.path.join(V2_ROOT, "Maps")


def esc(s):
    """Escape for safe HTML *text*. Content dicts below intentionally contain
    a small, controlled set of inline tags (<em>, <strong>), so we DON'T escape
    the body strings — they are authored, not user input. esc() is used only
    where a value flows into an attribute or <title>."""
    return html.escape(s, quote=True)


# ----------------------------------------------------------------------------
# The page template. Extracted verbatim from M10's design system (tokens,
# paper-grain, GROUND-NOW, reduced-motion, escapeHtml-free authored content,
# license comment). Placeholders are {NAME}. Literal CSS braces are doubled.
# ----------------------------------------------------------------------------
TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE} · Map Atlas {MNUM} · Expand the Box</title>
<meta name="description" content="{META_DESC}">
<link href="../_assets/fonts/fonts.css" rel="stylesheet">
<style>
/* ============================================================
   MAP ATLAS — shared design system (template for all maps).
   Tokens, paper-grain, GROUND-NOW, reduced-motion and the
   license comment are inherited from the ETB course design system
   (see Map Atlas / M10 - New Map of Feelings.html). Keep in sync.
   ============================================================ */
:root {{
  --ivory: #f4ecdc;
  --ivory-shade: #ece2c8;
  --ivory-deep: #e3d7b9;
  --ink: #0e0a05;
  --ink-soft: #2a221a;
  --ink-mute: #4a3f30;
  --rule: #b8a98a;
  --vermillion: #c43b1c;
  --vermillion-deep: #962a13;
  --vermillion-soft: rgba(196, 59, 28, 0.08);
  --vermillion-glow: rgba(196, 59, 28, 0.32);
  --mustard: #d8b04a;
  --mustard-text: #b8902c;
  --mustard-soft: rgba(216, 176, 74, 0.18);
  --sky: #4a6b7c;
  --display: 'Fraunces', 'EB Garamond', Georgia, serif;
  --body: 'EB Garamond', Georgia, serif;
  --mono: 'JetBrains Mono', 'Courier New', monospace;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: var(--body);
  background: var(--ivory);
  color: var(--ink);
  font-size: 18px;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
  position: relative;
  background-image:
    radial-gradient(ellipse at top left, rgba(216, 176, 74, 0.06) 0%, transparent 40%),
    radial-gradient(ellipse at bottom right, rgba(196, 59, 28, 0.04) 0%, transparent 50%);
}}
body::before {{
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 1;
  opacity: 0.5;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.055 0 0 0 0 0.04 0 0 0 0 0.02 0 0 0 0.18 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}}
a.skip-link {{
  position: absolute; left: -9999px; top: 8px; z-index: 200;
  background: var(--ink); color: var(--ivory); font-family: var(--mono);
  font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase;
  padding: 12px 18px; text-decoration: none;
}}
a.skip-link:focus {{ left: 8px; }}
.wrap {{ max-width: 1100px; margin: 0 auto; padding: 36px 48px 80px; position: relative; z-index: 2; }}

/* HEADER BAR */
header.top {{
  display: flex; justify-content: space-between; align-items: baseline;
  font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--ink-mute);
  padding-bottom: 32px; border-bottom: 1px solid var(--rule); gap: 24px;
}}
header.top .left {{ display: flex; gap: 24px; flex-wrap: wrap; align-items: baseline; }}
header.top .right {{ display: flex; gap: 22px; flex-wrap: wrap; align-items: baseline; }}
header.top .num {{ color: var(--vermillion); font-weight: 500; }}
header.top .brand {{ color: var(--ink-mute); }}
header.top a {{
  color: var(--ink-mute); text-decoration: none;
  border-bottom: 1px solid transparent; padding-bottom: 2px; transition: all 0.2s;
}}
header.top a:hover {{ color: var(--vermillion); border-bottom-color: var(--vermillion); }}
header.top a:focus-visible {{ outline: 2px solid var(--vermillion); outline-offset: 3px; }}

/* HERO */
.hero {{ margin: 48px 0 24px; max-width: 920px; }}
.eyebrow {{
  font-family: var(--mono); font-size: 11px; letter-spacing: 0.22em;
  text-transform: uppercase; color: var(--vermillion); margin-bottom: 16px;
}}
h1.display {{
  font-family: var(--display); font-weight: 350;
  font-size: clamp(44px, 6.5vw, 84px);
  font-variation-settings: 'opsz' 144, 'SOFT' 50, 'WONK' 1;
  line-height: 0.98; letter-spacing: -0.025em; margin-bottom: 22px;
}}
h1.display em {{
  font-style: italic;
  font-variation-settings: 'opsz' 144, 'SOFT' 100, 'WONK' 1;
  color: var(--vermillion);
}}
.lede {{
  font-family: var(--body); font-size: 21px; line-height: 1.5;
  color: var(--ink-soft); max-width: 760px; font-style: italic;
}}

/* MAP FIGURE */
figure.map-figure {{
  margin: 56px 0 16px; padding: 28px; background: var(--ivory-shade);
  border: 1px solid var(--rule); border-top: 3px solid var(--vermillion);
  text-align: center;
}}
figure.map-figure a.map-link {{ display: block; position: relative; text-decoration: none; cursor: zoom-in; }}
figure.map-figure a.map-link:focus-visible {{ outline: 3px solid var(--vermillion); outline-offset: 4px; }}
figure.map-figure img {{
  width: 100%; max-width: 720px; height: auto; margin: 0 auto; display: block;
  border: 1px solid var(--rule); background: var(--ivory);
  box-shadow: 0 14px 40px rgba(14, 10, 5, 0.16);
  transition: transform 0.3s cubic-bezier(0.2, 0.7, 0.2, 1), box-shadow 0.3s;
}}
figure.map-figure a.map-link:hover img {{ transform: translateY(-3px); box-shadow: 0 20px 50px rgba(14, 10, 5, 0.22); }}
figure.map-figure figcaption {{
  font-family: var(--mono); font-size: 11px; letter-spacing: 0.16em;
  text-transform: uppercase; color: var(--ink-mute); margin-top: 20px;
}}
figure.map-figure figcaption .zoom-hint {{ color: var(--vermillion); }}

/* SECTION FRAME */
.section {{ margin-top: 56px; padding: 48px 52px; background: var(--ivory-shade); border-top: 3px solid var(--vermillion); }}
.section .section-label {{
  font-family: var(--mono); font-size: 11px; letter-spacing: 0.22em;
  text-transform: uppercase; color: var(--vermillion); margin-bottom: 14px;
}}
.section h2 {{
  font-family: var(--display); font-weight: 400;
  font-size: clamp(28px, 3.4vw, 40px);
  font-variation-settings: 'opsz' 144, 'SOFT' 50, 'WONK' 1;
  line-height: 1.05; letter-spacing: -0.015em; margin-bottom: 18px; color: var(--ink);
}}
.section h2 em {{ font-style: italic; font-variation-settings: 'opsz' 144, 'SOFT' 100, 'WONK' 1; color: var(--vermillion); }}
.section .prose {{ font-family: var(--body); font-size: 19px; line-height: 1.6; color: var(--ink-soft); max-width: 760px; }}
.section .prose p {{ margin-bottom: 16px; }}
.section .prose p:last-child {{ margin-bottom: 0; }}
.section .prose em {{ color: var(--ink); font-style: italic; }}
.section .prose strong {{ color: var(--ink); font-weight: 600; }}
.section .prose .emph {{
  font-family: var(--display); font-style: italic;
  font-variation-settings: 'opsz' 144, 'SOFT' 100, 'WONK' 1;
  color: var(--vermillion); font-weight: 400;
}}

/* STEPPER (distinctions) */
.stepper-head {{ display: flex; justify-content: space-between; align-items: baseline; gap: 16px; margin: 28px 0 6px; flex-wrap: wrap; }}
.stepper-count {{ font-family: var(--mono); font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink-mute); }}
.stepper-count .now {{ color: var(--vermillion); font-weight: 700; }}
.progress {{ display: flex; gap: 4px; margin: 8px 0 22px; }}
.progress .seg {{ flex: 1; height: 3px; background: var(--rule); transition: background 0.2s; }}
.progress .seg.done {{ background: var(--mustard); }}
.progress .seg.current {{ background: var(--vermillion); }}
.step-card {{
  background: var(--ivory); border: 1.5px solid var(--ink-mute);
  border-left: 4px solid var(--vermillion); padding: 34px 38px; min-height: 200px;
  animation: rise 0.4s cubic-bezier(0.2, 0.7, 0.2, 1);
}}
.step-card[hidden] {{ display: none; }}
.step-card .sc-kicker {{ font-family: var(--mono); font-size: 10px; letter-spacing: 0.22em; text-transform: uppercase; color: var(--mustard-text); font-weight: 600; margin-bottom: 10px; }}
.step-card .sc-name {{
  font-family: var(--display); font-weight: 400; font-style: italic;
  font-size: clamp(28px, 3.6vw, 42px);
  font-variation-settings: 'opsz' 144, 'SOFT' 100, 'WONK' 1;
  line-height: 1.05; color: var(--vermillion); margin-bottom: 16px;
}}
.step-card .sc-body {{ font-family: var(--body); font-size: 19px; line-height: 1.6; color: var(--ink-soft); }}
.step-card .sc-body em {{ color: var(--ink); font-style: italic; }}
.step-card .sc-body strong {{ color: var(--ink); font-weight: 600; }}
.step-card .sc-rows {{ margin-top: 6px; }}
.step-card .sc-row {{
  display: grid; grid-template-columns: 120px 1fr; gap: 16px; padding: 10px 0;
  border-top: 1px dashed var(--rule); font-size: 17px; line-height: 1.5;
}}
.step-card .sc-row:first-child {{ border-top: none; }}
.step-card .sc-row .lbl {{ font-family: var(--mono); font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink-mute); font-weight: 600; padding-top: 4px; }}
.step-card .sc-row .val {{ color: var(--ink-soft); }}
.step-card .sc-row .val.shadow {{ font-family: var(--display); font-style: italic; font-variation-settings: 'opsz' 144, 'SOFT' 100; color: var(--ink-mute); }}
@keyframes rise {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: translateY(0); }} }}

/* RECALL DECK + FLIP CARDS */
.flip-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; margin-top: 26px; }}
@media (max-width: 760px) {{ .flip-grid {{ grid-template-columns: 1fr; }} }}
.flip {{ background: transparent; perspective: 1400px; min-height: 230px; cursor: pointer; border: none; padding: 0; text-align: left; font: inherit; display: block; width: 100%; }}
.flip:focus-visible {{ outline: 2px solid var(--vermillion); outline-offset: 4px; }}
.flip-inner {{ position: relative; width: 100%; min-height: 230px; height: 100%; transition: transform 0.55s cubic-bezier(0.2, 0.7, 0.2, 1); transform-style: preserve-3d; }}
.flip[aria-pressed="true"] .flip-inner {{ transform: rotateY(180deg); }}
.flip-face {{ position: absolute; inset: 0; -webkit-backface-visibility: hidden; backface-visibility: hidden; padding: 26px 28px; display: flex; flex-direction: column; justify-content: flex-start; }}
.flip-face .fc-tag {{ font-family: var(--mono); font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase; font-weight: 700; margin-bottom: 12px; }}
.flip-face .fc-text {{ font-family: var(--display); font-weight: 400; font-size: 21px; font-variation-settings: 'opsz' 144, 'SOFT' 60, 'WONK' 1; line-height: 1.3; }}
.flip-face .fc-hint {{ margin-top: auto; padding-top: 16px; font-family: var(--mono); font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase; }}
.flip-front {{ background: var(--ivory); border: 1.5px solid var(--ink-mute); }}
.flip-front .fc-tag {{ color: var(--ink-mute); }}
.flip-front .fc-tag::before {{ content: '?  '; color: var(--mustard-text); }}
.flip-front .fc-text {{ color: var(--ink); font-style: italic; }}
.flip-front .fc-hint {{ color: var(--ink-mute); }}
.flip-back {{ background: var(--ink); border: 1.5px solid var(--ink); transform: rotateY(180deg); }}
.flip-back .fc-tag {{ color: var(--mustard); }}
.flip-back .fc-tag::before {{ content: '\2192  '; color: var(--mustard); }}
.flip-back .fc-text {{ color: var(--ivory); }}
.flip-back .fc-text em {{ color: var(--mustard); font-style: italic; }}
.flip-back .fc-hint {{ color: rgba(244, 236, 220, 0.5); }}

/* MISUNDERSTANDINGS — wrong/right flip cards (✗ / ✓) */
.flip-mis .flip-front .fc-tag::before {{ content: '\2717  '; color: var(--ink-mute); }}
.flip-mis .flip-back .fc-tag::before {{ content: '\2713  '; color: var(--mustard); }}

/* SAFETY ROUTING (EHP study-level maps) */
.practice-meta {{ font-family: var(--mono); font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--ink-mute); margin: 22px 0 8px; }}
.practice-closer {{
  margin-top: 24px; padding: 22px 26px; background: var(--ivory);
  border-left: 3px solid var(--vermillion); font-family: var(--display);
  font-style: italic; font-variation-settings: 'opsz' 144, 'SOFT' 100;
  font-size: 18px; line-height: 1.5; color: var(--ink);
}}
.practice-capture {{ margin-top: 24px; display: flex; gap: 14px; align-items: center; flex-wrap: wrap; }}
.capture-state {{ font-family: var(--mono); font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--mustard-text); }}

/* REFLECTION */
.reflect-label {{ display: block; font-family: var(--mono); font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink-mute); margin: 22px 0 12px; }}
textarea.reflect {{
  width: 100%; padding: 22px 26px; font-family: var(--display); font-style: italic;
  font-size: 21px; font-variation-settings: 'opsz' 144, 'SOFT' 100;
  background: var(--ivory); color: var(--ink); border: 1.5px solid var(--rule);
  resize: vertical; min-height: 120px; line-height: 1.45; display: block;
}}
textarea.reflect:focus {{ outline: none; border-color: var(--vermillion); }}
.reflect-row {{ display: flex; gap: 14px; margin-top: 16px; align-items: center; flex-wrap: wrap; }}
.reflect-saved {{ font-family: var(--mono); font-size: 10px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--mustard-text); }}
.privacy-note {{ margin-top: 18px; font-family: var(--mono); font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--ink-mute); }}
.prior-entry {{
  margin-top: 18px; padding: 18px 22px; background: var(--ivory);
  border-left: 3px solid var(--mustard); font-family: var(--display); font-style: italic;
  font-variation-settings: 'opsz' 144, 'SOFT' 100; font-size: 17px; line-height: 1.5; color: var(--ink-soft);
}}
.prior-entry[hidden] {{ display: none; }}
.prior-entry .pe-label {{ font-family: var(--mono); font-style: normal; font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink-mute); display: block; margin-bottom: 8px; }}

/* BUTTONS */
.btn {{
  font-family: var(--mono); font-size: 11px; font-weight: 500; letter-spacing: 0.18em;
  text-transform: uppercase; padding: 13px 24px; background: transparent; color: var(--ink);
  border: 1.5px solid var(--ink); cursor: pointer; transition: all 0.2s; text-decoration: none;
  display: inline-flex; align-items: center; gap: 8px;
}}
.btn:hover {{ background: var(--ink); color: var(--ivory); }}
.btn:focus-visible {{ outline: 2px solid var(--vermillion); outline-offset: 3px; }}
.btn.primary {{ background: var(--vermillion); border-color: var(--vermillion); color: var(--ivory); }}
.btn.primary:hover {{ background: var(--vermillion-deep); border-color: var(--vermillion-deep); }}
.btn.ghost {{ border-color: var(--ink-mute); color: var(--ink-mute); }}
.btn.ghost:hover {{ background: transparent; color: var(--ink); border-color: var(--ink); }}
.btn[disabled] {{ opacity: 0.35; cursor: not-allowed; }}
.btn[disabled]:hover {{ background: transparent; color: var(--ink); }}

/* FOOTER */
footer.bottom {{ margin-top: 72px; padding-top: 32px; border-top: 1px solid var(--rule); }}
footer.bottom .nav-row {{ display: flex; justify-content: space-between; flex-wrap: wrap; gap: 16px; font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-mute); }}
footer.bottom .nav-row a {{ color: var(--ink-mute); text-decoration: none; border-bottom: 1px solid transparent; padding-bottom: 2px; transition: all 0.2s; }}
footer.bottom .nav-row a:hover {{ color: var(--vermillion); border-bottom-color: var(--vermillion); }}
footer.bottom .nav-row a:focus-visible {{ outline: 2px solid var(--vermillion); outline-offset: 3px; }}
footer.bottom .license {{ margin-top: 26px; font-family: var(--mono); font-size: 10px; line-height: 1.7; letter-spacing: 0.04em; color: var(--ink-mute); max-width: 860px; }}
footer.bottom .license a {{ color: var(--ink-mute); text-decoration: underline; }}
footer.bottom .license a:hover {{ color: var(--vermillion); }}
footer.bottom .license .cc {{ color: var(--ink-soft); font-weight: 600; letter-spacing: 0.06em; }}

/* GROUND NOW */
.ground-now {{
  position: fixed; top: 24px; right: 24px; z-index: 50; background: var(--vermillion);
  color: var(--ivory); border: 2px solid var(--vermillion-deep); font-family: var(--mono);
  font-size: 12px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase;
  padding: 16px 22px; cursor: pointer; box-shadow: 0 8px 24px rgba(196, 59, 28, 0.28);
  transition: all 0.25s ease; line-height: 1.1;
}}
.ground-now:hover {{ background: var(--vermillion-deep); transform: translateY(-1px); box-shadow: 0 10px 28px rgba(196, 59, 28, 0.36); }}
.ground-now:focus-visible {{ outline: 2px solid var(--ink); outline-offset: 3px; }}
.ground-now .small {{ display: block; font-size: 9px; letter-spacing: 0.18em; font-weight: 500; opacity: 0.85; margin-top: 3px; }}

/* GROUNDING MODAL */
.modal {{ display: none; position: fixed; inset: 0; z-index: 100; background: rgba(14, 10, 5, 0.86); align-items: center; justify-content: center; padding: 32px; }}
.modal.show {{ display: flex; }}
.modal-inner {{ max-width: 620px; width: 100%; background: var(--ivory); border: 2px solid var(--vermillion); padding: 44px 40px 36px; position: relative; max-height: 90vh; overflow-y: auto; }}
.modal-inner::before {{ content: 'GROUNDING · 60 SECONDS'; position: absolute; top: -12px; left: 28px; background: var(--vermillion); color: var(--ivory); padding: 5px 14px; font-family: var(--mono); font-size: 11px; letter-spacing: 0.22em; font-weight: 600; }}
.modal-inner h2 {{ font-family: var(--display); font-style: italic; font-weight: 400; font-size: 32px; font-variation-settings: 'opsz' 144, 'SOFT' 100, 'WONK' 1; margin-bottom: 18px; color: var(--ink); }}
.modal-inner h2 em {{ font-style: italic; color: var(--vermillion); }}
.modal-inner ol {{ margin: 0 0 22px 22px; font-size: 18px; line-height: 1.55; color: var(--ink-soft); }}
.modal-inner ol li {{ margin-bottom: 12px; }}
.modal-inner ol li strong {{ color: var(--ink); }}
.modal-inner .session-paused {{ font-family: var(--mono); font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink-mute); margin-top: 10px; }}
.modal-inner .modal-actions {{ display: flex; gap: 14px; flex-wrap: wrap; margin-top: 26px; }}

@media (max-width: 760px) {{
  .wrap {{ padding: 24px 20px 60px; }}
  .section {{ padding: 32px 26px; }}
  .step-card {{ padding: 28px 24px; }}
  .ground-now {{ top: 16px; right: 16px; padding: 12px 16px; font-size: 11px; }}
  .modal-inner {{ padding: 36px 24px 28px; }}
  .step-card .sc-row {{ grid-template-columns: 1fr; gap: 4px; }}
}}

@media (prefers-reduced-motion: reduce){{
  *,*::before,*::after{{
    animation-duration:.001ms!important; animation-iteration-count:1!important;
    transition-duration:.001ms!important; scroll-behavior:auto!important;
  }}
  .flip[aria-pressed="true"] .flip-inner {{ transition: none; }}
}}
</style>
</head>
<body>

<a href="#main" class="skip-link">Skip to map</a>

<!-- floating safety button — always available; map study can engage the emotional body -->
<button class="ground-now" id="groundNowBtn" type="button" onclick="openGround()" aria-haspopup="dialog">
  GROUND NOW
  <span class="small">60-second pause</span>
</button>

<div class="wrap">

  <!-- 1 · HEADER BAR -->
  <header class="top">
    <div class="left">
      <span><span class="num">MAP ATLAS · {MNUM}</span></span>
      <span class="brand">Possibility Management</span>
    </div>
    <div class="right">
      <a href="index.html">← All maps</a>
      <a href="{DAY_HREF}">Taught in {DAY_LABEL} →</a>
    </div>
  </header>

  <!-- 2 · HERO -->
  <section class="hero" id="main">
    <div class="eyebrow">Study the map · {EYEBROW}</div>
    <h1 class="display">{H1}</h1>
    <p class="lede">{LEDE}</p>
  </section>

  <!-- 3 · THE MAP -->
  <figure class="map-figure">
    <a class="map-link" href="../Maps/{MNUM}.png" target="_blank" rel="noopener" aria-label="Open the full-size {TITLE_ATTR} in a new tab">
      <img src="../Maps/{MNUM}.png" alt="{IMG_ALT}">
    </a>
    <figcaption>{TITLE} · <span class="zoom-hint">click the map to open full-size →</span></figcaption>
  </figure>

  <!-- 4 · WHAT THIS MAP SHOWS -->
  <section class="section" aria-labelledby="shows-h">
    <div class="section-label">What this map shows</div>
    <h2 id="shows-h">{SHOWS_H}</h2>
    <div class="prose">{SHOWS_PROSE}</div>
  </section>

  <!-- 5 · WALK THE DISTINCTIONS (stepper) -->
  <section class="section" aria-labelledby="walk-h">
    <div class="section-label">Key distinctions</div>
    <h2 id="walk-h">Take them <em>one at a time.</em></h2>
    <p class="prose">Step through the load-bearing distinctions this map draws. Move at the pace of your body, not your reading speed.</p>

    <div class="stepper-head">
      <div class="stepper-count">Distinction <span class="now" id="stepNow">1</span> of <span id="stepTotal">{STEP_TOTAL}</span></div>
    </div>
    <div class="progress" id="stepProgress" aria-hidden="true"></div>

    <div id="stepRegion" aria-live="polite"></div>

    <div class="quote-tools" style="margin-top: 22px; display:flex; gap:14px; flex-wrap:wrap;">
      <button class="btn ghost" id="stepPrev" type="button" onclick="stepBy(-1)" disabled>← Prev</button>
      <button class="btn primary" id="stepNext" type="button" onclick="stepBy(1)">Next →</button>
    </div>
  </section>

  <!-- 6 · RECALL DECK (generate-then-flip) -->
  <section class="section" aria-labelledby="recall-h">
    <div class="section-label">Recall deck · generate, then flip</div>
    <h2 id="recall-h">Answer it <em>first.</em> Then turn the card.</h2>
    <p class="prose">Each card asks one question this map answers. Say your answer out loud before you flip — generating the answer yourself is what files it. Click a card, or focus it and press Enter or Space, to turn it over. No score is kept.</p>
    <div class="flip-grid" id="recallGrid"></div>
  </section>

  <!-- 7 · COMMON MISUNDERSTANDINGS -->
  <section class="section" aria-labelledby="mis-h">
    <div class="section-label">Common misunderstandings</div>
    <h2 id="mis-h">Each card shows the <em>wrong</em> belief. Flip it for the correction.</h2>
    <p class="prose">Click a card — or focus it and press Enter or Space — to turn it over.</p>
    <div class="flip-grid" id="misGrid"></div>
  </section>

  {PRACTICE_SECTION}

  <!-- 9 · REFLECTION CAPTURE -->
  <section class="section" aria-labelledby="reflect-h">
    <div class="section-label">Reflection</div>
    <h2 id="reflect-h">What <em>landed?</em></h2>
    <p class="prose">{REFLECT_PROMPT}</p>

    <div class="prior-entry" id="priorEntry" hidden>
      <span class="pe-label">Your last reflection · this device</span>
      <span id="priorEntryText"></span>
    </div>

    <label class="reflect-label" for="reflectInput">Your reflection on {TITLE}</label>
    <textarea class="reflect" id="reflectInput" aria-label="Your reflection on {TITLE_ATTR} — what landed for you" placeholder="What landed…"></textarea>
    <div class="reflect-row">
      <button class="btn primary" type="button" onclick="saveReflection()">Save reflection</button>
      <button class="btn ghost" type="button" onclick="clearReflection()">Clear</button>
      <span class="reflect-saved" id="reflectSaved" role="status"></span>
    </div>
    <p class="privacy-note">Saved on this device only, in your browser (localStorage). Nothing is uploaded. No accounts, no telemetry, no external calls except the web-font request.</p>
  </section>

  <!-- 10 · FOOTER -->
  <footer class="bottom">
    <div class="nav-row">
      <a href="index.html">← All maps · Map Atlas</a>
      <a href="{DAY_HREF}">Taught in {DAY_LABEL} →</a>
    </div>
    <p class="license">
      <span class="cc">🄯 World Copyleft 2026 · Expand the Box (Digital).</span>
      Licensed <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener">CC BY-SA 4.0</a>.
      Re-presents Possibility Management thoughtware originated by Clinton Callahan &amp; the Possibility Management community. Please share, share-alike.
      Powered by Possibility Management — <a href="https://possibilitymanagement.org" target="_blank" rel="noopener">possibilitymanagement.org</a>.
      Full terms: <code>LICENSE.md</code> in the course root. This Atlas page is consistent with the spirit of World Copyleft; it is not an official Possibility Management product.
    </p>
  </footer>
</div>

<!-- modal: grounding (60-second sequence) -->
<div class="modal" id="groundModal" role="dialog" aria-modal="true" aria-labelledby="groundModalTitle">
  <div class="modal-inner">
    <h2 id="groundModalTitle">Ground. <em>Now.</em></h2>
    <ol>
      <li><strong>Stop.</strong> Stand up — both feet flat on the floor. Feel the contact.</li>
      <li><strong>Breathe out, longer than in</strong> — three slow exhales.</li>
      <li><strong>Name three things you can see</strong> in this room. Out loud is best.</li>
      <li><strong>Name one thing you can hear.</strong> The fridge. Traffic. Your own breath.</li>
      <li><strong>One hand on your sternum, one on your belly.</strong> Notice your body is here.</li>
      <li><strong>Then decide:</strong> continue, pause 10 minutes, or stop for today. Any of the three is fine.</li>
    </ol>
    <p class="session-paused">Take as long as you need.</p>
    <div class="modal-actions">
      <button class="btn primary" type="button" onclick="closeGround()">I'm grounded — continue</button>
      <a href="index.html" class="btn ghost">Stop — return to the Atlas</a>
    </div>
  </div>
</div>

<script>
/* ============================================================
   {MNUM} — {TITLE}. Teaching content sourced from the v2 module
   ({DAY_LABEL}) and the canonical-phrasing ledger (Voice and Style
   Guide §6). Local-only: the single localStorage key {STORE_KEY}.
   ============================================================ */

const DISTINCTIONS = {DISTINCTIONS_JSON};
const RECALL = {RECALL_JSON};
const MISUNDERSTANDINGS = {MIS_JSON};
const STORE_KEY = '{STORE_KEY}';

function kb(e, fn) {{
  if (e.key === 'Enter' || e.key === ' ' || e.key === 'Spacebar') {{ e.preventDefault(); fn(); }}
}}

/* ---- STEPPER ---- */
let stepIndex = 0;
function buildProgress() {{
  const p = document.getElementById('stepProgress');
  p.innerHTML = DISTINCTIONS.map(() => '<div class="seg"></div>').join('');
  document.getElementById('stepTotal').textContent = DISTINCTIONS.length;
}}
function renderStep(focusCard) {{
  const d = DISTINCTIONS[stepIndex];
  const region = document.getElementById('stepRegion');
  let inner = '<div class="sc-kicker">' + d.kicker + '</div><div class="sc-name">' + d.name + '</div>';
  if (d.rows) {{
    inner += '<div class="sc-rows">';
    for (const row of d.rows) {{
      const shadow = (row[0] === 'Shadow') ? ' shadow' : '';
      inner += '<div class="sc-row"><div class="lbl">' + row[0] + '</div><div class="val' + shadow + '">' + row[1] + '</div></div>';
    }}
    inner += '</div>';
  }} else {{
    inner += '<div class="sc-body">' + d.body + '</div>';
  }}
  region.innerHTML = '<article class="step-card" id="stepCard" tabindex="-1" aria-label="' + d.name.replace(/<[^>]*>/g, '') + '">' + inner + '</article>';
  document.getElementById('stepNow').textContent = stepIndex + 1;
  document.querySelectorAll('#stepProgress .seg').forEach((s, i) => {{
    s.classList.remove('done', 'current');
    if (i < stepIndex) s.classList.add('done');
    else if (i === stepIndex) s.classList.add('current');
  }});
  document.getElementById('stepPrev').disabled = stepIndex === 0;
  document.getElementById('stepNext').disabled = stepIndex === DISTINCTIONS.length - 1;
  if (focusCard) {{ const card = document.getElementById('stepCard'); if (card) card.focus({{ preventScroll: true }}); }}
}}
function stepBy(delta) {{
  const next = stepIndex + delta;
  if (next < 0 || next >= DISTINCTIONS.length) return;
  stepIndex = next; renderStep(true);
}}

/* ---- RECALL DECK ---- */
function buildRecall() {{
  const grid = document.getElementById('recallGrid');
  grid.innerHTML = RECALL.map((m, i) => `
    <button class="flip" type="button" id="recall${{i}}" aria-pressed="false"
            aria-label="Recall question ${{i + 1}}: ${{m.q.replace(/<[^>]*>/g, '').replace(/"/g, '')}} — activate to reveal the answer"
            onclick="toggleFlip('recall', ${{i}})" onkeydown="kb(event,()=>toggleFlip('recall', ${{i}}))">
      <div class="flip-inner">
        <div class="flip-face flip-front">
          <div class="fc-tag">Answer it aloud first</div>
          <div class="fc-text">${{m.q}}</div>
          <div class="fc-hint">Flip for the map's answer →</div>
        </div>
        <div class="flip-face flip-back">
          <div class="fc-tag">On this map</div>
          <div class="fc-text">${{m.a}}</div>
          <div class="fc-hint">← Flip back</div>
        </div>
      </div>
    </button>`).join('');
}}

/* ---- MISUNDERSTANDINGS ---- */
function buildMis() {{
  const grid = document.getElementById('misGrid');
  grid.innerHTML = MISUNDERSTANDINGS.map((m, i) => `
    <button class="flip flip-mis" type="button" id="mis${{i}}" aria-pressed="false"
            aria-label="Misunderstanding ${{i + 1}}: ${{m.wrong.replace(/<[^>]*>/g, '').replace(/"/g, '')}} — activate to reveal the correction"
            onclick="toggleFlip('mis', ${{i}})" onkeydown="kb(event,()=>toggleFlip('mis', ${{i}}))">
      <div class="flip-inner">
        <div class="flip-face flip-front">
          <div class="fc-tag">Common belief</div>
          <div class="fc-text">${{m.wrong}}</div>
          <div class="fc-hint">Flip for the correction →</div>
        </div>
        <div class="flip-face flip-back">
          <div class="fc-tag">On this map</div>
          <div class="fc-text">${{m.right}}</div>
          <div class="fc-hint">← Flip back</div>
        </div>
      </div>
    </button>`).join('');
}}

function toggleFlip(prefix, i) {{
  const el = document.getElementById(prefix + i);
  const flipped = el.getAttribute('aria-pressed') === 'true';
  el.setAttribute('aria-pressed', flipped ? 'false' : 'true');
}}

/* ---- REFLECTION + STATE ---- */
function currentData() {{
  let data = {{}};
  try {{ data = JSON.parse(localStorage.getItem(STORE_KEY) || '{{}}'); }} catch (e) {{ data = {{}}; }}
  return data;
}}
function loadState() {{
  const data = currentData();
  if (data.reflection) {{
    document.getElementById('reflectInput').value = data.reflection;
    const prior = document.getElementById('priorEntry');
    document.getElementById('priorEntryText').textContent = data.reflection;
    prior.hidden = false;
    if (data.savedAt) document.getElementById('reflectSaved').textContent = 'Last saved ' + new Date(data.savedAt).toLocaleString();
  }}
}}
function saveReflection() {{
  const val = document.getElementById('reflectInput').value.trim();
  const data = currentData();
  data.reflection = val;
  data.savedAt = new Date().toISOString();
  try {{
    localStorage.setItem(STORE_KEY, JSON.stringify(data));
    document.getElementById('reflectSaved').textContent = val ? 'Saved ✓ · ' + new Date().toLocaleString() : 'Saved (empty) ✓';
    const prior = document.getElementById('priorEntry');
    if (val) {{ document.getElementById('priorEntryText').textContent = val; prior.hidden = false; }}
    else {{ prior.hidden = true; }}
  }} catch (e) {{
    document.getElementById('reflectSaved').textContent = 'Could not save (storage blocked).';
  }}
}}
function clearReflection() {{
  document.getElementById('reflectInput').value = '';
  const data = currentData();
  delete data.reflection; delete data.savedAt;
  try {{ localStorage.setItem(STORE_KEY, JSON.stringify(data)); }} catch (e) {{}}
  document.getElementById('priorEntry').hidden = true;
  document.getElementById('reflectSaved').textContent = 'Cleared.';
}}

/* ---- GROUNDING MODAL ---- */
let _groundReturnFocus = null;
function openGround() {{
  _groundReturnFocus = document.activeElement;
  const modal = document.getElementById('groundModal');
  modal.classList.add('show');
  const firstBtn = modal.querySelector('.modal-actions .btn');
  if (firstBtn) firstBtn.focus();
}}
function closeGround() {{
  document.getElementById('groundModal').classList.remove('show');
  if (_groundReturnFocus && typeof _groundReturnFocus.focus === 'function') _groundReturnFocus.focus();
  _groundReturnFocus = null;
}}
document.addEventListener('keydown', (e) => {{
  if (e.key === 'Escape') {{
    const modal = document.getElementById('groundModal');
    if (modal.classList.contains('show')) closeGround();
  }}
}});

/* ---- INIT ---- */
window.addEventListener('DOMContentLoaded', () => {{
  buildProgress();
  renderStep(false);
  buildRecall();
  buildMis();
  loadState();
}});
</script>

<!-- World Copyleft 2026 — Expand the Box (Digital). Licensed CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/). Re-presents Possibility Management thoughtware originated by Clinton Callahan & the Possibility Management community. Please share, share-alike. Powered by Possibility Management — possibilitymanagement.org. Consistent with the spirit of World Copyleft; not an official Possibility Management product. Full terms: LICENSE.md in the course root. -->
</body>
</html>
"""


# Practice / safety-routing block for the three EHP study-level maps (§B.5).
# No do-it-now steps. Routes the practice impulse to the gated Day 6 walker,
# carrying the trauma carve-out — wording pattern copied from the fixed M12.
EHP_SAFETY_SECTION = """  <!-- 8 · STUDY-LEVEL ONLY — route practice to the gated Day 6 walker -->
  <section class="section" aria-labelledby="embody-h">
    <div class="section-label">Study level only · where the practice lives</div>
    <h2 id="embody-h">This page is a <em>locator,</em> not a walk-through.</h2>
    <p class="prose">{ROUTE_PROSE}</p>
    <div class="practice-meta">Study / locator level · the practice is gated in the Day 6 walker</div>

    <div class="practice-closer" role="note">
      <strong style="font-style:normal;color:var(--vermillion);">The carve-out travels with the practice.</strong>
      The EHP is <strong style="font-style:normal;">not</strong> trauma processing. Trauma needs a professionally held container — a qualified clinician with a trauma-built protocol. If the material is trauma-coded, the walker will tell you to stop, and so does this page. Even a small solo EHP runs <strong style="font-style:normal;">only</strong> through the gated walker, whose consent gate and trauma carve-out are structural, not optional.
    </div>

    <div class="practice-capture">
      <a class="btn primary" href="../Interactive%20Tools/Day%2006/ehp-walker.html">Open the gated EHP walker →</a>
      <span class="capture-state">Day 6 · consent gate + Position 0 required</span>
    </div>
  </section>
"""

# Generic (non-EHP) practice/closer block — a quiet study closer, no scoring,
# no do-it-now embodiment that would duplicate the module's own practice.
STUDY_CLOSER_SECTION = """  <!-- 8 · CARRY IT — quiet study closer -->
  <section class="section" aria-labelledby="embody-h">
    <div class="section-label">Carry it</div>
    <h2 id="embody-h">{CLOSER_H}</h2>
    <p class="prose">{CLOSER_PROSE}</p>
    <div class="practice-meta">{CLOSER_META}</div>
    <div class="practice-capture">
      <a class="btn primary" href="{DAY_HREF}">Run the full practice in {DAY_LABEL} →</a>
      <span class="capture-state">The module carries the embodied practice</span>
    </div>
  </section>
"""


# ----------------------------------------------------------------------------
# Day source map (§B.4) — for header link + footer + "taught in".
# ----------------------------------------------------------------------------
DAY_FILES = {
    "01": "Day 01 - Orientation, New Context, Radical Responsibility.md",
    "03": "Day 03 - Liquid State, Center-Ground-Bubble, Five Bodies.md",
    "05": "Day 05 - Feelings vs Emotions, Old Map of Feelings, Numbness Bar.md",
    "06": "Day 06 - Mixed Emotions and Emotional Healing Process.md",
    "07": "Day 07 - Low Drama, Gremlin Food, Shifting to Responsible Game.md",
    "08": "Day 08 - Listening, Speaking, Communication, Completion Loops.md",
    "10": "Day 10 - Map of Possibility, Bright Principles, Three Powers, Integration.md",
}


def day_href(num):
    # %20-encode for file:// from the Map Atlas dir.
    from urllib.parse import quote
    return "../Days/" + quote(DAY_FILES[num])


def day_label(num):
    return "Day " + num


# ----------------------------------------------------------------------------
# CONTENT — one entry per new map. Authored against the v2 module text and the
# canonical ledger (Voice and Style Guide §6). Inline tags <em>/<strong> only.
# EHP maps (M38/M39/M40) set kind="ehp" -> safety routing block, no practice.
# ----------------------------------------------------------------------------
CONTENT = {

# ===================== M32 — Map of Responsibility and Culture (Day 01) =====================
"M32": {
  "title": "Map of Responsibility and Culture",
  "day": "01",
  "eyebrow": "Radical Responsibility · Day 1",
  "h1": "Responsibility <em>and culture.</em>",
  "lede": "A culture is readable as the distribution of where its people stand on the levels of responsibility — a population curve over child, adolescent, adult, radical.",
  "meta_desc": "Interactive teaching tool for the Possibility Management Map of Responsibility and Culture — a culture read as the distribution of where its people stand on the levels of responsibility.",
  "img_alt": "The Map of Responsibility and Culture: a population curve plotted over the levels of responsibility — child and adolescent on the left under a tall hump labelled mainstream modern culture, with a long thin tail toward adult and radical labelled culture creatives.",
  "shows_h": "A culture is <em>a distribution,</em> not a flag.",
  "shows_prose": (
    "<p>This map plots a population curve over the same levels you just learned: number of people on the vertical axis, <em>child</em> through <em>radical</em> on the horizontal. The tall hump sits over child and adolescent. That hump is labelled <strong>mainstream modern culture.</strong> The long thin tail toward radical is labelled <strong>culture creatives</strong> — the people sourcing next cultures.</p>"
    "<p>Read what the curve claims: <strong>a culture is readable as the distribution of where its people stand on responsibility.</strong> The culture most of us were raised in clusters where responsibility means burden, blame, and \"avoid as much as I can get away with.\" The old map of responsibility on the left — drudgery, no choice, guilt, compliance, responsibility confused with financial security. The new map on the right — responsibility as <span class=\"emph\">consciousness in action,</span> being at source, authoring the life you want.</p>"
    "<p>None of this is an insult to anyone. It is a structural reading of where the curve currently piles up — and a map of which way it can move, one person at a time.</p>"
  ),
  "distinctions": [
    {"kicker": "Level 1", "name": "Child", "rows": [
      ["Stance", "Someone else is responsible. The frame is given; I live inside it."],
      ["Produces", "Blame, guilt, suffering — the map files these here on purpose."],
      ["Sentence", "<em>\"It's not my fault. Look what they did to me.\"</em>"]]},
    {"kicker": "Level 2", "name": "Adolescent", "rows": [
      ["Stance", "Rebellion against an unfair authority. The frame is still intact; I have flipped my sign."],
      ["Note", "The one most often mistaken for maturity. You are still organised <em>around</em> the authority you defy."],
      ["Sentence", "<em>\"Watch me — I'll do the opposite.\"</em>"]]},
    {"kicker": "Level 3", "name": "Adult", "rows": [
      ["Stance", "I do my share. My ability to create results; I keep my agreements."],
      ["Note", "Clean, necessary, the floor for this work — and still doing your part inside a situation someone else is framing."],
      ["Sentence", "<em>\"I'll do my part. Here's what I can commit to.\"</em>"]]},
    {"kicker": "Level 4", "name": "Radical", "rows": [
      ["Stance", "I am at cause. I am the author of what this becomes next."],
      ["Note", "Consciousness in action. <strong>Not</strong> \"I caused it\" and <strong>not</strong> \"it's my fault\" — that reading is blame, back at child level."],
      ["Sentence", "<em>\"I am here. I will create what is needed.\"</em>"]]},
    {"kicker": "The reading", "name": "Culture is downstream.",
      "body": "A culture is the <em>accumulated distribution</em> of where its people stand. It changes only as individual people change which level they author from. The work is personal before it is political: <strong>you move the curve by moving where you stand.</strong>"},
  ],
  "recall": [
    {"q": "What, on this map, <em>is</em> a culture?", "a": "The distribution of where its people stand on the levels of responsibility — a population curve, not an opinion poll or a flag."},
    {"q": "Where does the tall hump sit, and what is it labelled?", "a": "Over <em>child and adolescent</em> — labelled mainstream modern culture. The thin tail toward radical is the culture creatives."},
    {"q": "Name the four levels in order.", "a": "Child · adolescent · adult · radical. Child produces blame and suffering; radical is consciousness in action."},
    {"q": "Why is adolescent mistaken for maturity?", "a": "Rebellion <em>feels</em> like a stand, but you are still organised around the authority you defy. The frame is intact; you have flipped your sign, not authored a new one."},
    {"q": "Does radical responsibility mean \"it's all my fault\"?", "a": "No. Blame and fault are <em>child-level.</em> Radical is being at cause for what you do next — author of the next move, not of your past or conditioning."},
    {"q": "How does a culture actually change?", "a": "One person at a time, by changing which level they author from. The curve is the sum of individual stances; there is no other lever."},
  ],
  "mis": [
    {"wrong": "\"A culture is its values, its flag, its slogans.\"", "right": "On this map a culture is the <em>distribution</em> of where its people actually stand on responsibility. What people source from, accumulated — not what they profess."},
    {"wrong": "\"Radical responsibility means everything bad that happened is my fault.\"", "right": "Blame and fault are <em>child-level</em>; the map files them there on purpose. Radical responsibility is being at cause for your next move — not the author of your conditioning or your trauma."},
    {"wrong": "\"Getting to Adult is the goal — 'I do my share' and you've arrived.\"", "right": "Adult is the clean floor for this work. The course operates from <em>radical:</em> at cause for the whole field you stand in, not just your part inside someone else's frame."},
    {"wrong": "\"Being on the left of the curve makes someone a worse person.\"", "right": "The map is a structural reading, not a moral ranking. It describes where the curve piles up and which way it can move — not anyone's worth."},
  ],
  "closer_h": "Read your own culture <em>off the curve.</em>",
  "closer_prose": "Hold this map next to the levels you learned and ask: where does the culture I was raised in pile up, and where on the curve was I standing in my last hard conversation? The Day 1 four-level practice runs that sentence through your body, one level at a time.",
  "closer_meta": "Solo · the four-level sentence · Day 1 module",
  "reflect_prompt": "One or two lines. Where does the culture you were raised in sit on this curve? Where were you standing in your last charged conversation — and what becomes available from radical that was invisible from child?",
},

# ===================== M33 — Feelings vs Emotions (Day 05) =====================
"M33": {
  "title": "Feelings vs Emotions",
  "day": "05",
  "eyebrow": "The Emotional Body · Day 5",
  "h1": "Feelings <em>vs</em> emotions.",
  "lede": "Two panels, same four names. Feelings originate in the present and last three to five minutes; emotions originate in the past, last longer, and arrive mixed. Feelings are for creating, now; emotions are for healing.",
  "meta_desc": "Interactive teaching tool for the Possibility Management Feelings vs Emotions map — present-time clean feelings versus past-time mixed emotions, and the 5-minute test that tells them apart.",
  "img_alt": "The Feelings vs Emotions map: two stacked panels with the same four names — anger, sadness, fear, joy. The top panel marks feelings as present-time, lasting three to five minutes, for creating now. The bottom panel marks emotions as past-time, lasting longer than five minutes, arriving mixed, for healing.",
  "shows_h": "The whole module hangs on <em>this split.</em>",
  "shows_prose": (
    "<p>Two panels, top and bottom, same four names in each: anger, sadness, fear, joy. The top panel says feelings originate in the <strong>present</strong> and last three to five minutes at most. The bottom panel says emotions originate in the <strong>past,</strong> last longer than five minutes, and arrive mixed. Each panel ends by naming what that class is <em>for</em>: feelings are for <span class=\"emph\">creating, in the now;</span> emotions are for <span class=\"emph\">healing.</span></p>"
    "<p>A <strong>feeling</strong> is present-time, one of four, short, informational, and clean — no story, no \"because you always.\" An <strong>emotion</strong> is a feeling that arose earlier, was not allowed to move, and got stored; it runs on autopilot, mixes, comes with a story, and repeats instead of acting. An emotion often carries the voice of an external authority — the person or rule that blocked the feeling the first time.</p>"
    "<p>Confusing the two has a large blast radius. You feel an emotion of anger toward your partner, mistake it for a present-time feeling, \"express\" it as if it were information about them, and create damage. The anger was about the third-grade teacher. The partner was the trigger, not the source.</p>"
  ),
  "distinctions": [
    {"kicker": "Distinction 1", "name": "Time of origin", "rows": [
      ["Feeling", "Present-time. It arises because of something happening <em>right now.</em>"],
      ["Emotion", "Past-time. A feeling from earlier — a year ago, twenty years ago, childhood — that was not allowed to move."]]},
    {"kicker": "Distinction 2", "name": "Duration", "rows": [
      ["Feeling", "Three to five minutes at full intensity, then it passes."],
      ["Emotion", "Longer than five minutes — often years. It repeats rather than completes."]]},
    {"kicker": "Distinction 3", "name": "Composition", "rows": [
      ["Feeling", "Clean. One of the four. No story, no interpretation."],
      ["Emotion", "Mixed. Two or three feelings tangled with a memory and a story."]]},
    {"kicker": "Distinction 4", "name": "Purpose", "rows": [
      ["Feeling", "For <em>creating,</em> in the now. It tells you what you care about and what to do next."],
      ["Emotion", "For <em>healing.</em> It is asking to be completed, not acted out at whoever is present."]]},
    {"kicker": "The field test", "name": "The 5-minute test.",
      "body": "<strong>How long has this been going on?</strong> If five minutes later you are still in it, you are in an emotion — the feeling underneath, if there ever was one, has been replaced by the emotional loop on top. The test is observable; your opinion of yourself is not."},
  ],
  "recall": [
    {"q": "Where does a <em>feeling</em> originate, and how long does it last?", "a": "In the present, because of something happening now. Three to five minutes at full intensity, then it passes."},
    {"q": "Where does an <em>emotion</em> originate?", "a": "In the past. A feeling that arose earlier, was not allowed to move, got stored, and now runs on autopilot — longer than five minutes, mixed, with a story."},
    {"q": "What is each class <em>for?</em>", "a": "Feelings are for creating, in the now. Emotions are for healing — completing the stored thing, not acting it out."},
    {"q": "State the 5-minute test.", "a": "How long has this been going on? Still happening after five minutes? You are in an emotion, not a clean feeling."},
    {"q": "Why is confusing the two costly?", "a": "You express a stored emotion onto a present-day person as if it were information about them — and create damage. The trigger is not the source."},
    {"q": "Does an emotion ever carry someone else's voice?", "a": "Often. An emotion frequently carries the voice of an <em>external authority</em> — the person or rule that blocked the feeling the first time it arose."},
  ],
  "mis": [
    {"wrong": "\"Feeling and emotion are two words for the same thing.\"", "right": "They differ on every axis: time of origin (now vs then), duration (minutes vs years), composition (clean vs mixed), purpose (creating vs healing). Collapsing the words collapses the work."},
    {"wrong": "\"I can think my way to which one it is.\"", "right": "Run the 5-minute test on the clock and check for a story attached. The two tests are observable; your <em>opinion</em> of yourself is not."},
    {"wrong": "\"If I feel it strongly toward this person, it's about this person.\"", "right": "A present-day trigger is not the source. Strong charge usually means a stored emotion fired — the original event was somewhere else."},
    {"wrong": "\"Emotions are bad and feelings are good.\"", "right": "Neither is bad. Feelings create in the now; emotions are stored material asking to be healed. They are different jobs, not a good/bad pair."},
  ],
  "closer_h": "Run the bar reading <em>against the clock.</em>",
  "closer_prose": "The Day 5 Per-Feeling Bar Reading installs as your standing morning instrument — the Feelings Form. Each morning you read the four bars and, for whatever fired, you ask the 5-minute question. That is this map, used daily.",
  "closer_meta": "Solo · Per-Feeling Bar Reading · Day 5 module",
  "reflect_prompt": "One or two lines. Bring one charged state from the last 48 hours. Feeling or emotion? Run the 5-minute test in writing — what did the clock say, and was there a story attached?",
},

# ===================== M35 — Map of Feelings Sensations (Day 05) =====================
"M35": {
  "title": "Map of Feelings Sensations",
  "day": "05",
  "eyebrow": "The Emotional Body · Day 5",
  "h1": "Sensation, <em>not story.</em>",
  "lede": "The answer to every beginner's question — \"how do I know which feeling this is?\" You know by sensation. The sensation is the feeling; the thought about it is the story.",
  "meta_desc": "Interactive teaching tool for the Possibility Management Map of Feelings Sensations — a lookup table of the body sensations of anger, sadness, fear, and joy, used in both directions.",
  "img_alt": "The Map of Feelings Sensations: the four feelings — anger, sadness, fear, joy — each shown with its characteristic body sensations: anger as heat and rigidity, sadness as melting heaviness, fear as electricity and contraction, joy as opening and expansion.",
  "shows_h": "You know which feeling it is <em>by sensation.</em>",
  "shows_prose": (
    "<p>This map answers the question every learner asks in the first feelings practice: <em>\"How do I know which feeling this is?\"</em> You know by <strong>sensation.</strong> The sensation is the feeling; the thought about it is the story.</p>"
    "<p><strong>Anger</strong> announces itself as heat, rigidity in the arms and back, a tense forehead, energy pressing outward. <strong>Sadness</strong> as melting: chest-deep heaviness, a thickening throat, slow inward-turning energy. <strong>Fear</strong> as electricity: shiver, contraction, racing thoughts, heightened senses, a cold or fluttering belly. <strong>Joy</strong> as opening: a smile that starts in the eyes, lightness, expansion, warmth spreading.</p>"
    "<p>Use the map as a lookup table in <span class=\"emph\">both directions.</span> Direction one: you have named a feeling and you verify it against the body — is there heat? rigidity? where? Direction two, more often: you have an unnamed sensation — a tight throat, a cold belly — and the map tells you which quadrant you are standing in. In the morning bar reading, this is the map you are actually using.</p>"
  ),
  "distinctions": [
    {"kicker": "Feeling 1 of 4", "name": "Anger", "rows": [
      ["Sensation", "Heat. Rigidity in the arms and back. A tense forehead. Energy pressing <em>outward.</em>"],
      ["Body", "Bones · big muscles of legs and arms · jaw · hands."],
      ["Reads as", "Something I value is being violated."]]},
    {"kicker": "Feeling 2 of 4", "name": "Sadness", "rows": [
      ["Sensation", "Melting. Chest-deep heaviness. A thickening throat. Slow, inward-turning energy."],
      ["Body", "Heart · throat · soft tissue of the face · eyes."],
      ["Reads as", "Something I valued is gone."]]},
    {"kicker": "Feeling 3 of 4", "name": "Fear", "rows": [
      ["Sensation", "Electricity. Shiver, contraction, racing thoughts, heightened senses, a cold or fluttering belly."],
      ["Body", "Nervous system · skin · small nerves · belly."],
      ["Reads as", "Something I value is at risk."]]},
    {"kicker": "Feeling 4 of 4", "name": "Joy", "rows": [
      ["Sensation", "Opening. A smile starting in the eyes. Lightness, expansion, warmth spreading."],
      ["Body", "Whole organism · face · eyes · chest."],
      ["Reads as", "Something I value is alive and present."]]},
    {"kicker": "How to use it", "name": "A two-way lookup.",
      "body": "Direction one: name first, verify in the body. Direction two, the common one: an <em>unnamed sensation</em> arrives — tight throat, cold belly — and the map names the quadrant. The location is <strong>anatomy, not poetry.</strong>"},
  ],
  "recall": [
    {"q": "How do you know which feeling you're in?", "a": "By <em>sensation.</em> The sensation is the feeling; the thought about it is the story."},
    {"q": "What does anger feel like in the body?", "a": "Heat, rigidity in the arms and back, a tense forehead, energy pressing outward. Bones, big muscles, jaw, hands."},
    {"q": "What does sadness feel like?", "a": "Melting — chest-deep heaviness, a thickening throat, slow inward-turning energy. Heart, throat, eyes."},
    {"q": "What does fear feel like, and where?", "a": "Electricity — shiver, contraction, racing thoughts, a cold or fluttering belly. Nervous system, skin, belly."},
    {"q": "Name the two directions you can read this map.", "a": "Name-then-verify (you named a feeling, check the body) and sensation-then-name (an unnamed sensation arrives, the map names the quadrant)."},
    {"q": "Are the body locations metaphorical?", "a": "No — literal. Anger in bones and big muscles, sadness in heart and throat. The location is anatomy, not poetry."},
  ],
  "mis": [
    {"wrong": "\"The body locations are metaphorical.\"", "right": "They are literal. Anger lives in bones and big muscles; sadness in heart and throat; fear in the nervous system and belly. Look for the sensation in <em>those specific places.</em>"},
    {"wrong": "\"If I can name the feeling, I don't need the sensation.\"", "right": "The naming is the story-layer; the sensation is the feeling itself. Verify the name against the body, or you may be naming a thought about a feeling."},
    {"wrong": "\"A real feeling is intense and obvious.\"", "right": "Most useful sensations are faint — a flicker of heat, an <em>almost</em>-imperceptible buzz. Almost nothing is still data. The map reads the small ones."},
    {"wrong": "\"Two sensations at once means I'm doing it wrong.\"", "right": "Multiple sensations often arrive together. The map sorts them by quadrant; when they tangle with a memory and a story, that is a mixed emotion (M11), not an error."},
  ],
  "closer_h": "Use it as your morning <em>lookup table.</em>",
  "closer_prose": "In the Day 5 bar reading and the Feeling Locator, this is the map you reach for when a sensation arrives unnamed. Keep it open beside the practice: tight throat to sadness, cold belly to fear, heat to anger, eye-smile to joy.",
  "closer_meta": "Solo · Feeling Locator · Day 5 module",
  "reflect_prompt": "One or two lines. Pick a sensation present in your body right now, however faint. Which quadrant does the map place it in? Did naming it from the sensation feel different than reaching for a word first?",
},

# ===================== M37 — Fear Capacity Feelings Form (Day 05) =====================
"M37": {
  "title": "Fear Capacity Feelings Form",
  "day": "05",
  "eyebrow": "The Emotional Body · Day 5 annex",
  "h1": "Fear, read as a <em>capacity</em> reading.",
  "lede": "One Feelings Form sentence drawn large: \"I feel fear that I may not have enough capacity to initiate a project that fills me up with joy.\" Fear about something you want is a surveyor's report, not an alarm.",
  "meta_desc": "Interactive teaching tool for the Possibility Management Fear Capacity Feelings Form — fear about something you want, read as a measurement of the capacity still to build.",
  "img_alt": "The Fear Capacity Feelings Form map: a single Feelings Form sentence written out large — I feel fear that I may not have enough capacity to initiate a project that fills me up with joy — annotated to show how the form names the feeling, names what the fear is about, and keeps the joy in the same sentence.",
  "shows_h": "Fear's asked-for action is <em>prepare.</em>",
  "shows_prose": (
    "<p>One sentence, drawn large: <em>\"I feel fear that I may not have enough capacity to initiate a project that fills me up with joy.\"</em> That is a Feelings Form sentence written out in full, showing the instrument doing its most precise job.</p>"
    "<p>Read the anatomy. It names the feeling plainly — <em>I feel fear</em> — no euphemism, no \"I'm a bit stressed about.\" It names what the fear is <strong>about:</strong> not the project, but <span class=\"emph\">capacity</span> — the speaker's own current size relative to what they want to create. And it keeps the joy in the same sentence, because the fear only exists since something worth creating is in view.</p>"
    "<p>Fear read this way is not an alarm to silence. It is a surveyor's report: <em>here is the gap between what I want to build and what I can currently hold.</em> The asked-for action of fear is <strong>prepare</strong> — and at this resolution, prepare means <strong>build the capacity the sentence just measured.</strong> You do not need this annex every day. You need it the weeks you are deciding something.</p>"
  ),
  "distinctions": [
    {"kicker": "Anatomy 1", "name": "Name the feeling plainly.",
      "body": "<em>I feel fear.</em> No euphemism, no \"a bit stressed,\" no \"anxious about.\" The form will not work on a softened word — name the feeling on the New Map (M10) by its real name."},
    {"kicker": "Anatomy 2", "name": "Name what it is about.",
      "body": "Not the project — <strong>capacity.</strong> The fear is about your own current size relative to what you want to create. \"Capacity\" is the variable the sentence measures, and the thing you can build."},
    {"kicker": "Anatomy 3", "name": "Keep the joy in the sentence.",
      "body": "<em>…a project that fills me up with joy.</em> The fear only exists because something worth creating is in view. Drop the joy and the fear looks like a verdict; keep it and the fear is a measurement <em>of</em> something you want."},
    {"kicker": "The reading", "name": "Fear means prepare.",
      "body": "Fear's asked-for action is <strong>prepare</strong> — and here, prepare means build the capacity the sentence just measured. The named version is almost always smaller than the unnamed dread it replaces."},
    {"kicker": "When to use it", "name": "The weeks you are deciding.",
      "body": "Run the full form — <em>I feel fear that I may not have enough ___ to ___</em> — when a fear reading in your morning row is attached to something you want. Not every day. The weeks something is on the table."},
  ],
  "recall": [
    {"q": "How does this map ask you to read fear about a project you want?", "a": "As a <em>capacity reading</em> — a measurement of the gap between what you want to build and what you can currently hold. A surveyor's report, not an alarm."},
    {"q": "What is the full form sentence?", "a": "<em>I feel fear that I may not have enough ___ to ___.</em> Name the feeling, name what it is about (usually capacity), keep the joy in view."},
    {"q": "What is fear's asked-for action — and what does it mean here?", "a": "<em>Prepare.</em> At this resolution, prepare means build the capacity the sentence just measured."},
    {"q": "Why keep the joy in the same sentence?", "a": "The fear only exists because something worth creating is in view. The joy is what makes the fear a capacity reading rather than a verdict on the project."},
    {"q": "When do you reach for this annex?", "a": "The weeks you are deciding something — when a fear reading attaches to something you want. Not every day."},
    {"q": "Why name the feeling plainly, with no euphemism?", "a": "The form will not work on \"a bit stressed.\" Naming it <em>fear</em> on the New Map is what lets it read as a capacity measurement instead of a vague dread."},
  ],
  "mis": [
    {"wrong": "\"Fear means stop.\"", "right": "Fear means <em>prepare.</em> It only means move away when the signal says <em>actual</em> danger. Fear about a project you want is usually a capacity reading, not a verdict on the project."},
    {"wrong": "\"The named fear will be bigger and scarier once I write it out.\"", "right": "Most learners discover the named version is <em>smaller</em> than the unnamed dread it replaces. Precision shrinks it; vagueness inflates it."},
    {"wrong": "\"If I feel fear about it, I shouldn't do it.\"", "right": "The fear is measuring capacity, not vetoing the project. The move is to build the capacity the sentence named — prepare — not to abandon what fills you up with joy."},
    {"wrong": "\"I need this annex every morning.\"", "right": "You do not. The standing instrument is the bar reading; this annex is for the weeks a fear reading attaches to something you are deciding."},
  ],
  "closer_h": "Write the <em>full sentence</em> when something is on the table.",
  "closer_prose": "When tomorrow's fear bar attaches to a project you want, write the full form — I feel fear that I may not have enough ___ to ___ — and read what capacity it just named. The Day 5 module installs the Feelings Form this annex belongs to.",
  "closer_meta": "Solo · Feelings Form · Day 5 module",
  "reflect_prompt": "One or two lines. Bring one thing you want to create that you also feel some fear about. Write the full form sentence. What capacity did it name — and was the named fear smaller than the dread you started with?",
},

# ===================== M38 — EHP Spaceholding Twins (Day 06) =====================
"M38": {
  "title": "EHP Spaceholding Twins",
  "day": "06",
  "kind": "ehp",
  "eyebrow": "Emotional Healing Process · Day 6",
  "h1": "Spaceholding <em>Go! and Beep!</em>",
  "lede": "The Module 4 rapid-learning grammar, applied to the witness's own craft. Two columns — Go! (what works) and Beep! (the classic errors) — make spaceholding a learnable skill with reps and design data, not a personality trait.",
  "meta_desc": "Interactive teaching tool for the Possibility Management EHP Spaceholding Twins map — the Go!/Beep! field log of holding space as a witness. Study level only; practice is gated in the Day 6 EHP walker.",
  "img_alt": "The EHP Spaceholding Twins map: two columns headed Go! and Beep! The Go! column lists what works when holding space — keep the client's attention on the emotion's expression, speak up, be assertive, hold steadily. The Beep! column lists classic spaceholder errors — indecisive language, jumping between emotions, mismatched tone, doing the client's process for them.",
  "shows_h": "Spaceholding is a <em>learnable skill</em> with reps.",
  "shows_prose": (
    "<p>Two columns under two familiar names, <strong>Go!</strong> and <strong>Beep!</strong>: the Module 4 rapid-learning grammar applied to the witness's own craft. Spaceholding is a learnable skill with reps and design data like any other, and this map is its field log.</p>"
    "<p>The <strong>Go!</strong> column is what works: keep the client's attention on the emotion's <em>expression</em> rather than on its vocabulary; speak up, because a witness who mumbles hands the client doubt; be assertive enough that the container is unmistakably held; and hold it steadily even while the client's other feelings surge.</p>"
    "<p>The <strong>Beep!</strong> column is the classic spaceholder errors, each one a design specification: indecisive language (\"um, maybe you could…\") that drops the container; jumping between emotions instead of letting one complete; shouting an encouraging <em>\"Go!\"</em> in an angry tone while the client is in sadness, which collides with the feeling instead of holding it; and the Rescuer's classic — doing the client's process <em>for</em> them. A caught Beep! is a good rep: it goes in your Beep! Book with a Shift! line under it.</p>"
  ),
  "distinctions": [
    {"kicker": "Go! — what works", "name": "Hold the expression, not the vocabulary.",
      "body": "Keep the client's attention on the emotion's <em>expression</em> — the sounds, the body, the energy — rather than on finding the right word for it. The body leads; the words follow."},
    {"kicker": "Go! — what works", "name": "Speak up. Be assertive.",
      "body": "A witness who mumbles hands the client doubt. Be assertive enough that the container is <strong>unmistakably held,</strong> and hold it steadily even while the client's other feelings surge."},
    {"kicker": "Beep! — design data", "name": "Indecisive language drops the container.",
      "body": "<em>\"Um, maybe you could…\"</em> The hedge tells the client no one is holding. A Beep!, not a verdict: name it, write a Shift! line, hold more clearly next rep."},
    {"kicker": "Beep! — design data", "name": "Mismatched tone collides with the feeling.",
      "body": "Shouting an encouraging <em>\"Go!\"</em> in an angry tone while the client is in <em>sadness</em> collides with the feeling instead of holding it. Match the holding to the feeling that is actually present."},
    {"kicker": "Beep! — design data", "name": "Doing the process for them.",
      "body": "The Rescuer's classic. The witness's job is to be present while the feeling moves — <strong>not</strong> to advise, narrate, fix, or run the EHP on the client's behalf. Catch it, log it, hand the process back."},
  ],
  "recall": [
    {"q": "What grammar is this map built on?", "a": "Go! / Beep! — the Module 4 rapid-learning loop, applied to the witness's own craft. Spaceholding is a skill with reps and design data."},
    {"q": "Give two things in the Go! column.", "a": "Keep attention on the emotion's expression not its vocabulary; speak up and be assertive so the container is unmistakably held; hold steadily as other feelings surge."},
    {"q": "Why is mumbling a Beep!?", "a": "Indecisive language — \"um, maybe you could\" — drops the container and hands the client doubt that anyone is holding the space."},
    {"q": "What is the Rescuer's classic spaceholding error?", "a": "Doing the client's process <em>for</em> them — advising, narrating, fixing. The witness is present while the feeling moves; they don't run it."},
    {"q": "What do you do with a Beep! you catch in yourself?", "a": "It is a good rep: write it in your Beep! Book with a Shift! line under it. A caught Beep! is design data, not a verdict."},
    {"q": "Should the holding change as the client's feelings shift?", "a": "Yes — hold steadily even while other feelings surge, and match the tone to the feeling present. A loud \"Go!\" over sadness collides instead of holding."},
  ],
  "mis": [
    {"wrong": "\"Good spaceholders are just naturally good at it.\"", "right": "Spaceholding is a <em>learnable skill</em> with reps and design data, like any other. This map is its field log — Go! columns to repeat, Beep! columns to catch and shift."},
    {"wrong": "\"A gentle, soft witness is always the safest.\"", "right": "Indecisive, mumbled holding <em>drops</em> the container. Be assertive enough that the holding is unmistakable — gentleness is not the same as vagueness."},
    {"wrong": "\"Encouraging the client loudly always helps.\"", "right": "Tone has to match the feeling present. A loud angry-toned \"Go!\" over a client in sadness collides with the feeling instead of holding it."},
    {"wrong": "\"If I help by suggesting what to do, I'm being a good witness.\"", "right": "Advising and fixing is the Rescuer move — a Beep!. The witness's one job is to be present while the feeling moves, and to hand the process back to the client."},
  ],
  "route_prose": "This map is the witness's field log, studied here as a locator. The spaceholding it describes is practised inside a real EHP — and even a small solo EHP runs only through the gated Day 6 walker, where consent and the trauma carve-out are held for you. Study the Go!/Beep! columns here; bring them to the walker when you witness or are witnessed.",
  "reflect_prompt": "One or two lines. Which Beep! in this map do you recognise as your own reflex when someone near you is upset — fixing, narrating, hedging, mismatching tone? What would the Go! version be?",
},

# ===================== M39 — Map of Optional Healing Process (Day 06) =====================
"M39": {
  "title": "Map of Optional Healing Process",
  "day": "06",
  "kind": "ehp",
  "eyebrow": "Emotional Healing Process · Day 6",
  "h1": "Healing is <em>optional.</em>",
  "lede": "Six stations drawn as a path — golden cube, contact, sounds before words, the liquid-state cloud, the old-decision/new-decision arrow, the heart at the close. The word in the title is the whole teaching: nobody heals you, and nothing makes you heal.",
  "meta_desc": "Interactive teaching tool for the Possibility Management Map of Optional Healing Process — the six EHP stations drawn as a path, and the consent that the title word 'optional' names. Study level only; practice is gated in the Day 6 walker.",
  "img_alt": "The Map of Optional Healing Process: six stations drawn down the page as a path — the golden cube of workspace at the top, two figures making contact, sounds before words, the liquid-state cloud, an arrow from an old decision to a new decision, and a heart at the close. The stations are numbered one through six; the course names them Position 0 through Position 5.",
  "shows_h": "Nobody heals you. <em>Nothing makes you heal.</em>",
  "shows_prose": (
    "<p>Six stations down the page, drawn as a path: the golden cube of workspace at the top, two figures making contact, sounds before words, the liquid-state cloud, the old-decision/new-decision arrow, and a heart at the close. The map numbers its stations 1 through 6; the course names the same stations <strong>Position 0 through Position 5.</strong> Same path, two numbering conventions; the course uses the 0–5 names throughout.</p>"
    "<p>The word to sit with is in the title: <span class=\"emph\">optional.</span> A stored emotion can sit in an emotional body for sixty years and the person remains functional; plenty do exactly that. An EHP begins with a person choosing, out loud, to complete something — <em>\"What can I do for you?\"</em> is a question, and \"nothing today\" is a valid answer — and every later position stays inside that consent.</p>"
    "<p>This is not a soft disclaimer. It is what separates healing work from the things that get done <em>to</em> people, and it is why the course gates this module on your own confirmation rather than on a schedule. The choice is the first position before the first position.</p>"
  ),
  "distinctions": [
    {"kicker": "Position 0", "name": "First position.",
      "body": "Center · grounding cord · bubble · golden cube · bright principles. The Module 3 equipment plus the integrity layer. Without this foundation, you are doing catharsis with no container."},
    {"kicker": "Position 1", "name": "Make contact.",
      "body": "Being-to-being connection with the witness. Shake hands. The witness asks: <em>\"What can I do for you?\"</em> — the moment the EHP becomes a chosen practice between two consenting people."},
    {"kicker": "Position 2", "name": "Navigate to liquid state.",
      "body": "The witness coaches the client to close the eyes, let the emotion get bigger, make the <em>sounds</em> of the emotion — and only after, the words. The body's signal precedes language. You become liquid by giving the emotion more space, not by analysing it."},
    {"kicker": "Positions 3–4", "name": "Work the original event.",
      "body": "In liquid state, the witness navigates with concrete questions — daytime or night? inside or outside? alone or not? — meets the original event, surfaces the old decision, and a new, adult-stance decision is named to replace it. <em>Studied here, not walked here.</em>"},
    {"kicker": "Position 5", "name": "The end.",
      "body": "Vanish the golden cube and clean up. The energetic boundary closes; the container ends. The client is in ordinary life again, and <strong>changed</strong> — the energy bound in the stored emotion is now available to them. And note: these are six positions in <em>relationship,</em> not a staircase — you do not march through in order; you move when the material moves you. The positions are the terrain; the path is yours."},
  ],
  "recall": [
    {"q": "What does the word in the title — <em>optional</em> — mean here?", "a": "Nobody heals you and nothing makes you heal. An EHP begins with a person choosing it out loud, and every position stays inside that consent. \"Nothing today\" is a valid answer."},
    {"q": "How many positions, and how are they numbered?", "a": "Six — Position 0 through Position 5. The map's image numbers the stations 1 through 6; the course uses the 0–5 names throughout."},
    {"q": "What is Position 0?", "a": "First position: center, grounding cord, bubble, golden cube, bright principles. The foundation — without it you are doing catharsis with no container."},
    {"q": "Is the EHP a linear staircase?", "a": "No. Six positions in relationship. You find yourself in one, the witness helps you locate yourself, and you move when the material moves you. The path is yours."},
    {"q": "What is different by Position 5?", "a": "The container closes and the client is changed — the energy bound in the stored emotion is now available to them."},
    {"q": "How does liquid state get reached, on this map?", "a": "Close the eyes, let the emotion get bigger, make the <em>sounds</em> of it — and only after, the words. The body's signal precedes language; you become liquid by giving the emotion space, not by analysing it."},
  ],
  "mis": [
    {"wrong": "\"If I just decide to heal, the process will run on schedule.\"", "right": "Healing is <em>optional</em> and non-linear. It begins with a chosen out-loud yes and moves only as the material moves. There is no timetable to march through."},
    {"wrong": "\"Someone who loves me can decide I need this and walk me into it.\"", "right": "No one can be processed against their will; trying produces resistance or harm, not healing. The loving move toward an unconsenting person is to keep being someone they could one day choose to be witnessed by."},
    {"wrong": "\"The EHP has five positions.\"", "right": "It has <em>six</em> — Position 0 through Position 5. Position 0 is the foundation that makes the rest a container rather than catharsis."},
    {"wrong": "\"The positions are steps I complete in order.\"", "right": "They are positions in relationship, not a staircase. You navigate the terrain; the witness helps you locate where you are. Order is discovered, not marched."},
  ],
  "route_prose": "This page locates the six positions so you can recognise the terrain. It does not walk you through them, on purpose. Even a small solo EHP runs only through the gated Day 6 walker, because the walker's consent gate and trauma carve-out are structural — not optional. Study the path here; the practice is held there.",
  "reflect_prompt": "One or two lines. Sit with the word in the title — optional. What changes when you hold that no one heals you and nothing makes you heal? Which of the six positions is hardest to imagine, and why?",
},

# ===================== M40 — EHP Learnings (Day 06) =====================
"M40": {
  "title": "EHP Learnings",
  "day": "06",
  "kind": "ehp",
  "eyebrow": "Emotional Healing Process · Day 6",
  "h1": "What EHPs <em>teach.</em>",
  "lede": "A second Go!/Beep! card, harvested from many EHPs — and it describes the client's discipline as much as the spaceholder's. If you keep one line for your own practice, keep: thinking over feeling is the Beep!",
  "meta_desc": "Interactive teaching tool for the Possibility Management EHP Learnings map — the Go!/Beep! field log harvested from many EHPs, describing the client's discipline. Study level only; practice is gated in the Day 6 walker.",
  "img_alt": "The EHP Learnings map: a second Go!/Beep! card harvested from many Emotional Healing Processes. The Go! column — the feeling is found in the body, the body leads and words follow, the client experiences rather than narrates, one team. The Beep! column — performing instead of feeling, distractions, telling the client what they feel, thinking over feeling, managing toward a goal.",
  "shows_h": "Keep one line: <em>thinking over feeling</em> is the Beep!",
  "shows_prose": (
    "<p>A second Go!/Beep! card, harvested from many EHPs, and it describes the <em>client's</em> discipline as much as the spaceholder's.</p>"
    "<p>The <strong>Go!</strong> column: the feeling is found <em>in the body</em>; the body leads and the words follow; the client gets space to <em>experience</em> rather than narrate; the voice stays even and strong; both people are on one team; the emotion is sensed where it actually sits, right at the surface.</p>"
    "<p>The <strong>Beep!</strong> column is a catalogue of the ways the process gets stolen: performing instead of feeling; distractions; telling the client what they feel; firing too many questions too fast; the verdict <em>\"you are doing this\"</em>; coaching when the moment asked for witnessing; thinking over feeling; and managing the client toward a goal — the subtle one, because a goal-shaped EHP is no longer a discovery.</p>"
    "<p>If you keep one line from this map for your own practice, keep <span class=\"emph\">thinking over feeling.</span> Every learner hits the moment where the mind offers a tidy explanation in exchange for not feeling the next wave. The explanation is the Beep!</p>"
  ),
  "distinctions": [
    {"kicker": "Go! — what works", "name": "The body leads; words follow.",
      "body": "The feeling is found <em>in the body</em> and sensed where it actually sits, right at the surface. The client experiences rather than narrates. Sounds before sentences."},
    {"kicker": "Go! — what works", "name": "One team.",
      "body": "Both people are on one team — witness and client navigating the same terrain together. The voice stays even and strong; the container is steady, not anxious."},
    {"kicker": "Beep! — design data", "name": "Thinking over feeling.",
      "body": "The one to keep. The mind offers a tidy explanation in exchange for not feeling the next wave. <strong>The explanation is the Beep!</strong> Every learner hits this moment."},
    {"kicker": "Beep! — design data", "name": "Performing instead of feeling.",
      "body": "Acting out the shape of an emotion for the witness, rather than letting the actual feeling move. Distractions and side-stories belong here too — all ways the process gets stolen."},
    {"kicker": "Beep! — design data", "name": "Managing toward a goal.",
      "body": "The subtle one. A goal-shaped EHP is no longer a <em>discovery</em> — it has become a project with a target. Telling the client what they feel, or steering them toward a tidy ending, collapses the process into management."},
  ],
  "recall": [
    {"q": "What is the one Beep! line to keep for your own practice?", "a": "<em>Thinking over feeling.</em> The mind trades a tidy explanation for not feeling the next wave — and the explanation is the Beep!"},
    {"q": "Where is the feeling found, on the Go! side?", "a": "In the body, sensed where it actually sits, right at the surface. The body leads and the words follow; the client experiences rather than narrates."},
    {"q": "Why is \"managing toward a goal\" a Beep!?", "a": "A goal-shaped EHP is no longer a discovery — it becomes a project with a target. The EHP is a moment-to-moment discovery, not a managed outcome."},
    {"q": "Whose discipline does this card describe?", "a": "The <em>client's</em> as much as the spaceholder's. It is harvested from many EHPs and reads as a field log for both roles."},
    {"q": "Name two more Beep!-column errors.", "a": "Performing instead of feeling; distractions; telling the client what they feel; too many questions too fast; coaching when the moment asked for witnessing."},
    {"q": "On the Go! side, what is the relationship between the two people?", "a": "<em>One team.</em> Witness and client navigate the same terrain together; the voice stays even and strong, the container steady rather than anxious."},
  ],
  "mis": [
    {"wrong": "\"A good explanation of what I feel means the EHP is working.\"", "right": "<em>Thinking over feeling</em> is the Beep!. The tidy explanation is the mind's trade for not feeling the next wave. Insight is not the same as the feeling moving."},
    {"wrong": "\"The witness should tell the client what they're feeling.\"", "right": "Telling the client what they feel is a Beep!. The feeling is found in the client's body, by the client. The witness holds; they do not diagnose."},
    {"wrong": "\"An EHP should aim at a clear outcome.\"", "right": "Managing toward a goal collapses the EHP into a project. It is a moment-to-moment <em>discovery</em> — a goal-shaped process is no longer one."},
    {"wrong": "\"These learnings are only for the spaceholder.\"", "right": "The card describes the <em>client's</em> discipline as much as the witness's. Both people read it; both can run the Beep! column."},
  ],
  "route_prose": "These learnings are harvested from many EHPs and studied here as a field log. They come alive inside an actual process — and even a small solo EHP runs only through the gated Day 6 walker, where the consent gate and trauma carve-out are structural. Carry one line — thinking over feeling — into the walker.",
  "reflect_prompt": "One or two lines. Recall a moment you reached for an explanation to avoid feeling the next thing. What did the explanation let you skip? That move is the Beep! this map names.",
},

# ===================== M43 — Letting Your Heart Speak (Day 08) =====================
"M43": {
  "title": "Letting Your Heart Speak",
  "day": "08",
  "eyebrow": "Communication · Day 8",
  "h1": "Letting your <em>heart speak.</em>",
  "lede": "Between Adult speech and Possibility Speaking sits a gate most adults keep shut: speech that comes from the heart instead of from the mind's editor. If you want the fourth speaking, this gate opens first.",
  "meta_desc": "Interactive teaching tool for the Possibility Management map Letting Your Heart Speak — the gate between Adult speech and Possibility Speaking, where speech comes from the heart rather than the mind's editor.",
  "img_alt": "The Letting Your Heart Speak map: two routes for a sentence — one running through the mind's editor, which drafts, censors and polishes before delivering something defensible, and one running from the heart, which says the shorter, warmer, unpolished true sentence. The map sits between Adult speech and Possibility Speaking.",
  "shows_h": "Stop running every sentence through <em>the editor.</em>",
  "shows_prose": (
    "<p>Between Adult speech and Possibility Speaking sits a gate most adults keep shut: speech that comes from the <strong>heart</strong> instead of from the mind's editor. The mind drafts, censors, polishes, and delivers something defensible. The heart, given the channel, says the unpolished true sentence: shorter, warmer, sometimes shaky.</p>"
    "<p>Heart speech is not a performance of vulnerability and not emotional venting; it is what becomes available when you stop running every sentence through the editor first. <strong>Possibility Speaking is almost never reachable through the editor.</strong> If you want the fourth speaking, this gate opens first.</p>"
    "<p>The four speakings pair with the four listenings. Gremlin speech wants gremlin listening; Box speech wants confirming listening; Adult speech wants meaning-listening; Possibility Speaking is met by Possibility Listening. Both require the same infrastructure: liquid state, holding context, being sourced from <span class=\"emph\">being</span> rather than from Box or gremlin. The highest form of Possibility Speaking is a declaration — a spoken act that brings something into being, then followed by behaviour consistent with it.</p>"
  ),
  "distinctions": [
    {"kicker": "Route 1", "name": "Through the editor.",
      "body": "The mind drafts, censors, polishes, and delivers something <em>defensible.</em> Safe, controlled — and almost never able to reach Possibility Speaking, because the editor's whole job is to keep you defended."},
    {"kicker": "Route 2", "name": "From the heart.",
      "body": "Given the channel, the heart says the unpolished <strong>true</strong> sentence: shorter, warmer, sometimes shaky. Not a performance of vulnerability, not venting — what becomes available when the editor stops vetting first."},
    {"kicker": "The pairing", "name": "Speech and listening must match.",
      "body": "Gremlin speech wants gremlin listening; Box speech wants confirming listening; Adult speech wants meaning-listening; Possibility Speaking is met by Possibility Listening. A clear sentence can still fail if the two are mismatched."},
    {"kicker": "The infrastructure", "name": "Sourced from being.",
      "body": "Possibility Speaking requires liquid state, a holding context, and being sourced from <em>being</em> — not from Box or gremlin. You cannot Possibility-Speak from a defended position, and you cannot do it with a gremlin running the speech."},
    {"kicker": "The summit", "name": "The highest form is a declaration.",
      "body": "<em>I declare.</em> Not a prediction, hope, wish, promise, or goal — a spoken act that brings something into being by being spoken, then followed by behaviour consistent with it. Without a bright principle active, \"I declare\" is grandiosity; with it, a real act. Module 10 teaches it in full."},
  ],
  "recall": [
    {"q": "What sits between Adult speech and Possibility Speaking?", "a": "The gate of <em>heart speech</em> — speech from the heart rather than the mind's editor. If you want the fourth speaking, this gate opens first."},
    {"q": "What does the editor do, and why is it a problem here?", "a": "It drafts, censors, polishes, delivers something defensible. Possibility Speaking is almost never reachable through it — its job is to keep you defended."},
    {"q": "Is heart speech the same as venting or performing vulnerability?", "a": "No. It is the shorter, warmer, sometimes shaky <em>true</em> sentence that becomes available when you stop running every sentence through the editor first."},
    {"q": "Why can a clear sentence still fail?", "a": "Speech and listening must match. You may be Possibility-Speaking to a confirming-listening, or Adult-Speaking to a gremlin-listening. Mismatch breaks the communication."},
    {"q": "What is the highest form of Possibility Speaking?", "a": "A <em>declaration</em> — a spoken act that brings something into being, followed by consistent behaviour, sourced from a bright principle. Without that source it is grandiosity."},
    {"q": "Which speaking pairs with Possibility Listening?", "a": "Possibility Speaking. The four speakings pair with the four listenings — gremlin/gremlin, Box/confirming, Adult/meaning, Possibility/Possibility — and both ends need liquid state and sourcing from being."},
  ],
  "mis": [
    {"wrong": "\"Heart speech means oversharing my feelings.\"", "right": "It is not venting and not a performance of vulnerability. It is the unpolished <em>true</em> sentence — often shorter and quieter — that the editor would have filtered out."},
    {"wrong": "\"If my words are clear, the communication will land.\"", "right": "Speech and listening have to match. Clear Adult speech meeting a gremlin-listening still fails. The location of both speaker and listener matters as much as the words."},
    {"wrong": "\"I can Possibility-Speak whenever I decide to.\"", "right": "Not from a defended position and not with a gremlin running the speech. It needs liquid state, a holding context, and sourcing from being — get quiet and ground first."},
    {"wrong": "\"Saying 'I declare' makes it a declaration.\"", "right": "Without a bright principle active and behaviour that follows, \"I declare\" is grandiosity. A declaration brings something into being only when it is sourced and then lived."},
  ],
  "closer_h": "Try the fourth speaking <em>aloud.</em>",
  "closer_prose": "The Day 8 four-speaking voice memo runs one real topic from the gremlin, the Box, Adult, and Possibility — and the fourth recording is where you ground, let the heart have the channel, and find a bright principle before you speak. This map is the gate that recording opens.",
  "closer_meta": "Solo · four-speaking voice memo · Day 8 module",
  "reflect_prompt": "One or two lines. Recall a recent sentence you ran through the editor before saying. What would the heart's version have been — shorter, warmer, truer? What did the editor protect you from?",
},

# ===================== M44 — Linear and Nonlinear (Day 10) =====================
"M44": {
  "title": "Linear and Nonlinear",
  "day": "10",
  "eyebrow": "Possibility · Day 10",
  "h1": "Linear and <em>nonlinear.</em>",
  "lede": "Two kinds of possibility, and they are not two sizes of the same thing. Linear extends what already exists. Nonlinear becomes available only when the context itself changes — and from inside the old context it looks like nothing.",
  "meta_desc": "Interactive teaching tool for the Possibility Management map of Linear and Nonlinear possibility — extending the current context versus changing which context exists.",
  "img_alt": "The Linear and Nonlinear map: two kinds of possibility. Linear possibility shown as steps extending the current context — more, better, faster within the room you are in. Nonlinear possibility shown as reachable only when the context itself changes, through a declaration or a dangerous question, making a different set of next actions visible.",
  "shows_h": "Nonlinear changes <em>which room exists.</em>",
  "shows_prose": (
    "<p>Two kinds of possibility, and they are not two sizes of the same thing. <strong>Linear possibility</strong> extends what already exists: more clients, a better apartment, a clearer version of the conversation you already have. It is reachable by ordinary steps from the current context, and most planning, goal-setting, and self-improvement operates entirely inside it.</p>"
    "<p><strong>Nonlinear possibility</strong> is not reachable by extension at all. It becomes available only when the context itself changes — a declaration, a dangerous question, a context shift that makes a different set of next actions visible. From inside the old context, nonlinear possibility looks like <em>nothing,</em> which is exactly why the Box never objects to it in advance.</p>"
    "<p>Linear gets you a better seat in the room you are in. Nonlinear changes <span class=\"emph\">which room exists.</span> Neither is superior in every domain — renewing your passport is a linear job; do not declare at it — but every result you have already concluded is impossible lives, if it lives anywhere, on the nonlinear side. The two require different equipment: linear needs a plan; nonlinear needs the three keys and a speech act.</p>"
  ),
  "distinctions": [
    {"kicker": "Kind 1", "name": "Linear possibility.",
      "body": "Extends what already exists — more, better, faster, clearer — <em>inside</em> the current context. Reachable by ordinary steps. Most planning, goal-setting, and self-improvement lives entirely here. Its equipment is <strong>a plan.</strong>"},
    {"kicker": "Kind 2", "name": "Nonlinear possibility.",
      "body": "Not reachable by extension at all. Becomes available only when the <em>context itself</em> changes — a declaration, a dangerous question. Its equipment is <strong>the three keys and a speech act,</strong> not a plan."},
    {"kicker": "Why it hides", "name": "It looks like nothing.",
      "body": "From inside the old context, nonlinear possibility looks like nothing — which is exactly why the Box never objects to it in advance. You cannot brainstorm your way to it; brainstorm output is still linear."},
    {"kicker": "The difference", "name": "A better seat vs a different room.",
      "body": "Linear gets you a better seat in the room you are in. Nonlinear changes <em>which room exists.</em> Every result you have concluded is impossible lives, if anywhere, on the nonlinear side."},
    {"kicker": "Both are tools", "name": "Neither is superior everywhere.",
      "body": "Renewing your passport is a linear job — <em>do not declare at it.</em> The vocabulary matters because the two need different equipment, not because one ranks above the other."},
  ],
  "recall": [
    {"q": "What does linear possibility do?", "a": "Extends what already exists — more, better, faster, clearer — inside the current context. Reachable by ordinary steps. Its equipment is a plan."},
    {"q": "When does nonlinear possibility become available?", "a": "Only when the <em>context itself</em> changes — a declaration, a dangerous question, a context shift that makes different next actions visible."},
    {"q": "Why does the Box never object to nonlinear possibility in advance?", "a": "From inside the old context it looks like <em>nothing.</em> There is nothing yet for the Box to resist — which is exactly what makes it nonlinear."},
    {"q": "Linear vs nonlinear, in one image?", "a": "Linear gets you a better seat in the room you are in. Nonlinear changes which room exists."},
    {"q": "Is nonlinear always the better move?", "a": "No. Renewing your passport is a linear job; do not declare at it. Different domains need different equipment — a plan, or the three keys and a speech act."},
    {"q": "What equipment does each kind need?", "a": "Linear needs <em>a plan.</em> Nonlinear needs the three keys — held context, liquid state, dangerous question — and a speech act. Different jobs, different tools."},
  ],
  "mis": [
    {"wrong": "\"Nonlinear is just thinking outside the box.\"", "right": "Brainstorm output is still <em>linear</em> — ideas generated inside the current context. Nonlinear arrives by changing the context, which no amount of idea-volume accomplishes."},
    {"wrong": "\"Nonlinear possibility is rare and mystical.\"", "right": "It is undramatic in practice: a sentence said from a new context, after which different actions are simply available. A four-minute threshold rep is a nonlinear rep."},
    {"wrong": "\"Bigger goals are nonlinear.\"", "right": "A bigger goal is still linear — more of the same, inside the same room. Nonlinear is not a larger version of the current possibility; it is a different room."},
    {"wrong": "\"I should always go for the nonlinear option.\"", "right": "Neither kind is superior in every domain. Linear jobs want a plan; declaring at your passport renewal is a category error. Match the equipment to the task."},
  ],
  "closer_h": "Run a <em>nonlinear rep.</em>",
  "closer_prose": "The Day 10 threshold and declaration practices are nonlinear reps in four minutes: a sentence said from a new context, after which different actions are simply available. This map names what those practices are reaching for.",
  "closer_meta": "Solo · threshold + declaration practice · Day 10 module",
  "reflect_prompt": "One or two lines. Name one result you have quietly filed as impossible. Is it impossible by extension (linear) — or only invisible from your current context (nonlinear)? What context shift would put it on the board?",
},

# ===================== M46 — Map of Matrix (Day 10, also Day 03) =====================
"M46": {
  "title": "Map of Matrix",
  "day": "10",
  "eyebrow": "Matrix · Days 3 and 10",
  "h1": "The map of <em>matrix.</em>",
  "lede": "Your matrix is the energetic structure you build, through practice, that determines how much consciousness you can hold. Thoughtware upgrades install onto matrix; without enough of it, an upgrade has nowhere to live.",
  "meta_desc": "Interactive teaching tool for the Possibility Management Map of Matrix — the energetic structure you build through practice that determines how much consciousness you can hold. Built by reps, not by reading.",
  "img_alt": "The Map of Matrix: the energetic structure a person builds through practice that determines how much consciousness they can hold. The map shows matrix as something constructed by reps and feelings work, onto which thoughtware upgrades install, distinct from the cultural matrix a person is raised inside.",
  "shows_h": "Matrix is <em>built,</em> not learned.",
  "shows_prose": (
    "<p>The course has used the word <em>matrix</em> in passing since Module 2; here is its one definition, the same one everywhere in this course. <strong>Your matrix is the energetic structure you build, through practice, that determines how much consciousness you can hold.</strong> Distinctions, feelings at higher intensity, responsibility at larger scale: each requires matrix to hold it.</p>"
    "<p>Matrix is built through conscious practice — reps, feelings work, holding attention, taking on responsibility slightly beyond current capacity. It is <strong>not</strong> built by insight, reading, or intention. Thoughtware upgrades install onto matrix; without enough matrix, an upgrade has nowhere to live. This is why the course runs on experiments and a daily sit instead of on explanations: every rep you have logged since Module 0 has been matrix construction, whether or not it felt like progress that day.</p>"
    "<p>One bordering use of the word, always marked: <em>\"the cultural matrix\"</em> names the default cosmology a person is raised inside, which for most learners is the patriarchal one. When this course says <span class=\"emph\">matrix</span> without a qualifier, it always means the structure you build.</p>"
  ),
  "distinctions": [
    {"kicker": "The definition", "name": "What matrix is.",
      "body": "The energetic structure you build, through practice, that <strong>determines how much consciousness you can hold.</strong> Distinctions, higher-intensity feelings, responsibility at larger scale — each needs matrix to hold it."},
    {"kicker": "How it is built", "name": "By reps, not by reading.",
      "body": "Conscious practice: reps, feelings work, holding attention, taking on responsibility slightly beyond current capacity. <strong>Not</strong> by insight, reading, or intention. Matrix grows the way strength does — slightly beyond current load."},
    {"kicker": "What it holds", "name": "Upgrades install onto matrix.",
      "body": "Thoughtware upgrades install <em>onto</em> matrix. Without enough matrix, an upgrade has nowhere to live — which is why explanation alone changes nothing, and why a course of reps holds what a course of reading cannot."},
    {"kicker": "The bordering sense", "name": "\"The cultural matrix.\"",
      "body": "Always marked. <em>The cultural matrix</em> names the default cosmology a person is raised inside — for most learners, the patriarchal one. Bare <strong>matrix,</strong> in this course, always means the structure you build."},
    {"kicker": "Why it matters", "name": "It runs the whole course design.",
      "body": "The daily sit and the experiments are matrix construction. Your matrix determines how much noticing you can hold; what you can hold determines what becomes possible. The reps are the point, not the warm-up."},
  ],
  "recall": [
    {"q": "Define matrix in one sentence.", "a": "The energetic structure you build, through practice, that determines how much consciousness you can hold."},
    {"q": "How is matrix built?", "a": "By conscious practice — reps, feelings work, holding attention, taking responsibility slightly beyond current capacity. Not by insight, reading, or intention."},
    {"q": "What is the relationship between matrix and thoughtware?", "a": "Thoughtware upgrades install <em>onto</em> matrix. Without enough matrix, an upgrade has nowhere to live."},
    {"q": "What does \"the cultural matrix\" mean — and how is it marked?", "a": "The default cosmology you were raised inside, for most learners patriarchal. It is always qualified; bare \"matrix\" means the structure you build."},
    {"q": "Why does the course run on a daily sit and experiments?", "a": "Because matrix is built by reps, not explanation. Every rep since Module 0 has been matrix construction — explanation alone has nowhere to install."},
    {"q": "What does matrix let you hold more of?", "a": "Consciousness — finer distinctions, feelings at higher intensity, responsibility at larger scale. Each of those needs matrix to hold it; more matrix, more you can hold."},
  ],
  "mis": [
    {"wrong": "\"Matrix is a metaphor for knowledge — I build it by learning more.\"", "right": "Matrix is built by <em>practice,</em> not information. A learner who reads every Spark and runs no experiments has upgraded their library, not their matrix."},
    {"wrong": "\"I either have matrix or I don't.\"", "right": "Matrix grows by reps slightly beyond current capacity, the same way strength does. The thirty days of bar readings behind you are measurable construction."},
    {"wrong": "\"The matrix is patriarchy.\"", "right": "That is the qualified, secondary sense — the <em>cultural</em> matrix. Unqualified, in this course, matrix means the structure you build."},
    {"wrong": "\"Once I understand a distinction, it's installed.\"", "right": "Distinctions install onto matrix, in liquid state, across the bodies. Understanding keeps the work in the intellect; without matrix the upgrade has nowhere to live."},
  ],
  "closer_h": "Notice the reps are <em>building it.</em>",
  "closer_prose": "Day 3 first names matrix as the structure your equipment practice quietly builds; Day 10 gives it its full definition. Between them sit thirty days of bar readings and experiments — measurable construction. The daily sit is not the warm-up; it is the work.",
  "closer_meta": "Solo · the daily sit and experiments · Days 3 and 10",
  "reflect_prompt": "One or two lines. What in the last month built your matrix — which reps, which feelings work, which responsibility taken slightly beyond your capacity? What did you mistake for matrix-building that was actually just reading?",
},

# ===================== M47 — Map of 3 Games (Day 07) =====================
"M47": {
  "title": "Map of 3 Games",
  "day": "07",
  "eyebrow": "Drama and the Responsible Game · Day 7",
  "h1": "The <em>three games.</em>",
  "lede": "Three ways a game between people can be built: I win–you lose, win-win (and its shadow, lose-lose), and winning happening — where there is no option to lose because everyone is learning. The Responsible Game grows toward the third.",
  "meta_desc": "Interactive teaching tool for the Possibility Management Map of 3 Games — I win-you lose, win-win and its lose-lose shadow, and winning happening, where there is no option to lose.",
  "img_alt": "The Map of 3 Games: three numbered setups for a game between people. Game 1, I win-you lose, marked with gremlin and hierarchy. Game 2, win-win and its shadow lose-lose, marked with secret competition and compromise. Game 3, winning happening, built so there is no option to lose because everyone is always learning.",
  "shows_h": "Changing the game is the <em>bigger move.</em>",
  "shows_prose": (
    "<p>Three numbered setups — three ways a game between people can be built — and the Responsible Game gets its ground from the third.</p>"
    "<p><strong>Game 1: I win — you lose.</strong> Hierarchy, strategizing, competition. The map writes <em>gremlin</em> right into this line, because the Low Drama Triangle lives here: every low drama is a game-1 round, where somebody has to lose for the gremlin food to be produced.</p>"
    "<p><strong>Game 2: I win — you win… and its shadow, I lose — you lose.</strong> The civilized improvement — and the map is dry-eyed about its underside: <em>secret competition</em> and <em>compromise.</em> Plenty of \"win-win\" is game 1 in a collaboration costume, both players quietly keeping score.</p>"
    "<p><strong>Game 3: winning happening.</strong> A game built so there is <span class=\"emph\">no option to lose.</span> Always learning something. Generosity. Sharing research. A Beep! in game 3 is design data, not defeat. The Responsible Game at kitchen scale, and high drama at gameworld scale, are both game-3 setups: nobody has to lose for the thing to be worth playing, because what is produced is learning and creation rather than food.</p>"
  ),
  "distinctions": [
    {"kicker": "Game 1", "name": "I win — you lose.", "rows": [
      ["Setup", "Hierarchy, strategizing, competition. The map writes <em>gremlin</em> into this line."],
      ["Who lives here", "The Low Drama Triangle. Every low drama is a game-1 round."],
      ["Cost", "Somebody has to lose for the gremlin food to be produced."]]},
    {"kicker": "Game 2", "name": "Win-win, and its shadow.", "rows": [
      ["Setup", "I win — you win. The civilized improvement over game 1."],
      ["Shadow", "Secret competition; compromise; and lose–lose, where the consolation is that the other one also lost."],
      ["Watch for", "\"Win-win\" that is game 1 in a collaboration costume, both quietly keeping score."]]},
    {"kicker": "Game 3", "name": "Winning happening.", "rows": [
      ["Setup", "Built so there is <strong>no option to lose.</strong> Always learning, generous, sharing."],
      ["A Beep! here", "Design data, not defeat — the Beep! Book has been training game 3 since Module 0."],
      ["Where it lives", "The Responsible Game at kitchen scale; high drama at gameworld scale."]]},
    {"kicker": "High drama", "name": "Lives in game 3.",
      "body": "<strong>High drama is radical responsibility at gameworld scale</strong> — under Conscious Purpose, in the Responsible Game, where M20 places it. It is a game-3 setup: nobody has to lose, because what is produced is creation, not food. <em>High drama is not theatrical performance, and it is not gremlin food.</em>"},
    {"kicker": "The move", "name": "Change the game, not just your seat.",
      "body": "Changing your position inside game 1 is good work. Changing the <em>game</em> is the bigger move. When you decline a drama, ask: <em>what game was I invited into, and what game do I want to set up instead?</em>"},
  ],
  "recall": [
    {"q": "Name the three games.", "a": "Game 1: I win–you lose. Game 2: win-win and its shadow lose-lose. Game 3: winning happening — no option to lose because everyone is learning."},
    {"q": "Which game does the Low Drama Triangle live in, and why?", "a": "Game 1. Every low drama is a game-1 round — somebody has to lose for the gremlin food to be produced. The map writes <em>gremlin</em> into that line."},
    {"q": "What is game 2's shadow?", "a": "Secret competition and compromise, and lose-lose — where each party's main consolation is that the other one also didn't get what they wanted."},
    {"q": "What is game 3, winning happening?", "a": "A game built so there is no option to lose: always learning, generous, sharing. A Beep! here is design data, not defeat."},
    {"q": "Where does high drama sit on this map?", "a": "In game 3 — radical responsibility at gameworld scale, under Conscious Purpose, in the Responsible Game (M20). Not theatrical, not gremlin food."},
    {"q": "What is the bigger move when you decline a drama?", "a": "Changing the <em>game</em>, not just your position inside game 1. Ask what game you were invited into and what game you want to set up instead."},
  ],
  "mis": [
    {"wrong": "\"Game 2 is the goal — win-win is what mature adults do.\"", "right": "Game 2 is better than game 1 and still keeps score. The map names its failure modes on its own face: <em>secret competition</em> and <em>compromise.</em> Game 3 stops scoring losses entirely."},
    {"wrong": "\"Winning happening means everybody wins every time.\"", "right": "It means losing is not on the board: whatever happens, something is learned, shared, or created. Outcomes still vary — the <em>accounting</em> changes."},
    {"wrong": "\"Games are for games — this doesn't apply to my marriage or job.\"", "right": "Any field with more than one person is running one of these three setups right now, named or not. Naming which one is the first move toward changing it."},
    {"wrong": "\"High drama is theatrical, staged drama — and it's gremlin food too.\"", "right": "<em>No.</em> High drama is radical responsibility at gameworld scale, under Conscious Purpose, in the Responsible Game — a game-3 setup. It is <strong>not</strong> theatrical performance and <strong>not</strong> gremlin food. Only low drama feeds the gremlin."},
  ],
  "closer_h": "Name the game you were <em>invited into.</em>",
  "closer_prose": "The Day 7 drama detector ends by asking, when you decline a drama: what game was I being invited into, and what game do I want to set up instead? This map is the instrument that question reaches for. Changing the game is the bigger move.",
  "closer_meta": "Solo · drama detector · Day 7 module",
  "reflect_prompt": "One or two lines. Bring one charged exchange from this week. Which game was it set up as? What would the same exchange look like rebuilt as game 3 — winning happening, no option to lose?",
},

}


# ----------------------------------------------------------------------------
# Filenames (§B.1) — byte-exact. The module links already point at these.
# ----------------------------------------------------------------------------
FILENAMES = {
    "M32": "M32 - Map of Responsibility and Culture.html",
    "M33": "M33 - Feelings vs Emotions.html",
    "M35": "M35 - Map of Feelings Sensations.html",
    "M37": "M37 - Fear Capacity Feelings Form.html",
    "M38": "M38 - EHP Spaceholding Twins.html",
    "M39": "M39 - Map of Optional Healing Process.html",
    "M40": "M40 - EHP Learnings.html",
    "M43": "M43 - Letting Your Heart Speak.html",
    "M44": "M44 - Linear and Nonlinear.html",
    "M46": "M46 - Map of Matrix.html",
    "M47": "M47 - Map of 3 Games.html",
}


def _json(obj):
    """Compact JSON literal for embedding in the page script. We DON'T
    html-escape — these strings carry authored inline <em>/<strong> tags that
    must reach innerHTML intact, and they appear inside a <script> block where
    HTML entities would not be decoded. No '</script>' appears in content."""
    import json
    return json.dumps(obj, ensure_ascii=False)


def render_page(mnum):
    c = CONTENT[mnum]
    day = c["day"]
    href = day_href(day)
    label = day_label(day)
    store_key = "etb_atlas_" + mnum

    # practice / safety section
    if c.get("kind") == "ehp":
        practice = EHP_SAFETY_SECTION.replace("{ROUTE_PROSE}", c["route_prose"])
    else:
        practice = (STUDY_CLOSER_SECTION
                    .replace("{CLOSER_H}", c["closer_h"])
                    .replace("{CLOSER_PROSE}", c["closer_prose"])
                    .replace("{CLOSER_META}", c["closer_meta"])
                    .replace("{DAY_HREF}", href)
                    .replace("{DAY_LABEL}", label))

    # recall deck: store as {q, a}
    recall = [{"q": r["q"], "a": r["a"]} for r in c["recall"]]

    repl = {
        "{TITLE}": c["title"],
        "{TITLE_ATTR}": esc(c["title"]),
        "{MNUM}": mnum,
        "{META_DESC}": esc(c["meta_desc"]),
        "{EYEBROW}": c["eyebrow"],
        "{H1}": c["h1"],
        "{LEDE}": c["lede"],
        "{IMG_ALT}": esc(c["img_alt"]),
        "{SHOWS_H}": c["shows_h"],
        "{SHOWS_PROSE}": c["shows_prose"],
        "{STEP_TOTAL}": str(len(c["distinctions"])),
        "{DAY_HREF}": href,
        "{DAY_LABEL}": label,
        "{STORE_KEY}": store_key,
        "{PRACTICE_SECTION}": practice,
        "{REFLECT_PROMPT}": c["reflect_prompt"],
        "{DISTINCTIONS_JSON}": _json(c["distinctions"]),
        "{RECALL_JSON}": _json(recall),
        "{MIS_JSON}": _json(c["mis"]),
    }
    out = TEMPLATE
    for k, v in repl.items():
        out = out.replace(k, v)
    return out


# ----------------------------------------------------------------------------
# INDEX REGROUP (§B.6) — module-grouped sections 01->10, all 29 existing entries
# kept, the 11 new pages added in module position, M21 slot note, completion
# dots from etb_atlas_* presence. "Study the map" + recall-deck framing.
# Each group: (module label, day range, [ (mnum, title), ... ]).
# ----------------------------------------------------------------------------
MODULE_GROUPS = [
    ("Module 01", "Orientation · New Context · Radical Responsibility", "Day 1", [
        ("M01", "New Context (the chain)"),
        ("M24", "Levels of Responsibility"),
        ("M32", "Map of Responsibility and Culture"),
        ("M28", "Gameworld"),
    ]),
    ("Module 02", "Thoughtware · Thoughtmaps · Box Technology", "Day 2", [
        ("M02", "Map of Thoughtware"),
        ("M03", "Map of Thoughtmaps"),
        ("M04", "Anatomy of the Box"),
    ]),
    ("Module 03", "Liquid State · Center-Ground-Bubble · Five Bodies", "Day 3", [
        ("M05", "Liquid State"),
        ("M06", "Five Bodies"),
        ("M07", "Center, Grounding Cord, Bubble, Golden Cube"),
        ("M46", "Map of Matrix"),
    ]),
    ("Module 04", "Feedback · Coaching · Rapid Learning · Experiments", "Day 4", [
        ("M25", "Feedback and Coaching"),
        ("M26", "Rapid Learning"),
    ]),
    ("Module 05", "Feelings vs Emotions · Old Map · Numbness Bar", "Day 5", [
        ("M33", "Feelings vs Emotions"),
        ("M08", "Old Map of Feelings"),
        ("M09", "Numbness Bar"),
        ("M10", "New Map of Feelings"),
        ("M35", "Map of Feelings Sensations"),
        ("M37", "Fear Capacity Feelings Form"),
    ]),
    ("Module 06", "Mixed Emotions · Emotional Healing Process", "Day 6", [
        ("M11", "Mixed Emotions"),
        ("M12", "Emotional Healing Process"),
        ("M39", "Map of Optional Healing Process"),
        ("M38", "EHP Spaceholding Twins"),
        ("M40", "EHP Learnings"),
    ]),
    ("Module 07", "Low Drama · Gremlin Food · The Responsible Game", "Day 7", [
        ("M13", "Low Drama Triangle"),
        ("M27", "Your Gremlin"),
        ("M47", "Map of 3 Games"),
        ("M29", "Map of Reactivities"),
    ]),
    ("Module 08", "Listening · Speaking · Communication · Completion", "Day 8", [
        ("M14", "4 Listenings"),
        ("M15", "4 Speakings"),
        ("M43", "Letting Your Heart Speak"),
        ("M16", "Map of Communication"),
    ]),
    ("Module 09", "Ego States · Problem Ownership · Learning Spiral", "Day 9", [
        ("M17", "Ego States"),
        ("M18", "Problem Ownership"),
        ("M19", "Learning Spiral"),
    ]),
    ("Module 10", "Map of Possibility · Bright Principles · Three Powers", "Day 10", [
        ("M20", "Map of Possibility"),
        ("M44", "Linear and Nonlinear"),
        ("M21", "Bright Principles and Shadow Principles"),
        ("M22", "Is-Glue and Is-Glue Dissolver"),
        ("M23", "Three Powers (Choose, Ask Dangerous Questions, Declare)"),
    ]),
]


def _href_for(mnum, title):
    from urllib.parse import quote
    return quote(mnum + " - " + title + ".html")


INDEX_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Map Atlas · Expand the Box</title>
<meta name="description" content="The Map Atlas — the standalone, interactive companion to the 40 Possibility Management maps of the Expand the Box course, grouped by module. Each map taught on its own: study the map, walk its distinctions, run the recall deck.">
<link href="../_assets/fonts/fonts.css" rel="stylesheet">
<style>
:root {{
  --ivory: #f4ecdc; --ivory-shade: #ece2c8; --ivory-deep: #e3d7b9;
  --ink: #0e0a05; --ink-soft: #2a221a; --ink-mute: #4a3f30; --rule: #b8a98a;
  --vermillion: #c43b1c; --vermillion-deep: #962a13;
  --vermillion-soft: rgba(196, 59, 28, 0.08); --vermillion-glow: rgba(196, 59, 28, 0.32);
  --mustard: #d8b04a; --mustard-text: #b8902c; --mustard-soft: rgba(216, 176, 74, 0.18);
  --sky: #4a6b7c;
  --display: 'Fraunces', 'EB Garamond', Georgia, serif;
  --body: 'EB Garamond', Georgia, serif;
  --mono: 'JetBrains Mono', 'Courier New', monospace;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: var(--body); background: var(--ivory); color: var(--ink);
  font-size: 18px; line-height: 1.55; -webkit-font-smoothing: antialiased;
  min-height: 100vh; position: relative;
  background-image:
    radial-gradient(ellipse at top left, rgba(216, 176, 74, 0.06) 0%, transparent 40%),
    radial-gradient(ellipse at bottom right, rgba(196, 59, 28, 0.04) 0%, transparent 50%);
}}
body::before {{
  content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.5;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.055 0 0 0 0 0.04 0 0 0 0 0.02 0 0 0 0.18 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}}
a.skip-link {{ position: absolute; left: -9999px; top: 8px; z-index: 200; background: var(--ink); color: var(--ivory); font-family: var(--mono); font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; padding: 12px 18px; text-decoration: none; }}
a.skip-link:focus {{ left: 8px; }}
.wrap {{ max-width: 1100px; margin: 0 auto; padding: 36px 48px 80px; position: relative; z-index: 2; }}
header.top {{ display: flex; justify-content: space-between; align-items: baseline; font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-mute); padding-bottom: 32px; border-bottom: 1px solid var(--rule); gap: 24px; }}
header.top .left {{ display: flex; gap: 24px; flex-wrap: wrap; align-items: baseline; }}
header.top .right {{ display: flex; gap: 22px; flex-wrap: wrap; align-items: baseline; }}
header.top .num {{ color: var(--vermillion); font-weight: 500; }}
header.top .brand {{ color: var(--ink-mute); }}
header.top a {{ color: var(--ink-mute); text-decoration: none; border-bottom: 1px solid transparent; padding-bottom: 2px; transition: all 0.2s; }}
header.top a:hover {{ color: var(--vermillion); border-bottom-color: var(--vermillion); }}
header.top a:focus-visible {{ outline: 2px solid var(--vermillion); outline-offset: 3px; }}
.hero {{ margin: 48px 0 24px; max-width: 920px; }}
.eyebrow {{ font-family: var(--mono); font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase; color: var(--vermillion); margin-bottom: 16px; }}
h1.display {{ font-family: var(--display); font-weight: 350; font-size: clamp(44px, 6.5vw, 84px); font-variation-settings: 'opsz' 144, 'SOFT' 50, 'WONK' 1; line-height: 0.98; letter-spacing: -0.025em; margin-bottom: 22px; }}
h1.display em {{ font-style: italic; font-variation-settings: 'opsz' 144, 'SOFT' 100, 'WONK' 1; color: var(--vermillion); }}
.lede {{ font-family: var(--body); font-size: 21px; line-height: 1.5; color: var(--ink-soft); max-width: 800px; font-style: italic; }}
.hero .sub {{ font-family: var(--mono); font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--ink-mute); margin-top: 22px; }}
.hero .sub .count {{ color: var(--vermillion); font-weight: 700; }}
.dot-key {{ font-family: var(--mono); font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--ink-mute); margin-top: 14px; display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
.dot-key .dot {{ width: 9px; height: 9px; border-radius: 50%; display: inline-block; border: 1.5px solid var(--mustard-text); }}
.dot-key .dot.on {{ background: var(--mustard); border-color: var(--mustard-text); }}
.phase {{ margin-top: 56px; }}
.phase-head {{ display: flex; align-items: baseline; gap: 18px; flex-wrap: wrap; padding-bottom: 16px; border-bottom: 3px solid var(--vermillion); margin-bottom: 26px; }}
.phase-head .phase-num {{ font-family: var(--mono); font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase; color: var(--vermillion); font-weight: 500; }}
.phase-head h2 {{ font-family: var(--display); font-weight: 400; font-size: clamp(24px, 2.7vw, 33px); font-variation-settings: 'opsz' 144, 'SOFT' 50, 'WONK' 1; line-height: 1.05; letter-spacing: -0.015em; color: var(--ink); }}
.phase-head h2 em {{ font-style: italic; font-variation-settings: 'opsz' 144, 'SOFT' 100, 'WONK' 1; color: var(--vermillion); }}
.phase-head .phase-days {{ font-family: var(--mono); font-size: 10px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--ink-mute); margin-left: auto; }}
.card-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
@media (max-width: 900px) {{ .card-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
@media (max-width: 580px) {{ .card-grid {{ grid-template-columns: 1fr; }} }}
a.map-card {{ display: flex; flex-direction: column; gap: 12px; padding: 24px 26px; background: var(--ivory-shade); border: 1.5px solid var(--rule); border-left: 4px solid var(--vermillion); text-decoration: none; color: var(--ink); transition: transform 0.2s cubic-bezier(0.2, 0.7, 0.2, 1), box-shadow 0.2s, background 0.2s, border-color 0.2s; min-height: 132px; position: relative; }}
a.map-card:hover {{ transform: translateY(-3px); background: var(--ivory); border-left-color: var(--vermillion-deep); box-shadow: 0 14px 34px rgba(14, 10, 5, 0.16); }}
a.map-card:focus-visible {{ outline: 2px solid var(--vermillion); outline-offset: 3px; }}
a.map-card .mc-head {{ display: flex; justify-content: space-between; align-items: center; gap: 10px; }}
a.map-card .mc-num {{ font-family: var(--mono); font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--vermillion); font-weight: 700; }}
a.map-card .mc-dot {{ width: 9px; height: 9px; border-radius: 50%; border: 1.5px solid var(--rule); flex: none; }}
a.map-card .mc-dot.on {{ background: var(--mustard); border-color: var(--mustard-text); }}
a.map-card .mc-title {{ font-family: var(--display); font-weight: 400; font-size: 23px; font-variation-settings: 'opsz' 144, 'SOFT' 60, 'WONK' 1; line-height: 1.18; color: var(--ink); }}
a.map-card .mc-go {{ margin-top: auto; font-family: var(--mono); font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink-mute); transition: color 0.2s; }}
a.map-card:hover .mc-go {{ color: var(--vermillion); }}
.slot-note {{ grid-column: 1 / -1; font-family: var(--mono); font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--ink-mute); padding: 4px 2px 0; line-height: 1.6; }}
footer.bottom {{ margin-top: 72px; padding-top: 32px; border-top: 1px solid var(--rule); }}
footer.bottom .nav-row {{ display: flex; justify-content: space-between; flex-wrap: wrap; gap: 16px; font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-mute); }}
footer.bottom .nav-row a {{ color: var(--ink-mute); text-decoration: none; border-bottom: 1px solid transparent; padding-bottom: 2px; transition: all 0.2s; }}
footer.bottom .nav-row a:hover {{ color: var(--vermillion); border-bottom-color: var(--vermillion); }}
footer.bottom .nav-row a:focus-visible {{ outline: 2px solid var(--vermillion); outline-offset: 3px; }}
footer.bottom .license {{ margin-top: 26px; font-family: var(--mono); font-size: 10px; line-height: 1.7; letter-spacing: 0.04em; color: var(--ink-mute); max-width: 860px; }}
footer.bottom .license a {{ color: var(--ink-mute); text-decoration: underline; }}
footer.bottom .license a:hover {{ color: var(--vermillion); }}
footer.bottom .license .cc {{ color: var(--ink-soft); font-weight: 600; letter-spacing: 0.06em; }}
@media (max-width: 760px) {{ .wrap {{ padding: 24px 20px 60px; }} .phase-head .phase-days {{ margin-left: 0; width: 100%; }} }}
@media (prefers-reduced-motion: reduce){{ *,*::before,*::after{{ animation-duration:.001ms!important; animation-iteration-count:1!important; transition-duration:.001ms!important; scroll-behavior:auto!important; }} a.map-card:hover {{ transform: none; }} }}
</style>
</head>
<body>

<a href="#main" class="skip-link">Skip to the maps</a>

<div class="wrap">

  <header class="top">
    <div class="left">
      <span><span class="num">MAP ATLAS</span></span>
      <span class="brand">Expand the Box · Possibility Management</span>
    </div>
    <div class="right">
      <a href="../README.md">← Course</a>
      <a href="../Interactive Tools/index.html">Day tools →</a>
    </div>
  </header>

  <section class="hero" id="main">
    <div class="eyebrow">The Standalone Map Companion</div>
    <h1 class="display">Map <em>Atlas.</em></h1>
    <p class="lede">
      The Atlas is the standalone, interactive companion to the maps — each map taught on its own. Study the map, walk its distinctions, run the recall deck, flip its common misunderstandings, and keep a private reflection. One map at a time, at the pace of your body.
    </p>
    <p class="sub"><span class="count">{COUNT}</span> maps · grouped by course module · each one a self-contained teaching tool</p>
    <p class="dot-key"><span class="dot on" aria-hidden="true"></span> A filled dot means you have a saved note or reflection for that map on this device. Quiet presence only — no score, no streak.</p>
  </section>

{GROUPS}

  <footer class="bottom">
    <div class="nav-row">
      <a href="../README.md">← Expand the Box · course root</a>
      <a href="../Interactive Tools/index.html">Day-by-day tools →</a>
    </div>
    <p class="license">
      <span class="cc">🄯 World Copyleft 2026 · Expand the Box (Digital).</span>
      Licensed <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener">CC BY-SA 4.0</a>.
      Re-presents Possibility Management thoughtware originated by Clinton Callahan &amp; the Possibility Management community. Please share, share-alike.
      Powered by Possibility Management — <a href="https://possibilitymanagement.org" target="_blank" rel="noopener">possibilitymanagement.org</a>.
      Full terms: <code>LICENSE.md</code> in the course root. This Atlas is consistent with the spirit of World Copyleft; it is not an official Possibility Management product.
    </p>
  </footer>
</div>

<script>
/* Completion dots — quiet presence indicators only. A dot fills if the map's
   single localStorage key (etb_atlas_MXX) exists with a saved reflection.
   No scores, no streaks, no percentages. */
(function () {{
  document.querySelectorAll('a.map-card[data-mnum]').forEach(function (card) {{
    var mnum = card.getAttribute('data-mnum');
    var dot = card.querySelector('.mc-dot');
    if (!dot) return;
    var present = false;
    try {{
      var raw = localStorage.getItem('etb_atlas_' + mnum);
      if (raw) {{
        var d = JSON.parse(raw);
        present = !!(d && (d.reflection || d.said || d.embodied));
      }}
    }} catch (e) {{ present = false; }}
    if (present) {{ dot.classList.add('on'); dot.setAttribute('title', 'You have a saved note for this map on this device'); }}
  }});
}})();
</script>

<!-- World Copyleft 2026 — Expand the Box (Digital). Licensed CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/). Re-presents Possibility Management thoughtware originated by Clinton Callahan & the Possibility Management community. Please share, share-alike. Powered by Possibility Management — possibilitymanagement.org. Consistent with the spirit of World Copyleft; not an official Possibility Management product. Full terms: LICENSE.md in the course root. -->
</body>
</html>
"""


def render_index():
    total = sum(len(g[3]) for g in MODULE_GROUPS)
    groups_html = []
    for i, (label, sub, days, cards) in enumerate(MODULE_GROUPS, start=1):
        h2 = "<em>" + esc(sub) + "</em>"
        block = []
        block.append('  <section class="phase" aria-labelledby="m%d-h">' % i)
        block.append('    <div class="phase-head">')
        block.append('      <span class="phase-num">%s</span>' % esc(label))
        block.append('      <h2 id="m%d-h">%s</h2>' % (i, h2))
        block.append('      <span class="phase-days">%s</span>' % esc(days))
        block.append('    </div>')
        block.append('    <div class="card-grid">')
        for mnum, title in cards:
            href = _href_for(mnum, title)
            block.append('      <a class="map-card" data-mnum="%s" href="%s">' % (mnum, href))
            block.append('        <span class="mc-head"><span class="mc-num">%s</span><span class="mc-dot" aria-hidden="true"></span></span>' % mnum)
            block.append('        <span class="mc-title">%s</span>' % esc(title))
            block.append('        <span class="mc-go">Study the map →</span>')
            block.append('      </a>')
            if mnum == "M21":
                block.append('      <p class="slot-note">M21 · Bright &amp; Shadow Principles has no dedicated map image — the Map of Matrix (M46) and the Map of 3 Games (M47) are the adjacent maps; the card itself carries the full distinction.</p>')
        block.append('    </div>')
        block.append('  </section>')
        groups_html.append("\n".join(block))
    out = INDEX_TEMPLATE.replace("{COUNT}", str(total)).replace("{GROUPS}", "\n\n".join(groups_html))
    return out


# ----------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------
def main():
    written = []
    # 11 new pages
    for mnum in CONTENT:
        fn = FILENAMES[mnum]
        # filename must match content title byte-exact (guard)
        expect = mnum + " - " + CONTENT[mnum]["title"] + ".html"
        if fn != expect:
            print("FILENAME MISMATCH for %s: %r != %r" % (mnum, fn, expect), file=sys.stderr)
            sys.exit(2)
        path = os.path.join(ATLAS_DIR, fn)
        png = os.path.join(MAPS_DIR, mnum + ".png")
        if not os.path.exists(png):
            print("MISSING MAP IMAGE: %s" % png, file=sys.stderr)
            sys.exit(3)
        html_out = render_page(mnum)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_out)
        written.append(fn)

    # index regroup
    idx_path = os.path.join(ATLAS_DIR, "index.html")
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(render_index())
    written.append("index.html (regrouped)")

    print("gen_atlas.py — wrote %d files into %s" % (len(written), ATLAS_DIR))
    for w in written:
        print("  ·", w)


if __name__ == "__main__":
    main()
