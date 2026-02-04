# ADR-018: Documentation & Assembly Guide System

## Status
Accepted

## Context
The Amalgam requires a documentation system that supports:
- **Assembly Guides**: Step-by-step instructions for building the printer
- **Bills of Materials (BOM)**: Parts lists for different build tiers
- **Cut Lists**: Rod lengths, sheet dimensions
- **Configuration-Aware Content**: Show/hide sections based on user's config
- **CAD Integration**: Embed build123d renders directly in docs
- **Professional Output**: Printable PDFs + web HTML
- **Single Source of Truth**: Content generates both formats from same source

In 2026, documentation systems for engineering projects fall into:
1. **Static Markdown**: Plain markdown files + simple generators
2. **Software Docs**: MkDocs, Docusaurus, Sphinx (web-first)
3. **Computational Publishing**: Quarto (live code execution, professional output)

Each has different capabilities for parametric hardware documentation.

## Decision
We adopt **Quarto** as the documentation and assembly guide system.

### Documentation System Comparison

| Feature | MkDocs | Quarto |
|---------|---------|---------|
| **Primary Use Case** | Software libraries, "Vignettes" | Technical reports, Books, Engineering docs |
| **Code Execution** | Static (Shows code only) | **Live (Executes code during render)** |
| **Math/Science** | Excellent (via extensions) | **Native (Pro-grade LaTeX/Typst support)** |
| **Cross-Referencing** | Limited (Manual/Plugins) | **Deep (Auto-numbered Figs, Tabs, Eqs)** |
| **Output Formats** | Mostly HTML | **HTML, PDF, Word, ePub (Single Source)** |
| **Visual Editor** | No (Markdown only) | **Yes (Word-like interface for prose)** |

### Why Quarto

**1. Literate CAD Integration**
- **With MkDocs**: Manually run build123d, take screenshot, save image, link in markdown
- **With Quarto**: Execute Python code cells directly in `.qmd` files
- Automates rendering: Script runs, part generated, image embedded
- Documentation never out of sync with code
- **Single Source of Truth**: CAD code and docs in same ecosystem

**2. Professional PDF Assembly Guides**
- **MkDocs**: Web-first, PDF generation is afterthought, looks "website-y"
- **Quarto**: LaTeX (or Typst) creates professional textbook-quality PDFs
- Automatic page numbering, table of contents, high-resolution diagrams
- **Single Source**: Same `.qmd` file generates both HTML and PDF
- **Printable Manual**: Users get professional assembly guide in print or PDF

**3. Deep Cross-Referencing**
- **Common Need**: "Refer to the bolt shown in Figure 4.2"
- **MkDocs**: Manual figure management, breaks if figures added/removed
- **Quarto**: `@fig-bolt-assembly` auto-references, renumbers automatically
- Automatic equation numbering, table numbering, section references
- Adds/removing content doesn't break cross-references

**4. Conditional Content**
- **Configuration-Aware Docs**: Show/hide sections based on user's `config.py`
- **Example**: "If `printer_type == 'XL'`, include 'Large Bed Leveling' section"
- **Tier-Specific Content**: Show/hide based on Tier 1/2/3 selections
- **Material-Specific**: Show different fastener lists based on rod type
- **Single Master Doc**: One file adapts to all user configurations

**5. Native Code Execution**
- **Live Python**: Execute build123d cells during doc render
- **Data Visualization**: Use matplotlib, plotly for diagrams
- **Math Rendering**: Native LaTeX/Typst for equations
- **Dynamic Content**: Generate tables, BOMs, cut lists from config data
- **Automated Testing**: Validate code snippets during doc build

### Why Alternatives Were Rejected

**Plain Markdown**
- **No Code Execution**: Cannot run build123d or Python snippets
- **Manual Screenshots**: CAD renders must be manually captured and linked
- **Sync Issues**: Documentation can drift from code changes
- **Poor PDF**: Manual PDF generation, lacks professional formatting
- **Limited Cross-Referencing**: Manual figure/section management

**MkDocs with Extensions**
- **Static Content**: Code is displayed, not executed
- **Web-First**: PDF generation is weak/afterthought
- **Manual Cross-References**: Plugins provide limited functionality
- **No Conditional Content**: Complex to show/hide sections based on config
- **Limited Math**: Requires plugins for LaTeX support (not native)

**Sphinx (Python Docs)**
- **Software-Focused**: Designed for Python API documentation
- **Complex Setup**: Heavy configuration for simple docs
- **PDF Quality**: LaTeX output is functional but not professional
- **Limited Code Execution**: Requires additional setup for live execution
- **Steep Learning Curve**: ReStructuredText is less common than markdown

## Integration with build123d (ADR-017)

### Literate CAD Workflow
````qmd
---
title: "Corner Bracket Assembly"
---

## Build the Corner Bracket

```{python}
#| label: fig-corner
#| echo: false
from include.corner_components import make_standard_corner
from config import CORNER_SIZE, M12_FIT_DIA

corner = make_standard_corner(
    corner_size=CORNER_SIZE,
    m12_fit_dia=M12_FIT_DIA,
)
corner.visualize()
```

**Figure 1**: The corner bracket is parametrically generated using build123d.

## Assembly Steps

1. **Install M12 Rods** (@fig-rods): Thread rods through corner...
````

### Automated BOM Generation
````qmd
## Bill of Materials

```{python}
#| label: tbl-bom
#| echo: false
import pandas as pd
from config import BUILD_VOLUME, TIER

bom = pd.DataFrame({
    'Part': ['M12 Rod', 'M12 Nut', 'Corner Bracket'],
    'Qty': [12, 24, 8],
    'Source': ['Hardware Store', 'Hardware Store', '3D Printed']
})
bom
```

