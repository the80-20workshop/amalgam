# Neo-Darwin Project Plan

## Phase 0: Inventory What You Have
- [x] List all parts from your Ender 3 donor
- [ ] Measure what you're keeping vs. buying

## Phase 1: ADRs First (The "What" Defines the "How") ✅ COMPLETED
Convert AI conversations → ADRs because this will tell you exactly what parts you need:
- [x] ADR-001: Why M12 skeleton? (vs aluminum, 2020, etc.)
- [x] ADR-002: Why Greg's Wade? (vs Voron Clockwork, direct drive)
- [x] ADR-003: Why smooth rods? (vs linear rails, V-slot)
- [x] ADR-004: Why E3D V6 with CHT? (vs Volcano, Dragon)
- [x] ADR-005: Why Triple-Z? (vs single motor, belted)
- [x] ADR-006: Z-probe selection (BLTouch vs PINDA)
- [x] ADR-007: CAN bus architecture (optional upgrade)
- [x] ADR-008: Spider Trident bed support
- [x] ADR-009: Modular Puck system

This phase answers "what parts do I actually need?" - each ADR includes generic BOM scenarios for different donors.

## Phase 2: Update config.py & Design Parts (CURRENT PHASE)
Based on ADRs, expand config.py to include all parameters:
- [ ] Frame rod lengths (calculated from build volume)
- [ ] Motor positions and offsets
- [ ] Mounting hole patterns (boards, hotends, pucks)
- [ ] Puck dimensions and interfaces
- [ ] All parameters used by parts

Design workflow:
1. Update config.py with needed parameters
2. Write build123d part code referencing config.py
3. Render in VSCode to verify geometry
4. Report changes/issues, iterate

Parts to design (not necessarily sequential):
- [ ] Corner brackets (with optional diagonal supports)
- [ ] Z-pucks (motor mounts)
- [ ] Brain pucks (electronics mounts)
- [ ] Spider bed support (hub + 3 arms)
- [ ] X-carriage with Extruder Puck (Wade mount)
- [ ] Greg's Wade extruder parts
- [ ] Linear bearing clamps (X, Y, Z axes)

## Phase 3: Print & Assemble (Tier 3 Build)
- [ ] Cut M12 rods to calculated lengths
- [ ] Print all parts on donor printer
- [ ] Assemble frame (skeleton + corner brackets)
- [ ] Install smooth rods and gantry
- [ ] Install Wade extruder and hotend
- [ ] Install electronics and wiring
- [ ] Configure Klipper

## Phase 4: Build, Document, Test
- [ ] Document assembly as you go (take photos, notes)
- [ ] Frequency measurements, Input Shaping calibration
- [ ] Validate ±0.1mm claim (dimensional test prints)
- [ ] Refine design based on build issues

## Phase 5: Refine Documentation
- [ ] Convert assembly notes into proper docs
- [ ] Update mkdocs.yml when ready
- [ ] Publish comprehensive assembly guide
