# Neo-Darwin: Power Supply Configurations

## Overview

Neo-Darwin requires power for seven stepper motors (1×X, 2×Y, 3×Z, 1×E), a hotend, heated bed, control boards, and cooling fans. A single scavenged PSU from a donor printer (typically 150W–250W) is often insufficient. This document covers safe configurations for single and dual PSU setups.

---

## Power Budget Analysis

### Component Power Requirements

| Component | Power Draw | Notes |
|-----------|------------|-------|
| Control Boards (×2) | ~10W | Logic, drivers idle |
| Cooling Fans | ~10W | Hotend, part cooling, electronics |
| Stepper Motors (×7) | ~70W | Peak during rapid moves |
| Hotend (E3D V6) | 40W | 40W heater cartridge |
| Heated Bed (235×235) | 150W–220W | Largest single load |
| **Total** | **~280W–350W** | At full operation |

### Typical Scavenged PSU Ratings

| Donor Printer | Voltage | Wattage | Sufficient? |
|---------------|---------|---------|-------------|
| Anet A8 | 12V | 240W | ❌ No (12V system) |
| Ender 3 (original) | 24V | 270W | ⚠️ Marginal |
| Ender 3 Pro/V2 | 24V | 350W | ✅ Yes (barely) |
| Prusa MK2 | 12V | 240W | ❌ No (12V system) |
| Prusa MK3 | 24V | 240W | ⚠️ Marginal |
| CR-10 | 12V/24V | 360W–500W | ✅ Yes (check voltage) |

**Conclusion:** Most single scavenged PSUs are marginal or insufficient. Dual PSU configuration is recommended.

---

## ⚠️ CRITICAL SAFETY WARNINGS

### The Voltage Trap (12V vs 24V)

**This is the most dangerous mistake in scavenger builds.**

If your donor printer is older (Prusa MK2, Anet A8, early CR-10), it likely uses a **12V system**.

**The Danger:** Connecting a 12V component to 24V doesn't double the power—it **quadruples** it.

```
Power = Voltage² / Resistance

12V bed at 12V: P = 144/R = 150W (normal)
12V bed at 24V: P = 576/R = 600W (FIRE HAZARD)
```

**What Will Happen:**
- Connectors will melt
- MOSFETs will explode
- Heating traces may crack and arc
- **Fire is likely**

**Before Connecting Anything:**
1. Check labels on heated bed (underside)
2. Check capacitor voltage ratings on boards
3. If it says "12V" → Do NOT connect to 24V PSU

### Capacitor Voltage Ratings

Scavenged control boards have electrolytic capacitors (cylindrical components).

**The Check:** Look at the voltage rating printed on the capacitor.
- If it says "16V" → Will explode on 24V
- If it says "25V" or "35V" → Safe for 24V

**If capacitors are underrated:** Replace them or use that board only with a 12V PSU.

---

## Configuration 1: Single PSU (Simple)

### When This Works

- PSU is 350W+ at 24V
- Heated bed is 24V compatible
- All components match PSU voltage

### Wiring Diagram

```
┌─────────────────────────────────────────────────┐
│                 MAINS AC INPUT                   │
│            [Fused IEC Inlet + Switch]            │
└─────────────────────┬───────────────────────────┘
                      │
                      ▼
              ┌───────────────┐
              │    PSU 24V    │
              │    350W+      │
              └───┬───────┬───┘
                  │       │
               (+24V)   (GND)
                  │       │
       ┌──────────┴───────┴──────────┐
       │                             │
       ▼                             ▼
┌─────────────┐              ┌─────────────┐
│   Board 1   │──── USB ────│   Board 2   │
│ (X,Y1,Y2,E) │              │ (Z1,Z2,Z3)  │
└─────────────┘              └─────────────┘
       │                             │
       ▼                             ▼
   [Hotend]                     [Heatbed]
   [Fans]                       [Z-Motors]
```

### Limitations

- Single point of failure
- May brownout during bed heating + rapid moves
- Limited upgrade path

---

## Configuration 2: Dual PSU (Recommended)

### Why Dual PSU?

1. **Load Distribution:** Each PSU handles a manageable load
2. **Isolation:** Electrical noise from bed heater separated from motion system
3. **Redundancy:** If one PSU is marginal, the other compensates
4. **Scavenger Reality:** Two 200W PSUs are easier to find than one 400W

