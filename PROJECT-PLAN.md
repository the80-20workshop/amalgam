# Neo-Darwin Project Plan

## Phase 0: Inventory What You Have
- List all parts from your Ender 3 donor
- Measure what you're keeping vs. buying

## Phase 1: ADRs First (The "What" Defines the "How")
Convert AI conversations → ADRs because this will tell you exactly what parts you need:
- ADR-001: Why M12 skeleton? (vs aluminum, 2020, etc.)
- ADR-002: Why Greg's Wade? (vs Voron Clockwork, direct drive)
- ADR-003: Why smooth rods? (vs linear rails, V-slot)
- ADR-004: Why E3D V6 with CHT? (vs Volcano, Dragon)
- ADR-005: Why Triple-Z? (vs single motor, belted)

This phase answers "what parts do I actually need?" - each ADR should include the BOM implications.

## Phase 2: Update config.py
Based on ADRs, expand config.py to include:
- Frame rod lengths
- Motor positions
- Mounting hole positions
- All dimensions used by parts

## Phase 3: Design Parts (Tier 3)
Start with the skeleton:
- Corner brackets
- Motor mounts
- Z-pucks
- Spider bed support
Then Wade extruder parts

## Phase 4: Build, Document, Test
- Cut M12 rods to calculated lengths
- Print and assemble
- Document assembly as you go (take photos, notes)
- Frequency measurements, Input Shaping calibration
- Validate ±0.1mm claim

## Phase 5: Refine Documentation
- Convert assembly notes into proper docs
- Update mkdocs.yml when ready
