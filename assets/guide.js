'use strict';
(() => {
  const REVISION = '2026.09.27-r1';
  const KEY = 'hedge-field-record-2026-09';
  const fields = [...document.querySelectorAll('[data-save]')];
  const storageStatus = document.getElementById('storage-status');
  const message = document.getElementById('notes-message');
  const status = document.getElementById('offlineStatus');
  let storeAvailable = true;
  let cached = false;
  try {
    const theme = localStorage.getItem('hedge-theme');
    if (theme === 'light' || theme === 'dark') document.documentElement.dataset.theme = theme;
    const data = JSON.parse(localStorage.getItem(KEY) || '{}');
    for (const el of fields) {
      const value = data[el.dataset.save];
      if (el.type === 'checkbox') el.checked = value === true;
      else if (typeof value === 'string') el.value = value.slice(0, el.maxLength);
    }
    localStorage.setItem('hedge-storage-check', '1');
    localStorage.removeItem('hedge-storage-check');
  } catch (_) { storeAvailable = false; }
  const values = () => Object.fromEntries(fields.map(el => [el.dataset.save, el.type === 'checkbox' ? el.checked : el.value]));
  function readSaved() {
    const data = JSON.parse(localStorage.getItem(KEY) || '{}');
    if (!data || typeof data !== 'object' || Array.isArray(data)) throw new Error('Invalid saved record.');
    return data;
  }
  function save(changedField) {
    try {
      const data = readSaved();
      if (changedField) data[changedField.dataset.save] = changedField.type === 'checkbox' ? changedField.checked : changedField.value;
      else Object.assign(data, values());
      localStorage.setItem(KEY, JSON.stringify(data));
      storageStatus.textContent = 'Saved on this device. Export a backup to keep a separate copy.';
    } catch (_) {
      storeAvailable = false;
      storageStatus.textContent = 'This browser cannot save notes. Export them before leaving this page.';
      storageStatus.classList.add('hold');
    }
  }
  storageStatus.textContent = storeAvailable ? 'Notes save on this device only. No account or upload.' : 'This browser cannot save notes. Use Export notes before leaving.';
  if (!storeAvailable) storageStatus.classList.add('hold');
  fields.forEach(el => el.addEventListener('input', () => save(el)));
  window.addEventListener('storage', event => {
    if (event.key !== KEY) return;
    try {
      const data=readSaved();
      fields.forEach(el=>{
        if(el===document.activeElement) return;
        const value=data[el.dataset.save];
        if(el.type==='checkbox') el.checked=value===true;
        else el.value=typeof value==='string'?value.slice(0,el.maxLength):'';
      });
      storageStatus.textContent='Notes changed in another tab. Other fields have been updated; the field you are editing stays in place.';
    } catch(_) { storageStatus.textContent='Could not read the change from another tab. Export this tab’s notes before continuing.'; }
  });
  document.getElementById('themeToggle').addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem('hedge-theme', next); } catch (_) {}
  });
  document.getElementById('exportNotes').addEventListener('click', () => {
    const payload = {type:'hedge-field-notes', schema:1, guideRevision:REVISION, exportedAt:new Date().toISOString(), fields:values()};
    const url = URL.createObjectURL(new Blob([JSON.stringify(payload,null,2)], {type:'application/json'}));
    const a = document.createElement('a'); a.href=url; a.download='hedge-field-notes-'+new Date().toISOString().slice(0,10)+'.json'; document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    message.textContent = 'Backup download started. Keep the file private if it contains serial numbers or storage locations.';
  });
  document.getElementById('importNotesButton').addEventListener('click',()=>document.getElementById('importNotes').click());
  document.getElementById('importNotes').addEventListener('change', async event => {
    const file = event.target.files[0]; if (!file) return;
    try {
      if (file.size > 200000) throw new Error('File is too large.');
      const data = JSON.parse(await file.text());
      if (data.type !== 'hedge-field-notes' || data.schema !== 1 || !data.fields || typeof data.fields !== 'object' || Array.isArray(data.fields)) throw new Error('This is not a supported field-note backup.');
      const imported=fields.filter(el=>Object.hasOwn(data.fields,el.dataset.save));
      if(!imported.length) throw new Error('The backup has no recognized fields.');
      if(imported.some(el=>typeof data.fields[el.dataset.save] !== (el.type==='checkbox'?'boolean':'string'))) throw new Error('A field has an invalid value type.');
      if (!window.confirm('Replace this device’s current field notes with this backup?')) return;
      const merged=readSaved();
      for (const el of imported) {
        const v=data.fields[el.dataset.save];
        merged[el.dataset.save]=el.type==='checkbox'?v:v.slice(0,el.maxLength);
      }
      localStorage.setItem(KEY,JSON.stringify(merged));
      for(const el of fields){
        const v=merged[el.dataset.save];
        if(el.type==='checkbox')el.checked=v===true;
        else el.value=typeof v==='string'?v.slice(0,el.maxLength):'';
      }
      storageStatus.textContent='Saved on this device. Export a backup to keep a separate copy.';
      message.textContent = 'Notes imported. These records do not close the design release checks.';
    } catch(error) { message.textContent = 'Import failed: '+error.message; }
    finally { event.target.value=''; }
  });
  const chapters = [...document.querySelectorAll('.chapter')];
  const search = document.getElementById('searchGuide');
  const searchStatus = document.getElementById('searchStatus');
  const empty = document.getElementById('noResults');
  function filter() {
    const words = search.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let n = 0;
    chapters.forEach(section => {
      const content = section.textContent.toLowerCase();
      const match = words.every(word => content.includes(word));
      section.hidden = !match;
      if (match) n++;
      if (words.length && match) section.querySelectorAll('details').forEach(d => d.open=true);
    });
    empty.hidden = n !== 0;
    searchStatus.textContent = words.length ? n+' of '+chapters.length+' sections match. Clear search to show the full guide.' : '';
  }
  search.addEventListener('input', filter);
  function goTo(id) {
    search.value='';filter();
    const node=document.getElementById(id); if(node){location.hash=id;node.scrollIntoView({behavior:'auto',block:'start'});}
  }
  document.getElementById('sectionSelect').addEventListener('change', event => goTo(event.target.value));
  document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', () => {search.value='';filter();}));
  document.getElementById('expandDetails').addEventListener('click', event => {
    const details=[...document.querySelectorAll('.chapter:not([hidden]) details')];
    const open=details.some(d=>!d.open);
    details.forEach(d=>d.open=open);
    event.target.textContent=open?'Close details':'Open details';
  });
  let activeFrame=0;
  function updateActive(){
    activeFrame=0;
    const visible=chapters.filter(section=>!section.hidden);
    const threshold=document.querySelector('.toolbar').getBoundingClientRect().bottom+20;
    let current=visible[0];
    for(const section of visible) if(section.getBoundingClientRect().top<=threshold) current=section;
    if(!current)return;
    document.querySelectorAll('.toc a').forEach(a=>a.classList.toggle('active',a.hash==='#'+current.id));
    document.getElementById('sectionSelect').value=current.id;
  }
  function queueActive(){if(!activeFrame)activeFrame=requestAnimationFrame(updateActive);}
  window.addEventListener('scroll',queueActive,{passive:true});
  window.addEventListener('resize',queueActive);
  window.addEventListener('hashchange',queueActive);
  queueActive();
  let printState=[];
  window.addEventListener('beforeprint',()=>{
    printState=[...document.querySelectorAll('details')].map(d=>[d,d.open]);
    printState.forEach(([d])=>d.open=true);
    for(const el of fields.filter(f=>f.type!=='checkbox')){
      const copy=document.createElement('div');copy.className='print-value';copy.textContent=el.value||'(No entry)';el.after(copy);
    }
  });
  window.addEventListener('afterprint',()=>{
    printState.forEach(([d,open])=>d.open=open);
    document.querySelectorAll('.print-value').forEach(n=>n.remove());
  });
  document.getElementById('printGuide').addEventListener('click',()=>window.print());
  function showConnection(){
    status.textContent = cached ? (navigator.onLine?'Saved for offline use · '+REVISION:'Offline · saved guide '+REVISION) : (navigator.onLine?'Online · preparing offline copy':'Offline copy not yet verified');
  }
  document.getElementById('reloadGuide').addEventListener('click',()=>location.reload());
  function checkCache(){
    const target=navigator.serviceWorker.controller;
    if(target) target.postMessage({type:'CHECK_CACHE'});
  }
  window.addEventListener('online',showConnection); window.addEventListener('offline',showConnection);showConnection();
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.addEventListener('message',event=>{
      if(event.data?.type==='CACHE_STATUS') {
        if(event.data.revision!==REVISION && event.data.ready){
          document.getElementById('updateNotice').hidden=false;
          status.textContent='Update available · reload for revision '+event.data.revision;
        } else {cached=event.data.ready===true;showConnection();}
      }
    });
    navigator.serviceWorker.addEventListener('controllerchange',checkCache);
    navigator.serviceWorker.register('sw.js',{updateViaCache:'none'}).then(reg=>{
      reg.update().catch(()=>{});
      navigator.serviceWorker.ready.then(checkCache);
    }).catch(()=>{status.textContent='Offline storage unavailable. Use Print / save PDF.';});
  } else status.textContent='Offline storage unavailable. Use Print / save PDF.';
})();
