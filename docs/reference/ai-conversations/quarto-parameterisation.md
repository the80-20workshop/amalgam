You definitely don't need to write a custom script to find-and-replace text! Quarto has a built-in, robust **parameterization** system that allows you to pass variables into your `.qmd` file at render time.

This is much cleaner than manual templating because it keeps your logic inside the document and allows you to define default values.

---

## 1. How to Define Parameters

You define parameters in the YAML header of your `.qmd` file using the `params` key.

```yaml
---
title: "Monthly Sales Report"
params:
  region: "North America"
  year: 2025
  show_raw_data: false
---

```

## 2. How to Use Parameters

Once defined, you can access these parameters within your code cells. The syntax depends on which engine you are using:

### Using Python (Jupyter Engine)

Quarto makes a `params` dictionary available in your environment.

```python
#| echo: false
print(f"Generating report for: {params['region']}")

if params['show_raw_data']:
    display(df.head())

```

### Using R (Knitr Engine)

Parameters are stored in a list called `params`.

```r
print(params$region)

```

---

## 3. How to Render with New Values

When you are ready to automate, you pass the new values via the Command Line Interface (CLI). You do **not** need to edit the `.qmd` file.

### Via Terminal (CLI)

Use the `-P` flag to override the defaults:

```bash
quarto render report.qmd -P region:"Europe" -P year:2026

```

### Via Python Script

If you want to loop through many regions and generate multiple PDFs/HTML files, you can use the `quarto` Python package:

```python
import subprocess

regions = ["North America", "Europe", "Asia"]

for r in regions:
    subprocess.run([
        "quarto", "render", "report.qmd", 
        "-P", f"region:{r}", 
        "--output", f"report_{r}.html"
    ])

```

---

## Why this is better than "Search and Replace"

* **Type Safety:** Quarto treats `2025` as a number and `false` as a boolean, rather than just raw text strings.
* **Default Values:** Your document remains "runnable" on its own because it uses the defaults defined in the YAML.
* **Environment Integration:** You can use these parameters directly in your data queries (e.g., in a SQL `WHERE` clause) or for conditional formatting.

Would you like me to help you write a small Python or Bash loop to automate rendering a batch of these reports?
