# Document 2: Reference vs Optional Component Policy

## Purpose

This policy defines how components are classified to ensure:

* fairness across build tiers
* consistent documentation
* long-term maintainability
* minimal supply-chain dependency

---

## Reference Components

A **Reference Component** is the baseline expectation for all builds.

### A component may be Reference if it:

* is fully printable or uses generic hardware
* can be built without proprietary or precision kits
* is tolerant of part variation
* is reasonably achievable through scavenging or common suppliers
* does not impose a print-quality advantage over alternatives

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

### Optional components are explicitly non-normative.

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


