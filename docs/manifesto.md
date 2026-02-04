# Amalgam: A 2026 RepRap Reference Specification

**High-Mass, Low-Cost, Total Control.**

Amalgam is a scavenger-friendly 3D printer built from two donor printers. It replaces the "black-box" appliance philosophy of modern printers with an open, parametric system that adapts to what you scavenged.

> **"A Tractor with the Brain of a Racecar"**

---

## What is Amalgam?

A 3D printer that uses:
- **Heavy hardware** (geared extruder, overbuilt frame) for mechanical stability
- **Software intelligence** (Klipper) for precision and auto-leveling
- **Scavenged parts** to prove high-performance manufacturing from e-waste

| Spec | Target |
|------|--------|
| **Price** | < $300 AUD |
| **Build Volume** | 220×220×220mm |
| **Speed** | 70-120mm/s |
| **Accuracy** | ±0.1mm |

---

## Quick Links

| Document | Description |
|----------|-------------|
| [philosophy.md](philosophy.md) | The "Tractor" philosophy and 20 years of RepRap wisdom |
| [../REFERENCE-SPEC.md](../REFERENCE-SPEC.md) | The specific hardware choices (Pitan, E3D V6, etc.) |
| [../BUILDING.md](../BUILDING.md) | How to generate STL files from parametric CAD |
| [adr/](adr/) | Architecture Decision Records |
| [guides/](guides/) | Build guides |
| [deep-dives/](deep-dives/) | Design exploration documents |

---

## Frame Paths

Amalgam requires **two donor printers**. Pick your path based on what you scavenged:

| Path | Frame | Motion | Best Donors | Cost |
|------|-------|--------|-------------|------|
| **Scaffold** | M10 Threaded Rod + MDF | Smooth Rods + LM8UU | Anet A8, Wanhao, Prusa clones | ~$190-230 |
| **Mill** | Aluminum Extrusion + MDF | V-Slots + POM Wheels | Ender 3, CR-10 | ~$160-185 |
| **Lathe** | Aluminum Extrusion + MDF | Smooth Rods + IGUS | Ender 3 + bought rods, mixed | ~$235-280 |

**All paths share:** MDF base (squaring jig + damping), Triple-Z leveling, Pitan extruder + E3D V6 hotend, Klipper firmware.

**Optional:** Add MKS SKIPR (~$130) for cleaner single-board electronics.

---

## Shared Components (All Paths)

| Component | Choice | Why |
|-----------|--------|-----|
| **Base** | MDF | Squaring jig + mass damping |
| **Extruder** | Pitan (3:1 geared) | Single-drive, scavengeable NEMA17, $4-10 |
| **Hotend** | E3D V6 + CHT Nozzle | Proven reliability, consistent print quality across all builds |
| **Z-System** | Triple-Z Independent | Auto-leveling via Klipper Z-tilt |
| **Firmware** | Klipper | Input Shaping, Pressure Advance |

See [../REFERENCE-SPEC.md](../REFERENCE-SPEC.md) for complete details.

---

## Who is this for?

**Build Amalgam if you:**
- Have **two** broken/cheap printers to scavenge
- Love understanding every bolt and line of code
- Want a machine you can repair with hardware store parts
- Reject cloud-lock and proprietary ecosystems

**Buy an appliance if you:**
- Want "set-and-forget" out of the box
- Don't enjoy the engineering challenge
- Are buying all new parts anyway

---

## Getting Started

1. **Read the philosophy:** [philosophy.md](philosophy.md)
2. **Understand the hardware:** [../REFERENCE-SPEC.md](../REFERENCE-SPEC.md)
3. **Get two donors:** Match donor types if possible (two rod-based or two V-slot)
4. **Run the wizard:** `python scripts/wizard.py` — it recommends your frame path
5. **Build it:** [guides/](guides/)

---

## The Bootstrapping Path

1. **Get two matching donors** - Two Ender 3s, two Anet A8s, etc. (~$100-120 total)
2. **Print Amalgam parts** - Use one donor to manufacture all printed parts
3. **Tear down both donors** - Salvage motors, beds, PSUs, electronics, rods/extrusions
4. **Assemble Amalgam** - MDF base + frame + salvaged organs
5. **Transcend** - Re-print parts on the rigid new frame for higher precision

---

## Community & License

The Amalgam is released under **GNU GPL v3**, the same license as the original RepRap Darwin.

> *"You aren't just building a printer; you're joining a 20-year conversation about sovereignty."*

---

*For the complete philosophy, see [philosophy.md](philosophy.md).*
*For the hardware specification, see [../REFERENCE-SPEC.md](../REFERENCE-SPEC.md).*
