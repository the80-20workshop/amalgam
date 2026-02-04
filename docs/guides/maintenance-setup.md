# Mechanical Setup & Maintenance Guide

## 1. Purpose

This guide covers the practical setup and ongoing maintenance for Amalgam. Unlike the analysis documents (which explain *why*), this guide explains *how* — step-by-step procedures for keeping your printer running well.

**Scope:** Frame-agnostic procedures that apply to all paths (Scaffold, Mill, Lathe), with path-specific sections where needed.

---

## 2. Initial Mechanical Setup

### 2.1 Frame Squaring (All Paths)

Before any motion system work, verify your frame is square.

**Tools needed:**
- Machinist square or large framing square
- Measuring tape or calipers
- Feeler gauges (optional)

**Procedure:**

1. Place printer on flat, level surface
2. Measure diagonals of the frame (corner to corner)
   - Difference should be <2mm for a 300mm frame
   - If larger, adjust frame joints before proceeding
3. Check vertical members with square against MDF base
   - Should be 90° ±0.5°
4. For Scaffold path: check M10 rod parallelism
   - Measure spacing at top and bottom
   - Difference should be <1mm

**Why it matters:** A twisted frame causes binding, uneven wear, and dimensional inaccuracy that no amount of calibration can fix.

---

### 2.2 Smooth Rod Installation (Scaffold, Lathe)

**Tools needed:**
- Flat glass or granite surface plate
- Soft mallet (optional)
- Isopropyl alcohol and lint-free cloth

**Procedure:**

1. **Inspect rods** — Roll each rod on flat glass
   - Watch for wobble indicating bend
   - Bent rods: discard or straighten (difficult)

2. **Clean rods** — Wipe with IPA, remove all grease and debris

3. **Install rod holders** — Ensure holders are aligned and secure
   - Both holders for a rod should be in the same plane

4. **Insert rods** — Slide in gently, don't force
   - If binding, check holder alignment

5. **Check parallelism** — Measure rod spacing at multiple points
   - Maximum deviation: 0.5mm over full length

6. **Light lubrication** — Apply thin film of PTFE lubricant or light machine oil
   - Wipe excess — rod should not look wet

---

### 2.3 V-Slot Wheel Setup (Mill)

**Tools needed:**
- Eccentric nut wrench (8mm typically)
- Piece of paper

**Procedure:**

1. **Identify eccentric nuts** — Usually one per wheel set (bottom or back wheel)
   - The eccentric has an off-center hole

2. **Loosen all eccentric nuts** — Wheels should spin freely

3. **Position carriage** — Place on V-slot rail

4. **Adjust first wheel set:**
   - Tighten eccentric nut slowly while checking wheel contact
   - Goal: wheel touches rail with light preload
   - Test: slide piece of paper between wheel and rail
   - Correct: paper slides with slight resistance
   - Too tight: paper won't slide, or wheel won't spin freely
   - Too loose: paper slides freely, carriage wobbles

5. **Repeat for each wheel set** — Carriage should move smoothly without wobble

6. **Final check** — Push carriage along full travel
   - Should glide smoothly with consistent resistance
   - No tight spots or wobble

**Common mistakes:**
- Over-tightening (causes flat spots, premature wear)
- Under-tightening (causes wobble, poor print quality)
- Adjusting while carriage is loaded (incorrect preload)

---

### 2.4 Belt Installation and Tensioning

**Tools needed:**
- Belt tension gauge (optional but recommended)
- Zip ties (temporary holding)

**Procedure:**

1. **Route belt** — Follow your path's belt routing diagram
   - Teeth face inward on pulleys
   - Avoid twists

2. **Secure one end** — Clamp or tie to carriage

3. **Pull through** — Route around pulleys and idlers

4. **Initial tension:**
   - Pull belt taut by hand
   - Secure second end
   - Belt should "twang" when plucked (like guitar string)

5. **Measure tension** (if gauge available):
   - Target: 2-3 lbs (1-1.5 kg) deflection force
   - At mid-span, pressing ~10mm deflection

6. **Final adjustment:**
   - Too loose: sloppy motion, lost steps, ringing
   - Too tight: motor strain, bearing wear, noise
   - Just right: solid feel, clean motion, no ringing

**Check frequency:** Monthly, or if print quality degrades

---

### 2.5 Leadscrew and Z-Axis Setup

**Tools needed:**
- Level
- Calipers or ruler
- Anti-backlash nut (if equipped)

**Procedure:**

1. **Inspect leadscrews** — Check for bends, damage, contamination
   - Roll on flat surface like smooth rods
   - Clean with IPA if dirty

2. **Install anti-backlash nuts** (if used):
   - Pre-load spring to manufacturer spec
   - Don't over-tighten — causes binding

3. **Couple to motors:**
   - Use flexible couplers (not rigid)
   - Allow ~1mm axial play to prevent binding
   - Tighten set screws on motor shaft flat (if present)

