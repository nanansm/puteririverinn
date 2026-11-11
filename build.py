"""Generate site/index.html dari copy/copy_v2.md. Jalankan: python build.py"""
import json, re, html, urllib.parse, pathlib

ROOT = pathlib.Path(__file__).parent
C = {}
for ln in (ROOT / "copy/copy_v2.md").read_text().splitlines():
    if ln.startswith("---"):
        break
    m = re.match(r"([A-Z0-9_]+): (.+)", ln)
    if m:
        C[m[1]] = m[2].strip()
e = lambda k: html.escape(C[k])
import sys
sys.path.insert(0, str(ROOT / "lib"))
import symbols as SYM
SYMS = {n: SYM.GLYPHS[n][1] for n in SYM.ORDER}
SPRITE = '<svg width="0" height="0" style="position:absolute" aria-hidden="true">' + "".join(
    f'<symbol id="s-{n.lower()}" viewBox="0 0 120 120"><g class="sym">{g}</g></symbol>' for n, g in SYMS.items()) + '</svg>'
def sym(n, size, cls=""):
    return f'<svg class="{cls}" width="{size}" height="{size}" aria-hidden="true"><use href="#s-{n.lower()}"/></svg>'
def river(n=1, cls="river"):
    return f'<svg class="{cls}" viewBox="0 0 1200 24" preserveAspectRatio="none" aria-hidden="true"><path d="M0 12 C150 2 300 22 450 12 S750 2 900 12 S1100 22 1200 12" fill="none" stroke="currentColor" stroke-width="1.5" vector-effect="non-scaling-stroke"/></svg>'
EM = {"WHY_TITLE": "kamu rasakan", "SAUNG_TITLE": "pas", "DAY_TITLE": "juga boleh", "REVIEW_TITLE": "Google", "LOC_TITLE": "Maps", "FAQ_TITLE": "ditanya", "CTA_TITLE": "sekarang juga!"}
def h(k):
    s = e(k); w = EM.get(k)
    return s.replace(w, f"<em>{w}</em>", 1) if w and w in s else s

DOMAIN = "https://puteririverinn.com"
WA = "6282126259506"
WA_TXT = "0821-2625-9506"
MAPS = "https://maps.app.goo.gl/RGDRV91CGC49pa51A"
MENU = "https://drive.google.com/drive/folders/1kPOx1ZgOMOnStjVT3pmr6SewrySvKunC?usp=sharing"
IG = "https://www.instagram.com/puteririverinn/"
TT = "https://www.tiktok.com/@puteriverinn"
LAT, LNG = -6.9164431, 107.9457563


def wa(saung=None):
    msg = C["WA_MSG"].replace("{saung}", saung) if saung else "Halo Puteri River Inn, mau tanya ketersediaan saung."
    return f"https://wa.me/{WA}?text=" + urllib.parse.quote(msg)


SAUNG = [  # nama, kap, wd, we, maks extrabed
    ("Cihonje", 2, 300, 350, 1), ("Citengah", 2, 300, 350, 1), ("Cisoka", 2, 350, 400, 1),
    ("Ambu", 4, 550, 600, 2), ("Citundun", 4, 550, 600, 1), ("Indung", 4, 750, 850, 2),
    ("Cijolang", 6, 850, 950, 4), ("Cikarut", 6, 850, 950, 4), ("Dewa", 10, 1300, 1400, 5),
]
pr = lambda k: (f"{k/1000:g}".replace(".", ",") + "<small> jt</small>") if k >= 1000 else f"{k}<small> rb</small>"
rp = lambda k: f"Rp{k/1000:g} jt".replace(".", ",") if k >= 1000 else f"Rp{k} rb"

REVIEWS = [
    ("Yoga F.", "Sungainya jernih dan bersih, serta cukup aman utk anak2 bermain atau berenang. Makanan juga enak enak, harga cukup kompetitif."),
    ("NK Aroel", "Penginapannya estetik, nuansa perkampungannya dapat, nuansanya menenangkan, sejuk dan asri. Pelayanannya juga sangat ramah."),
    ("Anas B.", "Lokasinya pinggir sungai dan sawah, enak buat nyantai bersama keluarga."),
    ("Gadis S. B.", "Tempat yang nyaman dan aman untuk bermain air bersama anak kecil."),
]

