"""Render a cv-*.md resume to PDF. Usage: python3 tools/md2pdf.py companies/acme/cv-acme.md companies/acme/cv-acme.pdf"""
import re, sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, ListFlowable, ListItem

src, out = sys.argv[1], sys.argv[2]
NAVY = HexColor("#1f3a73")
GREY = HexColor("#444444")
base = dict(fontName="Helvetica", fontSize=9.5, leading=12.5)
S = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=18, leading=21, alignment=TA_CENTER, textColor=NAVY),
    "contact": ParagraphStyle("contact", fontSize=9.5, leading=12, alignment=TA_CENTER, textColor=GREY, fontName="Helvetica"),
    "body": ParagraphStyle("body", **base),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=NAVY, spaceBefore=8),
    "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10, leading=13, spaceBefore=6, spaceAfter=1),
    "sub": ParagraphStyle("sub", **base, spaceBefore=4, spaceAfter=1),
    "bullet": ParagraphStyle("bullet", **base),
}

def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    return t

lines = open(src).read().splitlines()
name = next((ln[2:].strip() for ln in lines if ln.startswith("# ")), "Resume")
blocks, cur = [], None  # merge wrapped lines into logical blocks
in_edu = False
for ln in lines:
    if ln.startswith("## "): in_edu = ln.strip() == "## Education"
    if not ln.strip():
        cur = None; continue
    if ln.startswith("  ") and cur is not None:
        cur[1] += " " + ln.strip(); continue
    if ln.startswith("- "):
        cur = ["li", ln[2:].strip()]; blocks.append(cur); continue
    if ln.startswith("#"):
        cur = None; blocks.append(["h", ln]); continue
    if cur is not None and cur[0] == "p" and not in_edu:
        cur[1] += " " + ln.strip(); continue
    cur = ["p", ln.strip()]; blocks.append(cur)

story, pending = [], []
def flush():
    global pending
    if pending:
        story.append(ListFlowable([ListItem(Paragraph(inline(b), S["bullet"]), leftIndent=10, value="•") for b in pending],
                                  bulletType="bullet", start="•", leftIndent=10, bulletFontSize=7, bulletOffsetY=-1))
        pending = []

first_p = True
for kind, text in blocks:
    if kind == "li":
        pending.append(text); continue
    flush()
    if kind == "h":
        lvl = len(text) - len(text.lstrip("#")); t = text.lstrip("#").strip()
        if lvl == 1:
            story.append(Paragraph(inline(t), S["name"]))
        elif lvl == 2:
            story.append(Paragraph(inline(t.upper()), S["h2"]))
            story.append(HRFlowable(width="100%", thickness=0.8, color=NAVY, spaceBefore=1, spaceAfter=3))
        else:
            story.append(Paragraph(inline(t), S["h3"]))
    else:
        if first_p:
            story.append(Paragraph(inline(text), S["contact"])); story.append(Spacer(1, 6)); first_p = False
        elif text.startswith("**"):
            story.append(Paragraph(inline(text), S["sub"]))
        else:
            story.append(Paragraph(inline(text), S["body"]))
flush()

doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=50, rightMargin=50, topMargin=40, bottomMargin=40,
                        title=f"{name} - Resume", author=name)
doc.build(story)
