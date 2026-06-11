#!/usr/bin/env python3
"""
_render_v1.py — v1 (May 2026) additive viewing shell renderer.
Renders the 10 Day .md files + START HERE → HTML in this folder.
ADDITIVE ONLY: does NOT touch any pre-existing file outside Course/.
Run from anywhere; paths are derived from this script's location.
"""
import os, re, html, pathlib, textwrap

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
V1_ROOT = SCRIPT_DIR.parent
DAYS_DIR = V1_ROOT / "Days"
START_HERE_SRC = V1_ROOT / "00 - START HERE (Learner Welcome).md"

ARCHIVE_BANNER = (
    'Archived May 2026 edition — the current course is the '
    '<a href="../Digital%20Expand%20The%20Box%20June%202026/index.html">'
    'June 2026 edition</a>.'
)

# ---- Day metadata (filename → output name, title, prev/next) ----
DAYS = [
    ("Day 01 - Orientation, New Context, Radical Responsibility.md",
     "day-01.html", "Day 1 — Orientation · New Context · Radical Responsibility"),
    ("Day 02 - Thoughtware, Thoughtmaps, Box Technology.md",
     "day-02.html", "Day 2 — Thoughtware · Thoughtmaps · Box Technology"),
    ("Day 03 - Liquid State, Center-Ground-Bubble, Five Bodies.md",
     "day-03.html", "Day 3 — Liquid State · Center-Ground-Bubble · Five Bodies"),
    ("Day 04 - Feedback, Coaching, Rapid Learning, Experiments.md",
     "day-04.html", "Day 4 — Feedback · Coaching · Rapid Learning · Experiments"),
    ("Day 05 - Feelings vs Emotions, Old Map of Feelings, Numbness Bar.md",
     "day-05.html", "Day 5 — Feelings vs Emotions · Old Map of Feelings · Numbness Bar"),
    ("Day 06 - Mixed Emotions and Emotional Healing Process.md",
     "day-06.html", "Day 6 — Mixed Emotions and Emotional Healing Process"),
    ("Day 07 - Low Drama, Gremlin Food, Shifting to Responsible Game.md",
     "day-07.html", "Day 7 — Low Drama · Gremlin Food · Shifting to Responsible Game"),
    ("Day 08 - Listening, Speaking, Communication, Completion Loops.md",
     "day-08.html", "Day 8 — Listening · Speaking · Communication · Completion Loops"),
    ("Day 09 - Ego States, Problem Ownership, Learning Spiral.md",
     "day-09.html", "Day 9 — Ego States · Problem Ownership · Learning Spiral"),
    ("Day 10 - Map of Possibility, Bright Principles, Three Powers, Integration.md",
     "day-10.html", "Day 10 — Map of Possibility · Bright Principles · Three Powers · Integration"),
]

# =====================================================================
# Minimal but faithful Markdown → HTML converter (stdlib only)
# Covers: ATX headings, setext, thematic breaks, paragraphs,
# bold/italic/code, blockquotes, fenced code, tables,
# ordered + unordered lists (including task lists), images, links,
# inline HTML passthrough, footnotes, <sub> passthrough.
# v1 content is rendered VERBATIM — bugs preserved as-is (archive).
# =====================================================================

def escape(s):
    """HTML-escape only the raw text; pass existing & entities through."""
    return html.escape(s, quote=False)

def inline(s):
    """Apply inline markdown: images, links, bold, italic, code, escape."""
    # Images: ![alt](src) — relative paths preserved verbatim
    s = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', lambda m:
        f'<img src="{m.group(2)}" alt="{escape(m.group(1))}" loading="lazy" style="max-width:100%;height:auto;display:block;margin:1.2em 0;">', s)
    # Links: [text](href)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m:
        f'<a href="{m.group(2)}">{escape(m.group(1))}</a>', s)
    # Bold-italic ***
    s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', s)
    # Bold **
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    # Italic *
    s = re.sub(r'\*([^*\n]+?)\*', r'<em>\1</em>', s)
    # Inline code `…`
    s = re.sub(r'`([^`]+)`', lambda m:
        f'<code>{html.escape(m.group(1))}</code>', s)
    return s

def render_table(rows_raw):
    """Convert a list of raw table row strings into an HTML table."""
    lines = [l.strip() for l in rows_raw if not re.match(r'^\|?[\s:|-]+\|', l)]
    out = ['<table>']
    for i, line in enumerate(lines):
        cells = [c.strip() for c in re.split(r'(?<!\|)\|(?!\|)', line.strip('|'))]
        tag = 'th' if i == 0 else 'td'
        row = ''.join(f'<{tag}>{inline(c)}</{tag}>' for c in cells)
        out.append(f'<tr>{row}</tr>')
    out.append('</table>')
    return '\n'.join(out)

