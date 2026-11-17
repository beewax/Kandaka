import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {join} from 'node:path';
import {selectArtwork,selectWeeklyVisuals,refreshArtwork} from '../static/js/artwork-updates.mjs';
const cases=JSON.parse(readFileSync(new URL('./fixtures/artwork-publication.json',import.meta.url)));
const byName=name=>cases.find(c=>c.name===name);
const pick=c=>selectArtwork(c.items,new Date(c.at)).map(w=>w.id);
test('every work in a new batch appears immediately, in deterministic date/source order',()=>{
  assert.deepEqual(pick(byName('midweek-four')),['new-a','new-b','new-c','new-d']);
  assert.deepEqual(pick(byName('newest-first')).slice(0,2),['a-newer','b-older']);
  assert.equal(pick(byName('midweek-one'))[0],'new-a');
  assert.ok(!pick(byName('before-publication')).includes('new-a'));
  assert.equal(pick(byName('at-publication'))[0],'new-a');
  assert.ok(!pick(byName('regional-only')).includes('foreign'));
  assert.equal(new Set(pick(byName('deduplicate'))).size,3);
});
test('seven-day priority expires by elapsed hours across both daylight-saving transitions',()=>{
  assert.equal(pick(byName('four-before-expiry')).length,4);
  assert.equal(pick(byName('four-at-expiry')).length,3);
  for(const name of ['at-expiry','four-at-expiry']){
    const c=byName(name);assert.deepEqual(pick(c),selectWeeklyVisuals(c.items,new Date(c.at),2).map(w=>w.id));
  }
  for(const name of ['fall-dst','spring-dst'])assert.equal(pick(byName(name))[0],'new-a');
});
test('browser refresh admits all new cards, preserves translations and stays duplicate-free',()=>{
  const c=byName('midweek-four');
  for(const language of ['en','ar']){
    let cards=c.items.map((w,i)=>({hidden:i>=3,dataset:{artworkId:w.id,artworkSince:w.since,artworkGroup:w.group}}));
    const grid={appendChild(card){cards=cards.filter(w=>w!==card);cards.push(card);}};
    const section={dataset:{language},hasAttribute:()=>true,querySelectorAll:()=>cards,querySelector:s=>s==='.art-grid'?grid:null};
    for(let i=0;i<2;i++)refreshArtwork(section,new Date(c.at));
    assert.deepEqual(cards.filter(c=>!c.hidden).map(c=>c.dataset.artworkId),pick(c));
  }
});
test('actual Hugo and browser selections match for all date/batch cases in both languages', {skip:!process.env.ARTWORK_HUGO_FIXTURE},()=>{
  for(const route of ['','ar']){
    const actual=JSON.parse(readFileSync(join(process.env.ARTWORK_HUGO_FIXTURE,'public',route,'index.html'),'utf8'));
    for(const c of cases)assert.deepEqual(actual.find(r=>r.name===c.name).selected,pick(c),route+' '+c.name);
  }
});
