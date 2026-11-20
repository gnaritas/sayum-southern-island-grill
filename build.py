#!/usr/bin/env python3
"""SaYum Southern Island Grill (Wilson NC) — page generator, template v2 T1, 2026-11-20.
All copy from the verified-facts card bank (Business Debut 2026-11-17 phone interview +
shop's own Facebook page + scan evidence). Unknowns (hours schedule, reopening date,
prices, full menu) omitted — never invented."""
import json, os

ORIGIN = "https://sayum-southern-island-grill-demo.up.railway.app"
ADDR_Q = "408+Nash+Street,+Wilson,+NC+27893"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
os.makedirs(OUT, exist_ok=True)

SHOP = "SaYum Southern Island Grill"
PHONE_D = "252-296-8083"
PHONE_T = "+12522968083"
EMAIL = "sayumislandgrill@gmail.com"
ADDR1 = "408 Nash Street"
GEO = {"latitude": 35.8055457, "longitude": -77.8578182}
FB = "https://www.facebook.com/profile.php?id=61595975817649"

# flame mark: fire with a curled tongue, island-grill brand mark
FLAME = ('<path d="M50 6 C 60 24 80 34 80 55 C 80 73 67 86 50 86 C 33 86 20 73 20 55 '
         'C 20 44 26 35 33 29 C 31 42 37 49 44 53 C 39 37 44 19 50 6 Z"/>'
         '<path d="M50 86 C 42 78 38 70 40 61 C 45 66 48 71 50 76 C 52 70 55 65 60 61 '
         'C 62 71 58 79 50 86 Z" opacity=".55"/>')

def flame(cls=""):
    return ('<svg class="%s" viewBox="0 0 100 100" role="img" aria-label="SaYum flame mark">'
            '<g fill="currentColor">%s</g></svg>' % (cls or "mark", FLAME))

def swoosh():
    return ('<svg class="swoosh" viewBox="0 0 340 14" aria-hidden="true">'
            '<path d="M2 8 C 60 13 120 3 180 8 C 240 13 300 5 338 9" fill="none" '
            'stroke="#e8842a" stroke-width="2.8" stroke-linecap="round"/></svg>')

NAV = ('<header class="top"><div class="wrap">'
       '<a class="brand" href="/">' + flame() +
       '<span class="word">SaYum<small>Southern Island Grill · Wilson NC</small></span></a>'
       '<nav class="main" aria-label="Main"><ul>'
       '<li><a href="/menu">Menu</a></li>'
       '<li><a href="/jamaican-classics">Jamaican Classics</a></li>'
       '<li><a href="/soul-food">Soul Food</a></li>'
       '<li><a href="/story">Our Story</a></li>'
       '<li><a href="/contact">Contact</a></li>'
       '<li><a class="btn" href="tel:%s">Call %s</a></li>'
       '</ul></nav></div></header>' % (PHONE_T, PHONE_D))

FOOT = ('<footer class="site"><div class="wrap">'
        '<div class="nap"><p class="fbrand">SaYum Southern Island Grill</p>'
        '<address>' + ADDR1 + '<br>Wilson, NC 27893<br>'
        '<a href="tel:%s">%s</a> · <a href="mailto:%s">%s</a><br>'
        '<a href="%s">Find us on Facebook</a></address></div>'
        '<nav aria-label="Footer"><ul>'
        '<li><a href="/menu">Menu</a></li>'
        '<li><a href="/jamaican-classics">Jamaican Classics</a></li>'
        '<li><a href="/soul-food">Soul Food</a></li>'
        '<li><a href="/story">Our Story</a></li>'
        '<li><a href="/contact">Contact</a></li>'
        '<li><a href="/privacy">Privacy</a></li></ul></nav>'
        '<p class="footline">© 2026 SaYum Southern Island Grill · Serving Wilson from '
        '408 Nash Street since 2013.</p></div></footer>'
        % (PHONE_T, PHONE_D, EMAIL, EMAIL, FB))

def head(title, desc, path, og=True):
    h = ['<!DOCTYPE html>', '<html lang="en">', '<head>',
         '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width, initial-scale=1">',
         f'<title>{title}</title>',
         f'<meta name="description" content="{desc}">',
         '<meta name="robots" content="noindex, nofollow">',
         f'<link rel="canonical" href="{ORIGIN}{path}">',
         '<link rel="icon" href="/favicon.svg" type="image/svg+xml">']
    if og:
        h += [f'<meta property="og:title" content="{title}">',
              f'<meta property="og:description" content="{desc}">',
              f'<meta property="og:url" content="{ORIGIN}{path}">',
              '<meta property="og:image" content="' + ORIGIN + '/og.png">',
              '<meta property="og:type" content="website">',
              '<meta name="twitter:card" content="summary_large_image">']
    h += ['<link rel="stylesheet" href="/style.css">', '</head>']
    return "\n".join(h)

