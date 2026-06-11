#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Expand the Box v2 — build pipeline (W-B4).

Runs OFFLINE with the Python standard library only (Python 3.6+). It will use
the `markdown` package if it is installed, but ships a faithful built-in
converter as the default so the build never depends on network access.

What it does, idempotently, with a build-date stamp:

  1. RENDER  Days/*.md  ->  Course/module-NN.html
       Self-contained design-system pages (fonts at ../_assets/fonts/fonts.css),
       faithful markdown: headings, tables, blockquotes, images, code blocks,
       ordered/unordered lists, inline emphasis/code/links, horizontal rules,
       raw-HTML passthrough (<sub>, <br>).
       Link rewrites inside rendered pages:
         - links to sibling Day*.md          -> module-NN.html
         - links to other shipping .md / .html (../Practice, ../Map Atlas, ...) unchanged
         - ../Maps/*.png unchanged (same depth from Course/ as from Days/)
       Nav: prev/next module + breadcrumb to ../index.html on every page.

  2. EDITIONS
       EXPAND THE BOX v2 — Learner Edition.md   (START HERE + Days 00-11 + Practice/)
       EXPAND THE BOX v2 — Operator Edition.md  (README + Docs 00-05 + Facilitator Resources/)
       Generated, build-stamped, never hand-edited.

  3. LINK CHECKER (release gate)
       Crawls every internal href/src in all V2 .html and .md, writes
       _build/linkcheck-html.md, exits nonzero on real breakage.
       Atlas pages M(32|33|35|37|38|39|40|43|44|46|47) - *.html that are absent
       are reported PENDING (Executor B may be mid-build) and do NOT fail the build.

Usage:
    python3 _build/build.py            # full build
    python3 _build/build.py --check    # link-check only (no render)
"""

import os
import re
import sys
import html
import datetime
from urllib.parse import unquote

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD_DIR)                       # the V2 course root
DAYS_DIR = os.path.join(ROOT, "Days")
COURSE_DIR = os.path.join(ROOT, "Course")
PRACTICE_DIR = os.path.join(ROOT, "Practice")
FACIL_DIR = os.path.join(ROOT, "Facilitator Resources")

BUILD_DATE = datetime.date.today().isoformat()

# Pending-Atlas pattern (Executor B's 11 in-flight pages).
PENDING_ATLAS_RE = re.compile(
    r"M(?:32|33|35|37|38|39|40|43|44|46|47) - .*\.html$"
)

# Standard World Copyleft footer (Voice Guide §8) as inline HTML for Course pages.
FOOTER_LICENSE_HTML = (
    '<span class="cc">\U0001F12F World Copyleft 2026 · Expand the Box (Digital).</span> '
    'Licensed <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" '
    'rel="noopener">CC BY-SA 4.0</a>, consistent with the spirit of World Copyleft. '
    'Re-presents Possibility Management thoughtware originated by Clinton Callahan &amp; '
    'the Possibility Management community. This course is an independent re-presentation, '
    '<strong>not an official Possibility Management training</strong>. Please share, share-alike. '
    'Powered by Possibility Management — '
    '<a href="https://possibilitymanagement.org" target="_blank" rel="noopener">'
    'possibilitymanagement.org</a>. Full terms: <code>LICENSE.md</code> in the course root.'
)

LICENSE_COMMENT = (
    "<!-- World Copyleft 2026 — Expand the Box (Digital). Licensed CC BY-SA 4.0 "
    "(https://creativecommons.org/licenses/by-sa/4.0/). Re-presents Possibility "
    "Management thoughtware originated by Clinton Callahan & the Possibility Management "
    "community. This course is an independent re-presentation, not an official "
    "Possibility Management training. Please share, share-alike. Powered by Possibility "
    "Management — possibilitymanagement.org. Full terms: LICENSE.md in the course "
    "root. -->"
)

# ===========================================================================
# Minimal, faithful Markdown -> HTML converter (stdlib only).
# Handles: ATX headings, GFM tables, fenced code, blockquotes (with nesting
# collapsed to one level), ordered/unordered lists (incl. simple nesting),
# images, links, inline **bold** *italic* `code`, horizontal rules,
# raw-HTML-line passthrough, and unicode.
# ===========================================================================

_INLINE_CODE = re.compile(r"`([^`]+)`")
_IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)")
_BOLD = re.compile(r"\*\*([^*]+)\*\*")
_BOLD_U = re.compile(r"__([^_]+)__")
_ITALIC = re.compile(r"(?<![\*\w])\*([^*\n]+)\*(?![\*\w])")
_ITALIC_U = re.compile(r"(?<![_\w])_([^_\n]+)_(?![_\w])")

# A line that is "raw HTML" and should pass through untouched.
_RAW_HTML_LINE = re.compile(r"^\s*<(/?)(sub|sup|br|div|span|details|summary|img|hr)\b")


def _esc(text):
    return html.escape(text, quote=False)


def render_inline(text, link_rewriter=None):
    """Render inline markdown to HTML on an already block-level-isolated string.

    Code spans are protected first so their contents are never reinterpreted.
    """
    placeholders = []

    def _stash(html_fragment):
        placeholders.append(html_fragment)
        return "\x00{}\x00".format(len(placeholders) - 1)

    # 1. inline code (protect contents)
    def _code(m):
        return _stash("<code>{}</code>".format(_esc(m.group(1))))
    text = _INLINE_CODE.sub(_code, text)

    # 2. images (before links — they share bracket syntax)
    def _img(m):
        alt, src, title = m.group(1), m.group(2), m.group(3)
        if link_rewriter:
            src = link_rewriter(src)
        t = ' title="{}"'.format(_esc(title)) if title else ""
        return _stash('<img src="{}" alt="{}"{} loading="lazy">'.format(
            _esc(src), _esc(alt), t))
    text = _IMG.sub(_img, text)

    # 3. links
    def _a(m):
        label, href, title = m.group(1), m.group(2), m.group(3)
        if link_rewriter:
            href = link_rewriter(href)
        t = ' title="{}"'.format(_esc(title)) if title else ""
        ext = ""
        if href.startswith("http://") or href.startswith("https://"):
            ext = ' target="_blank" rel="noopener"'
        # render emphasis inside label, then stash
        inner = _emphasis(_esc(label))
        return _stash('<a href="{}"{}{}>{}</a>'.format(_esc(href), t, ext, inner))
    text = _LINK.sub(_a, text)

    # 4. emphasis on the remaining (non-stashed) text
    text = _esc(text)
    text = _emphasis(text)

    # 5. restore placeholders
    def _restore(m):
        return placeholders[int(m.group(1))]
    text = re.sub(r"\x00(\d+)\x00", _restore, text)
    return text


def _emphasis(text):
    text = _BOLD.sub(r"<strong>\1</strong>", text)
    text = _BOLD_U.sub(r"<strong>\1</strong>", text)
    text = _ITALIC.sub(r"<em>\1</em>", text)
    text = _ITALIC_U.sub(r"<em>\1</em>", text)
    return text


def md_to_html(md_text, link_rewriter=None):
    """Convert a markdown document body to an HTML fragment."""
    lines = md_text.split("\n")
    out = []
    i = 0
    n = len(lines)

    def flush_para(buf):
        if buf:
            joined = " ".join(s.strip() for s in buf)
            out.append("<p>{}</p>".format(render_inline(joined, link_rewriter)))
            buf.clear()

    para = []

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # fenced code block
        if stripped.startswith("```"):
            flush_para(para)
            lang = stripped[3:].strip()
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # consume closing fence
            cls = ' class="language-{}"'.format(_esc(lang)) if lang else ""
            out.append("<pre><code{}>{}</code></pre>".format(
                cls, _esc("\n".join(code_lines))))
            continue

        # blank line
        if stripped == "":
            flush_para(para)
            i += 1
            continue

        # horizontal rule
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            flush_para(para)
            out.append("<hr>")
            i += 1
            continue

        # ATX heading
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush_para(para)
            level = len(m.group(1))
            text = m.group(2).rstrip("#").strip()
            out.append("<h{0}>{1}</h{0}>".format(
                level, render_inline(text, link_rewriter)))
            i += 1
            continue

        # table (GFM): a header row, a separator row of ---|---, then body
        if "|" in line and i + 1 < n and re.match(
                r"^\s*\|?[\s:\-|]+\|[\s:\-|]*$", lines[i + 1]) and "-" in lines[i + 1]:
            flush_para(para)
            i = _emit_table(lines, i, out, link_rewriter)
            continue

        # blockquote
        if stripped.startswith(">"):
            flush_para(para)
            quote_lines = []
            while i < n and lines[i].strip().startswith(">"):
                quote_lines.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner = md_to_html("\n".join(quote_lines), link_rewriter)
            out.append("<blockquote>{}</blockquote>".format(inner))
            continue

        # lists (ordered / unordered), with simple one-level nesting
        if re.match(r"^\s*([-*+]|\d+\.)\s+", line):
            flush_para(para)
            i = _emit_list(lines, i, out, link_rewriter)
            continue

        # raw HTML line passthrough (e.g. the <sub> footer)
        if _RAW_HTML_LINE.match(line):
            flush_para(para)
            # collect consecutive raw-html lines, inline-render link/emphasis
            # inside so the footer's markdown links still work.
            out.append(_render_raw_html_line(line, link_rewriter))
            i += 1
            continue

        # default: paragraph text
        para.append(line)
        i += 1

    flush_para(para)
    return "\n".join(out)


def _render_raw_html_line(line, link_rewriter):
    """A line that begins with a known raw HTML tag. The footer uses <sub> with
    markdown links and **bold** inside; render those but keep the tag."""
    # split out the leading/trailing tag so inner markdown gets rendered
    m = re.match(r"^(\s*<[^>]+>)(.*?)(</[^>]+>\s*)$", line, re.DOTALL)
    if m:
        open_tag, inner, close_tag = m.group(1), m.group(2), m.group(3)
        return open_tag + render_inline(inner, link_rewriter) + close_tag
    return line


def _emit_table(lines, i, out, link_rewriter):
    n = len(lines)
    header = lines[i]
    sep = lines[i + 1]

    def cells(row):
        row = row.strip()
        if row.startswith("|"):
            row = row[1:]
        if row.endswith("|"):
            row = row[:-1]
        return [c.strip() for c in row.split("|")]

    aligns = []
    for c in cells(sep):
        c = c.strip()
        left = c.startswith(":")
        right = c.endswith(":")
        if left and right:
            aligns.append("center")
        elif right:
            aligns.append("right")
        elif left:
            aligns.append("left")
        else:
            aligns.append("")

    heads = cells(header)
    body_rows = []
    i += 2
    while i < n and "|" in lines[i] and lines[i].strip() != "":
        if lines[i].strip().startswith("#"):
            break
        body_rows.append(cells(lines[i]))
        i += 1

    html_parts = ["<table>", "<thead>", "<tr>"]
    for idx, h in enumerate(heads):
        a = aligns[idx] if idx < len(aligns) else ""
        style = ' style="text-align:{}"'.format(a) if a else ""
        html_parts.append("<th{}>{}</th>".format(
            style, render_inline(h, link_rewriter)))
    html_parts.append("</tr></thead><tbody>")
    for r in body_rows:
        html_parts.append("<tr>")
        for idx in range(len(heads)):
            val = r[idx] if idx < len(r) else ""
            a = aligns[idx] if idx < len(aligns) else ""
            style = ' style="text-align:{}"'.format(a) if a else ""
            html_parts.append("<td{}>{}</td>".format(
                style, render_inline(val, link_rewriter)))
        html_parts.append("</tr>")
    html_parts.append("</tbody></table>")
    out.append("".join(html_parts))
    return i


def _emit_list(lines, i, out, link_rewriter):
    """Emit a (possibly nested) list. Nesting handled to one extra level by
    indentation >= 2 spaces."""
    n = len(lines)

    def list_kind(s):
        if re.match(r"^\s*\d+\.\s+", s):
            return "ol"
        if re.match(r"^\s*[-*+]\s+", s):
            return "ul"
        return None

    base_indent = len(lines[i]) - len(lines[i].lstrip())
    kind = list_kind(lines[i])
    out.append("<{}>".format(kind))

    while i < n:
        line = lines[i]
        if line.strip() == "":
            # peek: blank then another list item continues the list
            j = i + 1
            while j < n and lines[j].strip() == "":
                j += 1
            if j < n and list_kind(lines[j]) and (
                    len(lines[j]) - len(lines[j].lstrip())) >= base_indent:
                i = j
                continue
            break
        indent = len(line) - len(line.lstrip())
        lk = list_kind(line)
        if lk is None or indent < base_indent:
            break
        if indent > base_indent and lk:
            # nested list
            i = _emit_list(lines, i, out, link_rewriter)
            # attach nested list into the previous <li> by leaving as-is;
            # simple structure is acceptable for these docs.
            continue
        # this item's content
        content = re.sub(r"^\s*(?:\d+\.|[-*+])\s+", "", line)
        # gather continuation lines (wrapped text, indented more, no new bullet)
        i += 1
        cont = []
        while i < n:
            nxt = lines[i]
            if nxt.strip() == "":
                break
            nind = len(nxt) - len(nxt.lstrip())
            if list_kind(nxt) and nind <= indent + 1:
                break
            if nind > indent:
                cont.append(nxt.strip())
                i += 1
            else:
                break
        full = content
        if cont:
            full = content + " " + " ".join(cont)
        out.append("<li>{}</li>".format(render_inline(full, link_rewriter)))

    out.append("</{}>".format(kind))
    return i


# ===========================================================================
# Link rewriting for Course pages
# ===========================================================================

# map "Day NN - ....md" (raw or %20-encoded) -> module-NN.html
_DAY_LINK_RE = re.compile(r"(?:\.\./Days/)?Day(?:%20|\s)0*(\d{1,2})(?:%20|\s)[^)\"#?]*\.md")


def course_link_rewriter(href):
    """Rewrite a single href found inside a Day .md being rendered to Course/.

    - links to a sibling Day*.md -> module-NN.html (preserve #fragment/?query)
    - everything else unchanged (../Maps/, ../Practice/, ../Map Atlas/, http...)
    """
    # split off fragment/query to preserve
    frag = ""
    m = re.search(r"([#?].*)$", href)
    if m:
        frag = m.group(1)
        core = href[:m.start()]
    else:
        core = href

    dm = _DAY_LINK_RE.match(core)
    if dm:
        nn = int(dm.group(1))
        return "module-{:02d}.html{}".format(nn, frag)
    return href


# ===========================================================================
# Course page template
# ===========================================================================

DAY_FILES = [
    "Day 00 - Start Here and Getting Your Container.md",
    "Day 01 - Orientation, New Context, Radical Responsibility.md",
    "Day 02 - Thoughtware, Thoughtmaps, Box Technology.md",
    "Day 03 - Liquid State, Center-Ground-Bubble, Five Bodies.md",
    "Day 04 - Feedback, Coaching, Rapid Learning, Experiments.md",
    "Day 05 - Feelings vs Emotions, Old Map of Feelings, Numbness Bar.md",
    "Day 06 - Mixed Emotions and Emotional Healing Process.md",
    "Day 07 - Low Drama, Gremlin Food, Shifting to Responsible Game.md",
    "Day 08 - Listening, Speaking, Communication, Completion Loops.md",
    "Day 09 - Ego States, Problem Ownership, Learning Spiral.md",
    "Day 10 - Map of Possibility, Bright Principles, Three Powers, Integration.md",
    "Day 11 - Continuation, 90-Day Container and Possibility Team.md",
]


def module_title(day_filename):
    """'Day 03 - Liquid State, ...' -> ('03', 'Liquid State, ...')."""
    m = re.match(r"Day (\d{2}) - (.*)\.md$", day_filename)
    return m.group(1), m.group(2)


COURSE_CSS = """
:root{
  --ivory:#f4ecdc; --ivory-shade:#ece2c8; --ivory-deep:#e3d7b9;
  --ink:#0e0a05; --ink-soft:#2a221a; --ink-mute:#4a3f30; --rule:#b8a98a;
  --vermillion:#c43b1c; --vermillion-deep:#962a13; --mustard:#d8b04a;
  --mustard-text:#b8902c; --sky:#4a6b7c; --green:#1d4d3a;
  --display:'Fraunces','EB Garamond',Georgia,serif;
  --body:'EB Garamond',Georgia,serif;
  --mono:'JetBrains Mono','Courier New',monospace;
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  font-family:var(--body); background:var(--ivory); color:var(--ink);
  font-size:18px; line-height:1.62; -webkit-font-smoothing:antialiased;
  min-height:100vh; position:relative;
  background-image:
    radial-gradient(ellipse at top left, rgba(216,176,74,0.06) 0%, transparent 40%),
    radial-gradient(ellipse at bottom right, rgba(196,59,28,0.04) 0%, transparent 50%);
}
body::before{
  content:''; position:fixed; inset:0; pointer-events:none; z-index:1; opacity:0.5;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.055 0 0 0 0 0.04 0 0 0 0 0.02 0 0 0 0.18 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
a.skip-link{position:absolute;left:-9999px;top:8px;z-index:200;background:var(--ink);
  color:var(--ivory);font-family:var(--mono);font-size:12px;letter-spacing:0.12em;
  text-transform:uppercase;padding:12px 18px;text-decoration:none;}
a.skip-link:focus{left:8px;}
.wrap{max-width:820px;margin:0 auto;padding:36px 48px 90px;position:relative;z-index:2;}

header.top{
  display:flex;justify-content:space-between;align-items:baseline;gap:24px;
  font-family:var(--mono);font-size:11px;letter-spacing:0.12em;text-transform:uppercase;
  color:var(--ink-mute);padding-bottom:32px;border-bottom:1px solid var(--rule);flex-wrap:wrap;}
header.top .num{color:var(--vermillion);font-weight:600;}
header.top a{color:var(--ink-mute);text-decoration:none;border-bottom:1px solid transparent;
  padding-bottom:2px;transition:all 0.2s;}
header.top a:hover{color:var(--vermillion);border-bottom-color:var(--vermillion);}
header.top a:focus-visible{outline:2px solid var(--vermillion);outline-offset:3px;}

.module-eyebrow{font-family:var(--mono);font-size:11px;letter-spacing:0.22em;
  text-transform:uppercase;color:var(--vermillion);margin:48px 0 14px;}

/* rendered markdown prose */
.prose{margin-top:8px;}
.prose h1{font-family:var(--display);font-weight:350;
  font-size:clamp(40px,6vw,72px);font-variation-settings:'opsz' 144,'SOFT' 50,'WONK' 1;
  line-height:1.0;letter-spacing:-0.025em;margin:0 0 28px;color:var(--ink);}
