/* Atomic offline release: replace retired pages and avoid mixed content versions. */
const REVISION = '2026.09.27-r1';
const CACHE = 'hedge-field-v36-' + REVISION;
const ASSETS = [
  './', 'index.html', 'assets/guide.css?v=2026.09.27-r1', 'assets/guide.js?v=2026.09.27-r1', 'icon.svg', 'manifest.webmanifest',
  'build-manual.html', 'battery-wiring.html', 'deck-layout.html', 'bench-test.html',
  'fire-safety.html', 'gland-plan.html', 'panel-layout.html', 'panel-wiring.html',
  'wall-cabinet.html', 'cabinet-fab.html', 'mount-detail.html', 'plot-plan.html',
  'pump-skid.html', 'split-station.html', 'chicken-waterer.html', 'shed-freezer.html',
  'shopping.html', 'punch-list.html', 'litime-email.html', 'ask.html'
];
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(ASSETS.map(path => new Request(path, {cache:'reload'})))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(key => key.startsWith('hedge-field-') && key !== CACHE).map(key => caches.delete(key)))).then(() => self.clients.claim()));
});
self.addEventListener('message', event => {
  if (event.data?.type !== 'CHECK_CACHE') return;
  event.waitUntil(caches.open(CACHE).then(async cache => {
    const results=await Promise.all(ASSETS.map(path=>cache.match(new URL(path,self.registration.scope).href)));
    event.source?.postMessage({type:'CACHE_STATUS',revision:REVISION,ready:results.every(Boolean)});
  }));
});
self.addEventListener('fetch', event => {
  const request=event.request;
  const url=new URL(request.url);
  if(request.method!=='GET' || url.origin!==self.location.origin || !url.href.startsWith(self.registration.scope))return;
  if(request.mode==='navigate'){
    event.respondWith(caches.open(CACHE).then(async cache=>{
      // Serve a complete installed release. A new worker replaces the full cache,
      // then the page offers Reload. Never mix network HTML into an older release.
      const saved=await cache.match(request,{ignoreSearch:true});
      if(saved)return saved;
      try{return await fetch(request);}
      catch(_){return await cache.match(new URL('index.html',self.registration.scope).href);}
    }));
    return;
  }
  event.respondWith(caches.open(CACHE).then(async cache=>{
    const saved=await cache.match(request);
    if(saved)return saved;
    return fetch(request);
  }));
});