def ldjson(ld):
    if not ld:
        return ""
    return "\n<script type=\"application/ld+json\">\n" + \
        json.dumps(ld, ensure_ascii=False, indent=1) + "\n</script>"

def page(title, desc, path, body, ld, og=True):
    doc = (head(title, desc, path, og) + "\n<body>\n"
           '<a class="skip" href="#main">Skip to content</a>\n'
           '<div class="band" aria-hidden="true"></div>\n' + NAV +
           '\n<main id="main">' + body + '</main>\n' + FOOT +
           "\n<!-- BUILT-2026-11-20 -->" + ldjson(ld) + "\n</body>\n</html>")
    fn = "index.html" if path == "/" else path[1:] + ".html"
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote", fn, len(doc), "bytes")

def crumb(name, slug=None):
    items = [{"@type": "ListItem", "position": 1, "name": SHOP, "item": ORIGIN + "/"}]
    if name != "Home":
        items.append({"@type": "ListItem", "position": 2, "name": name, "item": ORIGIN + slug})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

def mapblock(note):
    return ('<div class="mapcell"><iframe src="https://www.google.com/maps?q=' + ADDR_Q +
            '&output=embed" title="Map: SaYum Southern Island Grill, 408 Nash Street, '
            'Wilson, North Carolina 27893" loading="lazy"></iframe>'
            '<p class="mapnote">' + note + '</p></div>')

REST = {
    "@type": "Restaurant",
    "@id": ORIGIN + "/#restaurant",
    "name": SHOP,
    "description": ("Jamaican classics and American soul food at 408 Nash Street, Wilson, "
                    "North Carolina. Reopening early December 2026 under new owner Yvonne "
                    "Collins, continuing where SaYum Jamaican Restaurant has served since 2013."),
    "url": ORIGIN + "/",
    "image": ORIGIN + "/og.png",
    "telephone": "tel:" + PHONE_T,
    "email": "mailto:" + EMAIL,
    "sameAs": FB,
    "servesCuisine": ["Jamaican", "American Soul Food"],
    "address": {"@type": "PostalAddress", "streetAddress": ADDR1,
                "addressLocality": "Wilson", "addressRegion": "NC",
                "postalCode": "27893", "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", **GEO},
    "hasMap": "https://www.google.com/maps?q=" + ADDR_Q,
}

def service(name, stype, blurb):
    return {"@context": "https://schema.org", "@type": "Service", "name": name,
            "serviceType": stype, "description": blurb,
            "provider": {"@type": "Restaurant", "name": SHOP,
                         "address": {"@type": "PostalAddress", "streetAddress": ADDR1,
                                     "addressLocality": "Wilson", "addressRegion": "NC",
                                     "postalCode": "27893", "addressCountry": "US"}},
            "areaServed": {"@type": "City", "name": "Wilson", "addressRegion": "NC"}}

def callband(h, btn="Contact us", href="/contact"):
    return ('<section class="callband"><div class="wrap"><h2>' + h + '</h2>'
            '<a class="btn ghost" href="%s">%s</a>'
            '<a class="btn" href="tel:%s">Call %s</a></div></section>' % (href, btn, PHONE_T, PHONE_D))

JAM = ["Oxtails", "Curry goat", "Curry chicken", "Brown stew chicken",
       "Fried fish", "Steamed fish", "Shrimp"]
SOUL = ["Candied yams", "Collard greens", "Mac and cheese", "Mashed potatoes",
        "Beans", "Fried fish"]

