const zone = 'America/Chicago';
const dayMs = 86400000;
const localParts = new Intl.DateTimeFormat('en-US', {timeZone: zone, year: 'numeric',
  month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric', hourCycle: 'h23'});
function parts(date) {
  return Object.fromEntries(localParts.formatToParts(date).filter(p => p.type !== 'literal')
    .map(p => [p.type, Number(p.value)]));
}
function chicagoMonday(day) {
  const target = Date.UTC(day.getUTCFullYear(), day.getUTCMonth(), day.getUTCDate(), 10);
  let instant = target;
  for (let i = 0; i < 3; i++) {
    const p = parts(new Date(instant));
    instant += target - Date.UTC(p.year, p.month - 1, p.day, p.hour, p.minute, p.second);
  }
  return new Date(instant);
}
export function libraryWeek(at = new Date()) {
  const p = parts(at);
  let monday = new Date(Date.UTC(p.year, p.month - 1, p.day));
  monday = new Date(+monday - ((monday.getUTCDay() + 6) % 7) * dayMs);
  let start = chicagoMonday(monday);
  if (+at < +start) {
    monday = new Date(+monday - 7 * dayMs);
    start = chicagoMonday(monday);
  }
  return {start, next: chicagoMonday(new Date(+monday + 7 * dayMs)),
    index: Math.round((+monday - Date.UTC(2026, 9, 12)) / (7 * dayMs))};
}
export function selectLibrary(items, at = new Date()) {
  const seen = new Set();
  const pool = [...items].sort((a, b) => a.id < b.id ? -1 : a.id > b.id ? 1 : 0)
    .filter(item => { if (seen.has(item.id)) return false; seen.add(item.id); return true; });
  if (!pool.length) return [];
  const offset = ((libraryWeek(at).index * 3) % pool.length + pool.length) % pool.length;
  return Array.from({length: Math.min(3, pool.length)}, (_, i) => pool[(offset + i) % pool.length]);
}
export function libraryLink(href, base = 'https://kandaka.com/') {
  if (!href) return null;
  try { return ['http:', 'https:'].includes(new URL(href, base).protocol) ? href : null; }
  catch { return null; }
}
export function libraryCard(doc, book, index) {
  const element = (tag, cls, text) => {
    const node = doc.createElement(tag);
    node.className = cls;
    if (text !== undefined) node.textContent = text;
    return node;
  };
  const card = element('div', 'k-lib-card');
  card.dataset.libraryId = book.id;
  card.appendChild(element('div', 'k-lib-icon', ['📖', '📊', '🗺️'][index]));
  const body = element('div', 'k-lib-body');
  body.appendChild(element('h3', '', book.title));
  body.appendChild(element('p', '', book.author + (book.year ? ' · ' + book.year : '')));
  if (book.desc) body.appendChild(element('p', 'k-lib-description', book.desc));
  const href = libraryLink(book.href, doc.baseURI);
  if (href) {
    const link = element('a', 'k-lib-btn ' + (book.download ? 'k-lib-btn-dl' : 'k-lib-btn-src'), book.label);
    link.setAttribute('href', href);
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    body.appendChild(link);
  }
  card.appendChild(body);
  return card;
}
const pools = new WeakMap();
export function refreshLibrary(notice, at = new Date(), doc = notice.ownerDocument) {
  const week = libraryWeek(at);
  const format = new Intl.DateTimeFormat(notice.dataset.language === 'ar' ? 'ar' : 'en-US', {
    timeZone: zone, weekday: 'long', year: 'numeric', month: 'long', day: 'numeric',
    hour: 'numeric', minute: '2-digit', timeZoneName: 'short'});
  for (const [selector, date] of [['[data-library-week]', week.start],
    ['[data-library-next-review]', week.next], ['[data-library-next-rotation]', week.next]]) {
    const element = notice.querySelector(selector);
    if (element) { element.dateTime = date.toISOString(); element.textContent = format.format(date); }
  }
  const section = notice.closest('[data-library-home]');
  if (!section) return;
  if (!pools.has(section)) pools.set(section, JSON.parse(section.querySelector('[data-library-pool]').textContent));
  const selected = selectLibrary(pools.get(section), at);
  const current = [...section.querySelectorAll('.k-lib-card')].map(card => card.dataset.libraryId);
  if (current.length === selected.length && current.every((id, i) => id === selected[i].id)) return;
  if (doc.activeElement && section.contains(doc.activeElement)) return;
  const fragment = doc.createDocumentFragment();
  selected.forEach((book, index) => fragment.appendChild(libraryCard(doc, book, index)));
  section.querySelector('.k-lib-stack').replaceChildren(fragment);
}
if (typeof document !== 'undefined') {
  const refresh = () => document.querySelectorAll('[data-library-updates]').forEach(notice => refreshLibrary(notice));
  refresh();
  setInterval(refresh, 60000);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) refresh(); });
}