4. **Check alignment:**
   - Leadscrew should spin freely when decoupled from bed
   - If binding when coupled, alignment is off

5. **Lubricate:**
   - Light grease (white lithium or PTFE)
   - Apply to threads, run up and down several times
   - Wipe excess

**Triple-Z specific:**
- All three leadscrews must be same length
- Z-tilt calibration handles minor differences
- Run Z_TILT_ADJUST after any Z-axis work

---

## 3. Periodic Maintenance

### 3.1 Maintenance Schedule

| Interval | Task | Applies To |
|----------|------|------------|
| Weekly | Visual inspection | All |
| Monthly | Belt tension check | All |
| Monthly | Eccentric nut check | Mill only |
| Monthly | Clean V-slots | Mill only |
| 3 months | Lubricate rods | Scaffold, Lathe |
| 3 months | Lubricate leadscrews | All |
| 6 months | Check bearing play | Scaffold, Lathe |
| 6 months | Check wheel wear | Mill only |
| Annually | Full mechanical inspection | All |

---

### 3.2 Monthly: Belt Tension Check

**Signs belt needs attention:**
- Ringing artifacts in prints
- Lost steps (layer shifts)
- Clicking sounds during fast moves
- Belt feels loose or too tight compared to initial setup

**Procedure:**
1. Power off printer
2. Move carriage to mid-position
3. Pluck belt and listen to pitch
   - Compare to "reference pitch" you noted during setup
   - Or use tension gauge
4. Adjust tensioner if needed
5. Re-check after adjustment

---

### 3.3 Monthly: Eccentric Nut Check (Mill)

**Signs adjustment needed:**
- Wobble in carriage (push side-to-side, check for play)
- Wheels don't spin freely
- Uneven wheel wear
- Print quality degradation

**Procedure:**
1. Power off, move carriage to accessible position
2. Try to wobble carriage perpendicular to rail
3. If play detected, tighten eccentric slightly
4. If wheels don't spin freely, loosen slightly
5. Re-test motion across full travel

---

### 3.4 Quarterly: Rod Lubrication (Scaffold, Lathe)

