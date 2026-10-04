# Project Hedge field brief

Current public revision: 2026.10.04-r1. This brief replaces the August brief. Use index.html and its section sources in _content as the current field record.

## Scope and state

- Main system supplies a separate office outlet. No ATS and no backfeed into tiny-house wiring.
- Six SS250P-60 250 W panels, arranged as three parallel strings of two series panels. 1500 W, 75.2 V Voc at standard conditions. Cold Voc remains to be verified below 100 V.
- Original photographed controller: TP-SC24-30N-MPPT, 30 A, 100 V PV, 780 W array limit at 24 V.
- Ordered replacement: TP-SC24-60N-MPPT, 60 A, 100 V PV, 1560 W array limit at 24 V. The newer TS60 is not selected.
- Four LiTime 24 V 100 Ah batteries in parallel: 25.6 V / 400 Ah / 10.24 kWh nominal. Four is the manufacturer parallel limit. Other two batteries belong to a separate shed plan.
- Standard battery model has no established low-temperature charging cutoff. Both MPPT and IOTA need independent all-pack temperature protection. Battery-powered heat must operate during an outage.
- Inverter is a photographed 24 V / 3000 W Reliable Electric unit. Exact model, manual and neutral arrangement pending.
- IOTA DLS-27-15 grid charger is planned on the middle exterior tiny-house outlet. First GFCI outlet also supplies networking; far outlet also supplies the Rinnai heater. These outlets share one branch. Breaker rating and GFCI coverage are unverified.
- Two steel cabinets are already stacked on the deck structure. Battery box sits beside them on the reported level aggregate pad. Front foam and foil end piece removed; internal battery support unresolved.
- Fans mounted on plates; lower thermostat mounted. Exact fan current/range and thermostat DC ratings pending. DDR-30G-24 received and mounted, candidate dedicated fan supply.
- No PV descent cables installed at last report. MNPV3 and all bars/output lug received. Three MNEPV15-150-1PNP breakers planned; no breakers yet, exact order unconfirmed.
- Delivered DIHOOL HT3-DZ47ZH-MC4, internal DZ47Z-60 60 A / 1000 V DC, is owned. Delivered manual confirms top input and bottom output. Actual lead size and compatible mating connectors remain open.
- Lower box photo: Tycon left, IOTA upper right, DDR/TPDIN/MC-9b left to right on lower rail. IQ-LIFEPO 2-stage module confirmed. Controller model and TPDIN version cannot be read in this view.
- Baomain-packaged LS Metasol MC-9b DC24V coil, A1 positive/A2 negative, assigned to IOTA AC control. Use regulated 24 V. Charger duty, fuse-conditioned fault rating and interface checks remain open.
- TOBSUN EA15-5V owned, provisional irrigation ESP32 supply. Nominal 12/24 V input, 5 V / 3 A maximum output, 15 W. Full input range and isolation unverified; not assigned to the isolated safety node.
- Measure IOTA fan clearance, minimum 4 inches; DDR 40 mm above, 20 mm below, 5 mm each side. Provide guarded AC wiring area separate from TPDIN network/sensors. No clearance approval from the photo.
- IOTA owner manual prohibits extension cords and cutting its cord. Plan a suitable permanent receptacle within factory-cord reach; the recorded 15 ft AC route is a distance estimate.

## Unresolved safety work

Final protection coordination, fault interruption, cable/terminal ratings, torque, cold Voc, clearances, heater controls, charger profiles and grounding remain open. The owned 80 A breaker cannot support full 3000 W inverter output. Do not approve the old ANL/70 A/30 A fuse set without the complete design.

The existing 50 A shore feed runs about 20 to 25 ft from a shop-fed receptacle to the tiny-house inlet. A rod is reported at the supply end. Verify the supply EGC and neutral-bond point. Provide permanent local cabinet/array/chassis bonding to an approved building PE point. The removable IOTA cord cannot be the sole permanent bond. Additional electrodes, if needed, must be integrated. No automatic battery-negative or inverter-neutral bond is approved.

Independent hardwired temperature permission must override TPDIN normal control. Actual TPDIN hardware/firmware, PV switching assembly, four heater kits, control interfaces and fail-safe tests remain unresolved. No field power-up is released by the guide's checkboxes.

Surge protection is a coordinated design proposal. MNSPD115 is not a 100 V clamp. AC/PV/DC/data candidates need maker and installation checks. No complete-system EMP immunity is claimed. Protected spares are proposed inventory; none is confirmed tested and shielded.

## Public and private records

Keep credentials, IP addresses, hostnames, coordinates, family/contact data, camera details, serial photos and precise spare storage locations out of the public site. Field log data stays in the user's browser and can be exported privately.

The water and separate shed/chicken plans are preserved under #other as records and measurements, with unresolved electrical work marked. Old URLs redirect to the current sections. Historical instructions are retained in git history only. Old PDFs in the private project folder remain superseded for electrical installation.

## Editing

Edit _content/*.html, then run python3 _gen/build_guide.py. Update revision strings in the generator, content, assets/guide.js and sw.js together. Increase the service-worker cache on each release. Verify phone layout, local notes and cache update before deployment.
