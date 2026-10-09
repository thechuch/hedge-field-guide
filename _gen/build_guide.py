"""Build static field guide. No network or runtime dependencies."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = [
('start','Start and next work'),('map','System map'),('equipment','Equipment status'),
('pv','PV and combiner'),('battery','Battery box'),('cabinets','Cabinets and fans'),
('thermal','Winter protection'),('bonding','Grounding and shared AC'),('surge','Surge protection'),
('spares','Protected spares'),('parts','Parts to arrange'),('commission','Release and test order'),
('field-log','Field notes'),('other','Water and other projects'),('record','Sources and offline use')]
content='\n'.join(path.read_text() for path in sorted((ROOT/'_content').glob('*.html')))
for num,(ident,title) in enumerate(SECTIONS,1):
    pattern=rf'<section id="{ident}" class="guide-section"([^>]*)>\s*<p class="eyebrow">(.*?)</p>\s*<h2([^>]*)>(.*?)</h2>'
    def heading(m):
        return f'<section id="{ident}" class="chapter" data-title="{title}"{m[1]}><div class="chapter-heading"><span class="number">{num:02}</span><div><p class="eyebrow">{m[2]}</p><h2{m[3]}>{m[4]}</h2></div></div>'
    content=re.sub(pattern,heading,content,flags=re.S)
nav='\n'.join(f'<a href="#{ident}"><span class="idx">{i:02}</span>{title}</a>' for i,(ident,title) in enumerate(SECTIONS,1))
options='\n'.join(f'<option value="{ident}">{i:02} · {title}</option>' for i,(ident,title) in enumerate(SECTIONS,1))
prefix='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#183c30"><meta name="description" content="Current Project Hedge field plan: solar, batteries, winter protection, bonding, surge protection and protected spares. Offline guide with private local field notes.">
<title>Hedge Field Guide | Current system plan</title><link rel="manifest" href="manifest.webmanifest"><link rel="icon" href="icon.svg"><link rel="apple-touch-icon" href="icon.svg"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="default"><link rel="stylesheet" href="assets/guide.css?v=2026.10.09-r1"><script src="assets/guide.js?v=2026.10.09-r1" defer></script></head>
<body><a class="skip-link" href="#start">Skip to the plan</a><header class="topbar"><a class="brand" href="./">HEDGE <span>FIELD GUIDE</span></a><span class="status" id="offlineStatus" role="status">Revision 2026.10.09-r1 · checking offline storage</span><button id="themeToggle" type="button" aria-label="Switch light or dark theme">Light / dark</button></header>
<div class="layout"><nav class="toc" aria-label="Guide sections"><p>In this guide</p>'''+nav+'''<p class="revision-note">Updated 9 October 2026<br>Revision 2026.10.09-r1<br><br>Design holds are shown at the point of use. Read them before work.</p></nav><main class="content" id="main">
<div id="updateNotice" class="notice" hidden><strong>A newer guide is saved.</strong><p>Reload to use the current instructions. Your saved field notes stay on this device.</p><button type="button" id="reloadGuide">Reload guide</button></div><div class="hero"><p class="eyebrow">Project Hedge · current field record</p><h1>The complete<br>system plan.</h1><p class="intro">Solar power, battery heating, protection and recovery. One guide for the equipment you have and the work still needed.</p><div class="hero-meta"><span>24 V · 1500 W solar · 4P bank</span><span>Offline field reference</span><span>Rev 2026.10.09-r1</span></div></div>
<div class="toolbar"><div class="mobile-nav"><label for="sectionSelect" class="visually-hidden">Jump to a section</label><select id="sectionSelect" aria-label="Jump to a section">'''+options+'''</select></div><div class="searchbox"><label for="searchGuide" class="visually-hidden">Search the guide</label><input id="searchGuide" type="search" placeholder="Search: combiner, ground, heater…" autocomplete="off"></div><button id="expandDetails" class="secondary" type="button">Open details</button></div><div id="searchStatus" class="search-status" role="status"></div><div class="empty-search" id="noResults" hidden>No matching section. Try a shorter term or clear the search.</div>
'''
footer='''<footer class="footer">Project Hedge · 2026.10.09-r1 · Public field reference<br>Check the current revision and the delivered equipment instructions before work.</footer></main></div></body></html>'''
(ROOT/'index.html').write_text(prefix+content+footer)
print(f'Built index.html: {len(content):,} content characters')
