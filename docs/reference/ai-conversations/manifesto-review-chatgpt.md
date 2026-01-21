This is a *good* manifesto already — it’s pragmatic, principled, and unusually honest about trade-offs. Dropping Wade in favour of the **Pitan** is not a philosophical retreat; it’s a clarification of priorities. I’ll break this into four parts:

1. **Is dropping Wade justified? (Yes, and you should say why)**
2. **What to update explicitly in the Manifesto**
3. **What (lightly) to pull in from the one-page philosophy**
4. **Whether to cross-pollinate Philosophy ↔ Reference/Optional Policy**

I’ll stay at the *design governance* level rather than rewriting the whole file unless you want that next.

---

## 1. Dropping Wade: philosophically correct, not a compromise

Your reasoning is sound **and aligned with the project’s core values**:

* Wade is:

  * heavy
  * designed for a different era (slow bedslingers, short spans)
  * mechanically “clever” but structurally unfriendly to M8 @ 250–300 mm
* The engineering workaround (rod supports / span reduction):

  * adds parts
  * adds alignment risk
  * violates your “low-tier simplicity” rule

This is an important distinction to make explicit:

> Wade fails **not because it is bad**, but because it *forces complexity downward* into Tier 1 and Tier 2.

That framing avoids alienating RepRap purists while staying honest.

---

## 2. Concrete Manifesto updates you should make

### A. Add an **Extruder Design Principle** section (short)

Right now, extruder choice is implicit. It should be explicit.

Suggested wording (conceptual, not literal):

> **Extruder Principle**
>
> The Neo-Darwin reference extruder must:
>
> * Be printable using common materials
> * Use scavengable or commodity hardware
> * Remain light enough to preserve print quality on M8 motion systems
> * Avoid requiring precision gear kits as a hard dependency
>
> Designs that push mechanical complexity onto the motion system are rejected, even if they offer theoretical advantages.

This *pre-justifies* Pitan and *pre-rejects* Wade without naming names.

---

### B. Explicitly name **Pitan as Reference Extruder**

Somewhere near where motion system / gantry assumptions are discussed:

> **Reference Extruder**
>
> The Neo-Darwin reference extruder is the **Pitan (Printed Titan-style) Extruder**.
>
> It represents the best balance of:
>
> * weight
> * printability
> * scavengability
> * proven extrusion quality
>
> Heavier legacy designs such as the Wade Geared Extruder are considered *optional* and are not supported as reference builds due to their impact on motion stiffness at lower tiers.

This is important: *reference ≠ best*. Reference = **safest default**.

---

### C. Clarify **why you are not “supporting M8” with braces**

You already hint at this, but it should be explicit:

> The project deliberately avoids structural “patches” (rod supports, mid-span braces) that exist only to accommodate overweight toolheads, as these increase build complexity and alignment burden for entry-level builders.

This turns a *design decision* into a *rule*.

---

## 3. Should you update the one-page philosophy?

Yes — but **only one line** needs to be added or sharpened.

Your philosophy already says (paraphrased):

> Cheap, simple, reproducible, no second-class tiers

What’s missing is the **downward pressure rule**.

Add something like:

> **No Downward Complexity Rule**
> Higher-performance components must never force additional mechanical or alignment complexity onto lower tiers of the build.

That single sentence explains:

* why Wade is out
* why Pitan is in
* why Triple-Z is allowed at Tier 1
* why SKIPR is Tier 3 only
* why Voron-style solutions are optional

It’s a *keystone principle*.

---

## 4. Should Philosophy influence Reference vs Optional Policy?

Yes — and this is where your governance becomes unusually strong.

### Add this explicit test to the **Reference vs Optional Policy**

Every component must answer **two questions**:

1. **Can a Tier-1 builder build this without added alignment or tooling complexity?**
2. **Does this component increase the load or precision requirement of another subsystem?**

If *either* answer is “yes” → **Optional**, not Reference.

This cleanly sorts:

| Component   | Outcome   | Why                        |
| ----------- | --------- | -------------------------- |
| Pitan       | Reference | Light, printable, tolerant |
| Orbiter 1.5 | Optional  | Gear kit dependency        |
| Voron M4    | Optional  | Precision gears            |
| Wristwatch  | Optional  | Niche complexity           |
| Wade        | Optional  | Weight → motion penalties  |
| Sherpa Mini | Optional  | Purchased gears            |

You are no longer arguing taste — you are enforcing policy.

---

## 5. Big picture: you are doing something rare (and right)

Most printer projects fail because:

* they chase theoretical perfection
* they optimise for experts
* they let “better” quietly break “simpler”

Your approach is the opposite:

* **print quality parity**
* **complexity containment**
* **choice without penalty**

Dropping Wade is not abandoning RepRap roots —
it’s applying RepRap *discipline*.

---

### If you want next:

* I can **rewrite the extruder sections verbatim** for the manifesto
* Or produce a **one-paragraph “Why Pitan” justification** suitable for README / Thingiverse
* Or help you define a **formal Tier Compliance Checklist**

Just say which direction.