# ---------------- HOME ----------------
home_body = (
    '<section class="hero"><div class="wrap">'
    '<span class="label">Opening early December · 408 Nash Street · Wilson, NC</span>'
    '<h1>' + SHOP + swoosh() + '</h1>'
    '<p class="sub">The Jamaican plates Wilson has eaten at this kitchen since 2013 — '
    'oxtails, curry goat, brown stew chicken — now joined by American soul food: candied '
    'yams, collard greens, mac and cheese. Same address, new chapter.</p>'
    '<div class="ctas"><a class="btn" href="/menu">See the announced menu</a>'
    '<a class="btn ghost" href="/story">Read the story</a></div>'
    '</div></section>'
    '<section class="block"><div class="wrap">'
    '<span class="label" style="color:var(--ember-deep)">Two kitchens, one board</span>'
    '<h2>Caribbean recipes, Southern sides</h2>'
    '<p class="lede">New owner Yvonne Collins is keeping the Jamaican dishes customers '
    'know and adding the soul food classics she grew up on — plates that pair Caribbean '
    'recipes with American Southern sides.</p>'
    '<div class="strip">'
    '<div class="chip"><h3>Jamaican classics</h3><p>Oxtails, curry goat, curry chicken, '
    'brown stew chicken, fried and steamed fish, and shrimp — the plates that made SaYum '
    'on Nash Street.</p><p><a href="/jamaican-classics">See the Jamaican board →</a></p></div>'
    '<div class="chip green"><h3>American soul food</h3><p>Candied yams, collard greens, '
    'mac and cheese, mashed potatoes, beans, and fried fish are joining the menu.</p>'
    '<p><a href="/soul-food">See the soul food board →</a></p></div>'
    '<div class="chip red"><h3>Opening soon</h3><p>Takeover happens the first week of '
    'December with about one day off to change the sign. Reopening date to be announced '
    'on our Facebook page.</p><p><a href="/contact">Ask us anything →</a></p></div>'
    '</div></div></section>'
    '<section class="block alt"><div class="wrap">'
    '<h2>Find us on Nash Street</h2>' + mapblock("Same corner kitchen as SaYum Jamaican "
    "Restaurant — look for the new SaYum Southern Island Grill sign.") + '</div></section>'
    + callband("Questions about the reopening? We answer every note."))

home_faq = {
    "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "When do you reopen?",
         "acceptedAnswer": {"@type": "Answer", "text": "Owner Yvonne Collins expects to "
         "take over the first week of December 2026, with about one day closed to change "
         "the sign. The exact reopening date is to be announced on the Facebook page."}},
        {"@type": "Question", "name": "What will be on the menu?",
         "acceptedAnswer": {"@type": "Answer", "text": "The most popular Jamaican plates "
         "from SaYum Jamaican Restaurant — oxtails, curry goat, curry chicken, brown stew "
         "chicken, fried and steamed fish, shrimp — alongside new American soul food "
         "classics like candied yams, collard greens, mac and cheese, mashed potatoes, "
         "beans, and fried fish."}},
        {"@type": "Question", "name": "Is it still the same restaurant?",
         "acceptedAnswer": {"@type": "Answer", "text": "Same kitchen at 408 Nash Street, "
         "where SaYum Jamaican Restaurant has served since about 2013. Yvonne Collins is "
         "assuming the business and rebranding it as SaYum Southern Island Grill."}},
        {"@type": "Question", "name": "What days will you be open?",
         "acceptedAnswer": {"@type": "Answer", "text": "The plan is Monday through "
         "Saturday. Some Sunday brunch plates are planned for the future, and breakfast "
         "is planned for the new year — schedules to be announced."}}]}

page("SaYum Southern Island Grill — Jamaican Plates & Soul Food, Wilson NC",
     "Jamaican classics and American soul food at 408 Nash Street, Wilson, NC. Reopening "
     "early December 2026 under new owner Yvonne Collins. Oxtails, curry goat, candied yams, collards.",
     "/", home_body,
     {"@context": "https://schema.org", "@graph": [REST, home_faq, crumb("Home")]})

# ---------------- MENU ----------------
menu_body = (
    '<div class="wrap pagehead"><span class="label">Announced menu · subject to change '
    'at launch</span><h1>What\u2019s coming to the board</h1>'
    '<p class="lede">Everything below is what Yvonne Collins told the press the new menu '
    'will carry. Full menu, portions, and prices are announced when the doors reopen.</p>'
    '<div class="ctarow"><a class="btn dark" href="/contact">Ask about the menu</a></div></div>'
    '<section class="block"><div class="wrap"><div class="boards">'
    '<div class="board"><h3>Jamaican classics</h3><ul>' +
    "".join("<li>%s</li>" % d for d in JAM) +
    '<p class="fine">Kept from the SaYum Jamaican Restaurant board — the plates customers '
    'asked to stay.</p></ul></div>'
    '<div class="board green"><h3>American soul food</h3><ul>' +
    "".join("<li>%s</li>" % d for d in SOUL) +
    '<p class="fine">New plates joining the kitchen for the reopening.</p></ul></div>'
    '</div><p class="pricenote">Sides are listed with the soul food plates; plated combos '
    'pairing Caribbean recipes with Southern sides are the plan for the board. Menu items '
    'as announced to Business Debut, November 17, 2026.</p></div></section>'
    + callband("Want a plate you don\u2019t see here? Tell us — the menu is being finalized.",
               "Suggest a dish"))

