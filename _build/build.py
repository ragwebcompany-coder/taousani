# -*- coding: utf-8 -*-
"""Γεννήτρια στατικών σελίδων για το site του BIOLAB."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import SITE, CATS
from catalog import catalog, TEAM_PREVIEW

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

S = SITE

# ── Εικόνα με webp fallback ────────────────────────────────────────────
def pic(name, alt, cls="", sizes="100vw", loading="lazy", width=None, height=None, fetch=None):
    attrs = f' class="{cls}"' if cls else ""
    dim = f' width="{width}" height="{height}"' if width else ""
    fp = ' fetchpriority="high"' if fetch else ""
    ld = f' loading="{loading}" decoding="async"' if loading == "lazy" else ' decoding="async"'
    return (f'<picture><source type="image/webp" srcset="assets/images/{name}.webp">'
            f'<img src="assets/images/{name}.jpg" alt="{alt}"{attrs}{dim}{ld}{fp}></picture>')


LOGO = '<img class="brand-logo" src="assets/images/biolab-logo-approved.png" alt="BIOLAB" width="272" height="250">'

CARET = ('<svg class="caret" viewBox="0 0 12 12" fill="none" aria-hidden="true">'
         '<path d="M2.5 4.5 6 8l3.5-3.5" stroke="currentColor" stroke-width="1.6" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

ARW = '<span class="arw" aria-hidden="true">→</span>'

NAV = [
    ("index.html", "Αρχική"),
    ("exetaseis.html", "Εξετάσεις"),
    ("ergastirio.html", "Το εργαστήριο"),
    ("omada.html", "Η ομάδα μας"),
    ("poiotita.html", "Ποιότητα"),
    ("epikoinonia.html", "Επικοινωνία"),
]


def head(title, desc, page, og="og-image", extra=""):
    canonical = f'{S["url"]}/{"" if page == "index.html" else page}'
    return f"""<!DOCTYPE html>
<html lang="el">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#05101f">
<meta property="og:type" content="website">
<meta property="og:locale" content="el_GR">
<meta property="og:site_name" content="BIOLAB — {S['tagline']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{S['url']}/assets/images/{og}.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/images/og-image.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{extra}</head>
<body class="has-floating">
<a class="skip-link" href="#main">Μετάβαση στο περιεχόμενο</a>
"""


def header(page):
    drops = "".join(
        f'<li><a href="{c["slug"]}"><span class="num">{c["n"]}</span><span>{c["nav"]}</span></a></li>'
        for c in CATS)
    exam_pages = {c["slug"] for c in CATS} | {"exetaseis.html"}

    items = []
    for href, label in NAV:
        if href == "exetaseis.html":
            cur = ' aria-current="page"' if page in exam_pages else ""
            items.append(
                f'<li class="has-drop"><a class="nav-link" href="{href}"{cur}>{label}{CARET}</a>'
                f'<ul class="dropdown">{drops}'
                f'<li class="all"><a href="exetaseis.html"><span class="num">→</span>'
                f'<span>Όλες οι εξετάσεις</span></a></li></ul></li>')
        else:
            cur = ' aria-current="page"' if page == href else ""
            items.append(f'<li><a class="nav-link" href="{href}"{cur}>{label}</a></li>')

    mob_sub = "".join(f'<li><a href="{c["slug"]}">{c["n"]} — {c["nav"]}</a></li>' for c in CATS)
    mob = []
    for href, label in NAV:
        mob.append(f'<li><a href="{href}">{label}</a>')
        if href == "exetaseis.html":
            mob.append(f'<ul class="mobile-sub">{mob_sub}</ul>')
        mob.append("</li>")

    return f"""<div class="topbar">
  <div class="container topbar-inner">
    <div class="topbar-hours"><span class="topbar-dot"></span><span>{S['hours']} · Σάββατο &amp; Κυριακή κλειστά</span></div>
    <div class="topbar-links">
      <a class="hide-sm" href="{S['maps']}" target="_blank" rel="noopener">{S['address']}, {S['city']}</a>
      <a href="mailto:{S['email']}">{S['email']}</a>
      <a href="tel:{S['phone_href']}">{S['phone']}</a>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="BIOLAB — Αρχική">
      {LOGO}
    </a>
    <nav aria-label="Κύρια πλοήγηση">
      <ul class="nav-links">{''.join(items)}</ul>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-sm" href="epikoinonia.html#rantevou">Κλείστε ραντεβού</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Άνοιγμα μενού">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<div class="mobile-nav" id="mobile-nav">
  <div class="container">
    <div class="mobile-nav-head">
      <span class="brand">{LOGO}</span>
      <button class="mobile-close" type="button" aria-label="Κλείσιμο μενού">✕</button>
    </div>
    <ul class="mobile-list">{''.join(mob)}</ul>
    <div class="mobile-foot">
      <a class="btn btn-light" href="epikoinonia.html#rantevou">Κλείστε ραντεβού</a>
      <a class="small" href="tel:{S['phone_href']}">{S['phone']}</a>
      <a class="small" href="mailto:{S['email']}">{S['email']}</a>
      <a class="small" href="{S['maps']}" target="_blank" rel="noopener">{S['address']}, {S['city']}</a>
    </div>
  </div>
</div>

<main id="main">
"""


def cta_band(title="Είμαστε εδώ για την επόμενη εξέτασή σας.",
             text="Επικοινωνήστε μαζί μας για να προγραμματίσουμε το ραντεβού σας ή για "
                  "οποιαδήποτε διευκρίνιση σχετικά με μια εξέταση."):
    return f"""<section class="cta-band">
  <div class="cta-band-media">{pic('cta-band', 'Δείγματα σε ράκα κατά την προετοιμασία ανάλυσης')}</div>
  <div class="container reveal">
    <p class="eyebrow">Επικοινωνία</p>
    <h2 class="h2">{title}</h2>
    <p class="lead">{text}</p>
    <div class="cta-actions">
      <a class="btn btn-light" href="tel:{S['phone_href']}">Καλέστε {S['phone']}{ARW}</a>
      <a class="btn btn-outline-light" href="epikoinonia.html#rantevou">Φόρμα ραντεβού</a>
    </div>
  </div>
</section>
"""


def footer():
    ex1 = "".join(f'<li><a href="{c["slug"]}">{c["nav"]}</a></li>' for c in CATS[:5])
    ex2 = "".join(f'<li><a href="{c["slug"]}">{c["nav"]}</a></li>' for c in CATS[5:])
    return f"""</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <span class="brand">{LOGO}</span>
        <p>{S['legal']} — σύγχρονο εργαστήριο μοριακής διάγνωσης στις Σέρρες, με δέσμευση
        σε αξιόπιστα αποτελέσματα για ιδιώτες και επαγγελματίες υγείας.</p>
        <div class="footer-contact">
          <a href="tel:{S['phone_href']}">{S['phone']}</a>
          <a href="tel:{S['mobile_href']}">{S['mobile']}</a>
          <a href="mailto:{S['email']}">{S['email']}</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Εξετάσεις</h4>
        <ul>{ex1}</ul>
      </div>
      <div class="footer-col">
        <h4>&nbsp;</h4>
        <ul>{ex2}</ul>
      </div>
      <div class="footer-col">
        <h4>Ωράριο &amp; διεύθυνση</h4>
        <div class="hours">
          <div><span>Δευτέρα – Παρασκευή</span><span>09:00 – 17:00</span></div>
          <div><span>Σάββατο – Κυριακή</span><span>Κλειστά</span></div>
        </div>
        <ul style="margin-top:22px">
          <li><a href="{S['maps']}" target="_blank" rel="noopener">{S['address']}, {S['postal']} {S['city']} ↗</a></li>
          <li><a href="ergastirio.html">Το εργαστήριο</a></li>
          <li><a href="omada.html">Η ομάδα μας</a></li>
          <li><a href="poiotita.html">Ποιότητα &amp; πιστοποιήσεις</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> {S['legal']} — Όλα τα δικαιώματα διατηρούνται.</span>
      <span class="links">
        <a href="politiki-aporritou.html">Πολιτική Απορρήτου</a>
        <a href="epikoinonia.html">Επικοινωνία</a>
        <a class="madeby" href="https://clinicbrain.gr" target="_blank" rel="noopener">
          Made by <strong>CLINICBRAIN</strong> <span aria-hidden="true">↗</span>
        </a>
      </span>
    </div>
  </div>
