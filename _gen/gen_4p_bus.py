# -*- coding: utf-8 -*-
"""
Project Hedge, SHEET E-2: 4P battery-to-bus schematic.

Emits the SVG for battery-wiring.html and the stud map table from the SAME
constants, so the drawing and the table can never disagree.

Run:  python3 _gen/gen_4p_bus.py > _gen/out.svg
      python3 _gen/gen_4p_bus.py --table > _gen/out-table.html

TOPOLOGY IS FINAL. GEOMETRY IS SCHEMATIC, NOT TO SCALE.
Cable cut lengths are deliberately NOT emitted here. They need three
measurements that are still open (battery post pitch and polarity, bus bar
length and stud pitch, bar placement on the board) and belong on a to-scale
sheet like deck-layout.html, not on a schematic.
"""
import sys

# ---- canvas ----
W, H = 1120, 700

# ---- bus geometry ----
BAR_H   = 24
POS_Y   = 140          # top of the + bus bars
NEG_Y   = 520          # top of the - bus bars
BAR_L_X, BAR_R_X, BAR_W = 130, 600, 390
STUD_L  = [175, 285, 395, 485]     # L1..L4
STUD_R  = [635, 725, 835, 945]     # R1..R4

# ---- batteries ----
BATT_W, BATT_H, BATT_Y = 104, 110, 300
BATT_CX = [285, 395, 725, 835]     # aligned to L2 L3 R2 R3
FUSE_Y  = 222                      # ANL row between packs and the + bus

# ---- end devices ----
INV   = dict(x=14,   y=176, w=104, h=118, label="INVERTER")
CHG   = dict(x=1002, y=176, w=104, h=118, label="CHARGERS")
LANE_CHG, LANE_INV = 596, 638      # the two long bottom returns

# ---- the stud map: single source of truth ----
# (stud, bus, what lands there, conductor, protection)
POS_MAP = [
 ("L1", "INVERTER +",      "2/0, ALONE on this stud", "80A DC breaker"),
 ("L2", "B1 +",            "2/0",                     "150A ANL"),
 ("L3", "B2 +",            "2/0",                     "150A ANL"),
 ("L4", "CHAIN LINK to R1","2/0 jumper",              "none, bus internal"),
 ("R1", "CHAIN LINK from L4","2/0 jumper",            "none, bus internal"),
 ("R2", "B3 +",            "2/0",                     "150A ANL"),
 ("R3", "B4 +",            "2/0",                     "150A ANL"),
 ("R4", "CHARGER GROUP +", "6ga + 10ga + 10ga, 3 rings", "70A / 30A / 10A"),
]
NEG_MAP = [
 ("L1", "CHARGER GROUP -", "6ga + 10ga + 10ga, 3 rings", "none, fused on +"),
 ("L2", "B1 -",            "2/0",                     "none, fused on +"),
 ("L3", "B2 -",            "2/0",                     "none, fused on +"),
 ("L4", "CHAIN LINK to R1","2/0 jumper",              "none, bus internal"),
 ("R1", "CHAIN LINK from L4","2/0 jumper",            "none, bus internal"),
 ("R2", "B3 -",            "2/0",                     "none, fused on +"),
 ("R3", "B4 -",            "2/0",                     "none, fused on +"),
 ("R4", "INVERTER -",      "2/0, ALONE on this stud", "none, breaker is on +"),
]

o = []
def a(s): o.append(s)
def txt(x, y, s, cls="", size=11.5, anchor="middle", extra=""):
    a(f'<text x="{x}" y="{y}" class="plan-lbl {cls}" font-size="{size}" '
      f'text-anchor="{anchor}"{extra}>{s}</text>')
def stud(x, y, col):
    a(f'<circle cx="{x}" cy="{y}" r="6.5" fill="var(--{col})" '
      f'stroke="var(--halo)" stroke-width="1.6"/>')

