Yes — **Pitan is a single-drive extruder**, and your intuition about **dual-drive systems** is *fundamentally correct*. What you’re describing is not folklore; it’s real mechanical behaviour that tends to get glossed over.

Let’s separate fact from hype.

---

## 1️⃣ Is Pitan single-drive?

**Yes.**

* One driven hobbed gear
* One idler bearing (spring-loaded)
* Filament is pinched, not counter-driven

Mechanically:

* Simple
* Predictable
* Tolerant of small misalignments
* Easy to calibrate

That simplicity is a **feature**, not a weakness.

---

## 2️⃣ Dual-drive extruders: what they promise vs reality

### What dual-drive *claims* to do

* Symmetrical filament grip
* Higher pushing force
* Better flexible filament handling
* Less filament deformation

All of that is **theoretically true**.

---

### What actually happens in practice

Dual-drive extruders introduce a **gear mesh dependency** that single-drive systems simply don’t have.

#### Core problem:

You are now relying on:

* Two hobbed gears
* With matched tooth profiles
* Under load
* Across many thermal cycles
* Printed or machined separately

Any mismatch causes:

* Micro stick–slip
* Periodic torque ripple
* Slight extrusion modulation

That modulation can *absolutely* manifest as:

* faint vertical banding
* subtle surface texture changes
* inconsistent line width under certain speeds

This is why:

* Bondtech gears are *precision matched*
* Cheap dual-drive clones vary wildly
* Printed dual-drive designs are notoriously finicky

---

## 3️⃣ Why this matters *more* than people think

Even **high-quality metal gears** are not perfectly matched unless:

* cut as a matched pair
* assembled with controlled preload
* run-in together

Printed gears?

* Layer lines
* Tooth anisotropy
* Slight ovality
* Thermal creep

You *can* make them work — but:

* they require more tuning
* they’re more sensitive to wear
* they fail less gracefully

---

## 4️⃣ Single-drive has a hidden advantage

A single-drive extruder:

* Has **one torque source**
* One periodic error
* One wear pattern

Any error is:

* smoother
* easier for firmware to compensate
* easier to diagnose

With Klipper:

* pressure advance easily absorbs idler compliance
* extrusion remains stable

This is why **single-drive extruders have printed good parts for a decade**.

---

## 5️⃣ Why dual-drive doesn’t usually improve print quality

This is the uncomfortable truth:

> Dual-drive improves *capability* (pushing force), not *quality*.

Once you have:

* sufficient grip
* no slipping
* consistent melt flow

…print quality is capped by:

* hotend
* motion system
* cooling
* filament

Not extruder topology.

So dual-drive is great for:

* very soft TPU
* extreme retraction scenarios
* ultra-high flow rates

Not for:

* cleaner layer lines
* dimensional accuracy
* surface finish

---

## 6️⃣ Why your instinct aligns with your philosophy

Let’s tie this back to your project principles:

| Goal                    | Single-drive (Pitan) | Dual-drive |
| ----------------------- | -------------------- | ---------- |
| Scavengable             | ✔                    | ⚠          |
| Printable               | ✔                    | ⚠          |
| Tolerant of variation   | ✔                    | ✖          |
| Easy to tune            | ✔                    | ✖          |
| No hidden failure modes | ✔                    | ✖          |
| Print quality parity    | ✔                    | ✔          |

Dual-drive **does not buy you quality**, but it *does* buy you complexity.

That violates your **No Downward Complexity** rule.

---

## 7️⃣ How to phrase this without starting a war 😄

If you want to encode this into documentation without poking the bear:

> “Dual-drive extruders primarily increase extrusion force and filament handling robustness. The Neo-Darwin reference design does not require this additional complexity to achieve consistent, high-quality prints.”

That’s factual, calm, and unarguable.

---

## 8️⃣ Bottom line (very clear)

* ✔ **Pitan is single-drive**
* ✔ Single-drive is mechanically simpler and more tolerant
* ✔ Dual-drive adds mesh-dependent behaviour
* ✔ Any quality advantage is marginal to non-existent
* ✔ For your goals, single-drive is the *correct* choice

You’re not rejecting dual-drive because it’s “worse” —
you’re rejecting it because it’s **unnecessary**.

That’s exactly the kind of decision good engineering makes.

If you want next, we can:

* add a short **Extruder Topology Rationale** appendix
* write a FAQ entry (“Why not dual-drive?”)
* or sanity-check whether Pitan needs *any* idler tweaks for TPU

Just say the word.


Done. Both pieces are now added to the canvas as:

* **Appendix: Extruder Topology Rationale**
* **FAQ Entry: Why Not Dual-Drive Extruders?**

They’re written to:

* sound calm and factual (not ideological)
* avoid antagonising dual-drive advocates
* clearly justify *why* single-drive is the reference without claiming it’s “better” in absolute terms
* align cleanly with your *No Downward Complexity* rule

Importantly, these sections also future-proof the project:

* if someone proposes a new dual-drive extruder later, the decision path is already documented
* you’re no longer defending a preference, you’re enforcing a rationale

If you want, next logical additions would be:

* **FAQ: Why Not CoreXY?**
* **FAQ: Why Smooth Rods Instead of Rails (as reference)?**
* **Appendix: Motion System Load Budget (Extruder + Hotend)**

But structurally, your documentation stack is now very solid.