</footer>

<div class="floating-cta">
  <a href="tel:{S['phone_href']}">☎ Τηλέφωνο</a>
  <a href="epikoinonia.html#rantevou">Ραντεβού</a>
</div>

<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def page_hero(eyebrow, title, lead, img, crumbs):
    cr = ['<a href="index.html">Αρχική</a><span aria-hidden="true">/</span>']
    for label, href in crumbs[:-1]:
        cr.append(f'<a href="{href}">{label}</a><span aria-hidden="true">/</span>')
    cr.append(f'<span aria-current="page">{crumbs[-1][0]}</span>')
    return f"""<section class="page-hero">
  <div class="page-hero-media">{pic(img, '', loading='eager')}</div>
  <div class="container">
    <nav class="breadcrumb" aria-label="Διαδρομή">{''.join(cr)}</nav>
    <p class="eyebrow">{eyebrow}</p>
    <h1 class="h1">{title}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
"""


def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  {name:38s} {len(html)//1024:>4d} KB")


# ═══════════════════════════════════════════════════════════════════════
#  ΑΡΧΙΚΗ
# ═══════════════════════════════════════════════════════════════════════
FEATURES = [
    ("shield", "Πιστοποίηση ISO 9001:2015",
     "Σύστημα διαχείρισης ποιότητας πιστοποιημένο από την EUROCERT."),
    ("clock", "Γρήγορη παράδοση",
     "Αποτελέσματα σε σύντομο χρόνο, με ασφαλή ηλεκτρονική παράδοση."),
    ("home", "Δειγματοληψία κατ' οίκον",
     "Αιμοληψία στον χώρο σας, κατόπιν ραντεβού, σε όλο τον νομό Σερρών."),
    ("users", "Εξειδικευμένη ομάδα",
     "Μοριακοί βιολόγοι και ιατροί βιοπαθολόγοι με πολυετή εμπειρία."),
]

ICONS = {
    "shield": '<path d="M12 2 4 5.5v6c0 5 3.4 9.2 8 10.5 4.6-1.3 8-5.5 8-10.5v-6L12 2Z"/><path d="m9 12 2 2 4-4"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 1.9"/>',
    "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5.5 9.5V20h13V9.5"/><path d="M10 20v-5.5h4V20"/>',
    "users": '<circle cx="9" cy="8" r="3.2"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16.5 5.4a3.2 3.2 0 0 1 0 5.2M17.5 14.4A6.5 6.5 0 0 1 21.5 20"/>',
}


def icon(name):
    return (f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            f'{ICONS[name]}</svg>')


def build_index():
    feats = "".join(
        f'<div class="feature-item reveal">{icon(k)}<h3>{t}</h3><p>{d}</p></div>'
        for k, t, d in FEATURES)

    cards = "".join(f"""<a class="exam-card reveal" href="{c['slug']}">
      <span class="num">{c['n']}</span>
      <h3>{c['short']}</h3>
      <p>{c['summary']}</p>
      <span class="go">Δείτε τις εξετάσεις</span>
    </a>""" for c in CATS)
    cards += f"""<a class="exam-card exam-card--cta reveal" href="epikoinonia.html#rantevou">
      <span class="num">—</span>
      <h3>Δεν βρίσκετε την εξέταση που ψάχνετε;</h3>
      <p>Ο κατάλογός μας είναι ευρύτερος από όσα παρουσιάζονται εδώ. Καλέστε μας στο
      {S['phone']} και θα σας ενημερώσουμε άμεσα για τη διαθεσιμότητα, την προετοιμασία
      και τον χρόνο απάντησης.</p>
      <span class="go">Επικοινωνήστε μαζί μας</span>
    </a>"""

    schema = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"MedicalLaboratory",
"name":"BIOLAB — Μικροβιολογικό & Μοριακό Εργαστήριο",
"alternateName":"Εργαστήριο BIOLAB — Μοριακή Διαγνωστική Ο.Ε.",
"url":"https://www.biolabs.gr","telephone":"+30 23211 21602","email":"info@biolabs.gr",
"image":"https://www.biolabs.gr/assets/images/og-image.jpg",
"address":{"@type":"PostalAddress","streetAddress":"Τσαλοπούλου 15","addressLocality":"Σέρρες","postalCode":"62122","addressCountry":"GR"},
"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"17:00"}],
"medicalSpecialty":["Pathology","Genetics"]}
</script>
"""

    return (
        head("BIOLAB — Μικροβιολογικό &amp; Μοριακό Εργαστήριο | Σέρρες",
             "Μικροβιολογικό και μοριακό εργαστήριο BIOLAB στις Σέρρες. Μικροβιολογικές και "
             "μοριακές εξετάσεις, γενετικός έλεγχος, προγεννητικός έλεγχος, ανδρολογία, "
             "μοριακή ογκολογία και έλεγχος πατρότητας.",
             "index.html", extra=schema)
        + header("index.html")
        + f"""
<section class="hero">
  <div class="hero-media">{pic('hero', 'Επιστήμονας του BIOLAB κατά την προετοιμασία δειγμάτων σε θάλαμο βιολογικής ασφάλειας', loading='eager', fetch=True)}</div>
  <div class="container hero-inner">
    <p class="eyebrow">Μικροβιολογικό &amp; Μοριακό Εργαστήριο · Σέρρες</p>
    <h1 class="display">Ακρίβεια στη διάγνωση.<br><em>Σαφήνεια</em> στην απάντηση.</h1>
    <p class="hero-lead">Στο BIOLAB συνδυάζουμε τη σύγχρονη τεχνολογία μοριακής διαγνωστικής
    με έμπειρο επιστημονικό προσωπικό, για αξιόπιστα αποτελέσματα που στηρίζουν
    πραγματικά την απόφαση του ιατρού και του ασθενούς.</p>
    <div class="hero-actions">
      <a class="btn btn-light" href="exetaseis.html#analytikes-ypiresies">Δείτε τις εξετάσεις{ARW}</a>
      <a class="btn btn-outline-light" href="epikoinonia.html#rantevou">Κλείστε ραντεβού</a>
    </div>
    <dl class="hero-stats">
      <div><dt>10</dt><dd>κατηγορίες εξειδικευμένων<br>διαγνωστικών υπηρεσιών</dd></div>
      <div><dt>ISO 9001</dt><dd>πιστοποιημένο σύστημα<br>διαχείρισης ποιότητας</dd></div>
      <div><dt>CE IVD</dt><dd>πιστοποιημένος εξοπλισμός<br>και αντιδραστήρια</dd></div>
    </dl>
  </div>
</section>

<section class="feature-strip">
  <div class="container">
    <div class="feature-grid">{feats}</div>
  </div>
</section>

<section class="sec">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Το εργαστήριο</p>
      <h2 class="h2">Μια εξέταση αξίζει<br>όσο και η ερμηνεία της.</h2>
      <p class="lead" style="margin-top:24px">Το εργαστήριο BIOLAB — Μοριακή Διαγνωστική Ο.Ε.
      λειτουργεί στις Σέρρες, καλύπτοντας τόσο τις κλασικές μικροβιολογικές αναλύσεις
      όσο και τον εξειδικευμένο μοριακό και γενετικό έλεγχο.</p>
      <p>Προτεραιότητά μας είναι η παροχή έγκυρων και αξιόπιστων αποτελεσμάτων,
      συνδυάζοντας τις πιο πρόσφατες επιστημονικές και τεχνολογικές εξελίξεις στη
      διαγνωστική ιατρική με άριστα εκπαιδευμένο προσωπικό και σύγχρονες υποδομές.</p>
      <ul class="check-list">
        <li>Πιστοποιημένος εξοπλισμός και αντιδραστήρια CE IVD σε κάθε ανάλυση</li>
        <li>Διακριτές ζώνες μοριακής εργασίας για αποκλεισμό επιμολύνσεων</li>
        <li>Εσωτερικός ποιοτικός έλεγχος σε κάθε σειρά μετρήσεων</li>
        <li>Άμεση επικοινωνία με τον θεράποντα ιατρό για κάθε εύρημα</li>
      </ul>
      <p style="margin-top:30px"><a class="textlink" href="ergastirio.html">Γνωρίστε τον χώρο και τον εξοπλισμό</a></p>
    </div>
    <div class="split-media wide reveal">
      {pic('about-lab', 'Ο χώρος μοριακής βιολογίας του εργαστηρίου BIOLAB')}
      <div class="badge-card"><strong>ISO 9001</strong><span>Πιστοποίηση συστήματος διαχείρισης ποιότητας από την EUROCERT</span></div>
    </div>
  </div>