ICON = {
    "wa": '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2.1 1-2.4c.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .5l-.3.5-.4.5c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.2.5.1.6 0l.9-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.1.1.7-.1 1.3Z"/>',
    "pin": '<path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/>',
    "ig": '<path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10Zm0 8.2A3.2 3.2 0 1 1 12 8.8a3.2 3.2 0 0 1 0 6.4ZM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4ZM12 2c-2.7 0-3 0-4.1.1C3.6 2.3 2.3 3.6 2.1 7.9 2 9 2 9.3 2 12s0 3 .1 4.1c.2 4.3 1.5 5.6 5.8 5.8 1.1.1 1.4.1 4.1.1s3 0 4.1-.1c4.3-.2 5.6-1.5 5.8-5.8.1-1.1.1-1.4.1-4.1s0-3-.1-4.1c-.2-4.3-1.5-5.6-5.8-5.8C15 2 14.7 2 12 2Zm0 1.8c2.7 0 3 0 4 .1 3.2.1 4 1 4.1 4.1.1 1 .1 1.3.1 4s0 3-.1 4c-.1 3.1-.9 4-4.1 4.1-1 .1-1.3.1-4 .1s-3 0-4-.1c-3.2-.1-4-1-4.1-4.1-.1-1-.1-1.3-.1-4s0-3 .1-4C4 4.8 4.8 4 8 3.9c1-.1 1.3-.1 4-.1Z"/>',
    "tt": '<path d="M16.6 2h-3.3v13.4a2.9 2.9 0 1 1-2-2.8V9.2a6.3 6.3 0 1 0 5.3 6.2V8.6a7.9 7.9 0 0 0 4.4 1.4V6.7a4.6 4.6 0 0 1-4.4-4.7Z"/>',
    "bed": '<path d="M3 6v13h2v-2h14v2h2v-6a3 3 0 0 0-3-3h-7v5H5V6H3Zm5 1a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5Z"/>',
    "list": '<path d="M4 5h16v2H4zm0 6h16v2H4zm0 6h10v2H4z"/>',
}
svg = lambda k, s=20: f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{ICON[k]}</svg>'


def card(i, n, kap, wd, we, xb):
    s = n.lower()
    thumbs = "".join(
        f'<img src="img/{s}_{i}.webp" width="200" height="190" loading="lazy" decoding="async" alt="Foto {n} {i}">' for i in range(1, 5)
    )
    return f'''<article class="card" data-kap="{kap}" id="saung-{s}">
<picture><source srcset="img/{s}.webp" type="image/webp"><img src="img/{s}.jpg" width="748" height="576" loading="lazy" decoding="async" alt="Saung {n}, Puteri River Inn Sumedang"></picture>
<div class="cb"><div class="ch">{sym(n,36)}<p class="lab">Saung {i:02d} · {kap} orang</p></div>
<h3>{n}</h3><p class="arti">{html.escape(SYM.meaning(n))}</p>
<p class="d">{e("DESC_" + n.upper())}</p>
<div class="th">{thumbs}</div>
<dl class="pr"><div><dt>Weekday · Rp</dt><dd>{pr(wd)}</dd></div><div><dt>Weekend · Rp</dt><dd>{pr(we)}</dd></div></dl>
<a class="btn wa" href="{wa(n)}" data-ev="wa_saung" data-saung="{n}" rel="noopener">{svg("wa",18)} {e("CARD_BTN")}</a></div></article>'''


faq = [(C[f"FAQ_Q{i}"], C[f"FAQ_A{i}"]) for i in range(1, 7)]

ld = [
    {
        "@context": "https://schema.org", "@type": "LodgingBusiness", "@id": DOMAIN + "/#pri",
        "name": "Puteri River Inn", "url": DOMAIN + "/", "telephone": "+62-821-2625-9506",
        "image": [DOMAIN + "/img/hero-d.jpg", DOMAIN + "/img/hero-m.jpg?v=2"],
        "description": C["META_DESC"], "priceRange": "Rp300.000 - Rp1.400.000",
        "address": {"@type": "PostalAddress", "streetAddress": "Citengah",
                    "addressLocality": "Sumedang Selatan", "addressRegion": "Jawa Barat", "postalCode": "45311", "addressCountry": "ID"},
        "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG},
        "hasMap": MAPS, "checkinTime": "14:00", "checkoutTime": "12:00",
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": a, "value": True}
                           for a in ["Kolam renang", "Water heater", "TV", "Restoran"]],
        "sameAs": [IG, TT],
        "containsPlace": [{"@type": "Accommodation", "name": f"Saung {n}", "occupancy": {"@type": "QuantitativeValue", "maxValue": k}} for n, k, *_ in SAUNG],
    },
    {"@context": "https://schema.org", "@type": "FAQPage",
     "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
]

