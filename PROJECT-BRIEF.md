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
- **Charge controller: Tycon TP-SC24-60N-MPPT.** Passively cooled, IP43, ambient limit 122F.
  **Must be set from "FLd" to Lithium, 28.8V, BEFORE the bank is ever connected.**
- **Inverter: WZRELB 3000W 24V pure sine.** Fans and DC studs are on the **same end**, and the
  **fans blow out**. AC outlets, display, rocker switch, and a 3-pole AC terminal block are on the
  long front face. Idles at 20 to 50W, so it gets switched off when not in use.
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
- **Cables enter the RIGHT side of both boxes.**
- **Clearances are below manufacturer spec in both boxes** (Tycon gets 4.7 inches above and below
  versus the 7.9 it asks for; the inverter gets about 1 inch versus 2). Acceptable only because
  both boxes have forced ventilation, since those specs assume still air. **Verify with a laser
  thermometer on a hot high-load day.**

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
- Heated chicken waterer: 24V DC, needs a load-rated snap-disc failsafe and a 40A DC contactor.
- Shed freezer: 2P bank plus about 800W of new panels, racked **above** the plastic shed so they
  double as a shade roof.

## Diagrams

All drawings live at https://thechuch.github.io/hedge-field-guide/
