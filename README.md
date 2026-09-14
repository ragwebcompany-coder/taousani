# BIOLAB — Μικροβιολογικό & Μοριακό Εργαστήριο

Στατικό site (HTML/CSS/JS, χωρίς framework και χωρίς build step).
Ανεβαίνει ως έχει σε Vercel, Netlify, GitHub Pages ή απλό web hosting.

## Δομή

```
index.html                      Αρχική
exetaseis.html                  Όλες οι εξετάσεις (+ συχνές ερωτήσεις)
mikroviologikes-exetaseis.html  01  Μικροβιολογικές
genetikos-elegchos.html         02  Μοριακές — γενετικός έλεγχος
ypogonimotita.html              03  Διερεύνηση υπογονιμότητας
andrologia.html                 04  Ανδρολογία
anosologia-aimatologia.html     05  Ανοσολογία — αιματολογία
moriaki-mikroviologia.html      06  Μοριακή μικροβιολογία
progennitikos-elegchos.html     07  Μη επεμβατικός προγεννητικός έλεγχος
moriaki-ogkologia.html          08  Μοριακή ογκολογία
elegchos-patrotitas.html        09  Έλεγχος πατρότητας
genetiki-symvouleftiki.html     10  Γενετική συμβουλευτική
ergastirio.html                 Ο χώρος και ο εξοπλισμός
omada.html                      Η ομάδα
poiotita.html                   Ποιότητα & πιστοποιήσεις
epikoinonia.html                Επικοινωνία, φόρμα ραντεβού, χάρτης
politiki-aporritou.html         Πολιτική απορρήτου

assets/css/style.css            Όλο το στυλ
assets/js/main.js               Μενού, accordion, animations, φόρμα
assets/images/                  Βελτιστοποιημένες εικόνες (.jpg + .webp)
_build/                         Προαιρετικά scripts παραγωγής (βλ. παρακάτω)
sitemap.xml, robots.txt
```

## Τοπική προεπισκόπηση

```bash
python3 -m http.server 8000
# http://localhost:8000
```

## Χρώματα & τυπογραφία

Ορίζονται ως CSS variables στην αρχή του `assets/css/style.css`:

| Μεταβλητή | Τιμή | Χρήση |
|---|---|---|
| `--navy-950` | `#05101f` | σκούρα τμήματα, footer, hero |
| `--navy-800` | `#0a2342` | κουμπιά, τίτλοι |
| `--blue` | `#2f7fbf` | τονισμοί, αριθμοί, σύνδεσμοι |
| `--ink` | `#101720` | κείμενο |
| `--off` | `#f6f8fa` | εναλλακτικό φόντο ενοτήτων |

Γραμματοσειρά: **Inter** (Google Fonts, με ελληνικό subset).

## Αλλαγές περιεχομένου

Κάθε σελίδα είναι αυτόνομο HTML — μπορείτε να την επεξεργαστείτε απευθείας.

Για μαζικές αλλαγές (π.χ. νέα κατηγορία εξέτασης, αλλαγή τηλεφώνου παντού),
υπάρχουν τα scripts στον φάκελο `_build/`:

```bash
cd _build
python3 build.py     # ξαναχτίζει όλα τα .html
python3 images.py    # ξαναφτιάχνει τις εικόνες από τα πρωτότυπα
```

Το `_build/content.py` κρατά τα στοιχεία επικοινωνίας (`SITE`) και όλο το
κείμενο των 10 κατηγοριών (`CATS`). **Προσοχή:** το `build.py` ξαναγράφει τα
αρχεία `.html`, οπότε αν έχετε επεξεργαστεί χειροκίνητα κάποια σελίδα, μην το
τρέξετε ξανά — ή περάστε πρώτα τις αλλαγές στο `content.py`.
Ο φάκελος `_build/` δεν χρειάζεται να ανέβει στο hosting.

## Φόρμα επικοινωνίας

Δεν υπάρχει backend. Η φόρμα στο `epikoinonia.html` ανοίγει το πρόγραμμα email
του χρήστη με προσυμπληρωμένο το αίτημα (`assets/js/main.js`, τέλος αρχείου).

Για κανονική αποστολή, αντικαταστήστε τον handler με το endpoint της υπηρεσίας
σας (Formspree, Web3Forms, Vercel serverless function κ.λπ.).

## Εκκρεμότητες πριν τη δημοσίευση

- [ ] Επιβεβαίωση στοιχείων επικοινωνίας (διεύθυνση, τηλέφωνα, Τ.Κ., ωράριο)
- [ ] Το υλικό για την **Ανδρολογία** — ενημέρωση του `andrologia.html`
- [ ] Σύνδεση της φόρμας με πραγματικό endpoint
- [ ] Αλλαγή του `SITE["url"]` στο `_build/content.py` αν το domain διαφέρει
      (επηρεάζει canonical URLs, Open Graph και `sitemap.xml`)
- [ ] Προσωπικές φωτογραφίες για τη σελίδα `omada.html` (τώρα χρησιμοποιούνται
      γενικές φωτογραφίες εργαστηρίου)
