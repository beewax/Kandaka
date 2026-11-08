const assert = require('node:assert/strict');
const { select, mount } = require('../static/js/nile-inline-selection.js');
const midnight = Date.parse('2026-11-09T00:00:00Z');
for (const seed of [0, 1, 4294967295, 195843927]) {
  for (let day = 0; day < 40; day++) {
    const at = midnight + day * 86400000;
    assert.equal(select(seed, 10, at - 1), (select(seed, 10, at) + 9) % 10);
    assert.equal(select(seed, 10, at), select(seed, 10, at + 86399999));
  }
}
assert.equal(select(1, 0, midnight), -1);
function run(locale) {
  let at = midnight - 1000, timer, visible, focused = false;
  const events = {}, slotEvents = {}, windowEvents = {};
  const initial = select(12345, 10, at);
  visible = initial;
  const slot = {
    contains: () => focused,
    replaceChildren: value => { visible = value; },
    addEventListener: (key, fn) => { slotEvents[key] = fn; },
    removeEventListener: key => { delete slotEvents[key]; }
  };
  const root = {
    querySelectorAll: () => Array.from({length:10}, (_, i) => ({content:{cloneNode:()=>i}})),
    querySelector: () => slot,
    getAttribute: key => key === 'data-nile-seed' ? '12345' : String(initial)
  };
  const doc = {hidden:false, activeElement:null,
    addEventListener:(key, fn)=>{events[key]=fn;}, removeEventListener:key=>{delete events[key];}};
  const win = {addEventListener:(key,fn)=>{windowEvents[key]=fn;},removeEventListener:key=>{delete windowEvents[key];}};
  const timers = {setTimeout:(fn,delay)=>{timer={fn,delay};return 1;},clearTimeout:()=>{timer=null;}};
  const control = mount(root,{now:()=>at,timers,document:doc,window:win});
  assert.equal(visible,initial); assert.equal(timer.delay,1050);
  at = midnight + 50; timer.fn();
  assert.equal(visible,select(12345,10,at));
  at += 3 * 86400000; events.visibilitychange();
  assert.equal(visible,select(12345,10,at));
  focused = true; const previous=visible; at += 86400000; timer.fn();
  assert.equal(visible,previous);
  focused=false; slotEvents.focusout(); timer.fn();
  assert.equal(visible,select(12345,10,at));
  at += 86400000; windowEvents.pageshow();
  assert.equal(visible,select(12345,10,at));
  const result=visible; control.destroy(); assert.equal(timer,null);
  assert.equal(Object.keys(events).length+Object.keys(slotEvents).length+Object.keys(windowEvents).length,0);
  return result;
}
assert.equal(run('en'),run('ar'));
console.log('PASS: UTC boundaries, full cycle, bilingual selection, midnight timer, sleeping tabs, page restore, focus preservation, cleanup.');
