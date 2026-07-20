/* Project Hedge Field Guide · offline shell cache */
const CACHE = 'hedge-field-v11';
const ASSETS = [
  './',
  'index.html',
  'plot-plan.html',
  'battery-wiring.html',
  'deck-layout.html',
  'shed-freezer.html',
  'shopping.html',
  'wall-cabinet.html',
  'cabinet-fab.html',
  'chicken-waterer.html',
  'litime-email.html',
  'assets/site.css',
  'icon.svg',
  'manifest.webmanifest'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  // Network-first for navigations (get fresh pages when online), fall back to cache offline.
  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(req, copy));
        return res;
      }).catch(() => caches.match(req).then((r) => r || caches.match('index.html')))
    );
    return;
  }
  // Cache-first for static assets.
  e.respondWith(caches.match(req).then((r) => r || fetch(req).then((res) => {
    const copy = res.clone();
    caches.open(CACHE).then((c) => c.put(req, copy));
    return res;
  }).catch(() => r)));
});