.prose h2{font-family:var(--display);font-weight:400;
  font-size:clamp(26px,3.2vw,38px);font-variation-settings:'opsz' 144,'SOFT' 50,'WONK' 1;
  line-height:1.08;letter-spacing:-0.015em;margin:52px 0 16px;color:var(--ink);
  padding-top:8px;border-top:1px solid var(--rule);}
.prose h3{font-family:var(--display);font-weight:500;font-size:24px;
  font-variation-settings:'opsz' 144,'SOFT' 50;line-height:1.15;margin:36px 0 12px;color:var(--ink);}
.prose h4{font-family:var(--mono);font-size:12px;letter-spacing:0.18em;text-transform:uppercase;
  color:var(--mustard-text);font-weight:600;margin:28px 0 10px;}
.prose p{margin:0 0 18px;color:var(--ink-soft);}
.prose strong{color:var(--ink);font-weight:600;}
.prose em{color:var(--ink);font-style:italic;}
.prose a{color:var(--vermillion-deep);text-decoration:none;
  border-bottom:1px solid rgba(150,42,19,0.35);transition:all 0.2s;}
.prose a:hover{border-bottom-color:var(--vermillion);color:var(--vermillion);}
.prose a:focus-visible{outline:2px solid var(--vermillion);outline-offset:2px;}
.prose ul,.prose ol{margin:0 0 20px 26px;color:var(--ink-soft);}
.prose li{margin-bottom:9px;}
.prose blockquote{margin:24px 0;padding:20px 28px;background:var(--ivory-shade);
  border-left:4px solid var(--vermillion);font-style:italic;color:var(--ink-soft);}
