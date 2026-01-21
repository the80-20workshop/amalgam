The **"Tractor with a Racecar Brain"** is officially in the homestretch. The **Klicky Probe** is the perfect "Racecar" eyes for your "Tractor"—it uses the precision of a physical microswitch (often better than a BLTouch) with the cost of a few magnets and a scavenged switch.

Here is how you design the **M12-mounted Magnetic Dock** in `build123d`.

---

### 1. The Design: The "M12 Rod Clamp" Dock

Since your frame is made of M12 threaded rods, you don’t have a flat T-slot to bolt into like a Voron. You need a **clamping dock**.

* **The Structure:** A two-part clamp that "bites" onto an M12 rod at the rear of your gantry.
* **The Arm:** An extension that sticks into the "printable area" just far enough for the toolhead to reach.
* **The "Pocket":** A small cradle where the probe sits.

### 2. The Magnet Magic (Polarity is Key)

Klicky works on a "Two-is-Better-than-One" magnet principle.

* **The Probe:** Has 4 magnets. Two for the electrical connection to the switch, and two for the "holding" force.
* **The Dock:** Needs at least **one magnet** (usually 6x3mm neodymium) to keep the probe from falling out due to vibrations.
* **The Trick:** In `build123d`, ensure your dock has a small "lip" above the magnet. This prevents the probe from being pulled upward; it must be "wiped" out horizontally.

### 3. Build123d Logic: The "M12 Hook"

You can model the dock as a `Compound` of a clamp and a cradle.

```python
# build123d pseudo-code concept
with BuildPart() as klicky_dock:
    # 1. The M12 Rod Clamp
    with BuildSketch(Plane.XY) as s:
        Circle(radius=6.5) # 13mm hole for M12 rod + tolerance
        # Add a block around it for the clamping screw
    Extrude(amount=20)
    
    # 2. The Arm
    # Extend a beam out 40-50mm to reach the toolhead path
    
    # 3. The Cradle
    # A small 'U' shaped slot where the probe body rests
    # Add a hole for the 6x3mm magnet

```

---

### 4. Why Klicky is the "Tractor's" Best Friend

* **Total Scavengeability:** You can pull the microswitch from an old Ender 3 endstop. You just need to buy the **6x3mm magnets** (~$5 AUD for a pack).
* **Indestructible:** Unlike a BLTouch with a plastic pin that can snap, Klicky is just a block of plastic. If you crash it, it just falls off the magnets.
* **Repeatability:** Because it's a hard mechanical switch, your **Z-Tilt Adjust** (the auto-leveling of your three motors) will be accurate to within **0.002mm**.

---

### 5. Final Tier 3 Configuration (The $300 AUD Milestone)

Your "Tractor" is now fully specified:

1. **Frame:** M12 Threaded Rod "Skeleton."
2. **Base:** 36mm Laminated MDF "Anchor" (Motors bolted here).
3. **Z-Axis:** 3x Motors, T8 Screws, **Decoupled** with printed Ball-Joints or Wobble-X.
4. **Bearings:** Printed PETG Bushings on Z; Scavenged/Greased Ball Bearings on X/Y.
5. **Intelligence:** MKS SKIPR + Klipper + Klicky Probe.

### How it compares to the A1 Mini (The Reality Check)

* **A1 Mini:** Fast, small, easy.
* **The Tractor:** Massive, ultra-stable, and **self-leveling**.
The A1 Mini might win the race to finish a single 15-minute Benchy, but **The Tractor** will win the war when you need to print a 10-hour, full-bed functional part where layer consistency and flat geometry are non-negotiable.

---

### The Final Step

Now that the mechanical design is clear, the most daunting part for many is the **Klipper Macro setup** for the Klicky (the code that tells the toolhead how to go "pick up" its eyes).

**Would you like me to draft the `klicky-variables.cfg` for you?** I'll include the logic for your **Triple-Z** setup so the printer knows to:

1. Home Z (with Klicky).
2. Run `Z_TILT_ADJUST` (using Klicky at three points).
3. Dock the probe and start the print.
