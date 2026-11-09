import { test } from 'node:test';
import assert from 'node:assert/strict';
import { artworkWeek, selectArtwork, refreshArtwork } from '../static/js/artwork-updates.mjs';
import { readFileSync } from 'node:fs';

test('review and rotation have separate boundaries and follow Chicago daylight saving', () => {
  const cases = [
    ['2026-11-09T18:00:00Z', '2026-11-14T16:00:00.000Z', '2026-11-14T16:30:00.000Z'],
    ['2026-11-14T16:15:00Z', '2026-11-21T16:00:00.000Z', '2026-11-14T16:30:00.000Z'],
    ['2026-11-14T16:30:00Z', '2026-11-21T16:00:00.000Z', '2026-11-21T16:30:00.000Z'],
    ['2026-10-31T15:30:00Z', '2026-11-07T16:00:00.000Z', '2026-11-07T16:30:00.000Z'],
    ['2027-03-13T16:30:00Z', '2027-03-20T15:00:00.000Z', '2027-03-20T15:30:00.000Z'],
  ];
  for (const [at, review, rotation] of cases) {
    const week = artworkWeek(new Date(at));
    assert.equal(week.nextReview.toISOString(), review, at);
    assert.equal(week.nextRotation.toISOString(), rotation, at);
  }
});
test('visible cards and dated notices advance together in both languages', () => {
  for (const language of ['en', 'ar']) {
    let cards = Array.from({length: 6}, (_, i) => ({hidden: i >= 3, dataset: {
      artworkId: String(i), artworkSince: '2026-10-10T10:00:00Z', artworkGroup: 'sudan-nubia',
    }}));
    const review = {}, rotation = {};
    const grid = {appendChild(card) { cards = cards.filter(item => item !== card); cards.push(card); }};
    const section = {
      dataset: {language}, hasAttribute: () => true, querySelectorAll: () => cards,
      querySelector: selector => selector === '.art-grid' ? grid :
        selector === '[data-artwork-next-review]' ? review : rotation,
    };
    const visible = () => cards.filter(card => !card.hidden).map(card => card.dataset.artworkId);
    refreshArtwork(section, new Date('2026-11-14T16:29:59Z'));
    const before = visible();
    assert.equal(rotation.dateTime, '2026-11-14T16:30:00.000Z');
    refreshArtwork(section, new Date('2026-11-14T16:30:00Z'));
    assert.notDeepEqual(visible(), before);
    assert.equal(visible().length, 3);
    assert.equal(rotation.dateTime, '2026-11-21T16:30:00.000Z');
    assert.equal(review.dateTime, '2026-11-21T16:00:00.000Z');
    assert.ok(review.textContent.length > 10);
    const after = visible();
    refreshArtwork(section, new Date('2026-11-17T01:00:00Z'));
    assert.deepEqual(visible(), after);
  }
});
test('the real catalogue changes on Saturday and stays stable midweek in both languages', () => {
  const catalogue = JSON.parse(readFileSync(new URL('../data/artworks.json', import.meta.url)));
  const items = catalogue.filter(work => work.image && work.homepage_since)
    .map(work => ({id: work.source, since: work.homepage_since, group: work.homepage_group}));
  const pick = at => selectArtwork(items, new Date(at)).map(item => item.id);
  assert.deepEqual(pick('2026-11-07T16:30:00Z'), pick('2026-11-14T16:29:59Z'));
  assert.notDeepEqual(pick('2026-11-14T16:29:59Z'), pick('2026-11-14T16:30:00Z'));
  assert.deepEqual(pick('2026-11-14T16:30:00Z'), pick('2026-11-18T01:00:00Z'));
  assert.equal(new Set(pick('2026-11-14T16:30:00Z')).size, 3);
  const sourceOnly = new Set(catalogue.filter(work => !work.image).map(work => work.source));
  assert.ok(pick('2026-11-14T16:30:00Z').every(id => !sourceOnly.has(id)));
});
