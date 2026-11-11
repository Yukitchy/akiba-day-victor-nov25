#!/usr/bin/env python3
"""Akihabara day for Victor (sample). python3 build.py -> index.html. Data in data.py, CSS style.css, map map.js"""
import json
from data import *
gm = lambda q: 'https://www.google.com/maps/search/?api=1&query=' + q.replace(' ', '+')
A = lambda u, t: f'<a href="{u}" target="_blank" rel="noopener">{t}</a>'
links = lambda *ls: '<ul class="links">' + ''.join('<li>' + A(u, t) + '</li>' for t, u in ls) + '</ul>'
nums = lambda *ns: '<dl class="nums">' + ''.join(f'<div><dt>{a}</dt><dd class="n">{b}</dd><dd class="s">{c}</dd></div>' for a, b, c in ns) + '</dl>'
ph = lambda s, alt: f'<div class="ph"><img src="img/{s}" alt="{alt}"></div>'
nxt = lambda t: f'<div class="next"><p class="nl">Next</p><p>{t}</p></div>'
jp = lambda s: f' <small style="font-weight:500;color:var(--mute);font-size:.5em">{s}</small>' if s else ''
TITLE, SUB = 'Akihabara with Yuuki', 'One Piece, Frieren, Black Clover and Pokémon cards, in three hours.'
DESC = 'Wednesday 25 November, 10:00 to 13:00: a private Akihabara tour for two. Figures, capsule toys, anime goods and Pokémon cards, then lunch.'
OG = URL + 'img/og.jpg'
tt = ''.join(f'<tr class="st-plain"><td class="v">{t}</td><td><span class="k">{k}</span></td></tr>' for t, k in BAND)
chips = ''.join(f'<span style="display:inline-block;border:1px solid var(--ink);border-radius:14px;padding:1px 10px;margin:4px 6px 0 0;font-size:13px;font-weight:700">{t}</span>' for t in TASTES)
S = [f'<article class="step" data-i="0"><p class="no"><i>0</i>The whole day</p><h2>Three hours, <span class="l2">10:00 to <em>13:00</em></span></h2>'
     '<p class="lead">A private tour for two, all on foot inside one square kilometre. Five shops picked for your favourites, then lunch.</p>'
     f'<div>{chips}</div><div class="tt"><p class="cap">The day</p><table>{tt}</table></div>'
     f'<ul class="pts"><li><b>Good for</b><span>Figures, anime goods, capsule toys, Pokémon cards.</span></li><li><b>Keep in mind</b><span>Times are approximate and can move on the day. You do not have to buy anything: looking is half the fun.</span></li></ul></article>']
n = 1
S.append('<article class="step" data-i="1"><p class="no"><i>1</i>10:00</p><h2>We meet at <em>Vie de France</em></h2>'
         + ph('hero.jpg', 'Akihabara at night')
         + '<p class="lead">I wait inside Vie de France, a bakery cafe on the ground floor of BiTO AKIBA. It is the building right in front of the Electric Town exit of Akihabara station.</p>'
         + nums(('Time', '10:00', DATE_LONG), ('Finish', DONE, 'Akihabara station')) + links(('Meeting point on Google Maps', gm('Vie de France BiTO AKIBA')))
         + nxt('Walk 2 min to Radio Kaikan') + '</article>')
for i, nx in [(2, 'Walk 4 min north to TRADER'), (3, 'Walk 1 min to Animate'), (4, 'Walk 3 min to Gachapon Kaikan'), (5, 'Walk 6 min to lunch')]:
    s = STOPS[i]
    extra = f'<p class="note" style="font-size:14px">{SWAP}</p>' if i == 2 else ''
    S.append(f'<article class="step" data-i="{i}"><p class="no"><i>{i}</i>{s[5]}</p><h2><em>{s[0]}</em>{jp(s[4])}</h2>' + ph(s[7], s[3])
             + f'<p class="lead">{PITCH[i]}</p>' + nums(('Hours', s[6].replace('Open ', '').replace('Building ', ''), ''))
             + extra + links((s[3] + ' on Google Maps', gm(s[3]))) + nxt(nx) + '</article>')
POPS = []
def tile(l):
    a, nm, njp, gen, hrs, where, q, img = l; pid = 'pop-' + a
    POPS.append(f'<dialog class="pop" id="{pid}" aria-label="{nm}"><button type="button" class="pclose" aria-label="Close">✕</button><img class="pimg" src="img/{img}" alt="{gen}"><div class="pbody"><p class="gn">{gen}</p><h3>{nm}{jp(njp)}</h3>'
                f'<p class="rt">{hrs}<br>{where}</p><p class="pl"><a href="{gm(q)}" target="_blank" rel="noopener">Map ↗</a></p><p class="pc">Photo: example, not always the shop itself.</p></div></dialog>')
    return f'<button type="button" class="tile" data-pop="{pid}"><img src="img/{img}" alt="{gen}" loading="lazy"><span class="cb"><span class="gn">{gen}</span><b>{nm}</b></span></button>'