</section>

<section class="sec sec-off" id="exetaseis">
  <div class="container">
    <div class="sec-head-split reveal">
      <div>
        <p class="eyebrow">Οι εξετάσεις μας</p>
        <h2 class="h2">Δέκα κατηγορίες.<br>Μία υπογραφή ποιότητας.</h2>
      </div>
      <p class="lead">Από τη γενική αίματος έως την αλληλούχιση νέας γενιάς — επιλέξτε την
      κατηγορία που σας αφορά για να δείτε αναλυτικά τις διαθέσιμες εξετάσεις, τις
      οδηγίες προετοιμασίας και τον χρόνο απάντησης.</p>
    </div>
    <div class="exam-grid">{cards}</div>
  </div>
</section>

<section class="sec sec-dark">
  <div class="container">
    <div class="sec-head reveal">
      <p class="eyebrow">Η εμπειρία σας</p>
      <h2 class="h2">Απλή διαδικασία,<br>ξεκάθαρο αποτέλεσμα.</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><span class="n">01</span><h3>Ραντεβού</h3>
        <p>Καλέστε μας ή στείλτε το αίτημά σας. Σας ενημερώνουμε αναλυτικά για την
        προετοιμασία, το κόστος και τον χρόνο απάντησης της εξέτασης.</p></div>
      <div class="step reveal"><span class="n">02</span><h3>Δειγματοληψία</h3>
        <p>Η λήψη γίνεται στο εργαστήριο ή, εφόσον χρειάζεται, στον χώρο σας. Κάθε δείγμα
        κωδικοποιείται και παρακολουθείται σε όλα τα στάδια της ανάλυσης.</p></div>
      <div class="step reveal"><span class="n">03</span><h3>Αποτέλεσμα</h3>
        <p>Παραλαμβάνετε την έκθεση από το εργαστήριο ή ηλεκτρονικά, με πλήρη επεξήγηση
        των ευρημάτων και επικοινωνία με τον θεράποντα ιατρό σας.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="container split">
    <div class="split-media tall reveal">{pic('quality', 'Επιστήμονας σε θάλαμο νηματικής ροής κατά την ανάλυση δείγματος')}</div>
    <div class="reveal">
      <p class="eyebrow">Ποιότητα</p>
      <h2 class="h2">Η αξιοπιστία δεν<br>δηλώνεται. Τεκμηριώνεται.</h2>
      <p class="lead" style="margin-top:24px">Το εργαστήριο εφαρμόζει πιστοποιημένο σύστημα
      διαχείρισης ποιότητας και συμμετέχει ενεργά στις εξελίξεις της μοριακής διάγνωσης
      μέσα από διεθνείς επιστημονικές κοινότητες.</p>
      <ul class="check-list">
        <li><strong>ISO 9001:2015</strong> — πιστοποίηση από την EUROCERT</li>
        <li><strong>ESHG</strong> — Ευρωπαϊκή Εταιρεία Γενετικής του Ανθρώπου</li>
        <li><strong>ESCCA</strong> — Ευρωπαϊκή Εταιρεία Κλινικής Ανάλυσης Κυττάρων</li>
        <li>Συμμετοχή σε σχήματα εξωτερικού ποιοτικού ελέγχου</li>
      </ul>
      <p style="margin-top:30px"><a class="textlink" href="poiotita.html">Διαβάστε την πολιτική ποιότητας</a></p>
    </div>
  </div>
</section>

<section class="sec sec-tight sec-off">
  <div class="container">
    <div class="sec-head-split reveal">
      <div>
        <p class="eyebrow">Ο χώρος μας</p>
        <h2 class="h2">Υποδομές που στηρίζουν<br>το αποτέλεσμα.</h2>
      </div>
      <p class="lead">Θάλαμοι βιολογικής ασφάλειας, σύγχρονοι αναλυτές και διακριτές ζώνες
      μοριακής εργασίας — σε έναν χώρο σχεδιασμένο για ακρίβεια και ασφάλεια.</p>
    </div>
    <div class="gallery reveal">
      <figure>{pic('facility-clean', 'Θάλαμος βιολογικής ασφάλειας στον χώρο μοριακής βιολογίας')}</figure>
      <figure>{pic('facility-seq', 'Σύστημα αλληλούχισης νέας γενιάς')}</figure>
      <figure>{pic('gallery-3', 'Αυτόματες πιπέτες ακριβείας')}</figure>
      <figure>{pic('pcr', 'Συσκευές Real-Time PCR και φυγόκεντρος')}</figure>
      <figure>{pic('facility-analyzer', 'Αυτόματος αναλυτής με σταθμό εργασίας')}</figure>
      <figure>{pic('hood-blue', 'Εξοπλισμός εντός θαλάμου νηματικής ροής')}</figure>
    </div>
    <p style="margin-top:34px" class="reveal"><a class="textlink" href="ergastirio.html">Δείτε όλο τον χώρο</a></p>
  </div>
</section>

"""
        + TEAM_PREVIEW
        + cta_band()
        + footer())


# ═══════════════════════════════════════════════════════════════════════
#  HUB ΕΞΕΤΑΣΕΩΝ
# ═══════════════════════════════════════════════════════════════════════
def build_exetaseis():
    cards = "".join(f"""<a class="icard reveal" href="{c['slug']}">
      <div class="icard-media">{pic(c['card_img'], c['short'])}</div>
      <div class="icard-body">
        <span class="num">{c['n']}</span>
        <h3>{c['short']}</h3>
        <p>{c['summary']}</p>
        <span class="go">Αναλυτικά</span>
      </div>
    </a>""" for c in CATS)

    return (
        head("Διαγνωστικές εξετάσεις | BIOLAB Σέρρες",
             "Όλες οι κατηγορίες εξετάσεων του BIOLAB: μικροβιολογικές, μοριακές, γενετικός "
             "έλεγχος, υπογονιμότητα, ανδρολογία, ανοσολογία, προγεννητικός έλεγχος, "
             "μοριακή ογκολογία, έλεγχος πατρότητας και γενετική συμβουλευτική.",
             "exetaseis.html")
        + header("exetaseis.html")
        + page_hero("Διαγνωστικές εξετάσεις",
                    "Βρείτε την εξέταση<br>που χρειάζεστε.",
                    "Δέκα κατηγορίες εξετάσεων, από τη μικροβιολογία ρουτίνας έως τον "
                    "εξειδικευμένο γενετικό έλεγχο. Επιλέξτε κατηγορία για αναλυτικές "
                    "πληροφορίες, οδηγίες προετοιμασίας και χρόνους απάντησης.",
                    "facility-clean", [("Διαγνωστικές εξετάσεις", "exetaseis.html")])
        + f"""
<section class="sec">
  <div class="container">
    <div class="card-grid">{cards}</div>
  </div>
</section>