menu_ld = {
    "@context": "https://schema.org", "@type": "Menu",
    "name": "SaYum Southern Island Grill — announced menu",
    "inLanguage": "en",
    "hasMenuSection": [
        {"@type": "MenuSection", "name": "Jamaican classics",
         "hasMenuItem": [{"@type": "MenuItem", "name": d} for d in JAM]},
        {"@type": "MenuSection", "name": "American soul food",
         "hasMenuItem": [{"@type": "MenuItem", "name": d} for d in SOUL]}],
    "about": {"@id": REST["@id"]}}

page("Menu — SaYum Southern Island Grill, Wilson NC",
     "The announced menu: oxtails, curry goat, curry chicken, brown stew chicken, fried and steamed fish, shrimp, candied yams, collards, mac and cheese.",
     "/menu", menu_body,
     {"@context": "https://schema.org", "@graph": [menu_ld, crumb("Menu", "/menu")]})

# ---------------- JAMAICAN CLASSICS ----------------
jam_body = (
    '<div class="wrap pagehead"><span class="label">The board that started in 2013 · '
    'Wilson NC</span><h1>Jamaican classics</h1>'
    '<p class="lede">SaYum Jamaican Restaurant built its name at 408 Nash Street on these '
    'plates. Under the SaYum Southern Island Grill name they stay on the board — the '
    'dishes customers asked to keep.</p>'
    '<div class="ctarow"><a class="btn dark" href="/menu">Full announced menu</a>'
    '<a class="btn" href="tel:%s">Call %s</a></div></div>'
    '<section class="block"><div class="wrap"><div class="boards">'
    '<div class="board"><h3>From the original board</h3><ul>' +
    "".join("<li>%s</li>" % d for d in JAM) +
    '</ul><p class="fine">As told to Business Debut, November 17, 2026. Prices announced '
    'at reopening.</p></div>'
    '<div class="board red"><h3>How they\u2019re served now</h3><ul>'
    '<li>Alongside new Southern sides</li><li>Candied yams and collards next to the curry</li>'
    '<li>Mac and cheese beside the brown stew</li>'
    '<li>Plates pairing Caribbean recipes with American Southern sides</li></ul>'
    '<p class="fine">The rebrand\u2019s menu direction, in owner Yvonne Collins\u2019 plan '
    'as reported by Business Debut.</p></div>'
    '</div></div></section>'
    + callband("Ask about a plate — oxtails, curry goat, the fish — we\u2019ll answer."))

page("Jamaican Oxtails, Curry Goat & Brown Stew — SaYum Southern Island Grill, Wilson NC",
     "The Jamaican plates Wilson has eaten at 408 Nash Street since 2013: oxtails, curry goat, curry chicken, brown stew chicken, fried and steamed fish, shrimp.",
     "/jamaican-classics", jam_body,
     {"@context": "https://schema.org", "@graph": [
         service("Jamaican classics at SaYum Southern Island Grill",
                 "Jamaican dinner plates",
                 "Oxtails, curry goat, curry chicken, brown stew chicken, fried and steamed fish, and shrimp served at 408 Nash Street, Wilson, NC."),
         crumb("Jamaican Classics", "/jamaican-classics")]})

# ---------------- SOUL FOOD ----------------
soul_body = (
    '<div class="wrap pagehead"><span class="label">New for the reopening · Wilson NC</span>'
    '<h1>Soul food &amp; comfort plates</h1>'
    '<p class="lede">“Whatever I can incorporate with American Southern style food, '
    'that’s what I’m gonna do,” Yvonne Collins told Business Debut. These are the '
    'Southern classics she is bringing to the board.</p>'
    '<div class="ctarow"><a class="btn dark" href="/menu">Full announced menu</a>'
    '<a class="btn" href="tel:%s">Call %s</a></div></div>'
    '<section class="block"><div class="wrap"><div class="boards">'
    '<div class="board green"><h3>Hitting the board</h3><ul>' +
    "".join("<li>%s</li>" % d for d in SOUL) +
    '</ul><p class="fine">As announced to Business Debut, November 17, 2026. More plates '
    'and prices to be revealed at reopening.</p></div>'
    '<div class="board"><h3>On the same plate as the Jamaican classics</h3><ul>'
    '<li>Candied yams with the oxtails</li><li>Collard greens with the curry goat</li>'
    '<li>Mac and cheese with the brown stew chicken</li>'
    '<li>Fried fish two ways — Southern and island</li></ul>'
    '<p class="fine">The pairing direction Collins describes: Caribbean recipes with '
    'American Southern sides.</p></div>'
    '</div></div></section>'
    + callband("Fixin\u2019s you want that aren\u2019t listed? Send us a note."))

