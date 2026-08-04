# Project Hedge, Field Brief

Context for answering questions about this build. Written so a fresh assistant can be useful
without the original conversation.

## Who you are talking to

Chuch (Estevan). Creative director by trade, strong maker skills, comfortable with electrical and
plumbing work. Communicates by voice-to-text, so transcripts have phonetic quirks ("sea flow" for
SEAFLO, "icb" for IBC).

**Writing rule: never use em-dashes or en-dashes.** Use commas, colons, periods, parentheses. For
ranges write "2 to 3", not "2-3".

He wants direct engineering guidance. Flag problems early, do not rubber-stamp, and say when you
are uncertain rather than guessing confidently.

## The site

Rural property near Ashland, southern Oregon, about 2,300 ft. Warm generally, but gets a couple of
weeks in the teens Fahrenheit every winter. Hard clay soil, terrible drainage, no natural slope.
Tiny house on a trailer, so it flexes and may eventually be moved. Half-acre pond, creek, attached
greenhouse, chicken run with 20 birds, garden, and a plastic shed with a freezer.

## Scope of the solar system

**This is SUPPLEMENTAL OFFICE POWER, not house backup.** One circuit to one outlet for office
equipment, roughly 100 to 300W. The office keeps its normal grid outlets; this adds a separate
solar outlet beside them.

**Hard rule: never tie this into the house wiring or panel.** It stays a standalone island.

## Electrical, as decided

- **Battery bank: 4P**, four LiTime 24V 100Ah, about 10.2 kWh nominal and 8 kWh usable, in an
  insulated deck box.
  - LiTime confirmed **in writing** that this model is rated for a **maximum of 4 in parallel**.
    6P is not supported and not advised. This is settled, do not reopen it.
  - **M8 terminal torque: 7 to 10 N·m**, confirmed by LiTime. Do not overtighten.
  - The other 2 batteries go to a separate 2P system for the shed freezer.
- **Array: 1,500W** (six 250W panels, 2S3P) on the tiny house roof. Not installed yet.
- **Charge controller: Tycon TP-SC24-60N-MPPT.** Passively cooled, IP43, 12/24V auto-detect.
  - **CONNECTION ORDER, the most important rule in the system: BATTERY FIRST, PV LAST.** It reads
    battery voltage at power-up to choose its system voltage. Disconnect is the exact reverse,
    **PV first, battery last.** Never break the battery connection while PV is live.
  - **Configure it with the BATTERY connected and PV disconnected**, then set the LiFePO4 24V preset,
    confirm 28.8V on screen, and disable temperature compensation. (An earlier note said to configure
    it before connecting the battery, which is impossible: it needs battery power to boot.)
  - **LOAD terminals stay EMPTY.** The manual explicitly forbids connecting an inverter there.
  - **Power terminal torque: 1.7 N·m (15 lbf·in).** Use ferrules on all stranded conductors.
  - The **70A fuse on its battery lead is correct** (the datasheet calls for 63A to 100A).
  - It has **no ground fault detection**, which is part of why bonding has to be right.
- **Inverter: WZRELB 3000W 24V pure sine.** Fans and DC studs are on the **same end**, and the
  **fans blow OUT** (confirmed on the bench). AC outlets, display, rocker switch, and a 3-pole AC
  terminal block (TB-2503L, 600V 25A) are on the long front face. Idles at 20 to 50W, so it gets
  switched off when not in use.
  - **MOUNTED FAN/DC END UP** (confirmed). That is the rule: whichever end blows hot air out points
    up, so its exhaust feeds the box's top exhaust fan instead of dumping into the intake stream.
  - Its rocker appears to isolate the DC input, so **no spark at connection with the switch off is
    normal**, not a fault.
  - For the permanent AC output, **bolt to the terminal block** rather than plugging a cord into the
    receptacles. Nothing to vibrate loose and it passes cleanly through a gland.
- **Grid charger: Iota DLS-27-15**, 15A at 27.2V. Needs the **IQ-LIFEPO module** for a correct
  LiFePO4 charge profile (default 27.2V is a float voltage and stalls around 85%).
  - Its job: top the bank up at night if the panels did not fill it.
  - Switched by a Baomain contactor driven by a TPDIN monitor watching battery voltage. Keep that
    contactor, it is what makes the system solar-first instead of letting grid do the work.
  - **Feed the Iota from the grid side only.** Never from the inverter.
- **ATS: owned but NOT used.** Nothing needs source selection, and its 20 to 30 second transfer
  delay could not protect a computer anyway. If ride-through is ever wanted, that is a small UPS.

## Enclosures, as built