{catalog()}
<section class="sec sec-tight sec-off">
  <div class="container container-narrow">
    <div class="sec-head center reveal" style="margin-bottom:34px">
      <p class="eyebrow center">Συχνές ερωτήσεις</p>
      <h2 class="h2">Πριν από την επίσκεψή σας</h2>
    </div>
    <div class="faq reveal">
      {faq([
        ("Χρειάζεται ραντεβού;",
         "Για τις αιματολογικές και βιοχημικές εξετάσεις ρουτίνας μπορείτε να προσέλθετε "
         "χωρίς ραντεβού εντός του ωραρίου λειτουργίας. Για τις εξειδικευμένες μοριακές και "
         "γενετικές εξετάσεις, τον προγεννητικό έλεγχο και τη γενετική συμβουλευτική "
         "απαιτείται ραντεβού, ώστε να σας δοθούν αναλυτικές οδηγίες προετοιμασίας."),
        ("Πρέπει να είμαι νηστικός;",
         "Για τις περισσότερες αιματολογικές και βιοχημικές εξετάσεις απαιτείται νηστεία "
         "8–12 ωρών, με ελεύθερη κατανάλωση νερού. Για τις μοριακές και γενετικές εξετάσεις "
         "δεν απαιτείται νηστεία. Σε κάθε περίπτωση, επιβεβαιώστε μαζί μας κατά τον "
         "προγραμματισμό του ραντεβού."),
        ("Χρειάζομαι παραπεμπτικό από ιατρό;",
         "Μπορείτε να απευθυνθείτε στο εργαστήριο και χωρίς παραπεμπτικό. Ωστόσο, για τις "
         "εξειδικευμένες εξετάσεις — ιδίως στη μοριακή ογκολογία και στον γενετικό έλεγχο — "
         "συνιστάται η παραπομπή από τον θεράποντα ιατρό, ώστε το πάνελ να επιλεγεί με βάση "
         "το κλινικό ερώτημα."),
        ("Πώς παραλαμβάνω τα αποτελέσματα;",
         "Τα αποτελέσματα παραδίδονται από το εργαστήριο ή αποστέλλονται ηλεκτρονικά, "
         "αποκλειστικά στον εξεταζόμενο ή σε πρόσωπο που αυτός έχει εξουσιοδοτήσει "
         "εγγράφως. Για κάθε παθολογικό εύρημα επικοινωνούμε απευθείας με τον θεράποντα "
         "ιατρό σας."),
        ("Γίνεται δειγματοληψία στο σπίτι;",
         "Ναι. Πραγματοποιούμε αιμοληψία κατ' οίκον κατόπιν ραντεβού, για ηλικιωμένους, "
         "ασθενείς με κινητικές δυσκολίες ή όποιον δυσκολεύεται να μετακινηθεί. "
         "Επικοινωνήστε μαζί μας για τη διαθεσιμότητα και το κόστος της υπηρεσίας."),
      ])}
    </div>
  </div>
</section>

"""
        + cta_band()
        + footer())


def faq(items):
    out = []
    for i, (q, a) in enumerate(items, 1):
        out.append(f"""<div class="faq-item">
        <h3><button class="faq-q" type="button" aria-expanded="false" aria-controls="faq-p{i}">
          <span>{q}</span><span class="sign" aria-hidden="true"></span>
        </button></h3>
        <div class="faq-a" id="faq-p{i}" style="height:0"><div class="faq-a-inner">{a}</div></div>
      </div>""")
    return "".join(out)


# ═══════════════════════════════════════════════════════════════════════
#  ΣΕΛΙΔΕΣ ΚΑΤΗΓΟΡΙΩΝ
# ═══════════════════════════════════════════════════════════════════════
def build_cat(c):
    side = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in c["side"])
    chips = "".join(
        f'<a class="chip" href="{o["slug"]}"{" aria-current=\"page\"" if o is c else ""}>{o["short"]}</a>'
        for o in CATS)
    title_plain = c["short"]

    return (
        head(f"{title_plain} | BIOLAB Σέρρες",
             c["lead"].replace('"', "'")[:300],
             c["slug"], og=c["hero"])
        + header(c["slug"])
        + page_hero(f"Εξετάσεις · {c['n']}", c["title"], c["lead"], c["hero"],
                    [("Διαγνωστικές εξετάσεις", "exetaseis.html"), (title_plain, c["slug"])])
        + f"""
<section class="sec">
  <div class="container detail-layout">
    <div class="prose reveal">{c['body']}</div>
    <aside class="reveal">
      <div class="sidecard">
        <div class="sidecard-head">
          <h3>Χρήσιμες πληροφορίες</h3>
          <p>Για αναλυτικές οδηγίες προετοιμασίας και κόστος, επικοινωνήστε με το εργαστήριο.</p>
        </div>
        <div class="sidecard-body">
          <dl>{side}</dl>
          <a class="btn" href="epikoinonia.html#rantevou">Κλείστε ραντεβού{ARW}</a>
          <p style="margin-top:16px;font-size:13.5px;color:var(--muted)">
            ή καλέστε <a href="tel:{S['phone_href']}" style="color:var(--navy-800);font-weight:600">{S['phone']}</a>
          </p>
        </div>
      </div>
    </aside>
  </div>
</section>

<section class="sec sec-tight sec-off">
  <div class="container">
    <p class="eyebrow">Όλες οι κατηγορίες</p>
    <div class="chip-row">{chips}</div>
  </div>
</section>

"""
        + cta_band()
        + footer())


# ═══════════════════════════════════════════════════════════════════════
#  ΤΟ ΕΡΓΑΣΤΗΡΙΟ
# ═══════════════════════════════════════════════════════════════════════
def build_ergastirio():
    return (
        head("Το εργαστήριο | BIOLAB Σέρρες",
             "Ο χώρος, ο εξοπλισμός και οι υποδομές του μικροβιολογικού και μοριακού "
             "εργαστηρίου BIOLAB στις Σέρρες.",
             "ergastirio.html", og="facility-clean")
        + header("ergastirio.html")
        + page_hero("Ο χώρος μας", "Υποδομές<br>σχεδιασμένες για ακρίβεια.",
                    "Ένα σύγχρονο εργαστήριο μοριακής διάγνωσης στο κέντρο των Σερρών, "
                    "με διακριτές ζώνες εργασίας, πιστοποιημένο εξοπλισμό και αυστηρά "
                    "πρωτόκολλα ασφάλειας.",
                    "facility-clean", [("Το εργαστήριο", "ergastirio.html")])
        + f"""
<section class="sec">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Οργάνωση χώρου</p>
      <h2 class="h2">Καθαρές ζώνες,<br>μονόδρομη ροή δείγματος.</h2>
      <p class="lead" style="margin-top:24px">Στη μοριακή διαγνωστική, η μεγαλύτερη απειλή
      για ένα αποτέλεσμα είναι η επιμόλυνση. Γι' αυτό ο χώρος του εργαστηρίου είναι
      οργανωμένος σε διακριτές, φυσικά διαχωρισμένες ζώνες.</p>
      <ul class="check-list">
        <li>Ξεχωριστή ζώνη προετοιμασίας αντιδραστηρίων, χωρίς είσοδο δείγματος</li>
        <li>Ζώνη εκχύλισης νουκλεϊκών οξέων σε θάλαμο βιολογικής ασφάλειας</li>
        <li>Απομονωμένη ζώνη ενίσχυσης και ανάλυσης προϊόντων PCR</li>
        <li>Μονόδρομη ροή προσωπικού, υλικών και δειγμάτων</li>
        <li>Θετικοί και αρνητικοί μάρτυρες σε κάθε σειρά αναλύσεων</li>
      </ul>
    </div>
    <div class="split-media wide reveal">{pic('facility-hood', 'Θάλαμος βιολογικής ασφάλειας στον χώρο εκχύλισης')}</div>
  </div>
</section>

