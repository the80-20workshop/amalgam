# Rename Tracking: Neo-Darwin → Amalgam

This document tracks the rename from "Neo-Darwin" to "Amalgam".

## Summary

- **Old name:** Neo-Darwin
- **New name:** Amalgam
- **Tagline:** "Tractor with a Racecar Brain" (unchanged)
- **Secondary phrases:** "Iron with Intelligence", "The Thinking Tank"
- **Directory:** Currently `/amalgam/` — rename after GitHub repo update

## Key Changes

### Structure (No More Tiers)

**Old (Neo-Darwin):**
- Tier 1: One donor (not Neo-Darwin)
- Tier 2: Two donors, dual-MCU
- Tier 3: Two donors + MKS SKIPR

**New:**
- One donor? Just add Klipper. Amalgam isn't for you.
- Two donors → Pick frame path + electronics path

### Frame Paths
| Path | Frame | Motion |
|------|-------|--------|
| Scaffold (was "Darwin") | M10 Threaded Rod + MDF | Smooth Rods |
| Mill (was "V-Core") | Aluminum Extrusion + MDF | V-Slots |
| Lathe (was "S-Core") | Aluminum Extrusion + MDF | Smooth Rods |

**Note:** Frame paths were renamed from Darwin/S-Core/V-Core to Scaffold/Mill/Lathe to avoid confusion with RepRap Darwin heritage references and the Rat Rig V-Core product.

### Electronics Paths
| Path | Description |
|------|-------------|
| Dual-MCU | Two scavenged boards, Klipper |
| SKIPR | MKS SKIPR single board (~$130) |

---

## Files to Update

### Priority 1: Core Documentation (Update Now)

| File | Status | Notes |
|------|--------|-------|
| `CLAUDE.md` | ✅ Done | AI context file |
| `README.md` | ✅ Done | Project introduction |
| `PHILOSOPHY.md` | ✅ Done | Tractor philosophy |
| `MANIFESTO.md` | ✅ Done | Quick overview |
| `REFERENCE-SPEC.md` | ⏳ Pending | Hardware specification |
| `BUILDING.md` | ⏳ Pending | Build instructions |
| `AGENTS.md` | ⏳ Pending | AI agent instructions |

### Priority 2: ADRs (Update Now)

| File | Status | Notes |
|------|--------|-------|
| `docs/adr/README.md` | ✅ Done | ADR index |
| `docs/adr/025-multi-frame-architecture.md` | ✅ Done | New architecture ADR |
| `docs/adr/000-engineering-philosophy.md` | ⏳ Pending | Core philosophy |
| `docs/adr/001-m10-skeleton.md` | ⏳ Pending | Frame decision |
| `docs/adr/005-triple-z.md` | ⏳ Pending | Z-axis |
| `docs/adr/012-mainboard-host-architecture.md` | ⏳ Pending | Electronics tiers → paths |
| `docs/adr/021-dual-rod-motion-system.md` | ⏳ Pending | Motion system |
| `docs/adr/022-linear-bearings.md` | ⏳ Pending | Bearings |
| `docs/adr/023-z-drop-architecture.md` | ⏳ Pending | Z-drop |
| `docs/adr/024-heated-bed-size.md` | ⏳ Pending | Bed size |
| Other ADRs (002-020) | ⏳ Pending | Various |

### Priority 3: Scripts & CAD (Update Now)

| File | Status | Notes |
|------|--------|-------|
| `scripts/wizard.py` | ⏳ Pending | Configuration wizard |
| `scripts/whatif.py` | ⏳ Pending | Trade-off comparisons |
| `scripts/analyze.py` | ⏳ Pending | Engineering analysis |
| `scripts/build.py` | ⏳ Pending | Build orchestration |
| `scripts/README.md` | ⏳ Pending | Scripts documentation |
| `scripts/builders/*.py` | ⏳ Pending | Builder modules |
| `scripts/registry/*.py` | ⏳ Pending | Parts registry |
| `scripts/analysis/*.py` | ⏳ Pending | Analysis modules |
| `cad/config.py.example` | ⏳ Pending | Master configuration |
| `cad/README.md` | ⏳ Pending | CAD documentation |
| `cad/build.sh` | ⏳ Pending | STL generation |
| `cad/configure.py` | ⏳ Pending | Configuration script |
| `cad/pyproject.toml` | ⏳ Pending | Python project |
| `cad/parts/*.py` | ⏳ Pending | Part scripts |
| `cad/include/*.py` | ⏳ Pending | Include modules |

### Priority 4: Documentation Site (Update Now)

| File | Status | Notes |
|------|--------|-------|
| `docs/_quarto.yml` | ⏳ Pending | Quarto config |
| `docs/index.qmd` | ⏳ Pending | Docs home |
| `docs/README.md` | ⏳ Pending | Docs readme |
| `docs/guides/*.qmd` | ⏳ Pending | Build guides |
| `docs/reference/donor-printer-guide.md` | ⏳ Pending | Donor guide |
| `mkdocs.yml` | ⏳ Pending | MkDocs config |

### Priority 5: Historical (Leave As-Is or Add Note)

| Directory | Status | Notes |
|-----------|--------|-------|
| `docs/reference/ai-conversations/` | 📝 Historical | ~40 files, keep as historical record |
| `docs/deep-dives/` | 📝 Historical | Design exploration, may reference old name |
| `docs/articles/` | 📝 Historical | Articles, keep as historical record |

---

## Rename Commands (For Later)

Once GitHub repo is renamed:

```bash
# Rename local directory
mv amalgam amalgam

# Update git remote (if needed)
git remote set-url origin git@github.com:username/amalgam.git

# Global find/replace in key files
find . -name "*.md" -o -name "*.py" -o -name "*.qmd" | xargs sed -i '' 's/Amalgam/Amalgam/g'
find . -name "*.md" -o -name "*.py" -o -name "*.qmd" | xargs sed -i '' 's/amalgam/amalgam/g'
```

---

## Domain Recommendations

Current domains owned:
- neodarwin.[com, org, tech, farm]
- thetractor.[org, farm, tech]

Suggested domains to check (amalgam.com is likely taken):
- `amalgam3d.com` — clear 3D printing context
- `amalgamprinter.com` — explicit
- `theamalgam.org` — matches "thetractor" pattern
- `amalgam.farm` — continues the farm theme
- `printamalgam.com` — action-oriented

---

*Created: 2026-01-28*
