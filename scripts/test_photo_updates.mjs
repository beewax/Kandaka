import {test} from 'node:test';
import assert from 'node:assert/strict';
import {refreshPhotos} from '../static/js/photo-updates.mjs';

function fixture(language = 'en') {
  let cards = Array.from({length: 9}, (_, i) => ({hidden: i >= 3,
    dataset: {photoId: String(i), photoSince: '2026-10-10T10:00:00Z'},
    querySelector(selector) { return selector === 'img' ?
      {getAttribute: () => `/images/photo-${i}.jpg`} :
      {textContent: `Photo ${i}`, getAttribute: () => `/${language}/images/photo-${i}/`}; },
  }));
  const review = {}, rotation = {}, featureImage = {}, featureTitle = {}, featureLink = {};
  featureImage.setAttribute = (name, value) => { featureImage[name] = value; };
  featureLink.setAttribute = (name, value) => { featureLink[name] = value; };
  const feature = {dataset: {photoId: 'stale'}, contains: () => false,
    querySelector: selector => selector === '.k-featured-media' ? featureImage :
      selector === '.k-featured-title' ? featureTitle : featureLink};
  const root = {activeElement: null, querySelector: () => feature};
  const stack = {appendChild(card) { cards = cards.filter(item => item !== card); cards.push(card); }};
  const section = {querySelectorAll: () => cards, querySelector: () => stack,
    contains: element => element === cards[0]};
  const notice = {dataset: {language}, closest: () => section,
    querySelector: selector => selector === '[data-photo-next-review]' ? review : rotation};
  return {notice, root, review, rotation, feature, featureImage, featureTitle, featureLink,
    cards: () => cards, visible: () => cards.filter(card => !card.hidden).map(card => card.dataset.photoId)};
}
test('photo dates, visible selection and featured image change together in EN and AR', () => {
  for (const lang of ['en', 'ar']) {
    const f = fixture(lang);
    refreshPhotos(f.notice, new Date('2026-11-14T16:29:59Z'), f.root);
    const before = f.visible();
    assert.equal(f.review.dateTime, '2026-11-14T16:30:00.000Z');
    assert.equal(f.rotation.dateTime, f.review.dateTime);
    refreshPhotos(f.notice, new Date('2026-11-14T16:30:00Z'), f.root);
    assert.notDeepEqual(f.visible(), before);
    assert.equal(f.visible().length, 3);
    assert.equal(f.review.dateTime, '2026-11-21T16:30:00.000Z');
    assert.equal(f.feature.dataset.photoId, f.visible()[0]);
    assert.equal(f.featureImage.src, `/images/photo-${f.visible()[0]}.jpg`);
    assert.equal(f.featureTitle.textContent, `Photo ${f.visible()[0]}`);
    assert.equal(f.featureLink.href, `/${lang}/images/photo-${f.visible()[0]}/`);
    const after = f.visible();
    refreshPhotos(f.notice, new Date('2026-11-17T12:00:00Z'), f.root);
    assert.deepEqual(f.visible(), after);
  }
});
test('rotation waits while a photo link is focused, then catches up', () => {
  const f = fixture();
  refreshPhotos(f.notice, new Date('2026-11-14T16:29:59Z'), f.root);
  const before = f.visible();
  f.root.activeElement = f.cards()[0];
  refreshPhotos(f.notice, new Date('2026-11-14T16:30:00Z'), f.root);
  assert.deepEqual(f.visible(), before);
  f.root.activeElement = null;
  refreshPhotos(f.notice, new Date('2026-11-14T16:31:00Z'), f.root);
  assert.notDeepEqual(f.visible(), before);
});
test('gallery dates follow Chicago DST without changing its full photo listing', () => {
  const f = fixture('ar');
  f.notice.closest = () => null;
  const before = f.visible();
  refreshPhotos(f.notice, new Date('2027-03-13T16:30:00Z'), f.root);
  assert.equal(f.review.dateTime, '2027-03-20T15:30:00.000Z');
  assert.deepEqual(f.visible(), before);
  assert.equal(f.feature.dataset.photoId, 'stale');
});