<section class="sec sec-dark">
  <div class="container">
    <div class="sec-head-split reveal">
      <div>
        <p class="eyebrow">Εξοπλισμός</p>
        <h2 class="h2">Πιστοποιημένος<br>σε κάθε βήμα.</h2>
      </div>
      <p class="lead">Όλες οι αναλύσεις εκτελούνται με εξοπλισμό και αντιδραστήρια
      πιστοποιημένα κατά CE IVD, με τεκμηριωμένο πρόγραμμα συντήρησης και διακρίβωσης.</p>
    </div>
    <div class="cert-grid reveal">
      <div class="cert"><span class="tag">Μοριακή βιολογία</span>
        <h3>Real-Time PCR &amp; αλληλούχιση</h3>
        <p>Συστήματα Real-Time PCR και αλληλούχισης νέας γενιάς για μοριακή μικροβιολογία,
        γενετικό έλεγχο και μοριακή ογκολογία.</p></div>
      <div class="cert"><span class="tag">Κυτταρομετρία</span>
        <h3>Κυτταρομετρία ροής</h3>
        <p>Ανοσοφαινοτυπικός έλεγχος πολλαπλών παραμέτρων για τη διάγνωση και
        παρακολούθηση αιματολογικών νοσημάτων.</p></div>
      <div class="cert"><span class="tag">Αυτοματοποίηση</span>
        <h3>Αυτόματοι αναλυτές</h3>
        <p>Αιματολογικοί, βιοχημικοί και ανοσολογικοί αναλυτές με συνεχή εσωτερικό
        ποιοτικό έλεγχο και ιχνηλασιμότητα δείγματος.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="container">
    <div class="sec-head reveal">
      <p class="eyebrow">Φωτογραφίες</p>
      <h2 class="h2">Ο χώρος μας</h2>
    </div>
    <div class="gallery reveal">
      <figure>{pic('brand-wall', 'Η υποδοχή του εργαστηρίου BIOLAB')}</figure>
      <figure>{pic('exam-room', 'Ο χώρος δειγματοληψίας')}</figure>
      <figure>{pic('gallery-1', 'Επιστήμονας κατά την ανάλυση δείγματος')}</figure>
      <figure>{pic('facility-analyzer', 'Σταθμός εργασίας με αυτόματο αναλυτή')}</figure>
      <figure>{pic('gallery-2', 'Λήψη δείγματος με πιπέτα ακριβείας')}</figure>
      <figure>{pic('tubes', 'Σωληνάρια δειγμάτων σε ράκα')}</figure>
      <figure>{pic('hood-blue', 'Εξοπλισμός εντός θαλάμου νηματικής ροής')}</figure>
      <figure>{pic('gallery-5', 'Προετοιμασία δειγμάτων προς ανάλυση')}</figure>
      <figure>{pic('cylinders', 'Ογκομετρικοί κύλινδροι')}</figure>
      <figure>{pic('gallery-6', 'Εργασία σε θάλαμο βιολογικής ασφάλειας')}</figure>
      <figure>{pic('monitor', 'Αναλυτής με σταθμό ελέγχου')}</figure>
      <figure>{pic('plate', 'Πλάκα 96 θέσεων κατά την προετοιμασία')}</figure>
    </div>
  </div>
</section>

"""
        + cta_band("Ελάτε να γνωριστούμε.",
                   "Το εργαστήριο βρίσκεται στην Τσαλοπούλου 15, στο κέντρο των Σερρών.")
        + footer())


# ═══════════════════════════════════════════════════════════════════════
#  Η ΟΜΑΔΑ
# ═══════════════════════════════════════════════════════════════════════
def build_omada():
    return (
        head("Η ομάδα μας | BIOLAB Σέρρες",
             "Η επιστημονική ομάδα του εργαστηρίου BIOLAB: μοριακοί βιολόγοι και ιατροί "
             "βιοπαθολόγοι με πολυετή εμπειρία στη μοριακή διάγνωση.",
             "omada.html", og="portrait-work")
        + header("omada.html")
        + page_hero("Εξειδίκευση &amp; αξιοπιστία", "Η ομάδα<br>του εργαστηρίου.",
                    "Εξειδικευμένοι επιστήμονες με πολυετή εμπειρία και αφοσίωση στον τομέα "
                    "της μοριακής διάγνωσης. Κάθε μέλος συμβάλλει με τη γνώση του στην "
                    "παροχή αξιόπιστων και εξατομικευμένων διαγνωστικών λύσεων.",
                    "portrait-work", [("Η ομάδα μας", "omada.html")])
        + f"""
<section class="sec">
  <div class="container">

    <article class="person reveal">
      <div class="person-media"><img src="assets/images/maria-taousani.png" alt="Μαρία Ταουσάνη, Μοριακή Βιολόγος" loading="lazy" decoding="async"></div>
      <div>
        <p class="person-role">Μοριακή Βιολόγος · Γενική Διευθύντρια</p>
        <h2>Ταουσάνη Μαρία</h2>
        <div class="bio">
          <p>Επικεφαλής Μοριακή Βιολόγος του εργαστηρίου, με εξειδίκευση στη Μοριακή
          Βιολογία και τη Γενετική. Διασφαλίζει την ποιότητα και την ακρίβεια των
          υπηρεσιών του BIOLAB, συμμετέχοντας ενεργά στις εξελίξεις της μοριακής διάγνωσης.</p>
        </div>
        <dl>
          <div><dt>Ακαδημαϊκές σπουδές</dt>
            <dd>Απόφοιτη του Τμήματος Βιολογίας του Αριστοτελείου Πανεπιστημίου Θεσσαλονίκης,
            με μεταπτυχιακό στη Γενετική Ανθρώπου και Γενετική Συμβουλευτική από το
            Πανεπιστήμιο Θεσσαλίας.</dd></div>
          <div><dt>Ερευνητική δραστηριότητα</dt>
            <dd>Συμμετοχή σε πολυάριθμες ερευνητικές μελέτες και διατριβές σε θέματα όπως
            ο διαβήτης τύπου 1 και ο κληρονομικός καρκίνος του μαστού.</dd></div>
          <div><dt>Εξειδίκευση</dt>
            <dd>Διαχείριση συστημάτων ποιότητας ISO 9001, με πιστοποιήσεις από τους
            οργανισμούς TÜV HELLAS και CQI/IRCA.</dd></div>
          <div><dt>Συμμετοχή σε οργανισμούς</dt>
            <dd>Μέλος του European Board of Medical Genetics, της European Society for
            Clinical Cell Analysis και της Ελληνικής Εταιρείας Κυτταρομετρίας Ροής.</dd></div>
        </dl>
      </div>
    </article>

    <article class="person reveal">
      <div class="person-media"><img src="assets/images/aikaterini-tzioura.jpg" alt="Αικατερίνη Τζιούρα, Ιατρός Βιοπαθολόγος" loading="lazy" decoding="async"></div>
      <div>
        <p class="person-role">Ιατρός Βιοπαθολόγος</p>
        <h2>Τζιούρα Αικατερίνη</h2>
        <div class="bio">
          <p>Έμπειρη ιατρός με ειδικότητα Ιατρικής Βιοπαθολογίας, την οποία ολοκλήρωσε στο
          Γ.Ν. «Γ. Παπανικολάου» Θεσσαλονίκης.</p>
        </div>
        <dl>
          <div><dt>Μεταπτυχιακές σπουδές</dt>
            <dd>Ελληνικό Ανοικτό Πανεπιστήμιο — Μεταπτυχιακό Πρόγραμμα «Διοίκηση Υπηρεσιών
            Υγείας του Ε.Σ.Υ.», Σχολή Κοινωνικών Επιστημών.</dd></div>
          <div><dt>Διδακτορική διατριβή</dt>
            <dd>Πανεπιστήμιο Θεσσαλίας, Τμήμα Ιατρικής — «Μοριακή δομή, αλλήλια και γενετικοί
            πολυμορφισμοί του συστήματος Rhesus· ανάλυση των αντιγόνων, διερεύνηση γονιδιακών
            μεταλλάξεων και γενετική μελέτη σε κλειστούς πληθυσμούς στη Βόρειο Ελλάδα».</dd></div>
          <div><dt>Επαγγελματική εμπειρία</dt>
            <dd>Από το 1997 Επιμελήτρια στην Αιμοδοσία του Νοσοκομείου Σερρών. Από το 2012
            Συντονίστρια Διευθύντρια, επιστημονικά και διοικητικά υπεύθυνη της Αιμοδοσίας,
            της Μονάδας Πρόληψης Μεσογειακής Αναιμίας και Δρεπανοκυτταρικής Νόσου και του
            Αιματολογικού Εργαστηρίου του Γ.Ν. Σερρών.</dd></div>
        </dl>
      </div>
    </article>

    <article class="person reveal">
      <div class="person-media"><img src="assets/images/chrysanthi-mpoutsiou.png" alt="Χρυσάνθη Μπούτσιου, Βοηθός Ιατρικών Εργαστηρίων" loading="lazy" decoding="async"></div>
      <div>
        <p class="person-role">Βοηθός Ιατρικών Εργαστηρίων</p>
        <h2>Μπούτσιου Χρυσάνθη</h2>
        <div class="bio">
          <p>Υποστηρίζει τις καθημερινές λειτουργίες του εργαστηρίου, με εξειδίκευση στην
          επεξεργασία των δειγμάτων και στην εκτέλεση των βασικών εργαστηριακών διαδικασιών.</p>
        </div>
        <dl>
          <div><dt>Εκπαίδευση</dt>
            <dd>Απόφοιτη επαγγελματικής κατάρτισης ως Βοηθός Ιατρικών Εργαστηρίων (2022).</dd></div>
          <div><dt>Ρόλος στο εργαστήριο</dt>
            <dd>Παραλαβή, κωδικοποίηση και προετοιμασία δειγμάτων, τήρηση των πρωτοκόλλων
            ιχνηλασιμότητας και υποστήριξη του αναλυτικού σταδίου.</dd></div>
        </dl>
      </div>
    </article>

  </div>
