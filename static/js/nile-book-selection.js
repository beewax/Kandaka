(function (scope) {
  'use strict';
  const DAY = 86400000;
  const EPOCH = Date.UTC(2026, 10, 2);

  function select(books, at) {
    const seen = new Set();
    const pool = books.filter(book => {
      const key = book.cover_key || book.cover || book.id;
      if (!book.id || seen.has(key)) return false;
      seen.add(key);
      return true;
    });
    if (!pool.length) return [];
    const day = Math.floor((Number(at) - EPOCH) / DAY);
    const start = ((day * 3) % pool.length + pool.length) % pool.length;
    return Array.from({ length: Math.min(3, pool.length) }, (_, offset) => pool[(start + offset) % pool.length]);
  }

  function calendar(books, at, days) {
    const start = Math.floor(Number(at) / DAY) * DAY;
    return Array.from({ length: days }, (_, i) => ({ at: start + i * DAY, books: select(books, start + i * DAY) }));
  }

  function mount(root, environment) {
    const env = environment || {};
    const clock = env.now || Date.now;
    const timers = env.timers || scope;
    const doc = env.document || document;
    const win = env.window || scope;
    const cards = Array.from(root.querySelectorAll('[data-book-id]'));
    const books = cards.map(card => ({ id: card.getAttribute('data-book-id'), cover_key: card.getAttribute('data-cover-key'), title: card.querySelector('h3').textContent }));
    const locale = root.getAttribute('data-book-locale') || 'en';
    const badge = root.querySelector('[data-book-next]');
    const dateFormat = new Intl.DateTimeFormat(locale, { month: 'short', day: 'numeric', timeZone: 'UTC' });
    let timer;

    function update() {
      const at = clock();
      const ids = new Set(select(books, at).map(book => book.id));
      cards.forEach(card => { card.hidden = !ids.has(card.getAttribute('data-book-id')); });
      if (badge) badge.textContent = root.getAttribute('data-book-next-label') + ': ' + dateFormat.format(new Date((Math.floor(at / DAY) + 1) * DAY));
      const table = root.querySelector('[data-book-calendar]');
      if (table) {
        table.replaceChildren();
        calendar(books, at, 8).forEach(row => {
          const tr = doc.createElement('tr');
          [dateFormat.format(new Date(row.at)), row.books.map(book => book.title).join(' / ')].forEach(text => {
            const td = doc.createElement('td'); td.textContent = text; tr.appendChild(td);
          });
          table.appendChild(tr);
        });
      }
    }

    function refresh() {
      update();
      timers.clearTimeout(timer);
      timer = timers.setTimeout(refresh, DAY - (clock() % DAY) + 50);
    }
    const onVisibility = () => { if (!doc.hidden) refresh(); };
    doc.addEventListener('visibilitychange', onVisibility);
    win.addEventListener('pageshow', refresh);
    refresh();
    return { refresh, destroy() { timers.clearTimeout(timer); doc.removeEventListener('visibilitychange', onVisibility); win.removeEventListener('pageshow', refresh); } };
  }

  const api = { select, calendar, mount };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  scope.KandakaBookSelection = api;
  if (typeof document !== 'undefined') {
    const start = () => document.querySelectorAll('[data-book-selection]:not([data-book-manual])').forEach(root => mount(root));
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
    else start();
  }
})(globalThis);