Two VEVOR steel IP65 boxes with built-in thermostat and fan, **stacked on the deck rail**, not on
the house. That was deliberate: the house wall has already had mold and water trouble, and the
house is on a trailer.

- **Box A, top:** 23.6 x 15.7 x 11.8 exterior, panel 19 x 11.5. **Inverter only**, mounted
  **vertically with the fan/DC end UP** so its exhaust feeds the box's top fan.
- **Box B, bottom:** 23.6 x 23.6 x 11.8, panel 19 x 19. **Tycon in a full-height left column**
  (nothing above or below it, that is its convection path), **Iota + IQ module + DIN rail** in the
  right column.
- **Airflow: side louvers on the left are INTAKE, fan on the top face is EXHAUST.**
- **Cables enter the RIGHT side of both boxes.** Not the bottom and not through the gap between
  them, because the lower box exhausts out its top face and that gap is already tight.
- **Clearances are below manufacturer spec in both boxes** (Tycon gets 4.7 inches above and below
  versus the 7.9 it asks for; the inverter gets about 1 inch versus 2). Acceptable only because
  both boxes have forced ventilation, since those specs assume still air. **Verify with a laser
  thermometer on a hot high-load day.**

### Gland positions, confirmed

All glands come from stock already on hand. **Nothing to buy.** Twelve entries, four in Box A and
eight in Box B, all on the right side face (11.8 inches deep by 23.6 tall).

**Box A, top, inverter:**
- **HIGH: two 1 inch NPT** for the 2/0 pair, level with the DC studs, which are up.
  Drill **1-3/8 inch**.
- **LOW: 3/4 inch NPT** for the AC out to the office (drill 1-1/8) and **1/4 inch NPT** for the
  inverter remote pair (drill 9/16).

**Box B, bottom:**
- **High: 3/8 inch NPT x2** for PV+ and PV- (drill 11/16). PV comes down from above.
- **Upper middle: 1/2 inch NPT x2** for the Tycon battery leads, 6 ga (drill 7/8). Stock is
  exactly consumed here, no spare.
- **Lower middle: 3/8 inch NPT x2** for the Iota DC leads, 10 ga (drill 11/16).
- **Low: 3/4 inch NPT** for grid AC in (drill 1-1/8) and one **3/4 inch NPT 4-PORT** gland
  carrying RS485, the TPDIN relay pair, and two spares through a single hole (drill 1-1/8).

**Drill totals:** 9/16 x1, 11/16 x4, 7/8 x2, 1-1/8 x3, 1-3/8 x2. Step bit handles up to 7/8, the
two larger sizes want a bi-metal hole saw or a knockout punch. Deburr and touch up paint on every
hole, and vacuum all swarf out before any electronics go in.

**Gland rules:** one cable per gland (the quad is one per port), match the gland to the cable OD
rather than the wire gauge, drip loop below every entry, tighten the compression nut on the cable
itself, and confirm each gland still has its locknut and gasket.

**Conduit vs glands:** glands for all the DC (the jackets are already rated for exposure and 2/0
would need 1-1/4 inch conduit), conduit for the AC run into the office. If liquid-tight flex is
used on an exposed run, do not try to seal it to a gland. Run it as a sleeve stopping short of the
gland, clamp it, and drill a weep hole at the low point so it drains instead of funneling water.

## Grounding, added 2026-08-02 (was missing entirely)

Two steel boxes with 120V inside, on a wooden deck rail, had **no path to earth**. That is fixed as
follows. **One rod, star topology, one DC bond.**

- **Ground bar in Box B.** Bond to it: both box bodies, both metal back panels, both doors (braided
  jumper), the DIN rail, the Tycon GND terminal, the Iota chassis, and the inverter chassis.
  **Scrape paint or use paint-piercing star washers**, these boxes are painted.
- **10 AWG green EGC between Box A and Box B.** **6 AWG from the ground bar to one ground rod.**
- **The DC system bond is exactly ONE conductor**: 6 AWG from the **deck box negative bus** to
  ground. Nowhere else, not at the array, the Tycon, the inverter, or the Iota. **Label it.**
- **The array rail and the DIHOOL enclosure** bond to the same rod. One electrode system.
- **Bond to the rod, not the trailer.** The house is on wheels. Put "disconnect the array
  down-conductor and the EGC" on a move checklist.
- Use **green insulated 6 AWG** for the array down-run, not bare copper (galvanic corrosion against
  aluminum rail and the metal roof). AL9CU dual-rated lug with antioxidant at the rail.

## Wiring blockers found in verification, 2026-08-02