def md_to_html(md_text):
    """Convert markdown string to an HTML <main> body string."""
    lines = md_text.splitlines()
    out = []
    i = 0

    def flush_list(items, ordered):
        tag = 'ol' if ordered else 'ul'
        res = [f'<{tag}>']
        for item in items:
            res.append(f'<li>{inline(item)}</li>')
        res.append(f'</{tag}>')
        return '\n'.join(res)

    # States
    in_blockquote = False
    bq_lines = []
    in_fenced = False
    fence_lang = ''
    fence_lines = []
    table_lines = []
    in_table = False
    list_items = []
    list_ordered = False
    in_list = False
    paragraph = []

    def flush_paragraph():
        if paragraph:
            txt = ' '.join(paragraph)
            out.append(f'<p>{inline(txt)}</p>')
            paragraph.clear()

    def flush_list_block():
        if list_items:
            out.append(flush_list(list_items, list_ordered))
            list_items.clear()

    def flush_bq():
        if bq_lines:
            inner = md_to_html('\n'.join(bq_lines))
            out.append(f'<blockquote>\n{inner}\n</blockquote>')
            bq_lines.clear()

    def flush_table():
        if table_lines:
            out.append(render_table(table_lines))
            table_lines.clear()

    while i < len(lines):
        line = lines[i]

        # Fenced code block
        if re.match(r'^```', line):
            if in_fenced:
                in_fenced = False
                code_content = html.escape('\n'.join(fence_lines))
                lang_class = f' class="language-{fence_lang}"' if fence_lang else ''
                out.append(f'<pre><code{lang_class}>{code_content}</code></pre>')
                fence_lines.clear()
                fence_lang = ''
            else:
                flush_paragraph()
                flush_list_block()
                flush_bq()
                flush_table()
                in_fenced = True
                fence_lang = line[3:].strip()
            i += 1
            continue

        if in_fenced:
            fence_lines.append(line)
            i += 1
            continue

        # Passthrough raw HTML tags (<sub>, etc.)
        if re.match(r'^\s*<', line):
            flush_paragraph()
            flush_list_block()
            flush_bq()
            flush_table()
            out.append(line)
            i += 1
            continue

        # Thematic break
        if re.match(r'^(\s*[-*_]){3,}\s*$', line) and re.sub(r'[\s\-*_]', '', line) == '':
            flush_paragraph()
            flush_list_block()
            flush_bq()
            flush_table()
            out.append('<hr>')
            i += 1
            continue

        # ATX headings
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            flush_paragraph()
            flush_list_block()
            flush_bq()
            flush_table()
            level = len(m.group(1))
            text = inline(m.group(2).rstrip('#').strip())
            out.append(f'<h{level}>{text}</h{level}>')
            i += 1
            continue

        # Table rows
        if '|' in line and re.match(r'.*\|', line):
            flush_paragraph()
            flush_list_block()
            flush_bq()
            table_lines.append(line)
            i += 1
            continue
        elif table_lines:
            flush_table()

        # Blockquote
        if line.startswith('>'):
            flush_paragraph()
            flush_list_block()
            flush_table()
            bq_lines.append(line[1:].lstrip())
            i += 1
            continue
        elif bq_lines:
            flush_bq()

        # Unordered list (- or * or +)
        m = re.match(r'^(\s*)[-*+]\s+(\[[ xX]\]\s+)?(.*)', line)
        if m:
            flush_paragraph()
            flush_table()
            flush_bq()
            task = m.group(2) or ''
            item_text = task + m.group(3) if task else m.group(3)
            if task:
                checked = 'x' in task.lower()
                checkbox = f'<input type="checkbox" disabled{"  checked" if checked else ""}> '
                item_text = checkbox + item_text
            list_items.append(item_text)
            list_ordered = False
            i += 1
            continue

        # Ordered list
        m = re.match(r'^\s*\d+\.\s+(.*)', line)
        if m:
            flush_paragraph()
            flush_table()
            flush_bq()
            list_items.append(m.group(1))
            list_ordered = True
            i += 1
            continue

        # Blank line
        if line.strip() == '':
            flush_paragraph()
            flush_list_block()
            flush_bq()
            flush_table()
            i += 1
            continue

        # Regular paragraph text
        flush_list_block()
        paragraph.append(line.strip())
        i += 1

    # Flush remaining
    flush_paragraph()
    flush_list_block()
    flush_bq()
    flush_table()
    if in_fenced and fence_lines:
        out.append(f'<pre><code>{html.escape(chr(10).join(fence_lines))}</code></pre>')

    return '\n'.join(out)


