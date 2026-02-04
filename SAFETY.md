# Safety

You are about to build a 3D printer from parts that other people threw away. This machine can burn you, shock you, pinch you, and—if you're careless with wiring—start a fire. Please don't become an Amalgam statistic.

This isn't meant to scare you off. Thousands of people build DIY printers safely every year. But they do it by respecting the hazards, not ignoring them.

**Read this before you start building.**

---

## The Scavenger Reality

You're not unboxing a factory-tested appliance. You're working with:

- **Unknown history** — That donor printer might have been "broken" because of a wiring fault
- **Worn components** — Frayed wires, cracked insulation, corroded connectors
- **Mystery PSUs** — May be undersized, damaged, or outright counterfeit
- **Dust and grime** — Years of accumulated filament dust, grease, and debris

**The rule is simple:** Inspect everything. If something looks wrong, replace it. The $3 you save reusing a sketchy cable isn't worth the risk.

---

## Before You Touch Donor Parts

### Dust and Contamination

Donor printers accumulate dust, dried lubricant, filament particles, and sometimes mold. Before disassembly:

- **Wear nitrile gloves** — Protects your hands from grime and old grease
- **Work in a ventilated area** — Compressed air kicks up fine particles
- **Blow out dust first** — Use compressed air or a blower before handling
- **Wash hands after** — Even with gloves, wash up before eating or touching your face

This isn't paranoia—old printers are genuinely grimy. Treat them like you'd treat any second-hand mechanical equipment.

### Visual Inspection

Before reusing any electrical component, inspect it:

| Check | What to Look For |
|-------|------------------|
| **Wires** | Cracked insulation, burn marks, melted spots, fraying |
| **Connectors** | Discoloration, melting, corrosion, loose pins |
| **PSU** | Bulging capacitors, burn marks, strange smells |
| **Bed heater** | Damaged pads, exposed traces, burnt spots |
| **Motors** | Grinding bearings, damaged shafts, burnt smell |

**If in doubt, replace it.** New wiring is cheap. House fires are not.

---

## Electrical Hazards

### Mains Power

The power supply connects to mains voltage (240V in Australia, 110-120V in North America). This can kill you.

- **Never open a PSU** — Capacitors hold charge even when unplugged
- **If you must work inside a PSU** — Unplug it, wait 10+ minutes for capacitors to discharge
- **Check mains wiring** — Use proper gauge wire, secure connections, strain relief
- **Use a grounded outlet** — The earth connection exists for a reason
- **Don't run extension cords under carpets** — Heat buildup is a fire risk

### Low Voltage (12V/24V)

The printer runs on 12V or 24V DC. This won't shock you, but it can:

- **Start fires** — A short circuit on a 20A bed heater line generates serious heat
- **Melt wires** — Undersized wiring gets hot under load
- **Damage components** — Reverse polarity kills electronics instantly

**Wire sizing matters:**
| Component | Minimum Wire Gauge (24V) |
|-----------|--------------------------|
| Bed heater | 16 AWG / 1.5mm² |
| Hotend heater | 22 AWG / 0.5mm² |
| Motors | 22 AWG / 0.5mm² |
| Thermistors | 26 AWG / 0.14mm² |

When in doubt, go one size thicker.

### Grounding and Static

- **Ground yourself** before touching electronics — Touch a grounded metal object first
- **Don't work on carpet** in socks — Static discharge kills components
- **Handle boards by edges** — Don't touch chips or traces

---

## Burn Hazards

### Hotend

The E3D V6 hotend operates at 190-285°C. At these temperatures:

- **Instant burns** — Contact causes immediate tissue damage
- **Radiant heat** — You can feel it from centimeters away
- **Thermal mass** — Takes 15-20 minutes to cool to safe temperatures

**After turning off the hotend, wait for it to cool before touching anything nearby.**

### Heated Bed

Bed temperatures range from 50°C (PLA) to 110°C (ABS):

- **50-60°C** — Uncomfortable but not immediately damaging
- **70-85°C** — Will burn with sustained contact
- **100°C+** — Instant burn, blistering

**The bed stays hot longer than the hotend** due to its thermal mass. Don't assume it's safe because the display shows "heating off."

### Extruded Filament

Freshly extruded plastic is at hotend temperature. It can:

- **Stick to skin** — Molten plastic adheres and continues burning
- **Drip unpredictably** — During filament changes or oozing
- **Fling during failures** — Spaghetti prints can throw hot strands

Don't grab at prints while they're still hot. Don't try to catch falling filament.

---

## Fire Hazards

### Thermal Runaway

If a thermistor fails or comes loose, the firmware may not know the heater is already at temperature. It keeps heating. Things melt. Things catch fire.

**Klipper has thermal runaway protection built in.** Make sure it's enabled and configured:

```ini
[heater_bed]
max_temp: 120

[extruder]
max_temp: 300
```

Don't disable safety features to "fix" false alarms. Find the actual problem.

### Unattended Operation

Most 3D printer fires happen when no one is watching:

- **Don't leave prints running overnight** until you trust the machine
- **Don't run prints while away from home** until you've done many supervised prints
- **Consider a smoke detector** near the printer
- **Consider a fire-resistant enclosure surface** if building an enclosure

A camera isn't a substitute for being there. By the time you see flames on a webcam, it's too late.

### Flammable Materials

- **Keep flammable liquids away** — IPA, acetone, contact cleaner
- **No loose paper or fabric** near the printer
- **Acetone vapour is extremely flammable** — Don't use acetone smoothing near ignition sources

---

## Mechanical Hazards

### Pinch Points

The printer has moving parts that don't know your fingers are there:

