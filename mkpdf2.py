#!/usr/bin/env python3
"""One-page A4 landscape PDF in the adopted Swiss (variant 2) design for the Victor page.
No route, no timeline, no per-stop times: frame (meet/finish) only, unnumbered shop cards.
Needs qrcode + playwright chromium. Run with /usr/local/bin/python3."""
import io, os, re, base64, tempfile
import qrcode

HERE = os.path.dirname(os.path.abspath(__file__))
URL = 'https://yukitchy.github.io/akiba-day-victor-nov25/'
OUT = os.path.join(HERE, 'victor-akiba-nov25')

def b64img(f):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(HERE, 'img', f), 'rb').read()).decode()

def sketch_svg():
    html = open(os.path.join(HERE, 'index.html')).read()
    m = re.search(r'<svg id="map".*?</svg>', html, re.S)
    assert m, 'map svg not found'
    svg = m.group(0)
    for f in ['radio-kaikan.jpg', 'trader.jpg', 'animate.jpg', 'gachapon.jpg']:
        svg = svg.replace(f'href="img/{f}"', f'href="{b64img(f)}"')
    return svg

def build_html():
    q = qrcode.make(URL, box_size=6, border=1)
    bb = io.BytesIO(); q.save(bb, 'PNG')
    qr = 'data:image/png;base64,' + base64.b64encode(bb.getvalue()).decode()
    photos = ''.join(f'<div><img src="{b64img(f)}" alt=""></div>' for f in ['hero.jpg', 'radio-kaikan.jpg', 'trader.jpg', 'animate.jpg'])
    shops = [
        ('Figures · Pokémon cards', 'Akihabara Radio Kaikan + BIG MAGIC', '秋葉原ラジオ会館 / BIG MAGIC 9F',
         'A tall building full of small shops. Figure floors for Evangelion, JoJo and Frieren, and BIG MAGIC on the 9th floor for Pokémon cards.'),
        ('Second-hand figures', 'TRADER Akihabara main store', 'トレーダー 秋葉原本店',
         'Three floors of second-hand figures sorted by series, so Evangelion, JoJo and Berserk are easy to hunt down, above floors of games.'),
        ('New anime goods', 'Animate Akihabara', 'アニメイト秋葉原',
         'Several floors of new anime and manga goods: new Frieren, Bocchi the Rock! and Edgerunners goods, with plenty of Evangelion and Pokémon too.'),
        ('Capsule toys', 'Akihabara Gachapon Kaikan', '秋葉原ガチャポン会館',
         'Hundreds of capsule toy machines. There are always Pokémon machines in the rows — try a few and keep what comes out.'),
    ]
    shop_html = ''.join(
        f'<div class="shop"><p class="genre">{g}</p><h3>{n} <span class="jp">{jp}</span></h3><p class="tx">{t}</p></div>'
        for g, n, jp, t in shops)
    lunch = [('Yakiniku Toraji', 'Yakiniku'), ('Kamadoka', 'Chicken, rice pots'), ('Juke Steak', 'Steak lunch'),
             ('Ootoya', 'Set meals'), ('Showa Shokudo', 'Diner set meals'), ('Kanda Tamagoken', 'Omurice')]
    lunch_html = ''.join(f'<div class="lunch"><b>{n}</b><span>{g}</span></div>' for n, g in lunch)
    chips = ''.join(f'<span>{t}</span>' for t in ['Evangelion', 'Frieren', 'JoJo', 'Bocchi the Rock!', 'Pokémon'])
    svg = sketch_svg()
    return f'''<!doctype html><meta charset="utf-8"><title>Akihabara for Victor — one-page sheet</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Noto+Sans+JP:wght@500;700;900&display=swap" rel="stylesheet">
<style>
@page{{size:A4 landscape;margin:0}}
*{{box-sizing:border-box}}html,body{{margin:0;padding:0}}
body{{font:11px/1.45 Archivo,"Noto Sans JP",sans-serif;color:#111;background:#fff}}
article{{width:297mm;height:209mm;padding:6mm 10mm;overflow:hidden;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;border-bottom:3px solid #111;padding-bottom:2mm;font-size:10px;font-weight:800;letter-spacing:.2em;text-transform:uppercase}}
h1{{font-weight:900;font-stretch:76%;font-size:37px;line-height:1.02;letter-spacing:-.015em;text-transform:uppercase;margin:3mm 0 2.5mm;white-space:nowrap}}
h1 em{{font-style:normal;color:#E2001A}}
.frame{{display:grid;grid-template-columns:auto auto 1fr;gap:1px;background:#111;border:1px solid #111}}
.frame .fi{{background:#fff;padding:1.8mm 3mm;font-size:12.5px}}
.ph{{display:grid;grid-template-columns:1.25fr 1fr 1fr 1fr;gap:4px;margin-top:3.5mm;height:27mm;flex:none}}
.ph div{{overflow:hidden}}.ph img{{display:block;width:100%;height:100%;object-fit:cover}}
.main{{display:grid;grid-template-columns:86mm 1fr;gap:7mm;margin-top:3.5mm;flex:1;min-height:0}}
.mapbox{{border:2.5px solid #111}}
.mapbox svg{{display:block;width:100%;height:auto}}
.pin .lbl{{display:block}}
.cap{{font-size:9.5px;color:#5A5A5A;margin:1.5mm 0 0}}
h2{{font-size:15px;font-weight:900;font-stretch:76%;text-transform:uppercase;margin:0 0 1mm;line-height:1.05}}
.shop{{border-top:1px solid #E3E3E3;padding:1.6mm 0}}
.shop:first-of-type{{border-top:none}}
.genre{{margin:0;font-size:9px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#E2001A}}
.shop h3{{margin:0;font-size:12.5px;font-weight:900;text-transform:uppercase}}
.shop h3 .jp{{font-size:10px;font-weight:700;color:#5A5A5A;text-transform:none}}
.shop .tx{{margin:0;font-size:10.5px;color:#333}}
.eat{{margin-top:3mm}}
.lgrid{{display:grid;grid-template-columns:1fr 1fr;gap:0.8mm 6mm}}
.lunch{{font-size:10.5px}}.lunch b{{font-weight:800}}.lunch span{{color:#5A5A5A;margin-left:2mm}}
.enote{{font-size:9.5px;color:#5A5A5A;margin:1.5mm 0 0}}
.foot{{display:flex;gap:4mm;align-items:center;margin-top:auto;border-top:2px solid #111;padding-top:2.5mm}}
.foot img{{width:15mm;height:15mm;flex:none}}
.foot p{{margin:0 0 1mm;font-size:9.5px;color:#555}}
.foot p b{{color:#111}}
.chips{{margin-left:auto;text-align:right;flex:none}}
.chips span{{display:inline-block;background:#111;color:#fff;font-size:9.5px;font-weight:900;letter-spacing:.05em;text-transform:uppercase;padding:1mm 2mm;margin:0 0 1mm 1mm}}
</style>
<article>
<header class="top"><span>Guest guide</span><span>Akihabara · Tokyo</span></header>
<h1>Akihabara <em>for Victor</em></h1>
<div class="frame"><span class="fi"><b>Wed 25 Nov</b></span><span class="fi"><b>10:00 – 13:00</b></span><span class="fi">Meet: <b>Vie de France, BiTO AKIBA PLAZA 1F</b>, 1-18-18 Sotokanda — inside the bakery cafe, in front of the Electric Town exit</span></div>
<div class="ph">{photos}</div>
<div class="main">
<div><div class="mapbox">{svg}</div><p class="cap">The four places are a few minutes apart on foot, inside Electric Town.</p></div>
<div>
<h2>The shops</h2>
{shop_html}
<div class="eat"><h2>Where we eat — we pick together</h2>
<div class="lgrid">{lunch_html}</div>
<p class="enote">Six places near the station, all open at lunchtime. We look, we talk, we choose — by appetite. Or we skip lunch and stay longer at the shops.</p></div>
</div>
</div>
<div class="foot"><img src="{qr}" alt=""><div><p><b>Full guide:</b> yukitchy.github.io/akiba-day-victor-nov25</p><p>Made for Victor Gonzalez and Romina Orozco, from Monterrey, Mexico · Guide: Yuuki · The plan is a sample — nothing is locked in, and the pace is ours on the day.</p></div><div class="chips">{chips}</div></div>
</article>'''

def main():
    html = build_html()
    tmp = os.path.join(tempfile.gettempdir(), 'victor-sheet2.html')
    open(tmp, 'w').write(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", args=["--no-sandbox"])
        pg = b.new_page(viewport={'width': 1123, 'height': 794})
        pg.goto('file://' + tmp)
        pg.wait_for_load_state('networkidle')
        pg.wait_for_timeout(2000)
        over = pg.evaluate("(()=>{const a=document.querySelector('article');return a.scrollHeight>a.clientHeight+1})()")
        pg.pdf(path=OUT + '.pdf', format='A4', landscape=True, print_background=True, prefer_css_page_size=True)
        pg.screenshot(path=OUT + '.png', full_page=False)
        b.close()
    d = open(OUT + '.pdf', 'rb').read()
    print('pages', len(re.findall(rb'/Type\s*/Page[^s]', d)), 'overflow', over, 'pdf bytes', len(d))

if __name__ == '__main__':
    main()
