#!/usr/bin/env python3
"""Akihabara day for Victor (sample), 12/10-page design. python3 build.py -> index.html. Data: data.py, CSS: dec10.css (verbatim copy of kagurazaka-ikebukuro-dec10)."""
from data import *
from html import escape as E
gm = lambda q: 'https://www.google.com/maps/search/?api=1&amp;query=' + q.replace(' ', '+')
CLOCK = '<svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 4.5V8l2.5 1.8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
TITLE = 'Akihabara for Victor'
DESC = 'A private Akihabara tour for Victor Gonzalez and a friend: figures, anime goods, capsule toys and Pokémon cards, then lunch. Wednesday 25 November, 10:00 to 13:00, guided by Yuuki.'
OGD = 'Figures, anime goods and Pokémon cards in Akihabara, Wednesday 25 November, 10:00 to 13:00.'
css = open('dec10.css').read()
# (n, tile tag, tile name, genre, card photo)
CARDS = {2: ('Figures &amp; cards', 'RADIO KAIKAN', 'Figures &middot; Pok&eacute;mon cards', 'radio-kaikan.jpg'),
         3: ('Used figures', 'TRADER', 'Second-hand figures', 'trader.jpg'),
         4: ('Anime goods', 'ANIMATE', 'New anime goods', 'animate.jpg'),
         5: ('Capsule toys', 'GACHAPON KAIKAN', 'Capsule toys', 'gachapon.jpg')}
PIN = {2: (470, 395), 3: (340, 290), 4: (470, 200), 5: (330, 120)}
SHORT = {2: 'Radio Kaikan', 3: 'TRADER', 4: 'Animate', 5: 'Gachapon Kaikan'}
no = lambda i: f'{i - 1:02d}'

pins = clips = ''
for i, (x, y) in PIN.items():
    n = i - 1; w = 12 * len(SHORT[i]) // 2 + 30
    clips += f'<clipPath id="pc{n}"><rect x="-21" y="-49" width="42" height="39" rx="2"/></clipPath>'
    pins += (f'<a class="pin" href="#p{n}" data-n="{n}"><g transform="translate({x} {y})"><polygon points="-6,-8 6,-8 0,0" fill="#121212"/>'
             f'<rect class="fr" x="-23" y="-64" width="46" height="56" rx="3" fill="#121212" stroke="#fff" stroke-width="1.5"/>'
             f'<image href="img/{CARDS[i][3]}" x="-21" y="-49" width="42" height="39" preserveAspectRatio="xMidYMid slice" clip-path="url(#pc{n})"/>'
             f'<text y="-52" text-anchor="middle" font-size="11" font-weight="900" fill="#fff">{n}</text>'
             f'<g class="lbl"><rect x="-{w // 2}" y="-94" width="{w}" height="26" fill="#121212"/><text y="-76" text-anchor="middle" font-size="13" font-weight="800" fill="#fff">{E(SHORT[i])}</text></g></g></a>')
grid = ''.join(f'<line x1="{x}" y1="-60" x2="{x}" y2="540" stroke="#fff" stroke-width="16"/>' for x in (70, 205, 340, 470, 560)) \
     + ''.join(f'<line x1="150" y1="{y}" x2="670" y2="{y}" stroke="#fff" stroke-width="16"/>' for y in (70, 200, 330, 470, 600))
svg = (f'<svg id="map" viewBox="195 -6 420 478" role="img" aria-label="Simple sketch map of the four places in Akihabara"><defs>{clips}</defs>'
       f'<rect x="150" y="-60" width="520" height="600" fill="#F6F1E6"/>{grid}<rect x="215" y="395" width="150" height="44" fill="#E4E0D6"/>'
       '<circle cx="420" cy="240" r="160" fill="none" stroke="#121212" stroke-width="2" stroke-dasharray="7 6"/>'
       '<text x="290" y="415" text-anchor="middle" font-size="14" font-weight="800" fill="#121212">AKIHABARA</text><text x="290" y="432" text-anchor="middle" font-size="14" font-weight="800" fill="#121212">STATION</text>'
       '<text x="405" y="458" text-anchor="middle" font-size="13" font-weight="700" fill="#5D5A54">dashed circle: Electric Town, all on foot</text>' + pins + '</svg>')