CSS = (ROOT / "style.css").read_text()
CSS = re.sub(r"/\*.*?\*/", "", CSS, flags=re.S)
CSS = re.sub(r"\s*\n\s*", "", CSS)

page = f'''<!doctype html><html lang="id"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e("TITLE_TAG")}</title>
<meta name="description" content="{e("META_DESC")}">
<link rel="canonical" href="{DOMAIN}/">
<meta name="theme-color" content="#154224">
<meta property="og:type" content="website"><meta property="og:url" content="{DOMAIN}/">
<meta property="og:title" content="{e("TITLE_TAG")}"><meta property="og:description" content="{e("META_DESC")}">
<meta property="og:image" content="{DOMAIN}/img/og.jpg"><meta property="og:locale" content="id_ID">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="img/favicon.png" type="image/png"><link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preload" href="fonts/fraunces-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/figtree.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" as="image" imagesrcset="img/hero-m-828.avif?v=2 828w, img/hero-m.avif?v=2 1080w" imagesizes="100vw" type="image/avif" media="(max-width:899px)" fetchpriority="high">
<link rel="preload" as="image" href="img/hero-d.avif" type="image/avif" media="(min-width:900px)" fetchpriority="high">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(",", ":"))}</script>
</head><body>
{SPRITE}
<header class="hero">
<picture><source media="(min-width:900px)" srcset="img/hero-d.avif" type="image/avif"><source media="(min-width:900px)" srcset="img/hero-d.webp" type="image/webp"><source srcset="img/hero-m-828.avif?v=2 828w, img/hero-m.avif?v=2 1080w" sizes="100vw" type="image/avif"><source srcset="img/hero-m-828.webp?v=2 828w, img/hero-m.webp?v=2 1080w" sizes="100vw" type="image/webp">
<img src="img/hero-m.jpg?v=2" width="1080" height="1920" alt="Foto udara seluruh area Puteri River Inn: saung, kolam renang, sungai, dan sawah di Citengah, Sumedang" fetchpriority="high"></picture>
<div class="hi">
<img class="logo" src="img/logo-putih.webp" width="120" height="120" alt="Logo Puteri River Inn">
<p class="lab">{e("HERO_LABEL")}</p>
<h1>{e("HERO_H1")}</h1>
<p class="sub">{e("HERO_SUB")}</p>
<nav class="links" aria-label="Tautan utama">
<a class="btn wa big" href="{wa()}" data-ev="wa_hero" rel="noopener">{svg("wa")} {e("BTN_BOOK")}</a>
<a class="btn ghost" href="{MENU}" data-ev="menu" rel="noopener">{svg("list")} {e("BTN_MENU")}</a>
<a class="btn ghost" href="{MAPS}" data-ev="maps" rel="noopener">{svg("pin")} {e("BTN_MAPS")}</a>
<div class="soc"><a class="ico" href="{IG}" data-ev="ig" rel="noopener" aria-label="Instagram @puteririverinn">{svg("ig",22)}</a><a class="ico" href="{TT}" data-ev="tiktok" rel="noopener" aria-label="TikTok @puteriverinn">{svg("tt",22)}</a></div>
</nav></div></header>

<main>
<section class="why wrap"><div class="wh"><h2>{h("WHY_TITLE")}</h2></div><ol class="list">
{"".join(f'<li><span class="no">{i:02d}</span><div><h3>{e(f"WHY_{i}_T")}</h3><p>{e(f"WHY_{i}_B")}</p></div></li>' for i in range(1,5))}
</ol></section>

<section id="saung" class="saung"><div class="wrap">
<p class="lab">Sembilan saung</p><h2>{h("SAUNG_TITLE")}</h2><p class="lead">{e("SAUNG_SUB")}</p>
<p class="note">{svg("bed",18)} {e("SAUNG_NOTE")} Check-in 14.00, check-out 12.00.</p>
<nav class="syms" aria-label="Lompat ke saung">{"".join(f'<a href="#saung-{n.lower()}" title="Saung {n}" aria-label="Saung {n}">{sym(n,30)}</a>' for n,*_ in SAUNG)}</nav>
<div class="flt" role="group" aria-label="Filter jumlah orang">
<button class="on" data-f="0">Semua</button><button data-f="2">2 orang</button><button data-f="4">4 orang</button><button data-f="6">6 orang</button><button data-f="10">10 orang</button></div>
<div class="cards">{"".join(card(i+1,*s) for i,s in enumerate(SAUNG))}</div>
</div></section>

<section class="day wrap"><div class="dt"><p class="lab">Buka 08.00–16.00</p><h2>{h("DAY_TITLE")}</h2><p>{e("DAY_BODY")}</p>
<a class="btn wa" href="{wa()}" data-ev="wa_day" rel="noopener">{svg("wa",18)} Tanya via WhatsApp</a></div>
<div class="gal">
<picture class="batu"><source srcset="img/g-anak.webp" type="image/webp"><img src="img/g-anak.jpg" width="800" height="1000" loading="lazy" decoding="async" alt="Pengunjung main air di sungai dangkal Puteri River Inn"></picture>
<picture class="off"><source srcset="img/g-sungai.webp" type="image/webp"><img src="img/g-sungai.jpg" width="800" height="1000" loading="lazy" decoding="async" alt="Sungai berbatu dan saung di Puteri River Inn"></picture>
</div></section>

<section class="rev"><div class="wrap"><p class="lab">Ulasan tamu</p><h2>{h("REVIEW_TITLE")}</h2><div class="rs">
{"".join(f'<figure>{river()}<blockquote>“{html.escape(t)}</blockquote><figcaption>{html.escape(n)} · Google</figcaption></figure>' for n,t in REVIEWS[:3])}
</div><a class="more" href="{MAPS}" data-ev="reviews" rel="noopener">{e("REVIEW_LINK")} →</a></div></section>

<section class="loc wrap"><div><p class="lab">Citengah · Sumedang Selatan</p><h2>{h("LOC_TITLE")}</h2><p>{e("LOC_BODY")}</p>
<a class="btn line" href="{MAPS}" data-ev="maps_loc" rel="noopener">{svg("pin",18)} {e("BTN_MAPS")}</a></div>
<div class="map"><iframe src="https://maps.google.com/maps?q={LAT},{LNG}&amp;t=k&amp;z=17&amp;hl=id&amp;output=embed" title="Peta satelit lokasi Puteri River Inn, Citengah, Sumedang" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</section>

<section class="faq wrap"><p class="lab">Sebelum berangkat</p><h2>{h("FAQ_TITLE")}</h2><div class="qs">
{"".join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q,a in faq)}</div>
</section>

<section class="cta"><div class="wrap"><p class="lab">Booking lewat WhatsApp</p><h2>{h("CTA_TITLE")}</h2><p>{e("CTA_BODY")}</p>
<a class="btn wa big" href="{wa()}" data-ev="wa_cta" rel="noopener">{svg("wa")} {WA_TXT}</a></div></section>
</main>

<footer>{river()}<div class="wrap">
<div class="official" role="note"><p class="lab">{svg("wa",16)} {e("FOOT_OFFICIAL_T")}</p><p class="num"><a href="{wa()}" data-ev="wa_official">{WA_TXT}</a></p><p>{e("FOOT_OFFICIAL_B")}</p></div>
<strong>Puteri River Inn</strong>
<div class="fsyms" aria-hidden="true">{"".join(sym(n,20) for n,*_ in SAUNG)}</div>
<p>Citengah, Sumedang Selatan, Sumedang Regency, West Java 45311</p>
<p class="fsoc"><a href="{IG}" rel="noopener">{svg("ig",18)} @puteririverinn</a><a href="{TT}" rel="noopener">{svg("tt",18)} @puteriverinn</a></p></div></footer>

<a class="fab" href="{wa()}" data-ev="wa_fab" rel="noopener" aria-label="Booking via WhatsApp">{svg("wa",22)} <span>Booking</span></a>
<script>
const fab=document.querySelector('.fab');new IntersectionObserver(([x])=>fab.classList.toggle('show',!x.isIntersecting)).observe(document.querySelector('.links'));
document.querySelectorAll('.flt button').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.flt button').forEach(x=>x.classList.toggle('on',x===b));const f=+b.dataset.f;document.querySelectorAll('.card').forEach(c=>c.hidden=f&&+c.dataset.kap!==f)}});
document.addEventListener('click',e=>{{const a=e.target.closest('[data-ev]');if(!a)return;const p={{event:a.dataset.ev,saung:a.dataset.saung||''}};(window.dataLayer=window.dataLayer||[]).push(p);if(window.fbq&&a.dataset.ev.startsWith('wa'))fbq('track','Contact',{{content_name:p.saung}})}});
</script>
</body></html>'''

(ROOT / "site/index.html").write_text(page)
(ROOT / "site/robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
(ROOT / "site/sitemap.xml").write_text(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{DOMAIN}/</loc><changefreq>monthly</changefreq><priority>1.0</priority></url></urlset>\n')
print("ok", len(page), "bytes")