# =====================================================================
# Page template
# =====================================================================

DESIGN_CSS = """
:root {
  --ivory: #f4ecdc;
  --ivory-shade: #ece2c8;
  --ivory-deep: #e3d7b9;
  --ink: #0e0a05;
  --ink-soft: #2a221a;
  --ink-mute: #4a3f30;
  --rule: #b8a98a;
  --vermillion: #c43b1c;
  --vermillion-deep: #962a13;
  --vermillion-soft: rgba(196,59,28,0.08);
  --mustard: #d8b04a;
  --mustard-text: #b8902c;
  --sky: #4a6b7c;
  --display: 'Fraunces','EB Garamond',Georgia,serif;
  --body: 'EB Garamond',Georgia,serif;
  --mono: 'JetBrains Mono','Courier New',monospace;
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  font-family:var(--body);
  background:var(--ivory);
  color:var(--ink);
  font-size:18px;
  line-height:1.6;
  -webkit-font-smoothing:antialiased;
  min-height:100vh;
  background-image:
    radial-gradient(ellipse at top left,rgba(216,176,74,0.06) 0%,transparent 40%),
    radial-gradient(ellipse at bottom right,rgba(196,59,28,0.04) 0%,transparent 50%);
}
body::before{
  content:'';position:fixed;inset:0;pointer-events:none;z-index:1;opacity:0.5;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.055 0 0 0 0 0.04 0 0 0 0 0.02 0 0 0 0.18 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
.wrap{max-width:860px;margin:0 auto;padding:36px 40px 80px;position:relative;z-index:2;}
.archive-banner{
  font-family:var(--mono);font-size:11px;letter-spacing:0.10em;text-transform:uppercase;
  color:var(--ink-mute);background:var(--ivory-shade);border:1px solid var(--rule);
  border-left:3px solid var(--mustard);padding:10px 16px;margin-bottom:28px;
}
.archive-banner a{color:var(--ink-mute);text-decoration:underline;}
.archive-banner a:hover{color:var(--vermillion);}
nav.breadcrumb{
  font-family:var(--mono);font-size:11px;letter-spacing:0.12em;text-transform:uppercase;
  color:var(--ink-mute);padding-bottom:24px;border-bottom:1px solid var(--rule);
  margin-bottom:32px;display:flex;gap:16px;flex-wrap:wrap;align-items:baseline;
}
nav.breadcrumb a{color:var(--ink-mute);text-decoration:none;border-bottom:1px solid transparent;padding-bottom:2px;transition:all 0.2s;}
nav.breadcrumb a:hover{color:var(--vermillion);border-bottom-color:var(--vermillion);}
nav.breadcrumb .sep{color:var(--rule);}
nav.page-nav{
  display:flex;justify-content:space-between;align-items:center;
  margin-top:56px;padding-top:24px;border-top:1px solid var(--rule);
  font-family:var(--mono);font-size:11px;letter-spacing:0.10em;text-transform:uppercase;
  flex-wrap:wrap;gap:12px;
}
nav.page-nav a{
  color:var(--ink-mute);text-decoration:none;
  border:1px solid var(--rule);padding:8px 16px;
  transition:all 0.2s;
}
nav.page-nav a:hover{color:var(--vermillion);border-color:var(--vermillion);}
main h1{
  font-family:var(--display);font-weight:350;font-size:clamp(1.8rem,4vw,2.8rem);
  letter-spacing:-0.01em;line-height:1.15;color:var(--ink);margin:8px 0 32px;
}
main h2{
  font-family:var(--display);font-weight:350;font-size:1.5rem;
  color:var(--ink);margin:2.4em 0 0.6em;
}
main h3{
  font-family:var(--body);font-weight:700;font-size:1.05rem;
  color:var(--ink-soft);margin:2em 0 0.5em;
}
main h4{font-family:var(--body);font-weight:700;font-size:0.95rem;margin:1.6em 0 0.4em;}
main p{margin-bottom:1.1em;}
main a{color:var(--vermillion-deep);text-decoration:underline;}
main a:hover{color:var(--vermillion);}
main strong{font-weight:700;}
main em{font-style:italic;}
main code{
  font-family:var(--mono);font-size:0.82em;
  background:var(--ivory-shade);border:1px solid var(--rule);
  padding:1px 5px;border-radius:2px;
}
main pre{
  font-family:var(--mono);font-size:0.82em;
  background:var(--ivory-shade);border:1px solid var(--rule);
  padding:16px 20px;overflow-x:auto;margin:1.2em 0;line-height:1.45;
}
main pre code{background:none;border:none;padding:0;font-size:inherit;}
main blockquote{
  border-left:3px solid var(--vermillion);
  margin:1.4em 0;padding:12px 24px;
  background:var(--vermillion-soft);color:var(--ink-soft);
}
main blockquote p:last-child{margin-bottom:0;}
main table{
  width:100%;border-collapse:collapse;margin:1.4em 0;font-size:0.92em;
}
main th,main td{
  border:1px solid var(--rule);padding:8px 14px;text-align:left;
}
main th{background:var(--ivory-shade);font-family:var(--mono);font-size:0.8em;letter-spacing:0.06em;text-transform:uppercase;}
main ul,main ol{margin:0.6em 0 1em 1.8em;}
main li{margin-bottom:0.3em;}
main hr{border:none;border-top:1px solid var(--rule);margin:2.4em 0;}
main img{max-width:100%;height:auto;display:block;margin:1.4em auto;border:1px solid var(--rule);}
footer{
  font-family:var(--mono);font-size:10px;letter-spacing:0.08em;
  color:var(--ink-mute);text-align:center;
  padding:28px 40px;border-top:1px solid var(--rule);
  position:relative;z-index:2;
}
footer a{color:var(--ink-mute);text-decoration:underline;}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto;}}
@media(max-width:600px){.wrap{padding:24px 20px 60px;}}
"""

