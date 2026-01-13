Choosing **Quarto** over a traditional system like **MkDocs** is a strategic move for an engineering project that relies on a "CAD-as-code" system like **build123d**.

While MkDocs is excellent for software API documentation, Quarto is designed for **Computational Publishing**. This distinction is critical for your 3D printer project.

---

### Quarto vs. MkDocs: The Engineering Perspective

| Feature | **MkDocs (with Material theme)** | **Quarto** |
| --- | --- | --- |
| **Primary Use Case** | Software libraries, "Vignettes" | Technical reports, Books, Engineering docs |
| **Code Execution** | Static (Shows code only) | **Live (Executes code during render)** |
| **Math/Science** | Excellent (via extensions) | **Native (Pro-grade LaTeX/Typst support)** |
| **Cross-Referencing** | Limited (Manual/Plugins) | **Deep (Auto-numbered Figs, Tabs, Eqs)** |
| **Output Formats** | Mostly HTML | **HTML, PDF, Word, ePub (Single Source)** |
| **Visual Editor** | No (Markdown only) | **Yes (Word-like interface for prose)** |

---

### Why Quarto Wins for Your Project

#### 1. "Literate CAD" Integration

With MkDocs, if you want to show a screenshot of a part, you have to:

1. Run your build123d script.
2. Manually take a screenshot.
3. Save the image and link it in Markdown.

With **Quarto**, you can use Python code cells directly in your `.qmd` files. When you render the documentation, Quarto can **trigger the build123d script, generate the part, and automatically embed a render** or a 3D view into the document. This ensures your documentation is never "out of sync" with your code.

#### 2. Professional PDF Assembly Guides

MkDocs is web-first; its PDF generation is often an afterthought and can look "website-y."
For a 3D printer, users often want a **high-quality, printable PDF assembly manual**. Quarto uses **LaTeX** (or the newer, faster **Typst**) to create PDFs that look like professional textbooks, with automatic page numbering, table of contents, and high-resolution diagrams.

#### 3. Deep Cross-Referencing

In a build guide, you often need to say: *"Refer to the bolt shown in Figure 4.2."*

* **MkDocs:** You have to manage these numbers manually.
* **Quarto:** You simply use `@fig-bolt-assembly`. If you add a new figure earlier in the document, Quarto automatically renumbers everything for you.

#### 4. The "Single Source of Truth"

You are building a system with many permutations. Quarto supports **conditional content**. You can write one master documentation file that hides or shows certain sections based on the user's `config.py`.

> *Example: "If `printer_type == 'XL'`, include the 'Large Bed Leveling' section; otherwise, skip it."*

---

### Summary for your ADR

"While **MkDocs** is the industry standard for software documentation, it lacks the native computational execution required for a parametric hardware project. **Quarto** allows us to treat our documentation as an extension of our code, enabling automated rendering of **build123d** models directly into professional-grade HTML and PDF assembly manuals."

**Would you like me to show you a sample `.qmd` structure that includes a build123d code block?**