a(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="4P battery to bus bar wiring schematic">')
a('<defs><marker id="ar4" markerWidth="11" markerHeight="10" refX="7" refY="4" '
  'orient="auto" markerUnits="userSpaceOnUse">'
  '<path d="M0,0 L8,4 L0,8 Z" fill="context-stroke"/></marker></defs>')

# group bands, 2 + 2
a(f'<rect x="{BAR_L_X-14}" y="108" width="{BAR_W+28}" height="436" '
  f'fill="var(--pos)" opacity=".035" rx="10"/>')
a(f'<rect x="{BAR_R_X-14}" y="108" width="{BAR_W+28}" height="436" '
  f'fill="var(--pos)" opacity=".035" rx="10"/>')
txt(BAR_L_X+BAR_W/2, 100, "BAR PAIR L &#183; packs B1 B2", "soft", 11)
txt(BAR_R_X+BAR_W/2, 100, "BAR PAIR R &#183; packs B3 B4", "soft", 11)

# ---- bus bars ----
for bx in (BAR_L_X, BAR_R_X):
    a(f'<rect x="{bx}" y="{POS_Y}" width="{BAR_W}" height="{BAR_H}" rx="4" '
      f'fill="var(--pos-soft)" stroke="var(--pos)" stroke-width="2"/>')
    a(f'<rect x="{bx}" y="{NEG_Y}" width="{BAR_W}" height="{BAR_H}" rx="4" '
      f'fill="var(--neg-soft)" stroke="var(--neg)" stroke-width="2"/>')
txt(BAR_L_X-20, POS_Y+17, "+ BUS", "pos tag", 12.5, "end")
txt(BAR_L_X-20, NEG_Y+17, "&#8722; BUS", "neg tag", 12.5, "end")

# chain jumpers, one per bus
for y, col in ((POS_Y, "pos"), (NEG_Y, "neg")):
    a(f'<path d="M{STUD_L[3]},{y+12} L{STUD_R[0]},{y+12}" stroke="var(--{col})" '
      f'stroke-width="5" fill="none" stroke-linecap="round"/>')
txt((STUD_L[3]+STUD_R[0])/2, POS_Y-12, "2/0 CHAIN JUMPER", "soft", 10.5)
txt((STUD_L[3]+STUD_R[0])/2, NEG_Y-12, "2/0 CHAIN JUMPER", "soft", 10.5)

# stud dots + labels
for i, x in enumerate(STUD_L + STUD_R):
    name = (["L1","L2","L3","L4"] + ["R1","R2","R3","R4"])[i]
    stud(x, POS_Y+12, "pos"); stud(x, NEG_Y+12, "neg")
    txt(x, POS_Y-24, name, "tag", 11)
    txt(x, NEG_Y+40, name, "tag", 11)

# ---- batteries, fuses, leads ----
for i, cx in enumerate(BATT_CX):
    bx = cx - BATT_W/2
    a(f'<rect x="{bx}" y="{BATT_Y}" width="{BATT_W}" height="{BATT_H}" rx="7" '
      f'fill="var(--board)" stroke="var(--board-stroke)" stroke-width="2"/>')
    txt(cx, BATT_Y+44, f"B{i+1}", "tag", 17)
    a(f'<text x="{cx}" y="{BATT_Y+66}" class="plan-lbl soft" font-size="10" '
      f'text-anchor="middle">24V 100Ah</text>')
    a(f'<text x="{cx}" y="{BATT_Y+82}" class="plan-lbl soft" font-size="9.5" '
      f'text-anchor="middle">45.85 lb</text>')
    # positive lead up through its own ANL
    a(f'<path d="M{cx},{BATT_Y} L{cx},{FUSE_Y+26}" stroke="var(--pos)" '
      f'stroke-width="3.2" fill="none"/>')
    a(f'<rect x="{cx-25}" y="{FUSE_Y}" width="50" height="26" rx="4" '
      f'fill="var(--fuse-fill)" stroke="var(--fuse)" stroke-width="2"/>')
    txt(cx, FUSE_Y+17, "150A", "tag", 10.5)
    a(f'<path d="M{cx},{FUSE_Y} L{cx},{POS_Y+BAR_H}" stroke="var(--pos)" '
      f'stroke-width="3.2" fill="none"/>')
    # the unfused stub, called out once
    if i == 0:
        a(f'<path d="M222,{FUSE_Y+30} L{cx-14},{FUSE_Y+30}" stroke="var(--flag)" '
          f'stroke-width="1.2" stroke-dasharray="3 3" fill="none"/>')
        txt(172, FUSE_Y+52, "this stub is LIVE", "flag", 10)
        txt(172, FUSE_Y+64, "and UNFUSED", "flag", 10)
        txt(172, FUSE_Y+76, "keep it under 7 in", "flag", 10)
    # negative lead straight down
    a(f'<path d="M{cx},{BATT_Y+BATT_H} L{cx},{NEG_Y}" stroke="var(--neg)" '
      f'stroke-width="3.2" fill="none"/>')

# ---- inverter, far left, + on L1 ----
a(f'<rect x="{INV["x"]}" y="{INV["y"]}" width="{INV["w"]}" height="{INV["h"]}" rx="7" '
  f'fill="var(--paper)" stroke="var(--ink)" stroke-width="2"/>')
txt(INV["x"]+INV["w"]/2, INV["y"]+34, "INVERTER", "tag", 12)
txt(INV["x"]+INV["w"]/2, INV["y"]+54, "3000W", "soft", 10.5)
txt(INV["x"]+INV["w"]/2, INV["y"]+70, "24V", "soft", 10.5)
ix = INV["x"]+INV["w"]/2
a(f'<path d="M{INV["x"]+INV["w"]},{INV["y"]+30} L{STUD_L[0]},{INV["y"]+30} '
  f'L{STUD_L[0]},{POS_Y+BAR_H}" stroke="var(--pos)" stroke-width="4" fill="none"/>')
a(f'<rect x="{STUD_L[0]-62}" y="{INV["y"]+17}" width="52" height="26" rx="4" '
  f'fill="var(--paper)" stroke="var(--pos)" stroke-width="2"/>')
txt(STUD_L[0]-36, INV["y"]+34, "80A", "tag", 10.5)
a(f'<path d="M{ix},{INV["y"]+INV["h"]} L{ix},{LANE_INV} L{STUD_R[3]},{LANE_INV} '
  f'L{STUD_R[3]},{NEG_Y+BAR_H}" stroke="var(--neg)" stroke-width="4" fill="none"/>')
txt((ix+STUD_R[3])/2, LANE_INV+18, "INVERTER &#8722; runs to the FAR stud. "
    "This diagonal is what makes the four packs share evenly.", "soft", 10.5)

# ---- chargers, far right, + on R4 ----
a(f'<rect x="{CHG["x"]}" y="{CHG["y"]}" width="{CHG["w"]}" height="{CHG["h"]}" rx="7" '
  f'fill="var(--paper)" stroke="var(--ink)" stroke-width="2"/>')
txt(CHG["x"]+CHG["w"]/2, CHG["y"]+30, "CHARGERS", "tag", 12)
txt(CHG["x"]+CHG["w"]/2, CHG["y"]+48, "Tycon 70A", "soft", 10)
txt(CHG["x"]+CHG["w"]/2, CHG["y"]+62, "Iota 30A", "soft", 10)
txt(CHG["x"]+CHG["w"]/2, CHG["y"]+76, "DIN 10A", "soft", 10)
cx_ = CHG["x"]+CHG["w"]/2
a(f'<path d="M{CHG["x"]},{CHG["y"]+30} L{STUD_R[3]},{CHG["y"]+30} '
  f'L{STUD_R[3]},{POS_Y+BAR_H}" stroke="var(--pos)" stroke-width="3.2" fill="none"/>')
a(f'<path d="M{cx_},{CHG["y"]+CHG["h"]} L{cx_},{LANE_CHG} L{STUD_L[0]},{LANE_CHG} '
  f'L{STUD_L[0]},{NEG_Y+BAR_H}" stroke="var(--neg)" stroke-width="3.2" fill="none"/>')
txt((cx_+STUD_L[0])/2, LANE_CHG-9, "CHARGER RETURN, diagonally opposite the inverter", "soft", 10.5)

# ---- landing tally ----
txt(W/2, 42, "4P BUS: 8 STUDS PER POLARITY, 2 SPENT ON THE LINK, 6 LANDINGS USED", "tag", 13)
txt(W/2, 62, "4 packs  +  inverter  +  charger group  =  exactly 6. There is no spare stud.",
    "soft", 11)

# ---- legend ----
a(f'<rect x="{BAR_L_X}" y="{H-42}" width="{W-2*BAR_L_X}" height="0" fill="none"/>')
txt(BAR_L_X, H-14, "Red = positive   &#183;   Black = negative   &#183;   "
    "Every pack positive passes its OWN 150A ANL   &#183;   Negatives land straight on the bus   "
    "&#183;   Schematic, not to scale", "soft", 10.5, "start")
a('</svg>')

def table():
    rows = []
    for title, mp, cls in (("+ BUS", POS_MAP, "p"), ("&#8722; BUS", NEG_MAP, "n")):
        rows.append(f'<tr class="grp"><td colspan="4"><b>{title}</b> '
                    f'<span class="soft">bar pair L chained to bar pair R</span></td></tr>')
        for s, what, cond, prot in mp:
            link = ' class="link"' if "LINK" in what else ''
            rows.append(f'<tr{link}><td><span class="id {cls}">{s}</span></td>'
                        f'<td>{what}</td><td>{cond}</td><td>{prot}</td></tr>')
    return ("<table>\n<thead><tr><th>Stud</th><th>What lands here</th>"
            "<th>Conductor</th><th>Protection</th></tr></thead>\n<tbody>\n"
            + "\n".join(rows) + "\n</tbody>\n</table>")

if "--table" in sys.argv:
    print(table())
else:
    print("\n".join(o))