**Lubricant options:**
- PTFE dry lubricant (preferred — doesn't attract dust)
- Light machine oil (3-in-1, sewing machine oil)
- White lithium grease (sparingly, for harsh environments)

**Procedure:**
1. Power off, move carriage to end of travel
2. Wipe rod with lint-free cloth (remove old lube and debris)
3. Apply small amount of lubricant to cloth
4. Wipe along rod — thin, even film
5. Move carriage back and forth several times
6. Wipe any excess that accumulates at bearings

**Warning:** Over-lubrication attracts dust and creates gummy residue. Less is more.

---

### 3.5 Quarterly: Leadscrew Maintenance

**Procedure:**
1. Move bed to top of travel
2. Wipe visible leadscrew threads with cloth
3. Apply thin bead of PTFE grease or white lithium
4. Run bed up and down full travel 3-5 times
5. Wipe any excess that squeezes out

**For Triple-Z:**
- Service all three leadscrews
- Run Z_TILT_ADJUST afterward

---

### 3.6 Semi-Annual: Bearing Inspection (Scaffold, Lathe)

**Signs of bearing wear:**
- Clicking or crunching sounds
- Rough motion (not smooth glide)
- Visible play in carriage
- Witness marks on rods (shiny wear tracks)

**Procedure:**
1. Remove carriage from rods
2. Roll bearing by hand — should be smooth, not gritty
3. Inspect rod surface for wear tracks
4. If wear detected:
   - Rotate bearing 90° to use unworn section
   - Or replace bearing
5. If rod shows significant wear track:
   - Rotate rod 90° (if mounting allows)
   - Or replace rod

**IGUS bearings:** May squeak when dry — this is normal initially. If squeaking persists, ensure rod is clean (no oil — IGUS runs dry).

---

### 3.7 Semi-Annual: Wheel Inspection (Mill)

**Signs of wheel wear:**
- Flat spots (visible or felt as bumps during motion)
- Grooves in wheel surface
- Wheel doesn't spin true (wobbles)
- Increased play despite proper eccentric adjustment

**Procedure:**
1. Remove carriage from rail
2. Inspect each wheel surface visually
3. Spin wheel by hand — should spin smoothly, no wobble
4. Check for flat spots by rotating slowly
5. Replace any worn wheels
6. Re-adjust eccentric nuts after reassembly

---

## 4. Troubleshooting Common Issues

### 4.1 Binding or Stiff Motion

| Possible Cause | Check | Fix |
|---------------|-------|-----|
| Misaligned rods/rails | Parallelism measurement | Re-align mounts |
| Over-tight eccentric (Mill) | Wheel spin test | Loosen eccentric |
| Over-tight belt | Belt deflection | Loosen tensioner |
| Dry bearings (rods) | Listen for squeaking | Lubricate |
| Bent rod | Roll on glass | Replace rod |
| Debris in V-slot | Visual inspection | Clean groove |

### 4.2 Play or Wobble

| Possible Cause | Check | Fix |
|---------------|-------|-----|
| Loose eccentric (Mill) | Wobble test | Tighten eccentric |
| Worn bearings (rods) | Roll carriage, feel for play | Replace bearings |
| Worn wheels (Mill) | Visual + spin test | Replace wheels |
| Loose belt | Pluck test | Tighten belt |
| Loose rod mounts | Wiggle rod holders | Tighten fasteners |

### 4.3 Noise During Motion

| Sound | Likely Cause | Fix |
|-------|--------------|-----|
| Clicking (rhythmic) | Flat spot on wheel | Replace wheel |
| Grinding | Dry bearing or debris | Clean and lubricate |
| Squeaking (rods) | Dry LM8UU bearing | Lubricate |
| Squeaking (IGUS) | Normal break-in OR contamination | Clean rod (no oil) |
| Whining | Belt too tight | Loosen tensioner |
| Thumping | Loose pulley set screw | Tighten set screw |

### 4.4 Z-Axis Issues

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Z binding | Misaligned leadscrew | Check coupler alignment |
| Inconsistent layer height | Leadscrew backlash | Adjust anti-backlash nut |
| Z wobble (wavy walls) | Bent leadscrew | Replace leadscrew |
| Z drift | Loose coupler | Tighten set screws |
| Bed tilt after homing | Z-tilt needs calibration | Run Z_TILT_ADJUST |

---

## 5. Hotend Maintenance

### 5.1 Nozzle Changes

**Frequency:** When switching materials, or if clogs occur

**Procedure:**
1. Heat hotend to printing temp (or +20°C for stubborn clogs)
2. While hot, use wrench to loosen nozzle
   - Counter-hold heater block to prevent spinning
3. Remove nozzle completely
4. Inspect nozzle bore — replace if damaged or worn
5. Install new nozzle:
   - Thread in by hand until finger-tight
   - Heat to printing temp
   - Final tighten (1/4 turn with wrench)

**Warning:** Always tighten nozzles hot. Cold-tightening leads to leaks.

### 5.2 Heat Break Maintenance

**Signs of issues:**
- Filament grinding in extruder
- Heat creep (jams after running for a while)
- Inconsistent extrusion

**Procedure:**
1. Remove hotend from carriage
2. Heat to ~150°C, remove nozzle
3. Pull out heat break (may need heating/cooling cycles)
4. Clean inside with brass brush or drill bit (hand-turn only)
5. Inspect for damage — replace if bore is damaged
6. Apply thermal compound to threads (optional, helps heat transfer)
7. Reassemble and re-tighten nozzle hot

---

## 6. Electronics Maintenance

### 6.1 Connection Checks

**Frequency:** Annually, or if intermittent issues occur

**Procedure:**
1. Power off and unplug
2. Inspect all connectors for:
   - Corrosion (green or white deposits)
   - Loose connections
   - Melted plastic (overheating)
3. Disconnect and reconnect each connector
   - This cleans contact surfaces
4. Check screw terminals:
   - Wires should be secure, not loose
   - No exposed wire outside terminal
5. Inspect stepper cables for damage (especially at flexing points)

### 6.2 Fan Cleaning

**Frequency:** Every 3-6 months (dusty environment: monthly)

**Procedure:**
1. Power off
2. Remove fan if accessible, or clean in place
3. Use compressed air to blow out dust
   - Hold fan blade to prevent spinning (generates voltage)
4. For heavy buildup, use soft brush
5. Reinstall and verify operation

---

## 7. Documentation & Records

### 7.1 What to Record

Keep a maintenance log with:
- Date of maintenance
- What was done
- Parts replaced
- Issues found
- Measurements (belt tension, bearing play, etc.)

### 7.2 Why It Matters

- Tracks wear patterns — helps predict replacement timing
- Documents what worked — useful for troubleshooting
- Establishes baseline — "was it always like this?"

### 7.3 Simple Log Format

```
Date: 2026-01-15
Tasks: Monthly check
- Belt tension: good (no adjustment)
- Eccentric nuts: Y-axis slightly loose, tightened 1/8 turn
- Visual: no issues
Notes: None
```

---

## 8. Quick Reference Card

### Weekly (30 seconds)
- [ ] Visual check — nothing loose, no debris

### Monthly (5 minutes)
- [ ] Belt tension — pluck test
- [ ] Eccentric nuts (Mill) — wobble test
- [ ] Clean build surface

### Quarterly (15 minutes)
- [ ] Rod lubrication (Scaffold, Lathe)
- [ ] Leadscrew lubrication
- [ ] V-slot cleaning (Mill)

### Semi-Annually (30 minutes)
- [ ] Bearing/wheel inspection
- [ ] Connection check
- [ ] Fan cleaning

### Annually (1 hour)
- [ ] Full mechanical inspection
- [ ] Replace wear items as needed
- [ ] Recalibrate (Input Shaping, Z-tilt)

---

*"A well-maintained tractor outlasts a neglected racecar."*