S.append('<article class="step" data-i="6"><p class="no"><i>6</i>12:25</p><h2><em>Lunch</em>, pick one of six</h2><p class="lead">Six places near the station, all open at lunchtime on a Wednesday. Tap a tile for details. Tell me what you feel like and we go.</p>'
         '<div class="cafes tiles">' + ''.join(tile(l) for l in LUNCH) + '</div><p class="asof">Hours from the Akihabara eatmap and Tabelog, checked 10 Nov 2026. If you would rather keep shopping, we skip lunch and stay longer at the shops.</p>'
         + f'<div class="next"><p class="nl">Finish</p><p>We are done at {DONE}, near Akihabara station.</p></div></article>')
credit = ('<footer class="credit"><p class="note" style="margin:0 0 10px">Times are approximate and can move on the day. Message Yuuki if you want to change anything. Sample plan.</p><details><summary>Photo credits</summary><ul>'
          '<li>Animate: Dick Thomas Johnson, CC BY 2.0</li><li>Radio Kaikan: Aimaimyi, CC BY-SA 3.0</li><li>TRADER (figure displays in Akihabara): Piotrus, CC BY-SA 3.0</li><li>Gachapon: Steve Nagata, CC BY 2.0</li><li>Night view: ElHeineken, CC BY 4.0</li><li>Lunch photos: Akihabara eatmap and Wikimedia Commons</li></ul>'
          '<p>Hours from the shops\' official sites, checked 10 Nov 2026. Map: Tiles © Esri / © ' + A('https://www.openstreetmap.org/copyright', 'OpenStreetMap') + '</p></details></footer>')
P = [None] + [(v[1], v[2], v[3], v[0], {1: 'l', 2: 'l', 3: 'r', 4: 'r', 5: 'r', 6: 'b'}[k], v[5]) for k, v in STOPS.items()]
P[1] = (P[1][0], P[1][1], P[1][2], 'Meet', 'r', P[1][5]); P[2] = P[2][:4] + ('l',) + P[2][5:]
dn = ''.join(f'<button type="button" class="dn" data-i="{i}" aria-label="stop {i}">{i}</button>' for i in range(len(P)))
head = ('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light"><meta name="robots" content="noindex,nofollow">'
        f'<title>{TITLE}</title><meta name="description" content="{DESC}"><meta property="og:title" content="{TITLE}"><meta property="og:description" content="{SUB}"><meta property="og:type" content="website"><meta property="og:url" content="{URL}">'
        f'<meta property="og:image" content="{OG}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
        '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 64 64%22%3E%3Crect width=%2264%22 height=%2264%22 fill=%22%23E5382B%22/%3E%3C/svg%3E">'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@500;700;900&display=swap">'
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css"><script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script><style>' + open('style.css').read() + '</style></head><body>')
intro = ('<div class="wrap"><div class="mapbox"><div id="map" aria-label="Map of the day"></div><p class="where"><small>Wed, November 25</small><b>The whole day</b></p>'
         '<nav class="dial"><button type="button" class="ar" data-d="-1" aria-label="Previous stop">&lsaquo;</button><div class="nums-r">' + dn + '</div><button type="button" class="ar" data-d="1" aria-label="Next stop">&rsaquo;</button></nav></div>'
         f'<main class="story"><header class="intro"><p class="date">{DATE_LONG} · 10:00 to {DONE}</p><h1>{TITLE}</h1><p class="who">For Victor Gonzalez and a friend. {SUB}</p>'
         f'<dl class="cn"><div><dt>Meet</dt><dd class="n">10:00</dd><dd class="s">Vie de France</dd></div><div><dt>Finish</dt><dd class="n">{DONE}</dd><dd class="s">Akihabara</dd></div></dl>'
         '<div class="tools"><a class="tool" href="victor-akiba-nov25.pdf" target="_blank" rel="noopener">Open the PDF (A4, 1 page)</a></div></header>')
LJ = [[35.69880, 139.77191, 'BiTO AKIBA', 'r']]
js = ('<script>const LI=99,LUNCH=%s,DAYS=%s,P=%s,GEO=[[35.6983,139.7732,"Akihabara Stn"]];' % (json.dumps(LJ), json.dumps(['The whole day'] + [v[5] for v in STOPS.values()]), json.dumps([None] + [[p[0], p[1], p[2], p[3], p[4], 0] for p in P[1:]]))) + open('map.js').read() + '</script>'
popjs = ("<script>document.querySelectorAll('.tile').forEach(function(t){t.addEventListener('click',function(){document.getElementById(t.dataset.pop).showModal()})});"
         "document.querySelectorAll('dialog.pop').forEach(function(d){d.addEventListener('click',function(e){if(e.target===d)d.close()});d.querySelector('.pclose').addEventListener('click',function(){d.close()})});</script>")
open('index.html', 'w').write(head + intro + ''.join(S) + credit + '</main></div>' + ''.join(POPS) + js + popjs + '<script src="devbar.js"></script></body></html>')
