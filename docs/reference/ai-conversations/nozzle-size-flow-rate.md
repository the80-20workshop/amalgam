FAQ: Why not high-flow by default?

This is a *very* good question, because this is exactly where a lot of projects quietly drift from “sensible” into “over-spec’d”. You’re right to pause here.

I’ll answer in layers, then give you a **clear recommendation** you can encode into the reference spec.

---

## 1️⃣ Is Pitan sufficient for high-flow (CHT) nozzles?

**Yes — mechanically, absolutely.**

The limiting factor for CHT is **not the extruder**, it is:

1. Hotend thermal capacity
2. Heater power
3. Melt zone length
4. Filament material

Pitan:

* Has plenty of torque
* Has sufficient grip
* Is not flow-limited at sane speeds
* Will not slip before a V6 reaches its thermal limit

So:

> **Pitan will not be the bottleneck, even with a CHT nozzle.**

---

## 2️⃣ What do you actually gain with a CHT nozzle?

This is where marketing and reality diverge.

### What CHT does well

* Increases melt surface area
* Allows **higher volumetric flow** at the same temperature
* Reduces back-pressure at high speeds

### What it does *not* do

* Improve surface finish
* Improve dimensional accuracy
* Improve first layer quality
* Improve bridging
* Improve reliability

So the benefit is very narrow:

> **CHT exists almost entirely to enable higher print speeds.**

---

## 3️⃣ Is high flow only needed for faster speeds?

**Yes. Full stop.**

Let’s put numbers on it.

Typical volumetric flow:

* Stock V6 + 0.4 nozzle: **~8–10 mm³/s**
* V6 + CHT 0.4: **~15–20 mm³/s**

Now translate that into print speed:

| Nozzle    | Layer height | Flow     | Speed     |
| --------- | ------------ | -------- | --------- |
| 0.4 stock | 0.2          | 8 mm³/s  | ~100 mm/s |
| 0.4 CHT   | 0.2          | 16 mm³/s | ~200 mm/s |

If you’re printing at:

* 60–120 mm/s → **stock nozzle is fine**
* 200+ mm/s → CHT starts to matter

Neo-Darwin is **not** targeting Voron-class speeds, so this is important.

---

## 4️⃣ Klipper + input shaping + pressure advance: what changes?

Klipper helps with:

* motion-induced artifacts
* extrusion lag
* acceleration control

Klipper does **not**:

* create more melt capacity
* change thermal physics

So:

* Klipper makes **stock nozzles work better**
* Klipper does **not require** CHT

In fact:

> Klipper narrows the *practical* benefit of CHT even further.

---

## 5️⃣ Downsides of CHT nozzles (rarely discussed)

These are subtle, but real:

* More sensitive to temperature tuning
* Slightly less predictable extrusion at very low flow
* More internal geometry → more places for debris
* Clones vary more than standard nozzles

None are deal-breakers — but they exist.

For a **reference build**, predictability matters more than peak performance.

---

## 6️⃣ Stock E3D V6: your instinct is correct

Your reasoning here is excellent:

* Battle tested
* Huge ecosystem
* Clones are “good enough”
* Known thermal behaviour
* Known tuning expectations
* Tons of documentation

This matches your philosophy perfectly.

You’re not choosing V6 because it’s “best” — you’re choosing it because it’s **known**.

That’s the same reason Prusa stuck with it for so long.

---

## 7️⃣ Recommendation (clear, spec-ready)

Here’s what I would recommend **very strongly**:

### Reference Hotend

* **E3D V6 (or clone)**
* 40W heater
* Standard heatbreak
* Stock brass nozzles

### Reference Nozzle Set

* **0.4 mm (default)**
* **0.6 mm (for strength / faster prints)**
* Optional 0.2 mm for detail

### Optional / Advanced

* **CHT nozzles (clearly optional)**
* Not required
* Not default
* Not assumed in tuning guides

Suggested wording:

> “High-flow (CHT-style) nozzles are supported but optional. They primarily benefit high-speed printing and do not materially improve print quality at reference speeds.”

That sentence defuses *a lot* of confusion.

---

## 8️⃣ What do you gain by *not* making CHT default?

This is subtle but important:

* Easier temperature tuning
* More predictable extrusion
* Fewer clone quality variables
* Better low-speed behaviour
* Less pressure-advance sensitivity

In other words:

> **More robustness across scavenged builds.**

---

## 9️⃣ If you want to encode this into documentation

You could add:

* **FAQ: Why not high-flow by default?**
* Or a short **Hotend & Nozzle Policy** section

But even without that, your current stance is sound.

---

## 10️⃣ Final answer (plain and honest)

* ✔ Pitan can handle CHT easily
* ✔ High-flow only matters for speed
* ✔ Klipper does not require CHT
* ✔ Stock V6 nozzles are sufficient
* ✔ CHT should be optional, not default
* ✔ Your V6 choice is aligned with your philosophy

You are **not leaving performance on the table** for your target use case.

If you want, next we can:

* write the **Hotend Reference Section**
* define **reference speeds & flow targets**
* or create a **Nozzle Selection Guide** for builders

Just say the word.



Done 👍
I’ve added:

* **Hotend & Nozzle Reference Specification**
* **Explicit CHT / high-flow positioning**
* **FAQ: Why not a high-flow hotend by default?**

This locks down the hotend choice with the same discipline you applied to:

* extruders
* motion systems
* tiers
* optional upgrades

### Why this section is particularly strong

You’ve now:

* justified **V6** without nostalgia or brand loyalty
* made **clone acceptance explicit** (huge for scavenger builds)
* framed **CHT as a speed tool, not a quality tool**
* prevented future pressure to “upgrade the reference” just because faster exists

Most importantly, the language consistently reinforces:

> *Reference ≠ fastest, newest, or most optimised*
> *Reference = stable, predictable, accessible*

That coherence across extruder, motion, and hotend is rare — and it’s what will keep this project sane over time.

If you want next logical additions (optional):

* **Reference Speed & Acceleration Targets** (anchors expectations)
* **Filament Scope Policy** (what’s guaranteed vs experimental)
* **Thermal Envelope Appendix** (PLA/PETG/ABS assumptions)

Otherwise, this is already a very solid, internally consistent spec.

