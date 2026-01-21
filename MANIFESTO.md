# Neo-Darwin: A 2026 RepRap Reference Specification

**High-Mass, Low-Cost, Total Control.**

The Neo-Darwin is a reimagining of the 2007 RepRap Darwin. It replaces the "black-box" appliance philosophy of modern 3D printers with an open, parametric, and rigid threaded-rod skeleton.

> **"A Tractor with the Brain of a Racecar"**

---

## What is Neo-Darwin?

A 3D printer that uses:
- **Heavy hardware** (M10 threaded rods, geared extruder) for mechanical stability
- **Software intelligence** (Klipper) for precision and auto-leveling
- **Scavenged parts** to prove high-performance manufacturing from e-waste

| Spec | Target |
|------|--------|
| **Price** | < $300 AUD |
| **Build Volume** | ~250mm³ |
| **Speed** | 70-120mm/s |
| **Accuracy** | ±0.1mm |

---

## Quick Links

| Document | Description |
|----------|-------------|
| [PHILOSOPHY.md](PHILOSOPHY.md) | The "Tractor" philosophy and 20 years of RepRap wisdom |
| [REFERENCE-SPEC.md](REFERENCE-SPEC.md) | The specific hardware choices (M10, Pitan, SKIPR, etc.) |
| [BUILDING.md](BUILDING.md) | How to generate STL files from parametric CAD |
| [docs/adr/](docs/adr/) | Architecture Decision Records |
| [docs/guides/](docs/guides/) | Tier-specific build guides |
| [docs/deep-dives/](docs/deep-dives/) | Design exploration documents |

---

## The Tier System

Build what fits your budget and parts bin:

| Tier | Description | Cost (AUD) |
|------|-------------|------------|
| **0** | Flash Klipper on your existing printer | $0 |
| **1** | Single donor, belt-driven Z | ~$80 |
| **2** | Dual donor, Triple-Z, multi-MCU | ~$200 |
| **3** | Reference Spec (MKS SKIPR, Triple-Z) | ~$270 |

---

## Reference Specification Summary

| Component | Choice | Why |
|-----------|--------|-----|
| **Frame** | M10 Threaded Rods | 3× rigidity of M8, standard 17mm wrench |
| **Extruder** | Pitan (3:1 geared) | Single-drive, scavengeable NEMA17, $4-10 |
| **Hotend** | E3D V6 + CHT Nozzle | Proven reliability, +50% flow |
| **Controller** | MKS SKIPR | Integrated Klipper, CAN bus ready |
| **Z-System** | Triple-Z Independent | Auto-leveling via Klipper |

See [REFERENCE-SPEC.md](REFERENCE-SPEC.md) for complete details.

---

## Who is this for?

**Build Neo-Darwin if you:**
- Have a broken/cheap printer to scavenge
- Love understanding every bolt and line of code
- Want a machine you can repair with hardware store parts
- Reject cloud-lock and proprietary ecosystems

**Buy an appliance if you:**
- Want "set-and-forget" out of the box
- Don't enjoy the engineering challenge
- Are buying all new parts anyway

---

## Getting Started

1. **Read the philosophy:** [PHILOSOPHY.md](PHILOSOPHY.md)
2. **Understand the hardware:** [REFERENCE-SPEC.md](REFERENCE-SPEC.md)
3. **Choose your tier:** Based on what you can scavenge
4. **Generate parts:** [BUILDING.md](BUILDING.md)
5. **Build it:** [docs/guides/](docs/guides/)

---

## The Bootstrapping Path

1. **Get a donor** - Used Ender 3, Anet A8, or similar ($50-80)
2. **Print Neo-Darwin parts** - Use the donor to manufacture its replacement
3. **Tear down the donor** - Salvage motors, bed, PSU, electronics
4. **Assemble Neo-Darwin** - The M10 skeleton + salvaged organs
5. **Transcend** - Re-print parts on the rigid new frame for higher precision

---

## Community & License

The Neo-Darwin is released under **GNU GPL v3**, the same license as the original RepRap Darwin.

> *"You aren't just building a printer; you're joining a 20-year conversation about sovereignty."*

---

*For the complete philosophy, see [PHILOSOPHY.md](PHILOSOPHY.md).*
*For the hardware specification, see [REFERENCE-SPEC.md](REFERENCE-SPEC.md).*
