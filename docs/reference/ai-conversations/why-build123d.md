Settling on **build123d** is a sophisticated choice that aligns perfectly with a "software-first" engineering mindset. While tools like OpenSCAD pioneered "CAD-as-code," build123d represents a generational leap by moving from basic constructive geometry to a full **BREP (Boundary Representation)** kernel (OpenCascade) within a standard Python environment.

Below is a comparison to help justify this decision in your ADR and documentation.

---

### Comparison of CAD Paradigms

| Feature | **TinkerCAD** | **FreeCAD (GUI)** | **OpenSCAD** | **build123d** |
| --- | --- | --- | --- | --- |
| **Core Paradigm** | Simple CSG (Visual) | BREP (Feature Tree) | Scripted CSG | **Scripted BREP** |
| **Language** | None (Drag/Drop) | Python (Optional) | OpenSCAD (Domain) | **Python (Native)** |
| **Geometry** | Meshes | Precise NURBS | Meshes/CSG | **Precise NURBS/STEP** |
| **Selection** | Mouse | Mouse (Unstable) | Manual Math | **Smart Selectors** |
| **Version Control** | Poor | Difficult (Binary) | Excellent (Text) | **Excellent (Python)** |

---

### Why the others were likely rejected

#### 1. OpenSCAD (The "Old Guard" of Code-CAD)

* **The Math Tax:** OpenSCAD doesn't "know" where a face or edge is. If you want to put a hole 5mm from the edge of a block, you have to keep track of the block's coordinates in your head. If the block size changes, you must update the math manually.
* **Fillet/Chamfer Nightmare:** Because it uses CSG (adding/subtracting shapes), doing a simple fillet on a complex edge is mathematically exhausting and often renders slowly.
* **Non-Standard Language:** You have to learn a proprietary, functional language that doesn't exist outside of OpenSCAD.

#### 2. FreeCAD & GUI Systems

* **The "Topological Naming" Problem:** In FreeCAD, if you change a dimension early in the tree, the internal names of faces often "shuffle." This breaks all subsequent features (your hole is suddenly on the wrong side).
* **Hard to Automate:** While FreeCAD has a Python API, it is bolted onto a GUI-first workflow, making it "clunky" for a pure CLI build system like yours.

---

### Why build123d is "The Future"

**Build123d** feels like the future because it treats 3D design like **modern software engineering**.

1. **Object Awareness (The BREP Advantage):** Unlike OpenSCAD, build123d understands topology. You can tell the script: *"Find the top-most face and fillet all edges that are parallel to the X-axis."* If the part grows or shrinks, the script still finds that face correctly.
2. **Native Python Power:** You aren't limited to a niche CAD language. You can use `pip install` to bring in NumPy for complex math, `requests` to pull data from an API, or `logging` to debug your build.
3. **The "Builder" vs. "Algebra" Modes:** It offers a "Builder" context (using `with` statements) that mimics how humans think about building—*“I am working on this face, now I am sketching here”*—making the code highly readable.
4. **Professional Output:** It exports true **STEP files**, which are the industry standard for CNC and professional manufacturing. OpenSCAD is largely stuck in the world of STL (meshes).

---

### Integration with Quarto

Since you are using **Quarto**, your choice of build123d is even more powerful. Quarto is built to execute Python code cells and render the results.

* **Literate CAD:** You can write your assembly documentation in Quarto and include the actual build123d code snippets.
* **Automated Diagrams:** You can use a Python library (like `cq-editor` or `ocp-vscode` helpers) to capture renders of your parts during the Quarto render process.
* **Single Source of Truth:** Your documentation and your 3D geometry can live in the same `.qmd` or `.py` files.

**Would you like me to help you draft the "Rationale" section of your ADR, specifically highlighting how build123d solves the "Topological Naming" issues found in other systems?**
