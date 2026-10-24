"""Builds the Coastal Golf Association static site (GitHub Pages).
Run: python3 build.py  -> writes index.html, coast-open/, junior-tour/, 404.html
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
CO_REG = "https://www.golfgenius.com/register?league_id=13075258007405735201&utm_source=cga_site&utm_medium=web&utm_campaign=coastopen2026_reg"
CO_SITE = "https://2026galleriabmwcoastopen.golfgenius.com"
CJT_REG = "https://www.golfgenius.com/pages/10581546764362329124"
CJT_AGES = "https://www.golfgenius.com/pages/11625365295928978936"
GALLERIA = "https://www.galleriabmw.com/"
FB = "https://www.facebook.com/profile.php?id=61590366791773"
IG = "https://www.instagram.com/coastaljuniortour/"
EMAIL = "coastaljuniortour@gmail.com"
NEWKS = "https://newks.com/"
NEOGOLF = "https://www.neogolfclub.com/"
ACTION = ["cjt-01","cjt-02","cjt-03","cjt-04","cjt-05","cjt-06","cjt-07","cjt-08"]
WINNERS = ["cjt-09","cjt-10","cjt-11","cjt-12"]

def gallery(pre, names, alt):
    return '<div class="gallery">' + "".join(f'<figure><img loading="lazy" src="{pre}assets/photos/{n}.jpg" alt="{alt}"></figure>' for n in names) + '</div>'


CONTOURS = """<svg class="contours" viewBox="0 0 1200 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><g fill="none" stroke="#F3F4D5" stroke-width="1.4">""" + "".join(
    f'<ellipse cx="{900}" cy="{330}" rx="{60+i*46}" ry="{36+i*30}" transform="rotate(-12 900 330)"/>' for i in range(14)
) + "</g></svg>"