### The Three Golden Rules

#### Rule 1: Common DC Ground (MANDATORY)

Both control boards must share the same reference for "zero volts."

**The Problem:** Without common ground, the "0V" on Board A might be 0.5V different from Board B. This causes:
- USB communication errors
- Data corruption
- Potential damage to Raspberry Pi USB ports

**The Fix:** Run a thick wire (14–16 AWG) between the Negative (−V or COM) terminals of both PSUs.

```
PSU 1 [-V] ════════════════════ PSU 2 [-V]
              (Common Ground)
```

#### Rule 2: Never Parallel the Positives (CRITICAL)

**NEVER connect the +V terminals of two PSUs together.**

**Why:** No two PSUs output exactly the same voltage.
- PSU 1 might output 24.1V
- PSU 2 might output 23.9V

If connected, they will "fight"—the higher voltage PSU tries to charge the lower one. This causes:
- Excessive current flow between PSUs
- Overheating
- PSU failure
- Potential fire

**The Fix:** Keep positive circuits completely isolated.
- Board A gets +V ONLY from PSU 1
- Board B gets +V ONLY from PSU 2

#### Rule 3: Single AC Switch (SAFETY)

Both PSUs must turn on and off together.

**The Risk:** If one PSU is on and the other is off while the printer tries to move:
- "Back-powering" through stepper motors
- Control board damage
- Unpredictable behavior

**The Fix:** Wire both PSUs to a single fused AC inlet and power switch.

### Dual PSU Wiring Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      MAINS AC INPUT                          │
│               [Fused IEC Inlet + Switch]                     │
│                    [Emergency Stop]                          │
└─────────────────────────┬───────────────────────────────────┘
                          │
            ┌─────────────┴─────────────┐
            │     Terminal Block        │
            │   (Live/Neutral Split)    │
            └─────┬───────────────┬─────┘
                  │               │
                  ▼               ▼
          ┌───────────┐   ┌───────────┐
          │   PSU 1   │   │   PSU 2   │
          │   24V     │   │   24V     │
          └─┬───────┬─┘   └─┬───────┬─┘
            │       │       │       │
         (+24V)  (GND)   (+24V)  (GND)
            │       │       │       │
            │       └───────┴───────┤  ← COMMON GROUND
            │           ║           │
            │           ║           │
    ┌───────┴───┐       ║       ┌───┴───────┐
    │  Board 1  │       ║       │  Board 2  │
    │(X,Y1,Y2,E)│       ║       │(Z1,Z2,Z3) │
    └─────┬─────┘       ║       └─────┬─────┘
          │             ║             │
          ▼             ║             ▼
      [Hotend]          ║         [Heatbed]
      [Fans]            ║         [Z-Motors]
                        ║
              (Common Ground Bus)

    ⚠️ +24V lines NEVER connected between PSUs
```

### Recommended Load Distribution

| PSU | Board | Components | Rationale |
|-----|-------|------------|-----------|
| PSU 1 | Board 1 | X, Y1, Y2, Extruder, Hotend, Fans | "Fast" motion, lower power |
| PSU 2 | Board 2 | Z1, Z2, Z3, Heatbed | "Slow" motion, high power |

**Why This Split:**
- Heatbed electrical noise isolated from X/Y signals
- High-current bed circuit on dedicated PSU
- Z-motors move slowly, less sensitive to noise

---

## Configuration 3: Mixed Voltage (12V + 24V)

### When This Is Necessary

- One donor is 12V (older printer)
- One donor is 24V (newer printer)
- You have a 12V heated bed

### The External MOSFET Solution

Use the 12V PSU exclusively for the heated bed, controlled by an external MOSFET triggered by the 24V board.

```
┌─────────────────────────────────────────────────────────────┐
│                      MAINS AC INPUT                          │
│               [Fused IEC Inlet + Switch]                     │
└─────────────────────────┬───────────────────────────────────┘
                          │
            ┌─────────────┴─────────────┐
            │                           │
            ▼                           ▼
    ┌───────────────┐           ┌───────────────┐
    │    PSU 1      │           │    PSU 2      │
    │    24V        │           │    12V        │
    └───┬───────┬───┘           └───┬───────┬───┘
        │       │                   │       │
     (+24V)  (GND)               (+12V)  (GND)
        │       │                   │       │
        │       └───────────────────┴───────┤  ← COMMON GROUND
        │                   ║               │
        ▼                   ║               ▼