- **Belts and pulleys** — Can trap fingers, hair, loose clothing
- **Lead screws** — Z-axis screws will not stop for you
- **Gears** — Extruder gears grip hard enough to extrude plastic; they'll grip your skin too

**Keep hands clear during operation.** Tie back long hair. Don't wear dangling jewelry or loose sleeves near the printer.

### Unexpected Movement

- **Homing is dangerous** — The machine moves to find its limits without knowing where anything is
- **Don't reach in during operation** — Even if it looks stopped, a G-code command might move it
- **Emergency stop** — Know where it is, know how to use it (power switch, Klipper emergency stop)

---

## Tool Safety During Build

Building Amalgam involves tools that can injure you:

### Cutting and Drilling

- **Wear safety glasses** — Drilling MDF throws particles; cutting threaded rod throws metal chips
- **Secure your workpiece** — Don't hand-hold parts while drilling
- **Deburr cut ends** — Freshly cut threaded rod and metal have sharp edges
- **Utility knives cut toward the holder** — Cut away from your body

### Cutting G10/FR4 (Build Plate)

If you're cutting G10 (Garolite/FR4) for a replacement build plate, take extra precautions. G10 is fiberglass-reinforced epoxy—the dust contains fine glass particles that irritate lungs, skin, and eyes.

- **Work outdoors or in a very well-ventilated area** — Not in your living space
- **Wear an N95/P2 mask minimum** — Fibreglass dust is a respiratory irritant
- **Wear safety glasses** — Glass particles and eyes don't mix
- **Wear long sleeves or coveralls** — Fibreglass on bare skin causes itching
- **Use a cutting method that minimizes dust** — Score-and-snap or wet cutting is better than power sanding
- **Clean up thoroughly** — Vacuum the area; don't sweep (spreads particles into the air)
- **Wash hands and arms after** — Soap and water, scrub well
- **Wash clothes separately** — Fibreglass particles transfer to other fabrics

If you're having a supplier cut G10 to size, you avoid this entirely. Worth the extra few dollars.

### Soldering and Heat Inserts

- **Soldering irons are 300-400°C** — Same burn hazard as hotends
- **Heat insert tips stay hot** — Don't set them down on flammable surfaces
- **Ventilate solder fumes** — Flux smoke isn't good for you
- **Let joints cool before touching** — Solder is still liquid-hot for several seconds

### Adhesives

- **Cyanoacrylate (super glue)** — Bonds skin instantly; acetone removes it (carefully)
- **Epoxy** — Skin sensitizer with repeated exposure; use gloves
- **Thread locker** — Not particularly hazardous but read the label anyway

### Cleaning Printed Parts

- **Deburring knives are sharp** — Cut away from yourself
- **Dremel cutoff wheels can shatter** — Wear eye protection
- **Support removal** — Flush cutters can slip; keep fingers clear

---

## Fumes and Ventilation

### During Printing

| Filament | Ventilation Needed |
|----------|-------------------|
| **PLA** | Minimal — low emissions, generally safe |
| **PETG** | Minimal — slight odor, not concerning |
| **TPU** | Low — some people find the smell unpleasant |
| **ABS** | **Yes** — styrene emissions; print in ventilated area or enclosure with extraction |

**If you're running donor PTFE-lined hotends** (not the recommended V6): PTFE breaks down above 250°C and releases toxic fumes. Don't push PTFE hotends past their limits.

### During Build

- **MDF dust** — Contains formaldehyde binders; wear a dust mask when cutting
- **Solder flux** — Ventilate or use a fume extractor
- **Contact cleaner** — Use in ventilated areas; don't breathe propellants

---

## Environment and Placement

- **Stable surface** — The printer should not wobble, tip, or fall
- **Away from edges** — A print failure shouldn't knock the machine off a table
- **Clear surroundings** — 30cm clearance from walls and flammable materials
- **Dry location** — Electronics and water don't mix
- **Accessible power** — You should be able to reach the plug quickly
- **Not in direct sunlight** — UV degrades printed parts; heat causes dimensional issues

---

## Children and Pets

- **Supervise children** around operating printers
- **Hot surfaces remain hot** after printing stops
- **Small parts are choking hazards** — Nozzles, screws, bearings
- **Cats love warm beds** — Seriously, keep pets away from heated beds
- **Curious fingers and paws** find moving parts fascinating

The printer doesn't know the difference between a print and a finger. Neither does a toddler.

---

## Summary: The Non-Negotiables

1. **Inspect all donor wiring** — Replace anything questionable
2. **Don't disable thermal runaway protection** — Ever
3. **Don't touch hot things** — Hotend, bed, fresh prints
4. **Don't reach into moving machinery** — Wait for it to stop
5. **Supervise until you trust the machine** — No overnight prints on day one
6. **Wear safety glasses when cutting and drilling** — Eyes don't heal
7. **Keep a fire extinguisher accessible** — And know how to use it

---

## First Aid Basics

**For burns:**
1. Cool under running water for 20 minutes
2. Don't apply ice, butter, or creams
3. Cover with clean, non-fluffy material
4. Seek medical attention for serious burns

**For electrical shock:**
1. Don't touch the person if they're still in contact with the source
2. Disconnect power if safe to do so
3. Call emergency services
4. Begin CPR if trained and the person is unresponsive

**For cuts:**
1. Apply pressure with clean cloth
2. Elevate if possible
3. Seek medical attention for deep cuts or if bleeding won't stop

---

## Final Thought

None of this is meant to make you paranoid. It's meant to make you aware. Thousands of people build and operate DIY printers without incident—because they respect what the machine can do.

Build carefully. Inspect thoroughly. Don't rush.

And seriously, replace that sketchy wiring.

---

*This document covers common hazards but isn't exhaustive. Use common sense. If something feels unsafe, it probably is.*
