// Only already reviewed, bilingual, image-backed cards are included by Hugo.
// Keep selection identical to the Hugo fallback, without waiting for a rebuild.
const zone = 'America/Chicago';
const dayMs = 86400000;
const partsFormatter = new Intl.DateTimeFormat('en-US', {
  timeZone: zone, year: 'numeric', month: 'numeric', day: 'numeric',
  hour: 'numeric', minute: 'numeric', second: 'numeric', hourCycle: 'h23',
});
function parts(date) {
  return Object.fromEntries(partsFormatter.formatToParts(date)
    .filter(p => p.type !== 'literal').map(p => [p.type, Number(p.value)]));
}
function chicagoTime(day, hour, minute) {
  const target = Date.UTC(day.getUTCFullYear(), day.getUTCMonth(), day.getUTCDate(), hour, minute);
  let instant = target;
  for (let i = 0; i < 3; i++) {
    const p = parts(new Date(instant));
    instant += target - Date.UTC(p.year, p.month - 1, p.day, p.hour, p.minute, p.second);
  }
  return new Date(instant);
}
export function artworkWeek(at = new Date()) {
  const p = parts(at);
  let saturday = new Date(Date.UTC(p.year, p.month - 1, p.day));
  saturday = new Date(+saturday - ((saturday.getUTCDay() + 1) % 7) * dayMs);
  let start = chicagoTime(saturday, 10, 30);
  if (+at < +start) {
    saturday = new Date(+saturday - 7 * dayMs);
    start = chicagoTime(saturday, 10, 30);
  }
  const nextDay = new Date(+saturday + 7 * dayMs);
  const nextRotation = chicagoTime(nextDay, 10, 30);
  let nextReview = chicagoTime(nextDay, 10, 0);
  if (+nextReview <= +at) nextReview = chicagoTime(new Date(+nextDay + 7 * dayMs), 10, 0);
  return {
    start, previous: chicagoTime(new Date(+saturday - 7 * dayMs), 10, 30),
    cutoff: new Date(Math.max(+start, Date.parse('2026-10-23T00:00:00Z'))),
    index: Math.round((+saturday - Date.UTC(2026, 9, 10)) / (7 * dayMs)),
    nextReview, nextRotation,
  };
}
function groupSelection(items, week, stride) {
  const seen = new Set();
  const pool = [...items].sort((a, b) => a.id < b.id ? -1 : a.id > b.id ? 1 : 0)
    .filter(item => {
      if (seen.has(item.id) || !(Date.parse(item.since) <= +week.cutoff)) return false;
      seen.add(item.id);
      return true;
    });
  if (!pool.length) return [];
  const fresh = pool.filter(item => Date.parse(item.since) > +week.previous &&
    Date.parse(item.since) > Date.parse('2026-10-23T00:00:00Z'))
    .sort((a, b) => a.since < b.since ? 1 : a.since > b.since ? -1 : 0);
  const selected = fresh.slice(0, 1);
  const offset = ((week.index * stride) % pool.length + pool.length) % pool.length;
  for (let i = 0; i < pool.length && selected.length < 3; i++) {
    const item = pool[(offset + i) % pool.length];
    if (!selected.some(pick => pick.id === item.id)) selected.push(item);
  }
  return selected;
}
export function selectArtwork(items, at = new Date()) {
  const week = artworkWeek(at);
  return groupSelection(items.filter(item => item.group === 'sudan-nubia'), week, 2);
}
export function selectWeeklyVisuals(items, at = new Date(), stride = 3) {
  return groupSelection(items, artworkWeek(at), stride);
}
export function refreshArtwork(section, at = new Date()) {
  const week = artworkWeek(at);
  const isAr = section.dataset.language === 'ar';
  const format = new Intl.DateTimeFormat(isAr ? 'ar' : 'en-US', {
    timeZone: zone, weekday: 'long', year: 'numeric', month: 'long', day: 'numeric',
    hour: 'numeric', minute: '2-digit', timeZoneName: 'short',
  });
  for (const [selector, date] of [
    ['[data-artwork-next-review]', week.nextReview],
    ['[data-artwork-next-rotation]', week.nextRotation],
  ]) {
    const element = section.querySelector(selector);
    if (element) { element.dateTime = date.toISOString(); element.textContent = format.format(date); }
  }
  if (!section.hasAttribute('data-artwork-homepage')) return;
  const cards = [...section.querySelectorAll('.art-card')];
  const items = cards.map(card => ({ id: card.dataset.artworkId,
    since: card.dataset.artworkSince, group: card.dataset.artworkGroup, card }));
  const selected = selectArtwork(items, at);
  const grid = section.querySelector('.art-grid');
  const visible = cards.filter(card => !card.hidden).map(card => card.dataset.artworkId);
  if (visible.length === selected.length && visible.every((id, index) => id === selected[index].id)) return;
  // Do not disrupt a visitor reading with the keyboard at the weekly boundary.
  if (typeof document !== 'undefined' && section.contains(document.activeElement)) return;
  cards.forEach(card => { card.hidden = true; });
  selected.forEach(item => { item.card.hidden = false; grid.appendChild(item.card); });
}
if (typeof document !== 'undefined') {
  const refresh = () => document.querySelectorAll('[data-artwork-updates]')
    .forEach(section => refreshArtwork(section));
  refresh();
  setInterval(refresh, 60000);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) refresh(); });
}