┌─────────────┐             ║       ┌───────────────┐
│   Board 1   │─────────────╫──────→│ External      │
│  (All MCU)  │  Signal     ║       │ MOSFET        │
└─────────────┘  (3.3V)     ║       └───────┬───────┘
        │                   ║               │
        ▼                   ║               ▼
    [Hotend]                ║         [12V Heatbed]
    [Steppers]              ║
    [Fans]                  ║
                            ║
                  (Common Ground Bus)
```

### External MOSFET Notes

- Cost: ~$5–10 (HA210N06 module or similar)
- Triggered by low-current signal from main board
- Switches high-current 12V to bed
- **Must share common ground with 24V system**

### ⚠️ Do NOT Use Software PWM Limiting

Some guides suggest using `max_power: 0.25` in Klipper to run a 12V bed on 24V.

**Why This Is Dangerous:**
- If Klipper crashes with the pin HIGH, bed goes to 400% power
- No hardware protection
- Fire risk

**Always use hardware voltage matching, not software limiting.**

---

## Configuration 4: Server PSU Scavenge

### The "Free Power" Option

Server PSUs from old HP, Dell, or IBM rack servers are often available free from e-waste centers.

**Common Types:**
- HP "Common Slot" PSUs (750W–1200W)
- Dell PowerEdge PSUs (500W–1100W)

### Server PSU Characteristics

| Feature | Value | Notes |
|---------|-------|-------|
| Voltage | 12V DC | Single rail, high current |
| Power | 500W–1200W | Massive headroom |
| Efficiency | 80%+ (Gold/Platinum) | Low heat, quiet |
| Cost | Free–$20 | E-waste goldmine |

### The 12V Limitation

Server PSUs output 12V, but Neo-Darwin prefers 24V.

**Options:**

1. **Use 12V System:** If all your components are 12V compatible
2. **Series Two PSUs:** Connect two 12V PSUs in series for 24V
3. **DC-DC Boost:** Use a boost converter (less efficient)

### Series Connection for 24V

```
┌─────────────┐      ┌─────────────┐
│  Server     │      │  Server     │
│  PSU 1      │      │  PSU 2      │
│  12V        │      │  12V        │
└──┬──────┬───┘      └──┬──────┬───┘
   │      │             │      │
(+12V)  (GND)        (+12V)  (GND)
   │      │             │      │
   │      └─────────────┘      │
   │            │              │
   │        (JOINED)           │
   │      This becomes         │
   │      the "middle"         │
   │                           │
   ▼                           ▼
(+24V)                       (GND)
   │                           │
   └─────── TO PRINTER ────────┘
```

**Critical:** The "joined" point (PSU1 GND to PSU2 +12V) must be isolated from chassis ground.

---

## USB Back-Powering Prevention

### The Problem

When control boards are connected to the Klipper host (Raspberry Pi) via USB, the USB cable can try to power the board through the 5V pin.

**The Risk:**
- If PSUs are off but Pi is on, board draws power through USB
- USB traces are rated for ~500mA, boards may try to draw more
- Can fry the Pi's USB port or the board's voltage regulator

### The Fix: 5V Pin Tape Trick

1. Look inside the USB-A connector (the end that plugs into Pi)
2. Identify the 5V pin (usually leftmost or rightmost, red wire)
3. Place a small piece of electrical tape over just that pin
4. Data pins (D+ and D−) remain connected

```
USB-A Connector Pin Layout:
┌─────────────────────┐
│  [5V] [D-] [D+] [GND]  │
│   ▲                    │
│   │                    │
│  TAPE THIS PIN         │
└─────────────────────────┘
```

**Alternative:** Some boards have a jumper to disable USB power input—check your board's documentation.

---

## Wiring Best Practices

### Ferrules Are Mandatory

Scavenged wires are often:
- Brittle from age
- Frayed at the ends
- Prone to loose strands

**The Risk:** A loose strand can bridge terminals, causing shorts, arcing, or fire.

**The Fix:** Use crimped ferrules on every wire going into a screw terminal.

- Ferrule crimping kit: ~$15–25
- Prevents strand separation
- Creates secure, repeatable connections

### Wire Gauge Guidelines

| Circuit | Minimum Gauge | Notes |
|---------|---------------|-------|
| Heated Bed | 14 AWG | High current, longest run |
| Hotend | 18 AWG | Moderate current |
| Stepper Motors | 22 AWG | Low current |
| Logic/Signals | 24 AWG | Very low current |
| Common Ground (Dual PSU) | 14–16 AWG | Must handle fault current |

### Earth/Ground Safety

**Mains Earth (Green/Yellow) must be connected to:**
- Metal frame of both PSUs
- Metal frame of printer (if any)
- Heated bed frame (if metal)

**This protects you if a wire shorts to the frame.**

---

## Klipper Multi-MCU Configuration

### Basic Dual-Board Setup

In `printer.cfg`:

```ini
[mcu]
serial: /dev/serial/by-id/usb-board_1_xxxxx