tl = [('10:00', 'Meet at Vie de France, BiTO AKIBA 1F', 'I wait inside this bakery cafe on the ground floor, right in front of the Electric Town exit of Akihabara station.'),
      ('10:10', 'Radio Kaikan + BIG MAGIC', 'A tall building of small shops: figures on the figure floors, Pok&eacute;mon cards at BIG MAGIC on 9F &mdash; <a href="#p1">place 01</a>.'),
      ('11:00', 'TRADER', 'Three floors of second-hand figures sorted by series &mdash; <a href="#p2">place 02</a>.'),
      ('11:30', 'Animate', 'New anime and manga goods &mdash; <a href="#p3">place 03</a>.'),
      ('11:55', 'Gachapon Kaikan', 'Hundreds of capsule toy machines &mdash; <a href="#p4">place 04</a>.'),
      ('12:25', 'Lunch &mdash; we pick one of six', 'All near the station. We choose together from the six under &ldquo;Where we eat&rdquo;, by appetite.'),
      ('13:00', 'Finish at Akihabara station', 'We end where we started, a few steps from the ticket gates.')]
tl = ''.join(f'<li><b>{t}</b><span>{a}<em>{b}</em></span></li>' for t, a, b in tl)

tiles = ''.join(f'<a class="tile" href="#p{i-1}"><img src="img/{c[3]}" alt="" loading="lazy"><b class="no">{no(i)}</b><span class="tt">{c[0]}</span><span class="tn">{c[1]}</span></a>' for i, c in CARDS.items())
cards = ''
for i, c in CARDS.items():
    s = STOPS[i]; n = i - 1
    cards += (f'<article class="card" id="p{n}"><div class="hd"><span class="big">{no(i)}</span><div><span class="genre">{c[2]}</span><h3>{E(s[3].upper())}</h3><p class="jp" lang="ja">{s[4]}</p></div></div>'
              f'<img class="ph" src="img/{c[3]}" alt="{E(s[3])}" loading="lazy"><p class="tx">{E(PITCH[i])}</p>'
              f'<p class="strip"><span>{CLOCK}<b class="today">{E(s[6])}</b></span></p><p class="hrs">{E(s[6])} (shop&rsquo;s official site, checked on 10 Nov 2026)</p>'
              f'<div class="bt"><a class="btn" href="{gm(s[3])}" target="_blank" rel="noopener">Google Maps <i>&rarr;</i></a></div></article>')

LD = {'a': 'Yakiniku, grilled meat, with lunch sets. One minute from the station.',
      'b': 'Chicken and rice cooked in iron pots, on the 6th floor of BiTO AKIBA &mdash; the building where we meet.',
      'c': 'A steak lunch place, three minutes from the station.',
      'd': 'A set-meal restaurant, on the 4th floor of BiTO AKIBA &mdash; the building where we meet.',
      'e': 'A diner serving set meals, three minutes from the station. Cash only.',
      'f': 'Omurice, the Japanese-style rice omelette, five minutes from the station.'}
lt = pops = ''
for a, nm, njp, gen, hrs, where, q, img in LUNCH:
    lt += f'<button type="button" class="ltile" data-pop="lpop-{a}"><img src="img/{img}" alt="Example photo: {E(gen)}" loading="lazy"><span class="lcb"><span class="lgn">{E(gen)}</span><b>{E(nm)}</b></span></button>'
    pops += (f'<dialog class="lpop" id="lpop-{a}" aria-label="{E(nm)}"><button type="button" class="pclose" aria-label="Close">&#10005;</button><img class="pimg" src="img/{img}" alt="Example photo: {E(gen)}">'
             f'<div class="pbody"><p class="lgn">{E(gen)}</p><h3>{E(nm)}</h3><p class="ljp" lang="ja">{njp}</p><p class="pt">{LD[a]}</p><p class="rt">{E(hrs)}<br>{E(where)}</p>'
             f'<p class="pl"><a href="{gm(q)}" target="_blank" rel="noopener">Map &#8599;</a></p><p class="pc">Photo: example, not always the shop itself. Hours from the Akihabara eatmap and Tabelog, checked on 10 Nov 2026.</p></div></dialog>')
chips = ''.join(f'<span>{E(t)}</span>' for t in TASTES)

head = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{TITLE}</title>
<meta name="robots" content="noindex,nofollow">
<meta name="description" content="{E(DESC)}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{E(OGD)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{URL}img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 64 64%22%3E%3Crect width=%2264%22 height=%2264%22 fill=%22%23D9342B%22/%3E%3C/svg%3E">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Noto+Sans+JP:wght@500;700;900&display=swap" rel="stylesheet">
<style>
{css}</style>
</head>
<body>
<div class="col">
<div class="top">
<span>GUEST GUIDE</span>
<span class="topr">
<span>AKIHABARA &middot; 4 PLACES</span>
<button type="button" class="sharebtn hd-share" id="copyLink" aria-label="Copy link to this page" title="Copy link">
<svg class="ic-share" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 15V4"/><path d="M7.5 8L12 3.5L16.5 8"/><path d="M5 13v7h14v-7"/></svg>
<svg class="ic-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
</button>
</span>
</div>
<h1>Places to visit in <em>Akihabara</em></h1>
</div>
<div class="col" style="padding:0">
<div class="hero" id="hero">
<img src="img/hero.jpg" alt="Akihabara Electric Town at night">
<img class="sl2" src="img/animate.jpg" alt="Animate Akihabara">
<div class="vt"><span class="on">秋葉原</span><span>アニメ</span></div>
<div class="hdots"><button type="button" class="on" aria-label="Show Akihabara"></button><button type="button" aria-label="Show anime shops"></button></div>
</div>
<script>
(function(){{var h=document.getElementById('hero');if(!h)return;var sl=h.querySelector('.sl2'),vt=h.querySelectorAll('.vt span'),dt=h.querySelectorAll('.hdots button'),cur=0,timer=null;function show(n){{cur=n;sl.classList.toggle('on',n===1);for(var i=0;i<2;i++){{vt[i].classList.toggle('on',i===n);dt[i].classList.toggle('on',i===n);}}}}function auto(){{timer=setInterval(function(){{show(1-cur);}},4500);}}for(var i=0;i<2;i++){{(function(n){{dt[n].addEventListener('click',function(){{if(timer)clearInterval(timer);show(n);auto();}});}})(i);}}auto();}})();
</script>
<div class="hb">
<span>Wed 25 Nov &middot; 10:00 to 13:00</span>
<b>Meet at Vie de France, BiTO AKIBA 1F</b>
</div>
</div>
<div class="col">
<section class="intro e">
<p class="ie-for">Made for Victor &middot; for you and a friend &middot; Guide: Yuuki &middot; Length: 3 hours</p>
<div class="ie-blk">
<h4><i>01</i>The plan</h4>
<p>Wednesday 25 November. I meet the two of you at <b class="t">Vie de France, 10:00</b>, on the ground floor of BiTO AKIBA &mdash; the building right in front of the Electric Town exit of Akihabara station. Then four shops picked for your favourites, all on foot inside one square kilometre, lunch together, and we finish back at <b class="t">Akihabara station, 13:00</b>.</p>
</div>
<div class="ie-blk">
<h4><i>02</i>What the day is for</h4>
<div class="ie-chips">{chips}</div>
<p>Figures, anime goods, capsule toys and Pok&eacute;mon cards. Each shop is there for a reason: it is where your favourites are easiest to find.</p>
</div>
<div class="ie-blk">
<h4><i>03</i>On the day</h4>
<p>The plan is set; the pace is ours. You do not have to buy anything &mdash; looking is half the fun. {E(SWAP)}</p>
</div>
</section>
<div class="bar">
<h2>THE DAY</h2>
<span>10:00 &ndash; 13:00</span>
</div>
<p class="gp">One plan, in the order we will live it. Times can breathe a little on the day.</p>
<ul class="tl">{tl}</ul>
<div class="maphd">
<h2 class="map">The map</h2>
</div>
{svg}
<div class="lg">
<span><i></i>The four places are a few minutes apart on foot, in this order from the south</span>
</div>
<section>
<div class="bar">
<h2>FOUR SHOPS, ONE MORNING</h2>
<span>1-4</span>
</div>
<div class="wall">{tiles}</div>
</section>
{cards}
</div>
<div class="lunch" id="lunch">
<div class="col">
<h2><em>Where we eat</em> &mdash; we pick together</h2>
<p>Lunch is not booked and not decided &mdash; that is the plan. Six places near the station, all open at lunchtime on a Wednesday: grilled meat, chicken in iron pots, steak, set meals, a diner and omurice. We look, we talk, we choose &mdash; by appetite. If you would rather keep shopping, we skip lunch and stay longer at the shops. Tap a tile for details.</p>
<div class="ltiles">{lt}</div>
<p class="lasof">Hours from the Akihabara eatmap and Tabelog, checked on 10 Nov 2026. Lunch photos are examples, not always the shops themselves.</p>
</div>
</div>
<div class="know">
<div class="col">
<h2>GOOD FOR</h2>
<ul>
<li>Figures, anime goods, capsule toys and Pok&eacute;mon cards, all within a few minutes&rsquo; walk</li>
<li>Fans of One Piece, Frieren, Black Clover and Pok&eacute;mon</li>
</ul>
</div>
</div>
<div class="know">
<div class="col">
<h2>KEEP IN MIND</h2>
<ul>
<li>Times are approximate and can move on the day</li>
<li>You do not have to buy anything &mdash; looking is half the fun</li>
<li>Message Yuuki if you want to change anything. This is a sample plan</li>
</ul>
</div>
</div>
<div class="col">
<div class="bar">
<h2>LINKS</h2>
</div>
<div class="bt">
<a class="btn" href="victor-akiba-nov25.pdf" target="_blank" rel="noopener">One-page PDF (A4) <i>&nearr;</i></a>
</div>
<div class="bt">
<a class="btn" href="{gm('Vie de France BiTO AKIBA')}" target="_blank" rel="noopener">Meeting point on Google Maps <i>&nearr;</i></a>
</div>
</div>
<details class="crd">
<summary>Photo credits and sources</summary>
<p class="cr">Photos: Animate by Dick Thomas Johnson (CC BY 2.0), Radio Kaikan by Aimaimyi (CC BY-SA 3.0), TRADER (figure displays in Akihabara) by Piotrus (CC BY-SA 3.0), Gachapon by Steve Nagata (CC BY 2.0), night view by ElHeineken (CC BY 4.0). Lunch photos are examples from the Akihabara eatmap and Wikimedia Commons. Opening hours from the shops&rsquo; official sites and Tabelog, checked on 10 November 2026. The map is a simple sketch, not to scale, and the positions of the places are approximate. Times on the day are approximate and can move.</p>
</details>
<script>
(function(){{var coarse=matchMedia('(pointer:coarse)').matches,onPin=null;
document.querySelectorAll('.pin').forEach(function(a){{a.addEventListener('click',function(ev){{ev.preventDefault();if(coarse&&onPin!==a){{if(onPin)onPin.classList.remove('on');onPin=a;a.classList.add('on');return}}var c=document.getElementById('p'+a.dataset.n);if(!c)return;c.scrollIntoView({{behavior:'smooth',block:'start'}});c.classList.add('hit');setTimeout(function(){{c.classList.remove('hit')}},1600);if(onPin){{onPin.classList.remove('on');onPin=null}}}})}});
document.getElementById('map').addEventListener('click',function(ev){{if(!ev.target.closest('.pin')&&onPin){{onPin.classList.remove('on');onPin=null}}}});}})();
</script>
{pops}
<script>document.querySelectorAll(".ltile").forEach(b=>{{b.addEventListener("click",()=>{{var d=document.getElementById(b.dataset.pop);if(d&&d.showModal)d.showModal()}})}});document.querySelectorAll(".lpop").forEach(d=>{{d.querySelector(".pclose").addEventListener("click",()=>d.close());d.addEventListener("click",e=>{{if(e.target===d)d.close()}})}});</script>
<script>document.getElementById("copyLink").addEventListener("click",function(){{var b=this,u="{URL}";function done(){{b.classList.add("done");setTimeout(function(){{b.classList.remove("done")}},1800)}}function fallback(){{var t=document.createElement("textarea");t.value=u;document.body.appendChild(t);t.select();try{{document.execCommand("copy");done()}}catch(e){{}}document.body.removeChild(t)}}if(navigator.clipboard&&navigator.clipboard.writeText){{navigator.clipboard.writeText(u).then(done).catch(fallback)}}else{{fallback()}}}});</script>
</body>
</html>
'''
open('index.html', 'w').write(head)