def page_html(title, body_html, prev_link, prev_label, next_link, next_label, is_start_here=False):
    depth_fonts = "../_assets/fonts/fonts.css"  # Course/ is one level below V1 root

    prev_nav = (f'<a href="{prev_link}">&#8592; {prev_label}</a>'
                if prev_link else '<span></span>')
    next_nav = (f'<a href="{next_link}">{next_label} &#8594;</a>'
                if next_link else '<span></span>')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)} · Expand the Box (May 2026 archive)</title>
<link rel="stylesheet" href="{depth_fonts}">
<style>
{DESIGN_CSS}
</style>
</head>
<body>
<div class="wrap">
  <div class="archive-banner">{ARCHIVE_BANNER}</div>
  <nav class="breadcrumb">
    <a href="../index.html">Expand the Box — May 2026</a>
    <span class="sep">/</span>
    <a href="../index.html#course">Course</a>
    <span class="sep">/</span>
    <span>{escape(title)}</span>
  </nav>
  <main>
{body_html}
  </main>
  <nav class="page-nav">
    {prev_nav}
    <a href="../index.html">&#8962; Front Door</a>
    {next_nav}
  </nav>
</div>
<footer>
  <p>Archived May 2026 edition &mdash; <a href="{depth_fonts.replace('_assets/fonts/fonts.css','')}"
     >current edition June 2026</a> &mdash;
  🄯 World Copyleft 2026 &middot; CC BY-SA 4.0 &middot;
  <a href="../LICENSE.md">LICENSE.md</a></p>
</footer>
</body>
</html>"""


def build():
    out_dir = SCRIPT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    # ----- Build Day pages -----
    all_pages = [("start-here.html", "Start Here")] + [(d[1], d[2]) for d in DAYS]
    # all_pages[0] = start-here, all_pages[1..10] = day-01..day-10

    # Start Here
    src = START_HERE_SRC.read_text(encoding='utf-8')
    body = md_to_html(src)
    prev_link, prev_label = None, None
    next_link, next_label = DAYS[0][1], "Day 1"
    html_out = page_html("Start Here", body, prev_link, prev_label, next_link, next_label, is_start_here=True)
    (out_dir / "start-here.html").write_text(html_out, encoding='utf-8')
    print("  Wrote: start-here.html")

    # Day pages
    for idx, (src_name, out_name, title) in enumerate(DAYS):
        src_path = DAYS_DIR / src_name
        md_text = src_path.read_text(encoding='utf-8')
        body = md_to_html(md_text)

        # prev
        if idx == 0:
            prev_link, prev_label = "start-here.html", "Start Here"
        else:
            prev_link, prev_label = DAYS[idx-1][1], f"Day {idx}"

        # next
        if idx < len(DAYS) - 1:
            next_link, next_label = DAYS[idx+1][1], f"Day {idx+2}"
        else:
            next_link, next_label = None, None

        html_out = page_html(title, body, prev_link, prev_label, next_link, next_label)
        (out_dir / out_name).write_text(html_out, encoding='utf-8')
        print(f"  Wrote: {out_name}")

    print("Done.")

if __name__ == '__main__':
    build()