.prose blockquote p:last-child{margin-bottom:0;}
.prose hr{border:none;border-top:1px dashed var(--rule);margin:40px 0;}
.prose code{font-family:var(--mono);font-size:0.86em;background:var(--ivory-shade);
  padding:2px 6px;color:var(--vermillion-deep);border:1px solid var(--rule);}
.prose pre{background:var(--ink);color:var(--ivory);padding:22px 24px;overflow-x:auto;
  margin:0 0 22px;border-left:4px solid var(--vermillion);}
.prose pre code{background:none;border:none;color:var(--ivory);padding:0;font-size:14px;
  line-height:1.6;}
.prose img{max-width:100%;height:auto;display:block;margin:28px auto;border:1px solid var(--rule);
  background:var(--ivory-shade);padding:12px;box-shadow:0 14px 40px rgba(14,10,5,0.14);}
.prose table{width:100%;border-collapse:collapse;margin:0 0 26px;font-size:16px;}
.prose th,.prose td{border:1px solid var(--rule);padding:10px 14px;text-align:left;
  vertical-align:top;color:var(--ink-soft);}
.prose th{background:var(--ivory-shade);font-family:var(--mono);font-size:11px;
  letter-spacing:0.08em;text-transform:uppercase;color:var(--ink);font-weight:600;}