def page(title, desc, path, body, active=""):
    pre = "../" * path.count("/")
    def nav(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{pre}{href}"{cur}>{label}</a>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://coastalgolfassociation.com/assets/cga-banner.png">
<link rel="icon" href="{pre}assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/site.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="{pre}index.html"><img src="{pre}assets/cga-emblem.png" alt=""><span><b>Coastal Golf Association</b><small>Mississippi Gulf Coast</small></span></a>
  <button class="menu-btn" onclick="document.querySelector('nav.main').classList.toggle('open')">Menu</button>
  <nav class="main">
    {nav('index.html#programs','Programs','programs')}
    {nav('coast-open/index.html','Coast Open','coast')}
    {nav('junior-tour/index.html','Junior Tour','cjt')}
    {nav('index.html#about','About','about')}
    {nav('index.html#contact','Contact','contact')}
    <a class="btn btn-orange nav-cta" href="{CO_REG}">Register</a>
  </nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
  <div><img src="{pre}assets/cga-emblem.png" alt="" style="display:inline-block;vertical-align:middle;margin-right:10px">© 2026 Coastal Golf Association · Mississippi Gulf Coast</div>
  <div><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{FB}">Facebook</a> · <a href="{IG}">Instagram</a></div>
</div></footer>
</body>
</html>
"""


def coast_band(pre):
    return f"""
<div class="band">
  <div class="left">
    <div class="eyebrow">November 13–15, 2026 · Sunkist Country Club, Biloxi</div>
    <h2>The 2026 Coast Open presented by Galleria BMW</h2>
    <p>Championship golf on the Mississippi Gulf Coast, with divisions for professionals, amateurs, seniors, super seniors and juniors.</p>
    <div class="facts">
      <div class="fact"><b>$10,000</b><span>Minimum professional purse</span></div>
      <div class="fact"><b>6 divisions</b><span>Pros, amateurs, seniors, juniors</span></div>
      <div class="fact"><b>$200–$550</b><span>Entry by division</span></div>
    </div>
    <div style="display:flex;gap:12px;flex-wrap:wrap">
      <a class="btn btn-orange" href="{CO_REG}">Register for the Coast Open →</a>
      <a class="btn btn-ghost" href="{pre}coast-open/index.html">Event details</a>
    </div>
  </div>
  <div class="right">
    <img src="{pre}assets/coast-open-logo.png" alt="Coast Open" style="width:150px">
    <span class="presented">Presented by</span>
    <a href="{GALLERIA}"><img class="galleria" src="{pre}assets/galleria-bmw-gray.png" alt="Galleria BMW"></a>
    <small>Hosted by the Coastal Golf Association</small>
  </div>
</div>"""


def contact_block(pre):
    return f"""
<section id="contact"><div class="wrap">
  <div class="contact">
    <div>
      <div class="eyebrow" style="color:#F4B596">Get in touch</div>
      <h2>Questions, sponsorships or getting involved?</h2>
      <p>Email us and Allan or Rory will get back to you. We're always glad to hear from players, parents, clubs and businesses that want to support golf on the Gulf Coast.</p>
      <a class="btn btn-orange" href="mailto:{EMAIL}">Email the CGA</a>
    </div>
    <div class="links">
      <a href="mailto:{EMAIL}">✉ {EMAIL}</a>
      <a href="{FB}">Facebook · Coastal Golf Association</a>
      <a href="{IG}">Instagram · @coastaljuniortour</a>
    </div>
  </div>
</div></section>"""


# ---------------- HOME ----------------
home = f"""
<section class="hero" style="padding:0">{CONTOURS}<div class="wrap">
  <div>
    <div class="eyebrow">Mississippi Gulf Coast Championship Golf</div>
    <h1>Golf on the Gulf Coast, run by PGA Professionals.</h1>
    <p class="lead">The Coastal Golf Association runs the Coast Open, the Coastal Junior Tour, PGA Jr. League and PGA HOPE, with events at clubs across the Mississippi Gulf Coast.</p>
    <div class="actions">
      <a class="btn btn-orange" href="{CO_REG}">Register for the 2026 Coast Open →</a>
      <a class="btn btn-ghost" href="#programs" style="color:var(--cream)">See our programs</a>
    </div>
  </div>
  <div class="hero-photo"><img src="assets/photos/cjt-01.jpg" alt="A junior golfer on the course at a Coastal Junior Tour event"><span class="badge"><img src="assets/cga-emblem.png" alt=""></span></div>
</div></section>

<section><div class="wrap">
  {coast_band('')}
</div></section>

<section><div class="wrap">
  <div class="section-head"><div class="eyebrow">On the course</div><h2>Moments from our events</h2><p>Scenes from Coastal Junior Tour events at Shell Landing, Windance and courses across the Gulf Coast.</p></div>
  {gallery('', ACTION, 'Coastal Junior Tour players during an event')}
  <p class="note" style="margin-top:14px">More photos and videos on <a href="{IG}">Instagram</a> and <a href="{FB}">Facebook</a>.</p>
</div></section>

<section class="alt" id="programs"><div class="wrap">
  <div class="section-head">
    <div class="eyebrow">What we run</div>
    <h2>Programs for every golfer</h2>
    <p>From a juniors' first tournament to a professional purse, every CGA program is organized and run by PGA Professionals.</p>
  </div>
  <div class="grid g4">
    <div class="card feature"><div class="tag" style="color:#F4B596">Championship</div><h3>The Coast Open</h3><p>Our annual championship at Sunkist Country Club, with a professional purse and divisions for amateurs, seniors and juniors.</p><a class="more" href="coast-open/index.html">Coast Open</a></div>
    <div class="card"><div class="tag">Juniors</div><h3>Coastal Junior Tour</h3><p>Affordable, competitive tournaments for boys and girls at courses across the Gulf Coast, played under USGA rules.</p><a class="more" href="junior-tour/index.html">Junior Tour</a></div>
    <div class="card"><div class="tag">Juniors</div><h3>PGA Jr. League</h3><p>Team golf for kids, with coaching from PGA Professionals and matches against other teams.</p><a class="more" href="#contact">Ask about teams</a></div>
    <div class="card"><div class="tag">Veterans</div><h3>PGA HOPE</h3><p>The PGA of America's golf program for military veterans, introducing golf to support physical, mental and social well-being.</p><a class="more" href="#contact">Get involved</a></div>
  </div>
</div></section>

<section id="about"><div class="wrap">
  <div class="grid g2" style="align-items:center;gap:48px">
    <div>
      <div class="eyebrow">About the CGA</div>
      <h2>Built on honesty, integrity and respect.</h2>
      <p>The Coastal Golf Association grew out of the Coastal Junior Tour. Our goal hasn't changed: grow the game on the Mississippi Gulf Coast, give golfers of every age affordable, well-run competition, and help juniors take their game to the next level, including earning college opportunities.</p>
      <p>Today the CGA brings the Junior Tour, PGA Jr. League, PGA HOPE and the Coast Open together under one association.</p>
    </div>
    <div class="grid" style="gap:16px">
      <div class="card person"><div class="ini">AM</div><div><h3>Allan Martel, PGA</h3><div class="role">Co-Founder · Tournament Director</div><p style="margin:0">PGA Class A Professional and owner of NeoGolf in D'Iberville and Ocean Springs.</p></div></div>
      <div class="card person"><div class="ini">RN</div><div><h3>Rory Nelson, PGA</h3><div class="role">Co-Founder · Tournament Director</div><p style="margin:0">PGA Professional and General Manager of Sunkist Country Club.</p></div></div>
    </div>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="section-head"><div class="eyebrow">Our partners</div><h2>Thank you to our sponsors</h2><p>Local businesses make affordable, well-run golf possible on the Gulf Coast.</p></div>
  <div class="sponsors">
    <a class="sponsor" href="{GALLERIA}"><small>Title Sponsor · 2026 Coast Open</small><img src="assets/galleria-bmw-gray.png" alt="Galleria BMW"></a>
    <a class="sponsor" href="{NEWKS}"><small>Coastal Junior Tour</small><img src="assets/newks-eatery.png" alt="Newk's Eatery"></a>
    <a class="sponsor" href="{NEOGOLF}"><small>Coastal Junior Tour</small><img src="assets/neogolf.png" alt="NeoGolf" style="height:48px"></a>
    <a class="sponsor" href="mailto:{EMAIL}?subject=Sponsoring%20the%20Coastal%20Golf%20Association"><small>Become a sponsor</small><b>Your business here</b></a>
  </div>
</div></section>
{contact_block('')}
"""

# ---------------- COAST OPEN ----------------
divs = [
    ("Professional Open", "54 holes · Fri–Sun", "$550"),
    ("PGA Professionals", "54 holes · Fri–Sun", "$400"),
    ("Amateur Championship", "54 holes · Fri–Sun", "$300"),
    ("Senior", "36 holes · Sat–Sun", "$200"),
    ("Super Senior", "36 holes · Sat–Sun", "$200"),
    ("Junior · Boys 14–18", "36 holes · Sat–Sun", "$200"),
]
rows = "".join(f'<tr><td><b>{n}</b><span class="sub">{d}</span></td><td class="price">{p}</td></tr>' for n, d, p in divs)
coast = f"""
<section class="page-head">{CONTOURS}<div class="wrap" style="position:relative">
  <div class="eyebrow">November 13–15, 2026 · Sunkist Country Club, Biloxi</div>
  <h1>The 2026 Coast Open</h1>
  <p>Championship golf on the Mississippi Gulf Coast with a $10,000 minimum professional purse, run by PGA Professionals and hosted by the Coastal Golf Association.</p>
  <div class="actions"><a class="btn btn-orange" href="{CO_REG}">Register now →</a><a class="btn btn-ghost" href="{CO_SITE}" style="color:var(--cream)">Event website & results</a></div>
  <div class="presented-strip"><span>Presented by</span><a href="{GALLERIA}"><img src="../assets/galleria-bmw-white.png" alt="Galleria BMW"></a></div>
</div></section>

<section><div class="wrap grid g2" style="gap:40px;align-items:start">
  <div>
    <div class="eyebrow">Entry fee by division</div>
    <h2>Find your division</h2>
    <table class="table"><thead><tr><th>Division</th><th style="text-align:right">Entry</th></tr></thead><tbody>{rows}</tbody></table>
    <p class="note" style="margin-top:12px">Divisions, eligibility and tees are set in the official event terms on Golf Genius.</p>
  </div>
  <div>
    <div class="eyebrow">At a glance</div>
    <h2>Event details</h2>
    <ul class="check">
      <li><b>Dates:</b> Friday–Sunday, November 13–15, 2026</li>
      <li><b>Course:</b> Sunkist Country Club, Biloxi, Mississippi</li>
      <li><b>Purse:</b> $10,000 minimum professional purse</li>
      <li><b>Host:</b> Coastal Golf Association</li>
      <li><b>Tournament directors:</b> Allan Martel, PGA and Rory Nelson, PGA</li>
    </ul>
    <a class="btn btn-navy" href="{CO_REG}">Register on Golf Genius →</a>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="band" style="grid-template-columns:1fr 1fr">
    <div class="left"><div class="eyebrow">Title partner</div><h2>Thank you, Galleria BMW</h2><p>Galleria BMW of D'Iberville is the title sponsor of the 2026 Coast Open. We're proud to have them backing championship golf on the Gulf Coast.</p><a class="btn btn-ghost" href="{GALLERIA}">Visit Galleria BMW</a></div>
    <div class="right"><img class="galleria" src="../assets/galleria-bmw-gray.png" alt="Galleria BMW"><small>11282 Mandal Pkwy · D'Iberville, MS</small></div>
  </div>
</div></section>
{contact_block('../')}
"""

# ---------------- JUNIOR TOUR ----------------
sched = [("Thursday, June 4", "Sunkist Country Club"), ("Sunday, June 14", "Grand Bear Golf Club"),
         ("Thursday, June 25", "The Club at Diamondhead"), ("Monday, June 29", "Windance Country Club"),
         ("Tuesday, July 7", "Shell Landing"), ("Monday, July 13", "Hattiesburg Country Club"),
         ("Tuesday, July 21", "Sunkist Country Club")]
srows = "".join(f"<tr><td>{d}</td><td><b>{c}</b></td></tr>" for d, c in sched)
cjt = f"""
<section class="page-head">{CONTOURS}<div class="wrap" style="position:relative">
  <div class="eyebrow">A Coastal Golf Association program</div>
  <h1>Coastal Junior Tour</h1>
  <p>Empowering tomorrow's leaders on and off the course. Competitive, affordable tournaments for junior golfers along the Mississippi Gulf Coast.</p>
  <div class="actions"><a class="btn btn-orange" href="{CJT_REG}">Register for the Junior Tour →</a><a class="btn btn-ghost" href="{CJT_AGES}" style="color:var(--cream)">Age groups & yardages</a></div>
</div></section>

<section><div class="wrap grid g2" style="gap:44px;align-items:start">
  <div>
    <div class="eyebrow">Who we are</div>
    <h2>Grow the game. Play for real.</h2>
    <p>Our core values are honesty, integrity and respect. The tour exists to grow the game of golf, give juniors competitive and affordable places to play, and help them earn college scholarship opportunities.</p>
    <ul class="check">
      <li>9 or 18 holes of individual stroke play under USGA rules</li>
      <li>Boys and girls divisions, each from their own tees</li>
      <li>Lunch and on-course beverages included</li>
      <li>Run by PGA Professionals</li>
    </ul>
  </div>
  <div>
    <div class="eyebrow">2026 season fees</div>
    <h2>Registration</h2>
    <table class="table"><tbody>
      <tr><td><b>Tour registration</b><span class="sub">Includes admin fees and a CJT hat, towel and headcover</span></td><td class="price">$100</td></tr>
      <tr><td><b>18-hole players</b><span class="sub">Per event</span></td><td class="price">$60</td></tr>
      <tr><td><b>9-hole players</b><span class="sub">Per event</span></td><td class="price">$30</td></tr>
    </tbody></table>
    <p class="note" style="margin-top:12px">Registration closes at noon on the Monday before each event.</p>
  </div>
</div></section>

<section class="alt"><div class="wrap grid g2" style="gap:44px;align-items:start">
  <div>
    <div class="eyebrow">Divisions</div>
    <h2>Age groups</h2>
    <table class="table"><thead><tr><th>Age group</th><th>Format</th></tr></thead><tbody>
      <tr><td><b>9 & under</b></td><td>9 holes · caddies required</td></tr>
      <tr><td><b>10–12</b></td><td>9 holes · no caddies</td></tr>
      <tr><td><b>13–15</b></td><td>18 holes</td></tr>
      <tr><td><b>16–18</b></td><td>18 holes</td></tr>
      <tr><td><b>B Flight</b></td><td>9 holes · for newer 18-hole players who can't yet break 100</td></tr>
    </tbody></table>
    <p class="note" style="margin-top:12px"><a href="{CJT_AGES}">Full age groups and yardages on Golf Genius</a></p>
  </div>
  <div>
    <div class="eyebrow">2026 summer schedule</div>
    <h2>Where we played</h2>
    <table class="table"><thead><tr><th>Date</th><th>Course</th></tr></thead><tbody>{srows}</tbody></table>
    <p class="note" style="margin-top:12px">The 2027 schedule will be posted here. Follow us on <a href="{IG}">Instagram</a> and <a href="{FB}">Facebook</a> for updates.</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div class="eyebrow">2026 season</div><h2>Our winners and players</h2><p>Medalists and action from the 2026 Coastal Junior Tour season.</p></div>
  {gallery('../', WINNERS, 'Coastal Junior Tour medalists')}
  <div style="height:14px"></div>
  {gallery('../', ACTION[1:5], 'Coastal Junior Tour players during an event')}
</div></section>

<section class="alt" id="policies"><div class="wrap">
  <div class="section-head"><div class="eyebrow">Resources</div><h2>Player and spectator guidelines</h2></div>
  <details><summary>Notice to players</summary><ol>
    <li>Practice rounds are available Monday–Wednesday after 1 p.m., based on availability.</li>
    <li>Range balls are provided.</li>
    <li>Players walk and carry their own bags; push carts are allowed. The 9 & under division may use caddies, and both caddies and players walk. Caddies may give their player advice.</li>
    <li>Cell phones are for emergencies only.</li>
    <li>Tee times begin at 8 a.m. from holes #1 and #10. Be on the tee at least 5 minutes before your starting time.</li>
    <li>Pace of play is 4 hours and 30 minutes. Keep up with the group ahead.</li>
    <li>The double par rule applies to B Flight.</li>
    <li>Drinks are in coolers on the course; lunch is served at the clubhouse after play.</li>
    <li>Scores are unofficial until scorecards are signed and returned to the scoring area.</li>
    <li>The awards ceremony starts once each division and flight is scored. Players are encouraged to attend.</li>
  </ol></details>
  <details><summary>Spectator policies and guidelines</summary>
    <p>Spectators are welcome at all events and follow the same etiquette and dress code as players. You're there to watch, not to caddie or coach.</p>
    <ul>
      <li><b>Conduct:</b> watch quietly from the cart path; keep tobacco and alcohol use to a minimum.</li>
      <li><b>Dress code:</b> golf attire; no jeans, tank tops or flip flops. Host club guidelines apply.</li>
      <li><b>Phones:</b> off or silent, and not used on the course.</li>
      <li><b>Talking with players:</b> only in front of other players and spectators, and only about food, water, sunscreen or health.</li>
      <li><b>Carts:</b> rented from the facility, on cart paths only, two people maximum, may carry players' drinks but not equipment, and may shuttle players only in an evacuation.</li>
      <li><b>On the course:</b> stay a reasonable distance back, never enter a fairway or green, and stay still and quiet during shots. Help spot lost balls, but never touch a player's ball.</li>
    </ul></details>
  <details><summary>Dress code, conduct and equipment</summary><ul>
    <li>Appropriate golf attire is required; the host facility's dress code applies.</li>
    <li>All events are soft spikes only.</li>
    <li>The tour provides beverages. Refillable bottles are allowed; coolers are not.</li>
    <li>Abuse or disrespect toward competitors, officials, spectators or facility staff may lead to disqualification and rejection from future events.</li>
  </ul></details>
</div></section>

<section id="sponsors"><div class="wrap">
  <div class="section-head"><div class="eyebrow">Thank you</div><h2>Junior Tour sponsors</h2><p>Interested in supporting junior golf on the Gulf Coast? Email us and we'll send sponsorship information.</p></div>
  <div class="sponsors">
    <a class="sponsor" href="{NEWKS}"><small>Junior Tour sponsor</small><img src="../assets/newks-eatery.png" alt="Newk's Eatery"></a>
    <a class="sponsor" href="{NEOGOLF}"><small>Junior Tour sponsor</small><img src="../assets/neogolf.png" alt="NeoGolf" style="height:48px"></a>
    <a class="sponsor" href="mailto:{EMAIL}?subject=Coastal%20Junior%20Tour%20sponsorship"><small>Become a sponsor</small><b>Your business here</b></a>
  </div>
</div></section>
{contact_block('../')}
"""

notfound = f"""<section class="page-head"><div class="wrap"><h1>Page not found</h1><p>That page moved when we became the Coastal Golf Association.</p><div class="actions"><a class="btn btn-orange" href="/">Go to the home page</a><a class="btn btn-ghost" style="color:var(--cream)" href="/junior-tour/">Coastal Junior Tour</a></div></div></section>"""

out = {
    "index.html": page("Coastal Golf Association · Mississippi Gulf Coast Golf", "The Coastal Golf Association runs the Coast Open, the Coastal Junior Tour, PGA Jr. League and PGA HOPE on the Mississippi Gulf Coast.", "index.html", home),
    "coast-open/index.html": page("2026 Coast Open presented by Galleria BMW · Nov 13–15 · Sunkist CC", "The 2026 Coast Open presented by Galleria BMW, November 13–15 at Sunkist Country Club in Biloxi. $10,000 minimum professional purse.", "coast-open/index.html", coast, "coast"),
    "junior-tour/index.html": page("Coastal Junior Tour · Coastal Golf Association", "Competitive, affordable junior golf tournaments along the Mississippi Gulf Coast, run by PGA Professionals.", "junior-tour/index.html", cjt, "cjt"),
    "404.html": page("Page not found · Coastal Golf Association", "Coastal Golf Association", "404.html", notfound),
}
for p, html in out.items():
    f = ROOT / p
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(html)
(ROOT / "CNAME").write_text("coastalgolfassociation.com\n")
print("built", list(out))