[mcu aux]
serial: /dev/serial/by-id/usb-board_2_xxxxx
```

### Pin Addressing

For the primary MCU:
```ini
[stepper_x]
step_pin: PB13
```

For the secondary MCU:
```ini
[stepper_z]
step_pin: aux:PB13
```

### Timing Synchronization

Klipper automatically synchronizes timing between MCUs. The common ground connection is essential for this to work reliably.

---

## Pre-Power Checklist

Before turning on your Neo-Darwin for the first time:

### Voltage Verification

- [ ] Check heated bed voltage rating (12V or 24V)
- [ ] Check capacitor voltage ratings on all boards
- [ ] Verify all components match PSU voltage

### Wiring Verification

- [ ] Common ground connected between PSUs (if dual)
- [ ] Positive rails are isolated (never paralleled)
- [ ] All ferrules crimped properly
- [ ] No loose strands visible
- [ ] Earth connected to frames

### Safety Verification

- [ ] Single AC switch controls all PSUs
- [ ] Fused inlet installed
- [ ] USB 5V pins taped (if needed)
- [ ] Emergency stop accessible

### Smoke Test Procedure

1. Connect PSU(s) to mains, switch OFF
2. Turn on—listen for capacitor charging (brief hum is normal)
3. Check for smoke, burning smell, or sparks
4. Measure output voltages with multimeter
5. Verify common ground with continuity test
6. Connect boards one at a time
7. Power cycle between each connection

---

## Troubleshooting

### Symptom: USB Disconnects Randomly

**Likely Cause:** Common ground not connected or poor connection

**Fix:** 
- Verify thick wire between PSU negatives
- Check for corrosion on terminals
- Use star-ground topology if multiple grounds

### Symptom: Heated Bed Heats Slowly

**Likely Cause:** PSU voltage sag under load

**Fix:**
- Check PSU wattage vs. actual load
- Use dedicated PSU for bed
- Check wire gauge (undersized wires drop voltage)

### Symptom: Steppers Skip or Lose Position

**Likely Cause:** Voltage brownout during bed heating

**Fix:**
- Separate bed onto different PSU
- Reduce stepper current slightly
- Add bulk capacitor near stepper drivers

### Symptom: Board Won't Power On

**Likely Cause:** 
- 12V board connected to 24V (check for damage)
- USB back-powering with low-current source

**Fix:**
- Verify voltage compatibility
- Apply 5V tape trick
- Check for blown fuses or burned components

---

## Summary: Recommended Configuration

For Neo-Darwin "Tier 0" scavenger build:

| Setup | Recommendation |
|-------|----------------|
| **PSU Count** | Two (from donor printers) |
| **Voltage** | 24V preferred, mixed 12V/24V acceptable |
| **PSU 1** | Board 1: X, Y1, Y2, Extruder, Hotend, Fans |
| **PSU 2** | Board 2: Z1, Z2, Z3, Heated Bed |
| **Common Ground** | 14–16 AWG between PSU negatives |
| **AC Side** | Single fused inlet, single switch |
| **Safety** | Ferrules, earth bonding, 5V tape trick |

**The Golden Rules:**
1. ✅ Common DC Ground (tie negatives together)
2. ❌ Never parallel positives
3. ✅ Single AC switch for all PSUs
4. ✅ Verify voltage compatibility before connecting

---

## References

- Klipper Multi-MCU Documentation
- Meanwell PSU Specifications
- RepRap Wiki: Power Supply
- 3D Printing Community Safety Guidelines