.prose sub{font-size:12px;color:var(--ink-mute);line-height:1.6;}
.prose sub a{color:var(--ink-mute);}

/* module nav */
nav.module-nav{display:flex;justify-content:space-between;gap:16px;margin:56px 0 0;
  padding-top:28px;border-top:1px solid var(--rule);flex-wrap:wrap;}
nav.module-nav a,nav.module-nav span{font-family:var(--mono);font-size:11px;
  letter-spacing:0.12em;text-transform:uppercase;text-decoration:none;color:var(--ink-mute);
  border:1.5px solid var(--rule);padding:12px 18px;transition:all 0.2s;max-width:46%;}
nav.module-nav a:hover{color:var(--vermillion);border-color:var(--vermillion);}
nav.module-nav a:focus-visible{outline:2px solid var(--vermillion);outline-offset:3px;}
nav.module-nav .nn-label{display:block;font-size:9px;letter-spacing:0.2em;color:var(--vermillion);
  margin-bottom:4px;}
nav.module-nav .disabled{opacity:0.4;}
nav.module-nav .next{text-align:right;margin-left:auto;}

footer.bottom{margin-top:60px;padding-top:30px;border-top:1px solid var(--rule);}
footer.bottom .nav-row{display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px;
  font-family:var(--mono);font-size:11px;letter-spacing:0.12em;text-transform:uppercase;
  color:var(--ink-mute);}