</section>

<section class="sec sec-tight sec-off">
  <div class="container container-narrow" style="text-align:center">
    <p class="eyebrow center reveal">Η φιλοσοφία μας</p>
    <h2 class="h2 reveal">Είμαστε πάντα δίπλα σας<br>για κάθε διευκρίνιση.</h2>
    <p class="lead reveal" style="margin-top:22px">Η ομάδα μας εργάζεται με αφοσίωση και
    επαγγελματισμό, παρέχοντας προηγμένες διαγνωστικές λύσεις για τις ανάγκες σας —
    και είναι στη διάθεσή σας για οποιαδήποτε απορία, πριν ή μετά από κάθε εξέταση.</p>
  </div>
</section>

"""
        + cta_band()
        + footer())


# ═══════════════════════════════════════════════════════════════════════
#  ΠΟΙΟΤΗΤΑ
# ═══════════════════════════════════════════════════════════════════════
def build_poiotita():
    return (
        head("Ποιότητα &amp; πιστοποιήσεις | BIOLAB Σέρρες",
             "Πολιτική ποιότητας, πιστοποίηση ISO 9001:2015 και διεθνείς συνεργασίες του "
             "εργαστηρίου BIOLAB — Μοριακή Διαγνωστική Ο.Ε.",
             "poiotita.html", og="quality")
        + header("poiotita.html")
        + page_hero("Διασφάλιση ποιότητας", "Ποιότητα<br>&amp; πιστοποιήσεις.",
                    "Το εργαστήριο δεσμεύεται να παρέχει υπηρεσίες που πληρούν τα υψηλότερα "
                    "πρότυπα ποιότητας, σύμφωνα με διεθνείς κανονισμούς και πιστοποιήσεις.",
                    "quality", [("Ποιότητα", "poiotita.html")])
        + f"""
<section class="sec sec-tight">
  <div class="container">
    <div class="card-grid">
      <div class="icard reveal" style="padding:34px 30px">
        <span class="num" style="font-size:11.5px;font-weight:600;letter-spacing:.16em;color:var(--blue)">ΠΙΣΤΟΠΟΙΗΣΗ</span>
        <h3 style="margin-top:14px;font-size:1.12rem">ISO 9001:2015</h3>
        <p style="margin-top:12px;font-size:14px;color:var(--muted)">Το εργαστήριο BIOLAB —
        Μοριακή Διαγνωστική Ο.Ε. έχει πιστοποιηθεί από την <strong>EUROCERT</strong> για την
        εφαρμογή του προτύπου ISO 9001:2015 στο σύστημα διαχείρισης ποιότητας.</p>
      </div>
      <div class="icard reveal" style="padding:34px 30px">
        <span class="num" style="font-size:11.5px;font-weight:600;letter-spacing:.16em;color:var(--blue)">ΜΕΛΟΣ</span>
        <h3 style="margin-top:14px;font-size:1.12rem">ESHG</h3>
        <p style="margin-top:12px;font-size:14px;color:var(--muted)">Μέλος της Ευρωπαϊκής
        Κοινότητας Γενετικής του Ανθρώπου. Συμμετέχουμε ενεργά στις εξελίξεις της γενετικής
        και συνεργαζόμαστε με κορυφαίους επιστήμονες στην Ευρώπη.</p>
      </div>
      <div class="icard reveal" style="padding:34px 30px">
        <span class="num" style="font-size:11.5px;font-weight:600;letter-spacing:.16em;color:var(--blue)">ΜΕΛΟΣ</span>
        <h3 style="margin-top:14px;font-size:1.12rem">ESCCA</h3>
        <p style="margin-top:12px;font-size:14px;color:var(--muted)">Μέλος της Κοινότητας
        Κλινικής Ανάλυσης Κυττάρων. Παρέχουμε προηγμένες υπηρεσίες ανάλυσης κυττάρων,
        αξιοποιώντας τα τελευταία δεδομένα και εκπαιδεύσεις στον τομέα.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="container container-narrow prose reveal">
    <p class="eyebrow">Πολιτική ποιότητας</p>
    <h2 class="h2" style="margin-top:0">Η δέσμευσή μας</h2>

    <p>Πολιτική για την ποιότητα του εργαστηρίου BIOLAB — Μοριακή Διαγνωστική Ο.Ε. αποτελεί
    η λειτουργία του και η παροχή αξιόπιστων, ανεξάρτητων, αμερόληπτων και υψηλού κύρους
    υπηρεσιών εργαστηριακών εξετάσεων επί κατάλληλων κατά περίπτωση βιολογικών δειγμάτων
    ανθρώπινης προέλευσης, ώστε να τεκμηριώνεται αναμφισβήτητα η συμμόρφωσή τους με τις
    απαιτήσεις των πελατών, της νομοθεσίας, των κριτηρίων διαπίστευσης και του προτύπου
    ISO 9001:2015.</p>

    <p>Το πεδίο εφαρμογής είναι η παροχή μοριακών διαγνωστικών εξετάσεων με χρήση
    πιστοποιημένου εξοπλισμού και πιστοποιημένων αντιδραστηρίων <strong>CE IVD</strong>.
    Οι εξετάσεις που πραγματοποιούνται περιλαμβάνονται στις υποκατηγορίες: γενετικός
    έλεγχος και γενετικά νοσήματα, γενετικός έλεγχος υπογονιμότητας, αιματολογία και
    ογκολογία, μοριακή ογκολογία, μοριακή μικροβιολογία, υγεία και διατροφή.</p>

    <h2>Δέσμευση της Διοίκησης</h2>
    <p>Η Διοίκηση δεσμεύεται να προσδιορίζει τις συνθήκες και τις προϋποθέσεις που κρίνονται
    απαραίτητες ώστε η λειτουργία του εργαστηρίου να παραμένει ανταγωνιστική, χωρίς καμία
    μείωση στα κριτήρια και τις απαιτήσεις της πιστοποίησης, και να λαμβάνει κάθε αναγκαίο
    μέτρο για τη διαρκή βελτίωση των παρεχόμενων υπηρεσιών και της αποτελεσματικότητας του
    Συστήματος Διαχείρισης Ποιότητας.</p>

    <p>Στο πλαίσιο αυτής της δέσμευσης εντάσσονται:</p>
    <ul>
      <li>Η στελέχωση με έμπειρο, κατάλληλα καταρτισμένο και διαρκώς επιμορφούμενο προσωπικό</li>
      <li>Η χρήση σύγχρονων και αξιόπιστων εργαστηριακών οργάνων, συστημάτων και εγκαταστάσεων</li>
      <li>Η υλοποίηση λεπτομερών και σαφών διαδικασιών σε κάθε στάδιο της ανάλυσης</li>
      <li>Η διασφάλιση της συνεχούς ροής των αναγκαίων πόρων</li>
    </ul>

    <h2>Αρχές λειτουργίας</h2>
    <p>Το εργαστήριο υιοθετεί πλήρως τις αρχές της <strong>ανεξαρτησίας</strong>, της
    <strong>αμεροληψίας</strong>, της <strong>ακεραιότητας</strong>, της
    <strong>εμπιστευτικότητας</strong> και της ισότιμης μεταχείρισης των πελατών, απαλλαγμένο
    από επιρροές και διακρίσεις, σε πνεύμα αμοιβαίου σεβασμού και με υψηλό αίσθημα
    επαγγελματικής ευθύνης.</p>

    <p>Το εξουσιοδοτημένο προσωπικό και η Διοίκηση φέρουν την ευθύνη για την άρτια και
    τεχνικά επαρκή εκτέλεση των εξετάσεων, με σεβασμό στα δικαιώματα και τις ανάγκες του
    εξεταζομένου και με γνώμονα την προστασία των προσωπικών του δεδομένων. Παράλληλα, το
    εργαστήριο μεριμνά για την υγιεινή και την ασφάλεια των εργαζομένων, για την
    αντιμετώπιση εκτάκτων συμβάντων και για την ασφαλή και σύννομη διαχείριση των αποβλήτων
    που παράγει.</p>

    <h2>Συνεχής βελτίωση</h2>
    <p>Η συνολική λειτουργία του εργαστηρίου βασίζεται στην πιστή εφαρμογή των διαδικασιών
    του Συστήματος Διαχείρισης Ποιότητας. Η Διοίκηση βρίσκεται διαρκώς σε εγρήγορση ώστε να
    εντοπίζει τις μεταβολές στο κανονιστικό και τυποποιητικό πλαίσιο και να λαμβάνει τις
    απαιτούμενες αποφάσεις για τη διατήρηση της αποτελεσματικότητας του συστήματος.</p>

    <div class="note">
      <strong>Εκ της Διοικήσεως</strong><br>
      Η Γενική Διευθύντρια του Εργαστηρίου — Ταουσάνη Μαρία
    </div>
  </div>
