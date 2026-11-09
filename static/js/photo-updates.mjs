import {artworkWeek, selectWeeklyVisuals} from './artwork-updates.mjs';

// Dates and the static photo fallback use the same Saturday 10:30 Chicago week.
// Hugo supplies only public, verified bilingual photos; no discovery drafts.
export function refreshPhotos(notice, at = new Date(), root = globalThis.document) {
  const next = artworkWeek(at).nextRotation;
  const format = new Intl.DateTimeFormat(notice.dataset.language === 'ar' ? 'ar' : 'en-US', {
    timeZone: 'America/Chicago', weekday: 'long', year: 'numeric', month: 'long',
    day: 'numeric', hour: 'numeric', minute: '2-digit', timeZoneName: 'short',
  });
  for (const selector of ['[data-photo-next-review]', '[data-photo-next-rotation]']) {
    const element = notice.querySelector(selector);
    if (element) { element.dateTime = next.toISOString(); element.textContent = format.format(next); }
  }
  const section = notice.closest('[data-photo-homepage]');
  if (!section) return;
  const cards = [...section.querySelectorAll('[data-photo-id]')];
  const items = cards.map(card => ({id: card.dataset.photoId, since: card.dataset.photoSince, card}));
  const selected = selectWeeklyVisuals(items, at);
  const visible = cards.filter(card => !card.hidden).map(card => card.dataset.photoId);
  const feature = root?.querySelector('[data-photo-feature]');
  const sameCards = visible.length === selected.length &&
    visible.every((id, index) => id === selected[index].id);
  const sameFeature = !feature || feature.dataset.photoId === selected[0]?.id;
  if (sameCards && sameFeature) return;
  if (root?.activeElement && (section.contains(root.activeElement) || feature?.contains(root.activeElement))) return;
  if (!sameCards) {
    const stack = section.querySelector('.k-photo-stack');
    cards.forEach(card => { card.hidden = true; });
    selected.forEach(item => { item.card.hidden = false; stack.appendChild(item.card); });
  }
  if (feature && selected.length && !sameFeature) {
    const first = selected[0].card;
    const titleLink = first.querySelector('.k-photo-caption strong a');
    const image = first.querySelector('img');
    feature.querySelector('.k-featured-media').setAttribute('src', image.getAttribute('src'));
    feature.querySelector('.k-featured-title').textContent = titleLink.textContent;
    feature.querySelector('.k-featured-link').setAttribute('href', titleLink.getAttribute('href'));
    feature.dataset.photoId = selected[0].id;
  }
}
if (typeof document !== 'undefined') {
  const refresh = () => document.querySelectorAll('[data-photo-updates]')
    .forEach(notice => refreshPhotos(notice));
  refresh();
  setInterval(refresh, 60000);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) refresh(); });
}