footer.bottom .nav-row a{color:var(--ink-mute);text-decoration:none;
  border-bottom:1px solid transparent;padding-bottom:2px;transition:all 0.2s;}
footer.bottom .nav-row a:hover{color:var(--vermillion);border-bottom-color:var(--vermillion);}
footer.bottom .license{margin-top:24px;font-family:var(--mono);font-size:10px;line-height:1.7;
  letter-spacing:0.04em;color:var(--ink-mute);max-width:760px;}
footer.bottom .license a{color:var(--ink-mute);text-decoration:underline;}
footer.bottom .license a:hover{color:var(--vermillion);}
footer.bottom .license .cc{color:var(--ink-soft);font-weight:600;letter-spacing:0.06em;}
.build-stamp{font-family:var(--mono);font-size:9px;letter-spacing:0.18em;text-transform:uppercase;
  color:var(--ink-mute);margin-top:18px;opacity:0.7;}

@media (max-width:760px){
  .wrap{padding:24px 20px 60px;}
  nav.module-nav a,nav.module-nav span{max-width:100%;}
}
@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{animation-duration:.001ms!important;animation-iteration-count:1!important;
    transition-duration:.001ms!important;scroll-behavior:auto!important;}
}
""".strip()


def render_course_page(idx, day_filename):
    nn, title = module_title(day_filename)
    src = os.path.join(DAYS_DIR, day_filename)
    with open(src, encoding="utf-8") as f:
        md = f.read()

    body_html = md_to_html(md, link_rewriter=course_link_rewriter)

    # prev / next
    prev_html = '<span class="prev disabled"><span class="nn-label">Start</span>The front door</span>'
    if idx > 0:
        pnn, ptitle = module_title(DAY_FILES[idx - 1])
        prev_html = ('<a class="prev" href="module-{:s}.html">'
                     '<span class="nn-label">← Module {:s}</span>{:s}</a>').format(
            "{:02d}".format(int(pnn)), pnn, _esc(ptitle))
    next_html = '<span class="next disabled"><span class="nn-label">End</span>Course complete</span>'
    if idx < len(DAY_FILES) - 1:
        nxn, ntitle = module_title(DAY_FILES[idx + 1])
        next_html = ('<a class="next" href="module-{:s}.html">'
                     '<span class="nn-label">Module {:s} →</span>{:s}</a>').format(
            "{:02d}".format(int(nxn)), nxn, _esc(ntitle))

    page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Module {nn} · {title_esc} · Expand the Box</title>
<meta name="description" content="Module {nn} of the Expand the Box course: {title_esc}.">
<meta name="generator" content="ETB build.py — generated page, do not hand-edit. Source: Days/{src_esc}">
<link href="../_assets/fonts/fonts.css" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to module</a>
<div class="wrap">
  <header class="top">
    <div><span class="num">EXPAND THE BOX</span> · Module {nn} of 11</div>
    <div><a href="../index.html">← Course front door</a></div>
  </header>

  <div class="module-eyebrow">Course · Module {nn}</div>

  <article class="prose" id="main">
{body}
  </article>

  <nav class="module-nav" aria-label="Module navigation">
    {prev}
    {next}
  </nav>

  <footer class="bottom">
    <div class="nav-row">
      <a href="../index.html">← Course front door</a>
      <a href="../Map%20Atlas/index.html">Map Atlas →</a>
      <a href="../Interactive%20Tools/index.html">Interactive Tools →</a>
    </div>
    <p class="license">{license}</p>
    <p class="build-stamp">Generated by build.py · {date} · do not hand-edit · source: Days/{src_esc}</p>
  </footer>
</div>
{comment}
</body>
</html>
""".format(
        nn=nn,
        title_esc=_esc(title),
        src_esc=_esc(day_filename),
        css=COURSE_CSS,
        body=body_html,
        prev=prev_html,
        next=next_html,
        license=FOOTER_LICENSE_HTML,
        date=BUILD_DATE,
        comment=LICENSE_COMMENT,
    )
    return page


