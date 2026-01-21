# Document 1: One‑Page Design Philosophy

## Purpose

This project exists to enable people to **build capable, high‑quality 3D printers using scavenged, reused, and widely available parts**, without sacrificing print quality or requiring specialised supply chains.

The goal is not to build the *fastest*, *lightest*, or *most precise* printer. The goal is to build a **printer that many people can realistically build, understand, modify, and maintain**.

---

## Core Principles

### 1. Accessibility over Optimisation

Design choices prioritise **availability, simplicity, and reuse** over theoretical performance gains. If a part is difficult to source, proprietary, or requires a specialised kit, it cannot be a reference component.

A design that performs 95% as well but is buildable by twice as many people is the superior design.

---

### 2. No Quality Penalty for Lower Tiers

All build tiers must be capable of producing **equivalent print quality**.

Higher tiers reduce:

* wiring complexity
* sourcing difficulty
* configuration effort

They **do not** unlock better prints.

Lower‑tier builders are not building an inferior printer — they are building the *same printer* with more effort and ingenuity.

---

### 3. Scavengability Is a First‑Class Requirement

Reference designs must:

* tolerate part variation
* accept imperfect or reused components
* work with metric hardware commonly found in old printers, appliances, or office equipment

If a design assumes precision parts or narrow tolerances, it is optional by definition.

---

### 4. Mechanical Honesty

The printer should be understandable as a machine.

Designs should:

* expose how forces flow
* favour visible, inspectable mechanisms
* avoid hidden complexity

This supports learning, debugging, and modification — key RepRap values.

---

### 5. Evolution, Not Replacement

The printer is designed to evolve:

* parts may be replaced
* subsystems may be upgraded
* configurations may vary

But **the core architecture remains stable**, so improvements do not fragment the ecosystem.

---

## Philosophy Summary (Short Form)

> *Build the simplest machine that prints well, using the parts people already have, and allow complexity only where it genuinely reduces burden — never just because it is possible.*

---

# Document 2: Reference vs Optional Component Policy

## Purpose

This policy defines how components are classified to ensure:

* fairness across build tiers
* consistent documentation
* long‑term maintainability
* minimal supply‑chain dependency

---

## Reference Components

A **Reference Component** is the baseline expectation for all builds.

### A component may be Reference if it:

* is fully printable or uses generic hardware
* can be built without proprietary or precision kits
* is tolerant of part variation
* is reasonably achievable through scavenging or common suppliers
* does not impose a print‑quality advantage over alternatives

### Reference components must:

* be documented first
* be supported across all tiers
* define the mechanical and electrical assumptions of the printer

### Example:

* **Extruder:** Pitan (printed gears, generic hardware)

---

## Optional Components

An **Optional Component** is a valid alternative that:

* improves ease of assembly, compactness, or aesthetics
* appeals to experienced builders or tinkerers
* may require purchased kits or specialised parts

Optional components **must not**:

* be required for acceptable print quality
* invalidate reference documentation
* create a perception that reference builds are inferior

### Optional components are explicitly non‑normative.

They are *choices*, not expectations.

---

## Classification Rules

A component is **Optional by default** unless it clearly satisfies all Reference criteria.

If a component:

* requires a gear kit, belt kit, or custom shaft
* depends on narrow tolerances
* assumes new parts availability

…it cannot be Reference.

---

## Extruder Policy (Concrete Example)

### Reference Extruder

* Pitan
* Generic NEMA17 motor
* Printed gears
* Generic bearings and fasteners

### Optional Extruders

* Orbiter v1.5
* Voron M4
* Wristwatch
* ProtXtruder

These options:

* do not materially improve print quality
* increase sourcing complexity
* are therefore excluded from the reference spec

---

## Tier Consistency Rule

Across Tier 1, Tier 2, and Tier 3:

* kinematics remain identical
* extrusion concept remains identical
* motion quality expectations remain identical

Tiers exist to reduce **logistical burden**, not to gate capability.

---

## Policy Summary

> *Reference defines what everyone can build. Optional defines what some may enjoy building. Confusing the two undermines the project.*

---

# Appendix: Extruder Topology Rationale

## Single‑Drive vs Dual‑Drive Extruders

The Neo‑Darwin reference design deliberately adopts a **single‑drive extruder topology**.

This decision is not based on cost alone, but on mechanical behaviour, tolerance to variation, and long‑term stability across scavenged and mixed‑quality components.

### Single‑Drive Characteristics

A single‑drive extruder uses one driven hobbed gear and a spring‑loaded idler to grip filament.