page("Soul Food, Candied Yams & Collard Greens — SaYum Southern Island Grill, Wilson NC",
     "American soul food joins the kitchen at 408 Nash Street: candied yams, collard greens, mac and cheese, mashed potatoes, beans, and fried fish.",
     "/soul-food", soul_body,
     {"@context": "https://schema.org", "@graph": [
         service("Soul food at SaYum Southern Island Grill",
                 "American soul food plates",
                 "Candied yams, collard greens, mac and cheese, mashed potatoes, beans, and fried fish served at 408 Nash Street, Wilson, NC."),
         crumb("Soul Food", "/soul-food")]})

# ---------------- STORY ----------------
story_body = (
    '<div class="wrap pagehead"><span class="label">2013 → today · 408 Nash Street</span>'
    '<h1>Our story</h1>'
    '<p class="lede">SaYum began in 2013 as SaYum Jamaican Restaurant, serving the plates '
    'of the island at 408 Nash Street. Today that dream continues as SaYum Southern '
    'Island Grill.</p>'
    '<div class="ctarow"><a class="btn dark" href="/contact">Say hello</a></div></div>'
    '<section class="block"><div class="wrap">'
    '<ol class="timeline">'
    '<li><span class="when">2013</span>SaYum Jamaican Restaurant opens at 408 Nash '
    'Street, and Wilson gets oxtails, curry goat, and brown stew chicken on Nash Street.</li>'
    '<li><span class="when">November 2026</span>Yvonne Collins announces she is assuming '
    'the business and rebranding it as SaYum Southern Island Grill.</li>'
    '<li><span class="when">First week of December 2026</span>Takeover day. Expect about '
    'one day closed while the new sign goes up — then the doors reopen, date to be '
    'announced.</li>'
    '<li><span class="when">December onward</span>The board keeps the most popular '
    'Jamaican plates and adds American soul food classics.</li>'
    '<li><span class="when">New year ahead</span>Breakfast service is planned for the '
    'new year, and some Sunday brunch plates may follow — schedules to be announced.</li>'
    '</ol>'
    '<blockquote class="quote">“Whatever I can incorporate with American Southern style '
    'food, that’s what I’m gonna do.”<span class="qsrc">— Yvonne Collins, told to Business '
    'Debut, November 17, 2026</span></blockquote>'
    '<p>Follow the reopening on our <a href="' + FB + '">Facebook page</a> — opening '
    'date, full menu, and schedules get posted there first.</p>'
    '</div></section>'
    + callband("New name, same kitchen, same corner. Come find us on Nash Street."))

page("Our Story — SaYum Southern Island Grill, Wilson NC",
     "From SaYum Jamaican Restaurant (2013) to SaYum Southern Island Grill: new owner Yvonne Collins, same address at 408 Nash Street, opening early December 2026.",
     "/story", story_body, crumb("Our Story", "/story"))

# ---------------- CONTACT ----------------
contact_body = (
    '<div class="wrap pagehead"><span class="label">We answer every note</span>'
    '<h1>Contact us</h1>'
    '<p class="lede">Questions about the reopening, the menu, or your holiday plate? '
    'Send a note — it lands in the restaurant\u2019s inbox.</p></div>'
    '<section class="block"><div class="wrap"><div class="contactgrid">'
    '<form class="card" method="post" action="/contact">'
    '<p><label for="f-name">Your name</label><input id="f-name" name="name" required autocomplete="name"></p>'
    '<p><label for="f-phone">Phone (optional)</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></p>'
    '<p><label for="f-email">Email (optional)</label><input id="f-email" name="email" type="email" autocomplete="email"></p>'
    '<p><label for="f-msg">Your note</label><textarea id="f-msg" name="message" required></textarea></p>'
    '<p><button class="btn" type="submit">Send it over</button></p></form>'
    '<div class="infocard"><h3>Walk in</h3><address>' + ADDR1 + '<br>Wilson, NC 27893</address>'
    '<h3>Call</h3><p><a href="tel:%s">' + PHONE_D + '</a></p>'
    '<h3>Email</h3><p><a href="mailto:%s">' + EMAIL + '</a></p>'
    '<h3>Planned hours</h3><p>Monday–Saturday planned. Exact opening schedule, reopening '
    'date, and future Sunday brunch are announced on our <a href="' + FB + '">Facebook '
    'page</a>.</p></div>'
    '</div>' + mapblock("408 Nash Street — the same corner kitchen as SaYum Jamaican Restaurant.")
    + '</div></section>')