</section>

"""
        + cta_band("Θέλετε να μάθετε περισσότερα;",
                   "Επικοινωνήστε μαζί μας για το σύστημα ποιότητας, τις πιστοποιήσεις ή "
                   "τις διαδικασίες του εργαστηρίου.")
        + footer())


# ═══════════════════════════════════════════════════════════════════════
#  ΕΠΙΚΟΙΝΩΝΙΑ
# ═══════════════════════════════════════════════════════════════════════
def build_epikoinonia():
    opts = "".join(f'<option value="{c["short"]}">{c["n"]} — {c["short"]}</option>' for c in CATS)
    return (
        head("Επικοινωνία &amp; ραντεβού | BIOLAB Σέρρες",
             "Επικοινωνήστε με το εργαστήριο BIOLAB στις Σέρρες — Τσαλοπούλου 15, "
             "τηλ. 23211 21602. Κλείστε ραντεβού για την εξέτασή σας.",
             "epikoinonia.html", og="brand-wall")
        + header("epikoinonia.html")
        + page_hero("Επικοινωνία", "Είμαστε<br>στη διάθεσή σας.",
                    "Καλέστε μας, στείλτε μας το αίτημά σας ή περάστε από το εργαστήριο "
                    "στην Τσαλοπούλου 15, στο κέντρο των Σερρών.",
                    "brand-wall", [("Επικοινωνία", "epikoinonia.html")])
        + f"""
<section class="sec" id="rantevou">
  <div class="container contact-layout">
    <div class="reveal">
      <p class="eyebrow">Στοιχεία επικοινωνίας</p>
      <h2 class="h2">Πώς θα μας βρείτε</h2>
      <dl class="info-list" style="margin-top:34px">
        <div class="info-row"><dt>Διεύθυνση</dt>
          <dd><a href="{S['maps']}" target="_blank" rel="noopener">{S['address']}, {S['postal']} {S['city']} ↗</a>
          <span class="sub">Στο κέντρο της πόλης</span></dd></div>
        <div class="info-row"><dt>Τηλέφωνο</dt>
          <dd><a href="tel:{S['phone_href']}">{S['phone']}</a>
          <span class="sub">Κινητό: <a href="tel:{S['mobile_href']}">{S['mobile']}</a></span></dd></div>
        <div class="info-row"><dt>Email</dt>
          <dd><a href="mailto:{S['email']}">{S['email']}</a></dd></div>
        <div class="info-row"><dt>Ωράριο</dt>
          <dd>Δευτέρα – Παρασκευή 09:00 – 17:00
          <span class="sub">Σάββατο &amp; Κυριακή κλειστά</span></dd></div>
        <div class="info-row"><dt>Κατ' οίκον</dt>
          <dd>Δειγματοληψία στον χώρο σας
          <span class="sub">Κατόπιν ραντεβού, σε όλο τον νομό Σερρών</span></dd></div>
      </dl>
    </div>

    <div class="reveal">
      <p class="eyebrow">Αίτημα ραντεβού</p>
      <h2 class="h2">Στείλτε μας το αίτημά σας</h2>
      <p class="lead" style="margin-top:18px;margin-bottom:30px">Συμπληρώστε τα στοιχεία σας
      και θα επικοινωνήσουμε μαζί σας για να επιβεβαιώσουμε το ραντεβού και να σας δώσουμε
      τις οδηγίες προετοιμασίας.</p>

      <form class="form" id="contact-form" novalidate>
        <div class="form-row">
          <div class="field">
            <label for="f-name">Ονοματεπώνυμο *</label>
            <input id="f-name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="f-phone">Τηλέφωνο *</label>
            <input id="f-phone" name="phone" type="tel" autocomplete="tel" required>
          </div>
        </div>
        <div class="field">
          <label for="f-email">Email</label>
          <input id="f-email" name="email" type="email" autocomplete="email">
        </div>
        <div class="field">
          <label for="f-service">Κατηγορία εξέτασης</label>
          <select id="f-service" name="service">
            <option value="">Επιλέξτε κατηγορία…</option>
            {opts}
            <option value="Άλλο / δεν γνωρίζω">Άλλο — δεν γνωρίζω</option>
          </select>
        </div>
        <div class="field">
          <label for="f-message">Μήνυμα</label>
          <textarea id="f-message" name="message" placeholder="Περιγράψτε σύντομα το αίτημά σας ή την εξέταση που σας ενδιαφέρει."></textarea>
        </div>
        <label class="consent">
          <input type="checkbox" name="consent" required>
          <span>Συμφωνώ με την <a href="politiki-aporritou.html">Πολιτική Απορρήτου</a> και
          με την επεξεργασία των στοιχείων μου για την εξυπηρέτηση του αιτήματός μου.</span>
        </label>
        <button class="btn" type="submit">Αποστολή αιτήματος{ARW}</button>
        <p class="form-note">Μην αποστέλλετε ευαίσθητα ιατρικά δεδομένα μέσω της φόρμας.
        Για επείγοντα περιστατικά καλέστε στο {S['phone']}.</p>
        <div class="form-status" role="status"></div>
      </form>
    </div>
  </div>
</section>

<section class="sec sec-tight sec-off">
  <div class="container">
    <div class="map-embed reveal">
      <iframe title="Χάρτης — BIOLAB, Τσαλοπούλου 15, Σέρρες" loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        src="https://www.google.com/maps?q=%CE%A4%CF%83%CE%B1%CE%BB%CE%BF%CF%80%CE%BF%CF%8D%CE%BB%CE%BF%CF%85+15%2C+%CE%A3%CE%AD%CF%81%CF%81%CE%B5%CF%82&output=embed"></iframe>
    </div>
  </div>
</section>