def build_course():
    os.makedirs(COURSE_DIR, exist_ok=True)
    written = []
    for idx, day in enumerate(DAY_FILES):
        nn, _ = module_title(day)
        page = render_course_page(idx, day)
        out_path = os.path.join(COURSE_DIR, "module-{:02d}.html".format(int(nn)))
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page)
        written.append(os.path.basename(out_path))
    return written


# ===========================================================================
# Editions
# ===========================================================================

def _rewrite_edition_links(md_text, src_rel_dir):
    """For a combined-edition file living at the V2 root, rewrite links that were
    written relative to a subfolder so they still resolve from the root.

    Day files use ../ (root-relative); root docs use no prefix. We normalise:
    a link beginning with ../ from a file in `src_rel_dir` (one level deep)
    drops the ../ ; a bare relative link from a root file stays.
    Day-to-Day .md links are pointed at the in-file anchors via module names.
    """
    if src_rel_dir and src_rel_dir not in (".", ""):
        # file was one level deep (Days/, Practice/, Facilitator Resources/)
        def fix(m):
            label, href = m.group(1), m.group(2)
            if href.startswith("../"):
                href = href[3:]
            return "[{}]({})".format(label, href)
        md_text = re.sub(r"\[([^\]]+)\]\((\.\./[^)]+)\)", fix, md_text)
    return md_text