page("Contact — SaYum Southern Island Grill, 408 Nash St, Wilson NC",
     "Contact SaYum Southern Island Grill — 408 Nash Street, Wilson, NC 27893. Call 252-296-8083, email sayumislandgrill@gmail.com, or send a note.",
     "/contact", contact_body % (PHONE_T, EMAIL),
     crumb("Contact", "/contact"))

# ---------------- PRIVACY ----------------
priv_body = (
    '<div class="wrap pagehead"><span class="label">Plain English</span><h1>Privacy</h1></div>'
    '<section class="block"><div class="wrap prose">'
    '<p>This site collects almost nothing. Here is the whole of it.</p>'
    '<h2>What we collect</h2>'
    '<p>The contact form sends your name — and optionally your phone and email — plus '
    'your note straight to the restaurant\u2019s inbox. It is used only to answer you. '
    'Nothing is sold, nothing is shared, and there are no cookies, no advertising '
    'trackers, and no third-party scripts on this site. The map embed on the contact '
    'page may set its own cookies once you interact with it — Google\u2019s privacy '
    'policy covers that part.</p>'
    '<h2>Who runs this site</h2>'
    '<p>SaYum Southern Island Grill operates this site for its guests. Want your note '
    'deleted after we\u2019ve answered it? Say so in the form — one sentence is enough.</p>'
    '<h2>Changes</h2>'
    '<p>If this page ever changes, the new version lives here and gets a new date below.</p>'
    '<p><em>Effective November 20, 2026.</em></p></div></section>'
    + callband("Questions about the site or the reopening? Use the form — it\u2019s shortest.",
               "Send a note"))

page("Privacy — SaYum Southern Island Grill, Wilson NC",
     "Privacy, in plain English: the contact form note goes to the restaurant's inbox and is used only to answer you. No cookies, no trackers.",
     "/privacy", priv_body, crumb("Privacy", "/privacy"))

# ---------------- THANKS ----------------
thanks_body = (
    '<section class="solo"><div class="wrap">' + flame("bigflame") +
    '<h1>Note received</h1>'
    '<p>Thank you — your message is on its way to the restaurant. We answer every note, '
    'usually within a day once the new schedule is set.</p>'
    '<p><a class="btn dark" href="/">Back to the front page</a></p></div></section>')

page("Thank you — SaYum Southern Island Grill",
     "Your note has been sent to SaYum Southern Island Grill in Wilson, NC.",
     "/thanks", thanks_body, None, og=False)

# ---------------- 404 ----------------
nf_body = (
    '<section class="solo"><div class="wrap">' + flame("bigflame") +
    '<h1>This plate isn\u2019t on the menu</h1>'
    '<p>The page you asked for isn\u2019t here. The front page, the announced menu, and '
    'the contact form all still work.</p>'
    '<p><a class="btn dark" href="/">Front page</a> <a class="btn" href="/menu">See the menu</a></p>'
    '</div></section>')

page("Page not found — SaYum Southern Island Grill",
     "Page not found at SaYum Southern Island Grill, Wilson NC.",
     "/404", nf_body, None, og=False)

# ---------------- assets ----------------
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
            "".join("  <url><loc>%s%s</loc></url>\n" % (ORIGIN, p)
                    for p in ["/", "/menu", "/jamaican-classics", "/soul-food",
                              "/story", "/contact", "/privacy"]) + '</urlset>\n')

with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % ORIGIN)

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
           '<rect width="100" height="100" rx="18" fill="#1c1712"/>'
           '<g fill="#e8842a">' + FLAME + '</g></svg>')
with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(FAVICON)

os.makedirs(OUT, exist_ok=True)
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "style.css")
if src != os.path.join(OUT, "style.css"):
    open(os.path.join(OUT, "style.css"), "w", encoding="utf-8").write(open(src, encoding="utf-8").read())
print("sitemap, robots, favicon, style copied")
print("done")
