# Project Hedge field guide

Live: https://thechuch.github.io/hedge-field-guide/

Static, phone-ready PWA. Current revision: **2026.10.04-r1**. The single guide includes the solar/battery design, winter controls, bonding, shared AC branch, surge coordination, parts status, protected spares, release checks and other project references.

## Maintain

1. Read PROJECT-BRIEF.md and the current field page. Current equipment is the 100 V TP60, not the 150 V TS60.
2. Edit `_content/*.html`. Run `python3 _gen/build_guide.py` to build `index.html`.
3. UI code: `assets/guide.css` and `assets/guide.js`.
4. Update the revision everywhere and bump `CACHE` in `sw.js` for each release. The full guide and retired-route redirects are precached atomically.
5. Run `python3 _gen/check_guide.py` and `node --check assets/guide.js`. Test responsive layout, search, local-note persistence, export/import, and offline navigation with the browser.
6. GitHub Pages publishes the root of `main`. Confirm the deployment and live revision after pushing.

## Data and safety

- Field notes stay in localStorage on each device. Export/import JSON provides manual transfer. No account, analytics, telemetry or live equipment controls.
- Checkboxes record preparation only. They cannot approve wiring or clear engineering holds.
- Old HTML routes forward to current sections. Historical diagrams are in git history, not the active site.
- External manuals are linked and are not included in the offline cache.
- Do not publish private master notes, credentials, network details, coordinates or exact spare-storage locations.
- The main bank remains 4P. Independent office output only. No grid backfeed or ATS.