**Table 1**: BOM for `@tbl-tier` configuration.
````

### Conditional Content
````qmd
---
title: "Assembly Guide"
---

```{r}
#| echo: false
#| include: false
#| condition: meta.tier == 3
```

## Laminated Plinth Assembly

{# This section only shown for Tier 3 builds #}

Drill MDF board using template...

```{r}
#| include: true
#| condition: meta.tier == 1 || meta.tier == 2
```

## Naked Frame Assembly

{# This section shown for Tier 1 and 2 #}

Place frame on rubber pads...
````

### Cross-Referencing
```qmd
Install the corner bracket as shown in @fig-corner.

See Table @tbl-bom for complete parts list.

Follow @sec-plinth-assembly for Tier 3 baseboard setup.
```

## Consequences

### Benefits
- **Literate CAD**: CAD code embedded in docs, automated rendering
- **Professional Output**: HTML for web, PDF for print from same source
- **Auto Cross-References**: Figures, tables, equations auto-numbered and referenced
- **Conditional Content**: Show/hide sections based on user configuration
- **Code Execution**: Live Python for data viz, BOM generation, CAD rendering
- **Single Source**: One file generates both web and print docs
- **Math Support**: Native LaTeX/Typst for engineering equations

### Trade-offs
- **Quarto Learning Curve**: New tool for team, different from MkDocs
- **Build Time**: Code execution adds time to doc rendering
- **Complexity**: More powerful tool means more configuration options
- **Ecosystem**: Smaller than MkDocs (but growing in data science)

### What This Enables
- **Literate Documentation**: CAD code, data viz, and prose in same file
- **Automated Rendering**: CAD views generated during doc build
- **Configuration-Aware Docs**: Tailored guides for each user's build
- **Professional PDFs**: Print-quality assembly manuals
- **Single Source**: HTML web docs and PDF print docs from same `.qmd` files
- **Testing**: Validate code snippets and CAD during doc render

### What This Replaces
- Static markdown docs (no code execution)
- MkDocs (no live code, weak PDF, limited cross-refs)
- Manual screenshot workflow (CAD → image → link)
- Multiple documentation sources (separate web and print docs)

## Implementation Notes

### Project Structure
```
docs/
├── adr/                  # Architecture Decision Records
│   ├── 000-engineering-philosophy.md
│   └── ...
├── reference/             # Reference documentation
│   ├── ai-conversations/
│   └── ...
├── articles/              # Articles and essays
│   ├── wisdom.md
│   └── ...
├── planning/              # Project planning docs
│   ├── PROJECT-PLAN.md
│   └── ...
├── _quarto.yml           # Quarto configuration
├── assembly-guide.qmd    # Main assembly guide (conditional content)
├── bom.qmd              # BOM generation
└── index.qmd             # Landing page
```

### Quarto Configuration (_quarto.yml)
```yaml
project:
  type: book
  output-dir: _site

format:
  html:
    theme: cosmo
    toc: true
    code-fold: true
  pdf:
    latex-engine: xelatex
    toc: true
    number-sections: true

execute:
  cache: false
  freeze: false
  warning: false

metadata-files:
  - config.yaml  # User config for conditional content
```

### Conditional Content Setup
```yaml
# config.yaml (generated from user's config.py)
tier: 3
bed_type: mk52
probe_type: superpinda
```

````qmd
```{r}
#| condition: meta.tier == 3
```

Tier 3 content...

```{r}
#| condition: meta.tier == 1 || meta.tier == 2
```

Tier 1/2 content...
````

### Code Cell Options
````qmd
```{python}
#| label: fig-part-render
#| echo: false      # Don't show code
#| eval: true       # Execute code
#| output: true     # Show output (render)
from build123d import *
part = Box(10, 10, 10)
part.visualize()  # Generates figure
````

### Cross-Referencing Syntax
- Figures: `@fig-label` or `See @fig-label`
- Tables: `@tbl-label` or `See @tbl-label`
- Sections: `@sec-label` or `See @sec-label`
- Equations: `@eq-label` or `See @eq-label`

### Publishing Workflow
```bash
# Render all formats (HTML + PDF)
quarto render

# Render HTML only
quarto render html

# Render PDF only
quarto render pdf

# Watch for changes and auto-render
quarto render --watch
```

### Integration with CI/CD
```yaml
# .github/workflows/docs.yml
name: Build Documentation
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: quarto-dev/quarto-actions/setup@v2
      - name: Render Docs
        run: quarto render
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_site
```

## References
- **docs/reference/ai-conversations/why-quarto.md**: Complete doc system discussion
- **docs/adr/017-parametric-cad-system.md**: build123d CAD system
- Quarto Documentation: [quarto.org](https://quarto.org/)
- Computational Publishing: [Computational Notebooks](https://computational-publishing-project.github.io/)

## Evolution Notes
This ADR establishes Quarto as the documentation system. Future documentation technologies will be evaluated against:
- Live code execution (not static)
- Professional HTML + PDF from single source
- Deep cross-referencing (auto-numbered figures/tables/sections)
- Conditional content support (show/hide based on config)
- Native LaTeX/Typst support for equations

Alternative emerging technologies:
- MkDocs with extensions (still static, weak PDF)
- Sphinx with MyST (complex setup, limited code execution)
- Jupyter Book (good for code, weaker for publishing)

Quarto represents best-in-class for computational publishing in 2026.
