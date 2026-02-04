# Amalgam Python Package

This is the main CAD package containing all parametric part designs.

## Structure

```
amalgam/
├── lib/                  # Shared libraries
│   ├── logo.py           # Amalgam logo (used by maker_coin, fidget_bolt)
│   ├── stylized_a.py     # The stylized "A" shape
│   ├── corner.py         # Corner bracket components
│   └── export.py         # Multi-format export system
│
└── parts/                # Buildable parts (one STL per script)
    ├── calibration/      # First layer tests
    ├── frame/            # Corner brackets
    └── victory/          # Maker coin, fidget bolt
```

## lib/ vs parts/

- **lib/** - Shared code imported by multiple parts. Not directly buildable.
- **parts/** - Each script generates one or more STL files via `./build.sh build <name>`

## Adding a New Part

1. Create a new `.py` file in the appropriate `parts/` subdirectory
2. Import from `build123d` and optionally from `lib/`
3. Add a `main()` function that:
   - Creates the part using build123d
   - Calls `export_part(part, "part_name")` from `amalgam.lib.export`

Example:

```python
from build123d import *
from amalgam.lib.export import export_part

def make_my_part():
    with BuildPart() as part:
        Box(10, 10, 10)
    return part.part

def main():
    part = make_my_part()
    export_part(part, "my_part")

if __name__ == "__main__":
    main()
```

The part will automatically be discovered by `./build.sh list`.

## Importing Shared Code

```python
# Import the logo
from amalgam.lib.logo import make_logo

# Import export function
from amalgam.lib.export import export_part

# Import config values
from config import BUILD_VOLUME, SMOOTH_ROD_DIA
```

## Config Integration

Parts can read values from `config.py`:

```python
try:
    from config import BUILD_VOLUME
    BED_X = BUILD_VOLUME["x"]
except ImportError:
    BED_X = 200  # Fallback default
```

This makes parts parametric to the user's printer configuration.

---

*Built with [build123d](https://github.com/gumyr/build123d) - Python BREP CAD.*