def build_edition(out_name, header_title, members, banner):
    """members: list of (relative_dir, filename) tuples to concatenate."""
    parts = []
    parts.append("<!-- GENERATED by _build/build.py on {} — DO NOT HAND-EDIT. "
                 "Edit the source files, then re-run the build. -->\n".format(BUILD_DATE))
    parts.append("# {}\n".format(header_title))
    parts.append("> {}\n".format(banner))
    parts.append("> **Generated {} by `_build/build.py`. Do not hand-edit "
                 "this file** — edit the sources and re-run the build.\n".format(BUILD_DATE))
    parts.append("\n---\n")

    for rel_dir, fname in members:
        path = os.path.join(ROOT, rel_dir, fname) if rel_dir else os.path.join(ROOT, fname)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            content = f.read()
        content = _rewrite_edition_links(content, rel_dir)
        label = fname[:-3] if fname.endswith(".md") else fname
        parts.append("\n\n<!-- ===== source: {} ===== -->\n".format(
            os.path.join(rel_dir, fname) if rel_dir else fname))
        parts.append("\n---\n\n")
        parts.append(content.rstrip() + "\n")

    out_path = os.path.join(ROOT, out_name)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("".join(parts))
    return out_name


def build_editions():
    learner_members = [("", "START HERE.md")]
    for day in DAY_FILES:
        learner_members.append(("Days", day))
    for p in ["Daily Practice Spine.md", "Beep Book Guide.md", "Feelings Form.md",
              "Coming Back.md", "My Map Book.md"]:
        learner_members.append(("Practice", p))
    build_edition(
        "EXPAND THE BOX v2 — Learner Edition.md",
        "Expand the Box v2 — Learner Edition (compiled)",
        learner_members,
        "Compiled learner reading order: the front door, all twelve modules "
        "(00–11), and the practice instruments. Links are rewritten to resolve "
        "from the course root.",
    )

    operator_members = [("", "README.md")]
    for d in ["00 - Course Manifest.md", "01 - Course Architecture and Pedagogy.md",
              "02 - Async Delivery Framework.md", "03 - Safety and Facilitation Framework.md",
              "04 - Container and Gatekeeping Protocol.md", "05 - Operator Run-Book.md"]:
        operator_members.append(("", d))
    # Facilitator Resources, alphabetical
    if os.path.isdir(FACIL_DIR):
        for fr in sorted(os.listdir(FACIL_DIR)):
            if fr.endswith(".md"):
                operator_members.append(("Facilitator Resources", fr))
    build_edition(
        "EXPAND THE BOX v2 — Operator Edition.md",
        "Expand the Box v2 — Operator Edition (compiled)",
        operator_members,
        "Compiled operator/contributor reference: the README, Docs 00–05, and "
        "the full Facilitator Resources pack. Links are rewritten to resolve from "
        "the course root.",
    )
    return [
        "EXPAND THE BOX v2 — Learner Edition.md",
        "EXPAND THE BOX v2 — Operator Edition.md",
    ]


# ===========================================================================
# Link checker (release gate)
# ===========================================================================

HREF_SRC_RE = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"')
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
MD_IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "#", "javascript:")
# directories we never crawl as link sources (still valid as targets)
SKIP_DIR_NAMES = {"_build"}
# generated compiled bundles: read as one flat document, so their inlined
# cross-references intentionally don't resolve as standalone files. They are
# build artifacts (like _build) and are excluded as link sources, not targets.
SKIP_FILE_NAMES = {
    "EXPAND THE BOX v2 — Learner Edition.md",
    "EXPAND THE BOX v2 — Operator Edition.md",
}


def iter_source_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_NAMES
                       and not d.startswith(".")]
        for fn in filenames:
            if fn in SKIP_FILE_NAMES:
                continue
            if fn.endswith(".html") or fn.endswith(".md"):
                yield os.path.join(dirpath, fn)


