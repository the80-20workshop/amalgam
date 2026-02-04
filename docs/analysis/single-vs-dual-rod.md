# Single vs Dual Rod Analysis: Why Single Rods Don't Work

## 1. Purpose

Some budget i3 clones use **single smooth rods** per axis instead of dual rods. This analysis quantifies why single-rod motion systems are not supported in Amalgam and what happens if you try to use one anyway.

**Bottom line:** Single rods have ~4× more deflection AND cannot resist rotation. Don't use them.

---

## 2. The Two Problems

### 2.1 Problem 1: Deflection

A single rod carries the entire load, not half of it.

### 2.2 Problem 2: Rotation

A single rod cannot resist torque around its axis. The carriage can pivot, causing:
- Nozzle angle variation
- Layer misalignment
- Inconsistent extrusion width

Dual rods solve this by creating a **moment arm** — the spacing between rods resists rotation.

---

## 3. Deflection Comparison

### 3.1 Beam Deflection Formula

For a simply supported beam with central point load:

```
δ = F × L³ / (48 × E × I)
```

### 3.2 Load Distribution

| Configuration | Load per Rod | Relative Deflection |
|--------------|--------------|---------------------|
| Dual rods | F/2 | 1× (baseline) |
| Single rod | F | 2× |

But wait — it gets worse.

### 3.3 The Stiffness Penalty

With dual rods, both rods deflect together, sharing the load. The **effective stiffness** of the system is:

```
k_dual = 2 × k_single_rod
```

Total system deflection comparison:

| Configuration | System Stiffness | Deflection Ratio |
|--------------|------------------|------------------|
| Dual 8mm rods | 2× single rod | 1× (baseline) |
| Single 8mm rod | 1× | 2× |
| Single 10mm rod | 2.4× of 8mm | 0.83× |
| Single 12mm rod | 5× of 8mm | 0.4× |

### 3.4 Numeric Example (350mm span, 600g toolhead)

| Configuration | Mid-Span Deflection |
|--------------|---------------------|
| Dual 8mm | 0.065 mm |
| Single 8mm | **0.130 mm** |
| Single 10mm | 0.054 mm |
| Single 12mm | 0.026 mm |

**Interpretation:** A single 8mm rod has 2× the deflection of dual 8mm. You'd need a single 10mm rod to match dual 8mm performance — but rotation is still unsolved.

---

## 4. Rotation Analysis

### 4.1 The Rotation Problem

Even with zero deflection, a single rod cannot resist torque. When the hotend applies force (during printing, acceleration, or retraction), the carriage rotates around the rod axis.

### 4.2 Sources of Rotation Torque

| Source | Direction | Magnitude |
|--------|-----------|-----------|
| Bowden tube push | Variable | Low |
| Direct drive motor torque | Around rod | Medium |
| Acceleration (offset mass) | Depends on geometry | High |
| Part adhesion (peel force) | Tilts nozzle | Medium |

### 4.3 Why Dual Rods Resist Rotation

With dual rods separated by distance `d`:

```
Resisting moment = F_bearing × d
```

Where F_bearing is the reaction force at each bearing.

For dual rods with 45mm spacing (typical):
- Even small bearing preload creates significant rotation resistance
- Carriage is constrained to translate, not rotate

For a single rod:
- Rotation resistance = 0 (theoretically)
- In practice, limited by bearing friction (unreliable)

### 4.4 Practical Effect

| Configuration | Rotation Resistance | Nozzle Stability |
|--------------|--------------------|--------------------|
| Dual rods, 45mm spacing | High | Excellent |
| Dual rods, 25mm spacing | Medium | Good |
| Single rod + secondary guide | Low-Medium | Acceptable* |
| Single rod only | Near zero | **Unacceptable** |

*Some single-rod designs add a secondary guide (rail, V-slot, or bearing block) to resist rotation. This works but adds complexity and cost.

---

## 5. Single Rod Workarounds

### 5.1 Add a Secondary Constraint

Some designs address single-rod rotation by adding:
- A parallel guide rail
- A V-slot wheel on one side
- A second bearing block on a stationary rod

**Problem:** This costs money and complexity. At that point, just use dual rods.

### 5.2 Use a Larger Single Rod

A 12mm single rod has less deflection than dual 8mm, but:
- Still can't resist rotation
- 12mm rods are heavier and harder to source
- Bearings (LM12UU) are larger and costlier

### 5.3 Accept the Limitations

If you insist on single 8mm rods:
- Limit acceleration to <3000 mm/s²
- Use Bowden extrusion (reduces motor torque on carriage)
- Accept ~0.1mm dimensional variation
- Print speed limited to ~50mm/s for quality

---

## 6. Why Amalgam Requires Dual Rods

The Amalgam specification requires dual rods because:

1. **Deflection is halved** — dual rods share the load
2. **Rotation is constrained** — carriage can only translate
3. **Scavenging is easier** — dual-rod donors are common (Anet A8, Wanhao, Prusa clones)
4. **Input Shaping works better** — predictable, consistent motion
5. **Direct drive is viable** — can handle NEMA17 + Pitan mass

---

## 7. Decision Matrix

| Your Donor Has | Recommendation |
|----------------|----------------|
| Dual 8mm smooth rods | **Use them** — Scaffold or Lathe path |
| Single 8mm + guide rail | **Maybe** — test stability before building |
| Single 8mm only | **Don't use** — buy rods or find different donor |
| V-slots + wheels | **Use them** — Mill path (rotation constrained by wheels) |

### 7.1 Cost to Fix Single-Rod Donors

If your donor has single rods:

| Fix | Cost | Result |
|-----|------|--------|
| Buy 8× 8mm smooth rods | ~$40-50 | Dual rod system |
| Buy 8× LM8UU bearings | ~$20-30 | Complete motion system |
| Total | ~$60-80 | Equivalent to dual-rod donor |

**Alternative:** Sell single-rod donor, buy dual-rod donor. Often cheaper and less hassle.

---

## 8. Summary

| Factor | Dual 8mm Rods | Single 8mm Rod |
|--------|---------------|----------------|
| Deflection | 0.065mm | 0.130mm (2×) |
| Rotation resistance | High | Near zero |
| Max safe acceleration | ~8000 mm/s² | ~3000 mm/s² |
| Direct drive viable? | Yes | No (Bowden only) |
| Recommended? | **Yes** | **No** |

Single rods are not supported because they can't provide the motion quality Amalgam targets. If your donor has single rods, either upgrade the motion system or find a better donor.

---

*"Two rods are not twice as good — they're four times as good. Plus they actually resist rotation."*