"""
        + footer())


# ═══════════════════════════════════════════════════════════════════════
#  ΠΟΛΙΤΙΚΗ ΑΠΟΡΡΗΤΟΥ
# ═══════════════════════════════════════════════════════════════════════
def build_privacy():
    return (
        head("Πολιτική Απορρήτου | BIOLAB",
             "Πολιτική απορρήτου και προστασίας προσωπικών δεδομένων του εργαστηρίου BIOLAB.",
             "politiki-aporritou.html")
        + header("politiki-aporritou.html")
        + page_hero("Νομικά", "Πολιτική<br>Απορρήτου.",
                    "Πώς συλλέγουμε, χρησιμοποιούμε και προστατεύουμε τα προσωπικά σας "
                    "δεδομένα, σύμφωνα με τον Γενικό Κανονισμό Προστασίας Δεδομένων (ΕΕ) 2016/679.",
                    "facility-seq", [("Πολιτική Απορρήτου", "politiki-aporritou.html")])
        + f"""
<section class="sec">
  <div class="container container-narrow prose reveal">
    <h2>Υπεύθυνος επεξεργασίας</h2>
    <p>{S['legal']}, {S['address']}, {S['postal']} {S['city']}.
    Τηλέφωνο: <a href="tel:{S['phone_href']}" style="color:var(--navy-800)">{S['phone']}</a> ·
    Email: <a href="mailto:{S['email']}" style="color:var(--navy-800)">{S['email']}</a>.</p>

    <h2>Ποια δεδομένα συλλέγουμε</h2>
    <ul>
      <li><strong>Στοιχεία ταυτοποίησης και επικοινωνίας</strong> — ονοματεπώνυμο, τηλέφωνο,
      email, διεύθυνση, ΑΜΚΑ όπου απαιτείται.</li>
      <li><strong>Δεδομένα υγείας</strong> — ιατρικό ιστορικό, παραπεμπτικά, δείγματα και
      αποτελέσματα εξετάσεων. Πρόκειται για ειδική κατηγορία δεδομένων, με ενισχυμένη προστασία.</li>
      <li><strong>Γενετικά δεδομένα</strong> — όπου εκτελείται γενετικός έλεγχος, με ρητή,
      χωριστή και έγγραφη συναίνεσή σας.</li>
      <li><strong>Δεδομένα χρήσης του ιστοτόπου</strong> — τεχνικά δεδομένα περιήγησης,
      εφόσον τα παρέχετε μέσω της φόρμας επικοινωνίας.</li>
    </ul>

    <h2>Σκοπός και νομική βάση</h2>
    <ul>
      <li>Παροχή διαγνωστικών υπηρεσιών — άρθρο 9 παρ. 2 στοιχ. η΄ ΓΚΠΔ (σκοποί υγείας).</li>
      <li>Εκπλήρωση νομικών υποχρεώσεων — φορολογική και υγειονομική νομοθεσία.</li>
      <li>Απάντηση σε αιτήματα επικοινωνίας — έννομο συμφέρον ή συναίνεση.</li>
      <li>Γενετικές εξετάσεις — ρητή συναίνεση, η οποία λαμβάνεται πάντοτε εγγράφως.</li>
    </ul>

    <h2>Αποδέκτες</h2>
    <p>Τα αποτελέσματα παραδίδονται αποκλειστικά στον ίδιο τον εξεταζόμενο ή σε πρόσωπο που
    αυτός έχει εξουσιοδοτήσει εγγράφως, καθώς και στον θεράποντα ιατρό εφόσον υπάρχει
    σχετική εντολή. Ενδέχεται να συνεργαζόμαστε με πιστοποιημένα συνεργαζόμενα εργαστήρια
    για εξειδικευμένες αναλύσεις, υπό αυστηρές συμβατικές δεσμεύσεις εμπιστευτικότητας.
    Δεν πωλούμε και δεν παραχωρούμε δεδομένα σε τρίτους για εμπορικούς σκοπούς.</p>

    <h2>Χρόνος τήρησης</h2>
    <p>Τα δεδομένα υγείας τηρούνται για το χρονικό διάστημα που ορίζει η κείμενη νομοθεσία
    για τα ιατρικά αρχεία. Τα δεδομένα επικοινωνίας που υποβάλλονται μέσω της φόρμας
    διατηρούνται μόνο για όσο απαιτείται η διεκπεραίωση του αιτήματός σας.</p>

    <h2>Τα δικαιώματά σας</h2>
    <ul>
      <li>Πρόσβαση στα δεδομένα σας και λήψη αντιγράφου</li>
      <li>Διόρθωση ανακριβών στοιχείων</li>
      <li>Διαγραφή, εφόσον δεν αντιβαίνει σε νόμιμη υποχρέωση τήρησης</li>
      <li>Περιορισμός ή εναντίωση στην επεξεργασία</li>
      <li>Φορητότητα των δεδομένων σας</li>
      <li>Ανάκληση της συναίνεσής σας οποτεδήποτε, χωρίς αναδρομική ισχύ</li>
    </ul>
    <p>Για την άσκηση των δικαιωμάτων σας επικοινωνήστε στο
    <a href="mailto:{S['email']}" style="color:var(--navy-800)">{S['email']}</a>. Έχετε επίσης
    δικαίωμα καταγγελίας στην Αρχή Προστασίας Δεδομένων Προσωπικού Χαρακτήρα
    (<span style="white-space:nowrap">www.dpa.gr</span>).</p>

    <h2>Ασφάλεια</h2>
    <p>Εφαρμόζουμε τεχνικά και οργανωτικά μέτρα για την προστασία των δεδομένων:
    ελεγχόμενη φυσική πρόσβαση στους χώρους του εργαστηρίου, κωδικοποίηση δειγμάτων,
    περιορισμένα δικαιώματα πρόσβασης στα πληροφοριακά συστήματα και δέσμευση
    εμπιστευτικότητας του συνόλου του προσωπικού.</p>

    <h2>Cookies</h2>
    <p>Ο παρών ιστότοπος δεν χρησιμοποιεί cookies παρακολούθησης ή διαφημιστικά cookies.
    Χρησιμοποιούνται μόνο γραμματοσειρές τρίτου παρόχου (Google Fonts) και ενσωματωμένος
    χάρτης (Google Maps) στη σελίδα επικοινωνίας, οι οποίοι ενδέχεται να λαμβάνουν τη
    διεύθυνση IP σας.</p>

    <div class="note">Τελευταία ενημέρωση: Σεπτέμβριος 2026.</div>
  </div>
</section>

"""
        + footer())


# ═══════════════════════════════════════════════════════════════════════
def build_extras():
    favicon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40">
<rect width="40" height="40" rx="7" fill="#05101f"/>
<path d="M13 7c0 6.5 15 8 15 13s-15 6.5-15 13" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" fill="none"/>
<path d="M27 7c0 6.5-15 8-15 13s15 6.5 15 13" stroke="#2f7fbf" stroke-width="2.4" stroke-linecap="round" fill="none"/>
</svg>
"""
    with open(os.path.join(OUT, "assets", "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(favicon)

    pages = ["index.html", "exetaseis.html"] + [c["slug"] for c in CATS] + \
            ["ergastirio.html", "omada.html", "poiotita.html", "epikoinonia.html",
             "politiki-aporritou.html"]
    urls = "".join(
        f'  <url><loc>{S["url"]}/{"" if p == "index.html" else p}</loc>'
        f'<priority>{"1.0" if p == "index.html" else "0.8" if p in ("exetaseis.html",) else "0.6"}</priority></url>\n'
        for p in pages)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + urls + "</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {S['url']}/sitemap.xml\n")
    print("  assets/favicon.svg, sitemap.xml, robots.txt")


# ═══════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Δημιουργία σελίδων:")
    write("index.html", build_index())
    write("exetaseis.html", build_exetaseis())
    for c in CATS:
        write(c["slug"], build_cat(c))
    write("ergastirio.html", build_ergastirio())
    write("omada.html", build_omada())
    write("poiotita.html", build_poiotita())
    write("epikoinonia.html", build_epikoinonia())
    write("politiki-aporritou.html", build_privacy())
    build_extras()
    print("Ολοκληρώθηκε.")