def extract_links(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    links = []
    if path.endswith(".html"):
        links += HREF_SRC_RE.findall(text)
    else:
        links += MD_LINK_RE.findall(text)
        links += MD_IMG_RE.findall(text)
    return links


def check_links():
    broken = []      # (source_rel, target, resolved_rel)
    pending = []     # (source_rel, target, resolved_rel)
    total = 0

    for path in iter_source_files():
        src_dir = os.path.dirname(path)
        src_rel = os.path.relpath(path, ROOT)
        for raw in extract_links(path):
            link = raw.strip()
            if not link or link.startswith(SKIP_PREFIXES):
                continue
            # strip fragment / query
            core = re.split(r"[#?]", link, 1)[0]
            if not core:
                continue
            total += 1
            decoded = unquote(core)
            target_path = os.path.normpath(os.path.join(src_dir, decoded))
            rel_target = os.path.relpath(target_path, ROOT)
            if os.path.exists(target_path):
                continue
            base = os.path.basename(target_path)
            if PENDING_ATLAS_RE.search(base):
                pending.append((src_rel, link, rel_target))
            else:
                broken.append((src_rel, link, rel_target))

    return total, broken, pending


def write_linkcheck_report(total, broken, pending):
    lines = []
    lines.append("# Link check — HTML + Markdown (V2)\n")
    lines.append("Generated by `_build/build.py` on **{}**. "
                 "Release gate: the build exits nonzero if any link is BROKEN. "
                 "PENDING links are Executor B's in-flight Atlas pages "
                 "(`M32/33/35/37/38/39/40/43/44/46/47 - *.html`) and do not fail "
                 "the build.\n".format(BUILD_DATE))
    lines.append("")
    lines.append("## Verdict\n")
    lines.append("| Metric | Count |")
    lines.append("|---|---|")
    lines.append("| Internal links crawled | {} |".format(total))
    lines.append("| **BROKEN** | **{}** |".format(len(broken)))
    lines.append("| PENDING (Atlas, Executor B) | {} |".format(len(pending)))
    lines.append("| Gate | {} |".format("FAIL" if broken else "PASS"))
    lines.append("")

    if broken:
        lines.append("## Broken links (gate failures)\n")
        lines.append("| Source file | Link | Resolves to |")
        lines.append("|---|---|---|")
        for s, l, r in sorted(broken):
            lines.append("| `{}` | `{}` | `{}` |".format(s, l, r))
        lines.append("")
    else:
        lines.append("## Broken links\n\nNone. ✓\n")

    if pending:
        lines.append("## Pending Atlas pages (Executor B — not a failure)\n")
        lines.append("| Source file | Link |")
        lines.append("|---|---|")
        seen = set()
        for s, l, r in sorted(pending):
            key = (s, l)
            if key in seen:
                continue
            seen.add(key)
            lines.append("| `{}` | `{}` |".format(s, l))
        lines.append("")
        # distinct pending targets
        targets = sorted({os.path.basename(unquote(re.split(r'[#?]', l, 1)[0]))
                          for _, l, _ in pending})
        lines.append("Distinct pending Atlas targets ({}):\n".format(len(targets)))
        for t in targets:
            lines.append("- `{}`".format(t))
        lines.append("")

    report_path = os.path.join(BUILD_DIR, "linkcheck-html.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return report_path


# ===========================================================================
# Main
# ===========================================================================

def main():
    check_only = "--check" in sys.argv
    print("ETB v2 build — {}".format(BUILD_DATE))
    print("Root: {}".format(ROOT))

    if not check_only:
        pages = build_course()
        print("\n[1/3] Course pages rendered ({}):".format(len(pages)))
        for p in pages:
            print("      Course/{}".format(p))

        editions = build_editions()
        print("\n[2/3] Editions generated:")
        for e in editions:
            print("      {}".format(e))

    print("\n[3/3] Link check (release gate):")
    total, broken, pending = check_links()
    report = write_linkcheck_report(total, broken, pending)
    print("      crawled : {} internal links".format(total))
    print("      BROKEN  : {}".format(len(broken)))
    print("      PENDING : {} (Executor B Atlas pages)".format(len(pending)))
    print("      report  : {}".format(os.path.relpath(report, ROOT)))

    if broken:
        print("\nGATE: FAIL — {} broken link(s). See the report.".format(len(broken)))
        for s, l, r in sorted(broken)[:25]:
            print("   BROKEN  {}  ->  {}".format(s, l))
        sys.exit(1)

    print("\nGATE: PASS — no broken links. "
          "({} Atlas page(s) still PENDING.)".format(len(pending)))
    sys.exit(0)


if __name__ == "__main__":
    main()