This topology:

* has a single torque source
* introduces only one periodic error source
* is tolerant of minor misalignment
* fails gradually and visibly

Any compliance or elasticity in the system is smooth and continuous, making it easy to compensate using firmware features such as pressure advance.

### Dual‑Drive Characteristics

Dual‑drive extruders use two opposing driven gears that must mesh correctly and remain synchronised under load.

This introduces additional dependencies:

* matched gear tooth profiles
* precise centre‑to‑centre spacing
* consistent preload
* uniform wear between gears

Small mismatches between gears — especially in printed or mixed‑quality parts — can introduce torque ripple or micro stick‑slip behaviour. These effects are difficult to detect, difficult to diagnose, and can subtly affect extrusion consistency.

### Design Conclusion

Dual‑drive extruders primarily increase **extrusion force and filament handling robustness**, not surface finish or dimensional accuracy.

For the extrusion forces required by the Neo‑Darwin reference design, a single‑drive system provides sufficient grip with fewer failure modes, greater tolerance to part variation, and lower mechanical complexity.

For these reasons, single‑drive extrusion is selected as the reference topology.

---

# FAQ Entry: Why Not Dual‑Drive Extruders?

**Q: Why does the Neo‑Darwin project not use a dual‑drive extruder as the reference?**

**A:** Dual‑drive extruders primarily improve extrusion force and filament grip, which is valuable for very soft filaments or extreme flow‑rate scenarios. However, they also introduce additional mechanical complexity and dependence on precise gear meshing.

For the materials and print speeds targeted by Neo‑Darwin, a single‑drive extruder provides equivalent print quality while being more tolerant of scavenged parts, easier to assemble, and easier to maintain. Because dual‑drive systems do not materially improve print quality for the reference use case, they are treated as optional rather than reference components.

Builders interested in experimenting with dual‑drive designs are free to do so, but the reference specification prioritises simplicity, robustness, and accessibility over theoretical performance gains.

---

# FAQ Entry: Why Not CoreXY?

**Q: Why does the Neo-Darwin project use a Cartesian motion system instead of CoreXY?**

**A:** CoreXY is an efficient and capable motion system, but it introduces additional belt paths, alignment sensitivity, and tuning complexity. These factors increase the build and debugging burden, particularly when using scavenged or mixed-quality components.

The Neo-Darwin project prioritises:

* mechanical clarity
* ease of diagnosis
* tolerance of part variation
* predictable behaviour under imperfect assembly

A fixed-gantry Cartesian layout achieves equivalent print quality at the speeds and accelerations targeted by the project, while remaining easier to understand, assemble, and repair. Because CoreXY does not materially improve print quality for the reference use case, it is treated as optional rather than reference.

---

# FAQ Entry: Why Smooth Rods Instead of Linear Rails?

**Q: Why does the reference design use smooth rods instead of linear rails?**

**A:** Linear rails offer high stiffness and compactness, but they require clean environments, careful alignment, and consistent lubrication to perform reliably. Scavenged rails vary widely in condition and are difficult to evaluate visually.

Smooth rods and linear bearings:

* are widely available from donor printers and office equipment
* tolerate minor misalignment
* fail gradually and visibly
* are easier to clean, replace, and realign

For the spans and loads used in the Neo-Darwin reference design, smooth rods provide sufficient stiffness without introducing additional sourcing or maintenance burden. Linear rails are therefore supported as optional upgrades, but not required for reference builds.

---

# Appendix: Motion System Load Budget

## Purpose

This appendix defines acceptable mass limits for moving components to ensure predictable motion behaviour across all build tiers.

The motion system is designed to operate within conservative stiffness margins using M8 or M10 smooth rods without mid-span supports.

---

## Reference Toolhead Load

The reference toolhead consists of:

* Pitan extruder (printed)
* NEMA17 stepper motor
* Standard V6-style hotend or equivalent
* Mounting hardware

**Target mass:**

* ~220–260 g (depending on motor and material choice)

This load remains within acceptable deflection limits for:

* M8 smooth rods at ≤280 mm span
* M10 smooth rods at ≤250 mm span

---

## Non-Reference Loads

Heavier toolheads increase dynamic deflection, acceleration sensitivity, and tuning burden.

Designs that exceed the reference load budget may:

* require reduced spans
* require additional structural support
* impose stricter acceleration limits

Such designs are therefore classified as **Optional**.

---

## Design Rule

> Reference components must not exceed the motion system load budget or require structural compensation to function correctly.

This ensures that motion quality and print consistency are preserved across all tiers without additional complexity.