- **NEVER use a Cat5 patch cable for the Tycon RS485.** The Tycon's RJ45 carries **+7V on pin 7 and
  +5V on pin 8**; the TPDIN's port is **RJ12 6-pin** and those land on its RS232 RX/TX. It would
  destroy the TPDIN. **Use the Tycon TPDIN-CABLE-485** (not the -232, that is for the older 20N/40N).
  It is only 48 inches, so measure the routed path, and check the molded plug fits the gland.
- **The inverter AC output needs overcurrent protection.** Add a **20A single-pole breaker** (or
  inline AC fuse) at the inverter output and run **12 AWG**. Terminal block straight to an outlet
  leaves the branch conductor unprotected.
- **Measure the inverter's neutral-to-ground bonding before wiring the GFCI.** Running, no load,
  read L-to-G and N-to-G. **120V and 0V** means internally bonded, change nothing. **About 60V on
  both** means floating, and **a GFCI will not protect anyone** until you make **one**
  neutral-to-ground bond at the inverter terminal block. One place only.
- **PV wire on the combined run goes to 8 AWG** (Y-branch through the DIHOOL to the controller).
  10 AWG is undersized for three strings combined. Per-string 10 AWG is fine.
- **Check the panel label for "max series fuse rating."** With three parallel strings a fault can be
  backfed at about 22A. If the label says 15A, **each string positive needs an inline fuse**.
- **Add a manual AC disconnect** upstream of the contactor in Box B, or feed it cord-and-plug.
- **Drive the contactor coil from a normally-open TPDIN channel**, so losing the TPDIN means no grid
  charging rather than charging forever. 1N4007 flyback across the coil, banded end to +24V.
- **Do not open the inverter** to tap the rocker for remote control. Check for a factory remote port
  first; otherwise the right answer is a DC contactor in the battery feed.
- **Do not install the dual-voltage plug and the IQ-LIFEPO at the same time.** IQ module only.
- **Segregate low voltage from line voltage** inside Box B, opposite sides of the panel.

## Array notes

- **2S3P is at Tycon's stated maximum series count** for a 100V unit. Confirmed correct.
- Array is **1500W against a 1560W controller limit**, so **it cannot grow** on this controller.

## Safety rules already established

- Each battery positive gets its **own 150A ANL fuse**.
- **Charger leads need their own fuses at the bus end**: 70A on the Tycon lead (6 ga), about 30A
  on the Iota lead (10 ga). A charger's internal fuse is at the wrong end.
- Keep the unfused battery-post-to-fuse stub **under 7 inches**, booted and routed clear.
- **Connect negatives first, positives one at a time, positive LAST.** Reverse to disconnect.
- **Pre-charge the inverter capacitors** (10 to 100 ohm for about 2 seconds) before closing the
  breaker. The caps draw inrush at connection whether the rocker is on or off.
- **Hydraulic-crimped lugs only.** No hammer lugs, no set-screw lugs, no solder.
- **Non-combustible barrier** under the bus bars and fuses.
- **Boots on every stud** plus a lift-off polycarbonate guard. The main hazard at 24V is a dropped
  tool, not shock.
- **Never hot-reconnect a battery whose BMS tripped.** Pull its fuse, charge that pack until it
  matches the bank, then reinsert.

## Water system, not built yet

Pond to SEAFLO pump to a 4-stage filter to a 1,600 gallon tank. Roof rain goes through a
first-flush diverter and a buried line to the same tank. A submersible in the tank pushes
distribution out the top to a manifold.

- Only about **10 PSI**, so keep mains at 1 inch and use **low-pressure drip tape**.
- **Motorized ball valves, not solenoids.** Solenoids need line pressure to seal.
- The shared trench carries **separate pipes, not a plumbed tee**. The pond fill line is
  pressurized and seasonal, the rain line is gravity and winter-critical, and the barrel line
  flows the opposite direction.

## Open items

- **Bus stud size (M8 vs 3/8 inch M10) is still unmeasured.** It gates the 2/0 ring lug order.
  This is the highest-leverage thing left: one caliper measurement unblocks the biggest purchase.
- Does the inverter have a **remote on/off port**? Not found in photos. If there is none, a small
  relay wired in parallel with the rocker (driven by the ESP32) gives remote and scheduled control,
  which matters because leaving a 3000W inverter idling for a 200W office load wastes about
  0.5 kWh per day.
- Heated chicken waterer: 24V DC, needs a load-rated snap-disc failsafe and a 40A DC contactor.
- Shed freezer: 2P bank plus about 800W of new panels, racked **above** the plastic shed so they
  double as a shade roof.

## Diagrams

All drawings live at https://thechuch.github.io/hedge-field-guide/
