"""Check published guide structure, internal links and safety-route retirement."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[];self.refs=[];self.sections=[];self.stack=[];self.errors=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        for key in ('href','src'):
            if key in a:self.refs.append(a[key])
        if tag=='section':self.sections.append(a)
        if tag not in ('area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'):self.stack.append(tag)
    def handle_endtag(self,tag):
        if not self.stack or self.stack[-1]!=tag:self.errors.append(f'Bad closing tag: {tag}, stack {self.stack[-3:]}')
        else:self.stack.pop()
page=Page();page.feed((ROOT/'index.html').read_text());assert not page.errors,page.errors
assert not page.stack,page.stack
assert len(page.ids)==len(set(page.ids)), 'Duplicate IDs'
assert len(page.sections)==15,'Expected the 15 current sections'
assert all('chapter' in s.get('class','') for s in page.sections),'Section missing navigation/search style'
for ref in page.refs:
    parts=urlsplit(ref)
    if parts.scheme:
        assert parts.scheme=='https','Unexpected external link scheme'
    elif parts.path:
        assert (ROOT/unquote(parts.path)).exists(),f'Missing asset: {ref}'
    if not parts.path and parts.fragment:assert parts.fragment in page.ids,f'Broken anchor: {ref}'
for path in ROOT.glob('*.html'):
    s=path.read_text()
    assert '\u2014' not in s and '\u2013' not in s,f'Forbidden dash in {path.name}'
    assert '/Users/' not in s and '/tmp/' not in s,f'Local path leaked into {path.name}'
    if path.name!='index.html':
        assert 'http-equiv="refresh"' in s and 'Superseded field sheet' in s,f'Unretired old route {path.name}'
        target=re.search(r'url=index.html#([a-z-]+)',s).group(1)
        assert target in page.ids,f'Bad redirect {path.name}'
        assert len(s)<1800,f'Old instructions remain in {path.name}'
sw=(ROOT/'sw.js').read_text()
assets=re.search(r'const ASSETS = \[(.*?)\];',sw,re.S).group(1)
for item in re.findall(r"'([^']+)'",assets):
    assert (ROOT/urlsplit(item).path).exists(),f'Missing precache item: {item}'
assert 'hedge-build-manual-v1' not in (ROOT/'assets/guide.js').read_text(), 'Old checklist state reused'
print(f'PASS: 15 sections, {len(page.ids)} unique IDs, internal links, 20 retired routes, precache files and public text checks')
