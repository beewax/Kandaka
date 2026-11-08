(function (scope) {
  'use strict';
  const DAY = 86400000;

  function select(seed, count, at) {
    if (!count) return -1;
    const index = Number(seed) + Math.floor(Number(at) / DAY);
    return ((index % count) + count) % count;
  }

  function mount(root, environment) {
    const env = environment || {};
    const clock = env.now || Date.now;
    const timers = env.timers || scope;
    const doc = env.document || document;
    const win = env.window || scope;
    const offers = Array.from(root.querySelectorAll('[data-nile-inline-offer]'));
    const slot = root.querySelector('[data-nile-inline-slot]');
    const seed = root.getAttribute('data-nile-seed');
    let current = Number(root.getAttribute('data-nile-selected'));
    let timer;

    function refresh() {
      const at = clock();
      const next = select(seed, offers.length, at);
      // Keep a focused call-to-action stable until the reader leaves the card.
      if (next >= 0 && next !== current && !slot.contains(doc.activeElement)) {
        slot.replaceChildren(offers[next].content.cloneNode(true));
        current = next;
      }
      timers.clearTimeout(timer);
      timer = timers.setTimeout(refresh, DAY - (at % DAY) + 50);
    }
    const onVisibility = () => { if (!doc.hidden) refresh(); };
    const onFocusOut = () => { timers.setTimeout(refresh, 0); };
    doc.addEventListener('visibilitychange', onVisibility);
    win.addEventListener('pageshow', refresh);
    slot.addEventListener('focusout', onFocusOut);
    refresh();
    return { refresh, destroy() {
      timers.clearTimeout(timer);
      doc.removeEventListener('visibilitychange', onVisibility);
      win.removeEventListener('pageshow', refresh);
      slot.removeEventListener('focusout', onFocusOut);
    } };
  }
  const api = { select, mount };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  scope.KandakaInlineSelection = api;
  if (typeof document !== 'undefined') {
    const start = () => document.querySelectorAll('[data-nile-inline]').forEach(root => mount(root));
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
    else start();
  }
})(globalThis);
