/* BIOLAB — βασικά σενάρια διεπαφής */
(function () {
  'use strict';

  /* Σκίαση header κατά το scroll */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* Μενού κινητού */
  var toggle = document.querySelector('.menu-toggle');
  var drawer = document.getElementById('mobile-nav');
  var closeBtn = document.querySelector('.mobile-close');

  function setMenu(open) {
    if (!drawer || !toggle) return;
    drawer.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
    if (open) {
      var first = drawer.querySelector('a, button');
      if (first) first.focus();
    } else {
      toggle.focus();
    }
  }

  if (toggle) toggle.addEventListener('click', function () {
    setMenu(!drawer.classList.contains('is-open'));
  });
  if (closeBtn) closeBtn.addEventListener('click', function () { setMenu(false); });
  if (drawer) drawer.addEventListener('click', function (e) {
    if (e.target.closest('a')) setMenu(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && drawer && drawer.classList.contains('is-open')) setMenu(false);
  });

  /* Αποκάλυψη στοιχείων κατά το scroll */
  var revealables = document.querySelectorAll('.reveal');
  if (revealables.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-in');
            io.unobserve(entry.target);
          }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      revealables.forEach(function (el, i) {
        el.style.transitionDelay = Math.min(i % 4, 3) * 70 + 'ms';
        io.observe(el);
      });
    } else {
      revealables.forEach(function (el) { el.classList.add('is-in'); });
    }
  }

  /* Συχνές ερωτήσεις (accordion) */
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel) return;
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';

      btn.closest('.faq').querySelectorAll('.faq-q[aria-expanded="true"]').forEach(function (other) {
        if (other === btn) return;
        var otherPanel = document.getElementById(other.getAttribute('aria-controls'));
        other.setAttribute('aria-expanded', 'false');
        if (otherPanel) otherPanel.style.height = '0px';
      });

      btn.setAttribute('aria-expanded', open ? 'false' : 'true');
      panel.style.height = open ? '0px' : panel.firstElementChild.offsetHeight + 'px';
    });
  });

  window.addEventListener('resize', function () {
    document.querySelectorAll('.faq-q[aria-expanded="true"]').forEach(function (btn) {
      var panel = document.getElementById(btn.getAttribute('aria-controls'));
      if (panel) panel.style.height = panel.firstElementChild.offsetHeight + 'px';
    });
  });

  /* Έτος στο footer */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* Φόρμα επικοινωνίας — άνοιγμα προσυμπληρωμένου email
     (Χωρίς backend· αντικαταστήστε με endpoint όταν υπάρχει server.) */
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;

      var data = new FormData(form);
      var get = function (k) { return (data.get(k) || '').toString().trim(); };

      var lines = [
        'Ονοματεπώνυμο: ' + get('name'),
        'Τηλέφωνο: ' + get('phone'),
        'Email: ' + get('email'),
        'Εξέταση / κατηγορία: ' + get('service'),
        '',
        'Μήνυμα:',
        get('message')
      ];

      var subject = 'Αίτημα ραντεβού — ' + (get('service') || 'BIOLAB');
      window.location.href = 'mailto:info@biolabs.gr'
        + '?subject=' + encodeURIComponent(subject)
        + '&body=' + encodeURIComponent(lines.join('\n'));

      var status = document.querySelector('.form-status');
      if (status) {
        status.className = 'form-status ok';
        status.textContent = 'Ανοίγει το πρόγραμμα email σας με συμπληρωμένο το αίτημα. Εναλλακτικά καλέστε μας στο 23211 21602.';
      }
    });
  }
})();

// Search the full service catalog, ignoring Greek accents and case.
(() => {
  const input = document.getElementById('analysis-search');
  if (!input) return;
  const cards = [...document.querySelectorAll('.analysis-card')];
  const status = document.getElementById('analysis-status');
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('el').replace(/ς/g, 'σ');
  const update = () => {
    const terms = normalize(input.value).trim().split(/\s+/).filter(Boolean);
    let count = 0;
    cards.forEach(card => {
      card.hidden = !terms.every(term => normalize(card.textContent).includes(term));
      if (!card.hidden) count++;
    });
    status.textContent = count ? `${count} από ${cards.length} κατηγορίες υπηρεσιών` : 'Δεν βρέθηκε εξέταση. Δοκιμάστε άλλη λέξη ή επικοινωνήστε μαζί μας.';
  };
  input.addEventListener('input', update);
  update();
})();
