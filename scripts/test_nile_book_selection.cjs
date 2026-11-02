const assert = require('node:assert/strict');
const fs = require('node:fs');
const api = require('../static/js/nile-book-selection.js');
const data = JSON.parse(fs.readFileSync(require('node:path').join(__dirname,'../data/nile_home_books.json'),'utf8'));
const epoch = Date.parse('2026-11-02T00:00:00Z');
const ids = items => items.map(x=>x.id);
let previous=[];
for(let day=-20;day<1000;day++) {
 const selected=api.select(data.items,epoch+day*86400000);
 assert.equal(selected.length,3);
 assert.equal(new Set(selected.map(x=>x.cover_key)).size,3);
 assert(!selected.some(x=>previous.includes(x.cover_key)),'adjacent-day cover repeat');
 previous=selected.map(x=>x.cover_key);
}
const rows=api.calendar(data.items,epoch,8);
rows.forEach(row=>assert.deepEqual(ids(row.books),ids(api.select(data.items,row.at))));
assert.deepEqual(ids(rows[0].books),ids(data.items.slice(0,3)));
assert.deepEqual(ids(rows[1].books),ids(data.items.slice(3,6)));
assert.deepEqual(ids(rows[4].books),ids(rows[0].books));
for(let n=0;n<=8;n++) {
 const pool=data.items.slice(0,n);
 const one=api.select(pool,epoch),two=api.select(pool,epoch+86400000);
 assert.equal(one.length,Math.min(3,n));
 if(n>=6)assert(!one.some(x=>two.some(y=>x.cover_key===y.cover_key)));
}
const duplicate=[...data.items,{...data.items[0],id:'duplicate'}];
assert.deepEqual(ids(api.select(duplicate,epoch)),ids(api.select(data.items,epoch)));
function mounted(locale, count=12) {
 let now=Date.parse('2026-11-02T23:59:00Z'),timer,visibility,pageshow;
 const badge={textContent:''};
 const cards=data.items.slice(0,count).map(x=>({hidden:false,getAttribute:key=>key==='data-book-id'?x.id:x.cover_key,querySelector:()=>({textContent:x[locale].title})}));
 const root={querySelectorAll:()=>cards,querySelector:s=>s==='[data-book-next]'?badge:null,getAttribute:key=>key==='data-book-locale'?locale:data.copy[locale].next};
 const doc={hidden:false,addEventListener:(type,fn)=>{visibility=fn;},removeEventListener:()=>{}};
 const win={addEventListener:(type,fn)=>{pageshow=fn;},removeEventListener:()=>{}};
 const timers={clearTimeout:()=>{timer=null;},setTimeout:(fn,delay)=>{timer={fn,delay};return 1;}};
 const control=api.mount(root,{now:()=>now,timers,document:doc,window:win});
 const visible=()=>cards.map((c,i)=>c.hidden?null:data.items[i].id).filter(Boolean);
 const start=visible();assert.deepEqual(start,ids(data.items.slice(0,Math.min(3,count))));
 assert.equal(timer.delay,60050);
 now=Date.parse('2026-11-03T00:00:01Z');timer.fn();
 const midnight=visible();assert.deepEqual(midnight,ids(api.select(data.items.slice(0,count),now)));
 now=Date.parse('2026-11-04T18:00:00Z');visibility();
 assert.deepEqual(visible(),ids(api.select(data.items.slice(0,count),now)));
 now=Date.parse('2026-11-05T12:00:00Z');pageshow();
 assert.deepEqual(visible(),ids(api.select(data.items.slice(0,count),now)));
 assert(badge.textContent.includes(locale==='en'?'Nov 6':'6'));
 control.destroy();assert.equal(timer,null);
 return {start,midnight,badge:badge.textContent};
}
const en=mounted('en'),ar=mounted('ar');assert.deepEqual(en.start,ar.start);assert.deepEqual(en.midnight,ar.midnight);
mounted('en',3);
const result={passed:true,adjacent_days_checked:1020,unique_covers:12,calendar_days:8,cycle_days:4,actual_mount_midnight:true,visibility_and_pageshow:true,en_ar_same_ids:true,short_pool:true,calendar:rows.map(r=>({date:new Date(r.at).toISOString().slice(0,10),titles:r.books.map(b=>b.en.title)}))};
console.log(JSON.stringify(result,null,2));
