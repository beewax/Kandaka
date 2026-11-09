import {test} from 'node:test';
import assert from 'node:assert/strict';
import {libraryWeek, selectLibrary, libraryLink, libraryCard, refreshLibrary} from '../static/js/library-updates.mjs';

test('Monday 10 Chicago boundaries survive both DST changes', () => {
  for (const [at, next] of [
    ['2026-11-09T15:59:59Z','2026-11-09T16:00:00.000Z'],
    ['2026-11-09T16:00:00Z','2026-11-16T16:00:00.000Z'],
    ['2026-10-26T15:00:00Z','2026-11-02T16:00:00.000Z'],
    ['2027-03-08T16:00:00Z','2027-03-15T15:00:00.000Z'],
  ]) assert.equal(libraryWeek(new Date(at)).next.toISOString(), next);
});
function docFixture() {
  const node = tag => ({tag, dataset: {}, children: [],
    appendChild(child) { this.children.push(child); }, setAttribute(name,value) { this[name]=value; }});
  return {baseURI:'https://kandaka.com/', activeElement:null, createElement:node, createDocumentFragment:()=>node('fragment')};
}
test('cards preserve labels and treat catalogue text as text', () => {
  const doc = docFixture();
  const book = {id:'1', title:'<img onerror=alert(1)>', author:'Author', year:'2026',
    desc:'A source description', href:'https://example.test/book.pdf', label:'File unavailable', download:true};
  const card = libraryCard(doc, book, 0);
  const body = card.children[1];
  assert.equal(body.children[0].tag,'h3');
  assert.equal(body.children[0].textContent, book.title);
  assert.equal(body.children.at(-1).textContent,'File unavailable');
  assert.equal(body.children.at(-1).href,book.href);
  assert.equal(libraryLink('javascript:alert(1)'),null);
  assert.equal(libraryLink('data:text/html,hello'),null);
});
test('dates and three catalogue cards roll together, preserving focused links', () => {
  for (const language of ['en','ar']) {
    const doc=docFixture(), dates=[{},{},{}];
    const pool=Array.from({length:9},(_,i)=>({id:String(i),title:`Book ${i}`,author:'Author',desc:'Text',href:'https://example.test/',label:'View source'}));
    let cards=[];
    const stack={replaceChildren(fragment){cards=fragment.children;}};
    const section={querySelectorAll:()=>cards, contains:element=>element===cards[0],
      querySelector:selector=>selector==='[data-library-pool]'?{textContent:JSON.stringify(pool)}:stack};
    const notice={dataset:{language},closest:()=>section,
      querySelector:selector=>dates[selector==='[data-library-week]'?0:selector==='[data-library-next-review]'?1:2]};
    refreshLibrary(notice,new Date('2026-11-09T15:59:59Z'),doc);
    const before=cards.map(card=>card.dataset.libraryId);
    assert.equal(cards.length,3);
    doc.activeElement=cards[0];
    refreshLibrary(notice,new Date('2026-11-09T16:00:00Z'),doc);
    assert.deepEqual(cards.map(card=>card.dataset.libraryId),before);
    assert.equal(dates[1].dateTime,'2026-11-16T16:00:00.000Z');
    doc.activeElement=null;
    refreshLibrary(notice,new Date('2026-11-09T16:01:00Z'),doc);
    assert.notDeepEqual(cards.map(card=>card.dataset.libraryId),before);
    const sameCards=cards;
    refreshLibrary(notice,new Date('2026-11-12T20:00:00Z'),doc);
    assert.equal(cards,sameCards);
    assert.deepEqual(cards.map(card=>card.dataset.libraryId),selectLibrary(pool,new Date('2026-11-12T20:00:00Z')).map(book=>book.id));
  }
});
