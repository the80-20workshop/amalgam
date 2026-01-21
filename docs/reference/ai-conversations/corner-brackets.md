[Gemini](https://gemini.google.com/app)  
I am building a box frame 3D printer using M12 threaded rods for the frame. I am designing the corner brackets and wold like to  
My stuff  
**Gemini Apps activity is off**  
[Turn it on here](https://myactivity.google.com/product/gemini?utm_source=gemini)  
[Opens in a new window](https://myactivity.google.com/product/gemini?utm_source=gemini)

# **Conversation with Gemini**

I am building a box frame 3D printer using M12 threaded rods for the frame. I am designing the corner brackets and wold like to discuss some challenges. Firstly strategies on getting the frame square, do we extend the arms of the brackets so we are dimensionally square, that make the bracker a bigger right angle or something? I notice on the old ReRap and the Prusa MK2, where they use M8 threaded rods, that the rode extend through minimal bracket, think a nut eiter side of the bracket and the one on the outside a second locking one for minor adjustement. But with the box design and three M12 rod converging in the corner what can we do? Although we can 'cut' the M12, this will not be a precision cut, so how can we adjust a rod, how can we make each side square etc. What are some strategties, build the left, then build the right, then join left-right side to build the front, then complete the back

Not too large, will need to support 235x235x235 build volume, so a little bigger than that. The ofset jig seem like it would be easier to adjust. I am building the brackets in build123d, so technically 'pytohn' could calcualte the 'centre', but given we plannign to have triple-z stepper motors, I think the Clevis or Nub might be better, perhaps with extended sleves, I cna see how a nut can pul is out from the sleve, not sure how to pull into the sleve, there a cutout to take a nuy in the sleve sloe to the corner, abd a nut on the M12 nut (outside of the sleve. Manually twist the M\!@ and it thread on to the internal nut (but will undo the opposite end correct) and how would we 'lock' this in place.

So not sure how to tighten the inner nut. So there a cutout fo rthe nut and space for a spanner? How did the opriginal Darwin RepRap do corners?

So should we switch to this offset method, we should be able to make each plane in the samw location, so in y (front to back)all on the inside etc

The **Offset Method** (the Darwin/RepRap style) is generally superior for a threaded-rod build because it simplifies the two biggest headaches: **rod cutting** and **squaring**.

By using the offset method, you treat the threaded rods as "rails" that the brackets slide along. This turns the assembly process from a "puzzle where every piece must be exact" into a "jig where every piece is adjustable."

---

## **1\. The "Standardized Plane" Strategy**

To keep your frame from becoming a confusing mess of offsets, you should follow a strict **Inside/Outside rule**. This ensures that despite the rods being offset, the *faces* of your printer remain flush and predictable for mounting panels or belts.

### **The Recommended Layout:**

* **X-Rods (Left-to-Right):** Place these on the **outermost** layer.  
* **Y-Rods (Front-to-Back):** Place these in the **middle** layer.  
* **Z-Rods (Vertical):** Place these on the **innermost** layer.

### **Why this works for Triple-Z:**

By keeping the **Z-rods on the inside**, you create a clear, unobstructed path for your build plate to move up and down. If the vertical rods were on the outside, the horizontal X and Y rods would "block" the bed's movement or require massive, complex bed brackets to reach around the frame.

---

## **2\. Designing the "Offset Bracket" in** build123d

In a box frame, your corner bracket needs to hold three rods that don't touch. Imagine a cube where:

1. The **X-rod** passes through a hole in the front face.  
2. The **Y-rod** passes through a hole 20mm behind it.  
3. The **Z-rod** passes through a hole 20mm to the side of that.

Since you are using Python, you can define these offsets as variables:

Python

offset \= 20 \# Distance between rod centers  
m12\_rad \= 6.2 \# Clearance for M12

\# In build123d, you would create three cylinders (the sleeves)   
\# and join them with a central 'block' or 'web'.  
with BuildPart() as corner:  
    \# Sleeve for X  
    with BuildSketch(Plane.YZ) as s1: Circle(15)  
    extrude(amount=50)  
      
    \# Sleeve for Y (offset in X and Z)  
    with BuildSketch(Plane.XZ.offset(offset)) as s2: Circle(15)  
    extrude(amount=50, dir\=(0,1,0))  
      
    \# Sleeve for Z (offset in X and Y)  
    with BuildSketch(Plane.XY.offset(offset)) as s3: Circle(15)  
    extrude(amount=50, dir\=(0,0,1))  
      
    \# Add a 'Hull' or a central box to connect these three tubes

---

## **3\. How to Square an Offset Frame**

The beauty of the offset method is that the rod length doesn't matter. If one rod is 5mm longer than the others, it just sticks out 5mm further past the nut.

1. **The Reference Face:** Pick one side (e.g., the Left Side). Assemble it on a flat table. Use a ruler to ensure the distance between the front and back Z-rods is exactly your target (e.g., 400mm). Lock the nuts.  
2. **The Mirror Side:** Assemble the Right Side. Use your ruler to match the *exact* distances you used on the Left Side.  
3. **The Squaring Measurement:** This is the most important part. Use a digital caliper or a fixed-length stick to measure the **diagonals** of the rectangles.  
   * If the diagonal from Top-Front to Bottom-Back is 565*mm* and the other is 567*mm*, your box is leaning.  
   * **The Fix:** Simply loosen the nuts on one rod and "nudge" the bracket 1*mm* until the diagonals match perfectly.

---

## **4\. Stability Tip: "The Triangulation"**

Box frames made of threaded rods can "rack" (tilt like a deck of cards) because M12 rods, while thick, can still pivot slightly at the nut interface.

**The Solution:** Since you have extra rod length with the offset method, you can easily add **diagonal braces**. A simple 45-degree M12 rod connecting the bottom-back-left corner to the top-back-right corner will make the frame exponentially more rigid than just the box alone.

---

**Would you like me to generate a** build123d **script for a "Universal Offset Corner" that you can use for all 8 corners of the box?**

OKay, squaring might kill the project. the Diagonale make sense, but is there a jig we can build, like how they square joints in woodworking? I realise the rode are ofset, but we could print a ofset square tool or something?

Also, we support a 235x235 headbed, to x-y will be larger to handle z motoers etc. Height can be anything up to about 280 marx (seem safe)

Squaring a frame doesn't have to be a nightmare of measuring and re-measuring. In woodworking, we use **clamping squares** and **assembly jigs**. Since you are 3D printing your parts, you can print your own "Precision Squaring Jigs" that account for the M12 rod offsets.

Here is how to design a system that makes squaring almost automatic.

---

## **1\. The "Squaring Block" Jig**

Instead of relying on a tape measure, print four **Squaring Blocks**. These are simple L-shaped tools that "snap" onto the M12 rods at the corners.

### **How it works:**

* The jig has two semi-circular channels for the M12 rods.  
* The channels are placed at exactly 90° to each other.  
* **The Magic:** The jig accounts for the "offset" (e.g., Rod X is 20mm higher than Rod Y). You print the channels at different heights on the jig so that when the rods sit in them, they are forced into a perfect 90° relationship in 3D space.

**Assembly Hack:** Use zip-ties to hold the rods into these jigs while you tighten the M12 nuts. Once the nuts are locked, snip the zip-ties and move the jig to the next corner.

---

## **2\. The "Internal Distance" Gauges**

The most common error in box frames is "Parallelogramming," where the top is shifted slightly to the left compared to the bottom.

To fix this, print two **"Gauge Sticks"**.

1. In build123d, design a simple rod or tube that is exactly your target internal frame dimension (e.g., 350mm).  
2. Place these sticks between your brackets at the bottom. Tighten.  
3. Move the *same sticks* to the top. If they don't fit or are loose, you know exactly which nut to turn.  
4. **This is much more accurate than a tape measure** because it eliminates human reading error.

---

## **3\. Dimensional Planning (235x235 Bed)**

To support a 235mm bed with Triple-Z motors and a toolhead, your frame needs "breathing room." If the frame is too tight, your cables will rub and your motors won't fit.

### **Recommended "Outside" Frame Dimensions:**

For a 235x235 bed, I recommend a rod-center-to-rod-center footprint of approximately **380mm x 380mm**.

| Axis | Calculation | Total Rod Length (Estimated) |
| :---- | :---- | :---- |
| **X (Width)** | Bed (235) \+ Lead Screws/Motors (80) \+ Clearance (65) | **\~450mm** |
| **Y (Depth)** | Bed (235) \+ Y-Carriage Travel (50) \+ Motor (60) | **\~450mm** |
| **Z (Height)** | Build Height (280) \+ Motor/Coupler (70) \+ Top Bracket (50) | **\~500mm** |

*Note: With the offset method, you can always buy 1-meter rods and cut them in half (500mm). Having "too much" rod sticking out isn't a problem; you can just put a plastic cap on the end.*

---

## **4\.** build123d **Logic for the Corner Bracket**

Since you want to ensure the vertical (Z) rods stay square, the bracket should have a "Sleeve" for the Z-rod that is at least 60mm tall. This acts as a physical guide.

Python

\# build123d Concept: Offset Corner with Support Web  
offset\_dist \= 25 \# Distance to prevent rod collision

with BuildPart() as corner\_bracket:  
    \# 1\. Create three cylinders (sleeves) at offsets  
    \# X-Sleeve  
    with BuildSketch() as s1: Circle(16)  
    extrude(amount=60)  
      
    \# Y-Sleeve (Offset in X and Z)  
    with BuildSketch(Plane.XZ.offset(offset\_dist)) as s2: Circle(16)  
    extrude(amount=60, dir\=(0,1,0))  
      
    \# Z-Sleeve (The tall one for squaring)  
    with BuildSketch(Plane.XY.offset(offset\_dist)) as s3: Circle(16)  
    extrude(amount=80, dir\=(0,0,1))  
      
    \# 2\. The "Squaring Web"   
    \# This joins the three tubes into a single rigid block.  
    \# A simple 'hull' or a 'Box' that encompasses the centers.  
    add(Hull(corner\_bracket.solids()))  
      
    \# 3\. Subtract the M12 Holes (13mm for clearance)  
    \# \[Insert hole subtraction logic here\]

---

## **5\. The "Golden Rule" for Assembly**

To avoid the "Squaring Kill," follow this sequence:

1. **Build the Floor:** Get the bottom four rods square using the diagonal method and the printed jigs. **Lock these nuts permanently.**  
2. **The "Plumb" Pillars:** Install the 4 vertical rods. Use a **spirit level** or a **plumb bob** (a weight on a string) to ensure they are vertical.  
3. **The "Top Cap":** Slide the top square onto the pillars. Because the bottom is locked and the pillars are "plumb," the top should naturally fall into place.

**Pro Tip:** Use **Nyloc nuts** for the final "locking" nut. They won't vibrate loose when the printer starts moving fast.

---

**Would you like me to draft a more detailed** build123d **script for the squaring jig specifically, or should we look at how to mount the Triple-Z lead screws to these M12 rods?**

With rods 450, 450, 500, wil M12 be strong enough? Als is it worth keeping the jigs on the fram for 'bracing' (just print more)

At **M12 (12mm diameter)**, you are moving from the "hobbyist" scale of the original RepRaps (M8) into "industrial/heavy machinery" territory.

### **1\. Is M12 Strong Enough?**

**Short answer: Yes, it is overkill.** For a frame with spans of 450mm–500mm, M12 steel threaded rod is incredibly stiff. To put it in perspective:

* **M8 rods** (8mm) have a cross-sectional area of about **50** *mm*  
* 2  
* .  
* **M12 rods** (12mm) have an area of about **113** *mm*  
* 2  
* .

You have more than double the steel of a standard Prusa-style frame. At 500mm lengths, the "sag" or "flex" from the weight of the printer head or a 235mm heated bed will be negligible. The main challenge won't be the strength of the steel, but the **rigidity of the joints**. Because you are using threaded rods, the frame's weak point is "racking" (the box tilting into a diamond shape).

---

### **2\. Using Jigs as Permanent Bracing**

**This is an excellent idea.** In engineering, this is essentially moving from a "pinned joint" to a "gusseted joint."

If you keep the squaring jigs on the frame, they act as **structural gussets**. Instead of the rod just being held by a nut against a thin plastic wall, the jig provides a long surface area that prevents the rod from pivoting.

#### **Strategies for "Bracing Jigs":**

* **The "Long Sleeve" Approach:** Design your corner brackets to be the jigs themselves. Instead of a small bracket, make the "sleeves" that hold the rods 60mm–100mm long. The longer the sleeve, the harder it is for the rod to "tilt" out of square.  
* **Triangulation (The True Fix):** If you find the frame still has a tiny bit of "wobble," you can use your M12 rod to create a **diagonal cross-brace** on the back and side faces. Even a single diagonal rod turned into a triangle will make the frame stiffer than any amount of thick plastic.

---

### **3\. Revised** build123d **Design for "Jig-Brackets"**

Since you are using Python, you can design a "Master Corner" that serves as both the connector and the squaring jig.

**Key Design Features:**

1. **Deep Sockets:** The rod should pass through at least 50mm of plastic.  
2. **Ribbing:** Add "webs" or "gussets" between the X, Y, and Z sleeves.  
3. **Nut Pockets:** Use the "Nut Sandwich" method we discussed, but put the nuts at the *ends* of the long sleeves to maximize leverage.

Python

\# Conceptual build123d structural corner  
with BuildPart() as corner:  
    \# Create the three sleeves as a single solid  
    \# We use a large 'Box' and then subtract the rod paths   
    \# to ensure the 'meat' of the bracket is solid.  
    with BuildSketch() as s:  
        \# A 60mm cube provides massive squaring surface  
        Rectangle(60, 60)  
    extrude(amount=60)  
      
    \# Now subtract the offset paths for M12  
    \# X path: offset by 15mm from bottom, 15mm from side  
    \# Y path: offset by 35mm from bottom, 35mm from side  
    \# Z path: offset in the remaining quadrant

---

### **4\. Weights and Vibrations**

One thing to keep in mind: **This frame will be heavy.** \* 450mm of M12 steel rod weighs about **0.33kg**.

* With 12 rods (4 per axis), plus nuts and brackets, your frame alone will weigh **5kg to 7kg**.

**The Benefit:** Mass is great for 3D printing. A heavy frame absorbs the "ringing" (ghosting) caused by the rapid changes in direction of the print head. Your M12 frame will likely produce much cleaner prints at high speeds than a lightweight aluminum extrusion frame.

---

### **Summary Checklist for your Build**

* **Rods:** 450mm (X), 450mm (Y), 500mm (Z).  
* **Brackets:** Use the "Offset" method to avoid cutting precision.  
* **Squaring:** Print "Gauge Blocks" (fixed-length spacers) to ensure the distance between brackets is identical on all four sides.  
* **Locking:** Use **Washers** between every nut and the plastic to prevent the nut from sinking into the print over time.

**Would you like me to help you design the "Triple-Z" motor mounts so they integrate directly into these heavy-duty M12 corner brackets?**

Okay, long sleve seem better approach. So is M10 enough? I just picked M12 cause more mass, and I saw someone do M12 in Mendel?

M10 is more than enough for a printer of this size. In fact, **M10 is often considered the "Sweet Spot"** for threaded-rod builds.

While M12 is impressively rigid, moving to M10 offers some practical advantages without sacrificing the structural integrity needed for a 235mm build volume.

### **1\. Comparing M10 vs. M12**

| Feature | M10 (10mm) | M12 (12mm) |
| :---- | :---- | :---- |
| **Cross-section** | \~78 *mm* 2 | \~113 *mm* 2 |
| **Rigidity** | Very High (3x M8) | Overkill (5x M8) |
| **Weight/Meter** | \~0.5 kg | \~0.7 kg |
| **Nut Size (Hex)** | 17mm | 19mm |
| **Printability** | Easier to fit into brackets | Can make brackets bulky |

**Why M10 might be better for you:**

* **Bracket Size:** An M12 nut is 19mm across the flats. Once you add 5mm of plastic wall on either side for a sleeve, your bracket becomes quite chunky. M10 allows for slightly sleeker, more refined parts.  
* **Hardware Availability:** M10 is incredibly common in automotive and construction. You can find "Flanged M10 Nuts," which are amazing for 3D printer frames because the built-in washer distributes the load perfectly against the plastic.

### **2\. Why did people use M12 in the Mendel?**

The original **Mendel** used M8. The version you likely saw was the **MendelMax 1.5/2.0** or a custom large-scale variant.

* **Vibration Damping:** Those builders wanted the frame to be so heavy that it couldn't move, even if the print head was heavy.  
* **Tensioning:** In a triangular Mendel, the rods are under tension. In your **Box Frame**, the rods are under compression and bending loads. M10 handles these beautifully for a 500mm span.

---

### **3\. Design Strategy: The "Long Sleeve" M10 Bracket**

Since you are using build123d, you can take advantage of the long sleeve for squaring. Here is how to optimize that bracket:

**The "Internal Stop" Design:** Instead of the rod passing all the way through, you can design the sleeve with a "shoulder" inside.

1. One rod enters from the left and hits a wall.  
2. One rod enters from the front and hits a wall.  
3. Because your Python code defines exactly where those "walls" are, the rods themselves help square the frame.

---

### **4\. Should you keep the "Jigs" as Bracing?**

**Yes, but integrate them.** Rather than having a "corner bracket" and a separate "jig," design a **Gusseted Corner**.

* In build123d, after you've created your three sleeves, use a Fillet or a Chamfer with a very large radius (e.g., 20mm or 30mm) to create a web of plastic between the sleeves.  
* This "Web" acts as a permanent squaring jig. It prevents the 90-degree angle from ever changing.

Python

\# build123d: Adding structural webbing between M10 sleeves  
with BuildPart() as corner:  
    \# (Sleeve creation code here...)  
      
    \# Create a triangular web between X and Y sleeves  
    with BuildSketch(Plane.XY) as web:  
        Polygon(\[(0,0), (50,0), (0,50)\])  
    extrude(amount=10) \# A 10mm thick structural plate

---

### **5\. Final Verdict on Rod Choice**

* **Stick with M12 if:** You already bought the rods or you want the absolute "tank" of a printer that will never move.  
* **Switch to M10 if:** You want a slightly easier time designing the brackets and want to save a little on the cost of nuts and washers.

Given your build volume (235mm), **M10 is the logical engineering choice**, but **M12 is the "cool" choice** for a heavy-duty industrial feel. Both will work perfectly for your squaring strategies.

---

**Would you like me to focus the next step on designing a Triple-Z lead screw mount that clamps onto the M10/M12 horizontal rods?**

Here the M12 version: https://www.thingiverse.com/thing:6783269

I affectionately call the design/printer "The Tractor"

"The Tractor" is a perfect name for an M12-based machine. Looking at the design philosophy of those heavy-duty threaded rod builds, you are essentially building a piece of industrial equipment rather than a desktop toy.

Since you've settled on the **M12 "Tractor"** build, let’s refine the strategy to ensure that mass works *for* you and doesn't become a nightmare to square.

### **1\. The "Tractor" Advantage: Massive Pre-load**

With M12, the amount of force you can apply with a standard wrench is enormous. You aren't just "holding" the frame together; you are **pre-loading** the plastic.

* **The Benefit:** Once you get those M12 nuts tightened against your long-sleeve brackets, the friction between the nut, washer, and plastic becomes a structural element.  
* **The Strategy:** Use **extra-thick fender washers** (M12 washers with a large outer diameter). This prevents the high torque from crushing the 3D-printed walls while ensuring the "grip" is distributed over a wider area, which drastically helps maintain squareness.

---

### **2\. Squaring "The Tractor" with Long Sleeves**

Since you are using build123d, you can design the sleeves to be **"Self-Centering Jigs."**

If your sleeve is, say, 60mm long, the rod has very little room to tilt. To make squaring "automatic," you can add **Internal Alignment Fins** inside the sleeve:

1. Instead of a perfectly smooth 13mm hole for the M12 rod, model three small longitudinal "ribs" (0.2mm high) inside the hole.  
2. The rod will "bite" into these ribs as it slides in.  
3. This centers the rod perfectly within the sleeve, ensuring that the rod's center axis is exactly where your Python code says it should be.

---

### **3\. Triple-Z on a Heavy Frame**

With an M12 frame, your Z-axis needs to be equally robust. For a "Tractor" build, mounting your Z-motors requires a bracket that doesn't just "sit" on the rod but **clamped** to it.

**The "Clamped Hub" Design:** Instead of a simple hole, design the motor mount with a "split" side.

* Use M5 bolts to "pinch" the M12 rod.  
* This allows you to slide the Z-motors to the *exact* micro-millimeter location to align with your bed's mounting points before locking them down.

---

### **4\. Integration Logic in** build123d

For "The Tractor," your corner code should probably look like a **structural node**. In build123d, you can use the hull() function effectively here to create a "solid mass" around the rod intersections, which fits the aesthetic and functional needs of a heavy printer.

Python

\# build123d logic for a 'Tractor' Corner  
with BuildPart() as tractor\_corner:  
    \# 1\. Define the three sleeves (X, Y, Z) as cylinders  
    \# Use the 'Offset' method we discussed (rods bypass each other)  
    \# 2\. Add a 'Structural Shell'  
    \# Use a large Box or a Sphere that encompasses all intersections  
    \# 3\. Use 'Fillet' on all edges (R=5mm or more)  
    \# This reduces stress concentrations which is vital for heavy frames.

---

### **5\. Assembly Tip: "The Leveling Feet"**

Because M12 rods are so heavy, "The Tractor" will be sensitive to whatever surface it sits on.

* **Next Step:** Design the **bottom 4 corner brackets** to include a threaded hole (or a trapped nut) for an **M10 or M12 leveling foot**.  
* This allows you to square the *frame* perfectly, and then "level" the printer to the table, preventing the heavy frame from rocking or vibrating during fast infills.

---

**Since you're using** build123d**, would you like a snippet of code that generates the "Offset Window" for the M12 nuts specifically tailored for the "Tractor" sleeves?**

I haven't settled on M12, just thought the mass damping effect would be better. But if it feels too industrial heavy might turn of users.

That is a valid concern. In the world of DIY 3D printing, there is a fine line between "Industrial/Robust" and "Over-engineered/Intimidating."

If your goal is to share this design with others (like on Thingiverse or Printables), the "mass damping" benefits of M12 might be outweighed by the **"User Friction"** of dealing with heavy steel.

Let's look at the trade-offs of scaling down to **M10** while keeping the "Tractor" spirit.

---

## **1\. The "Aesthetic" and "Feel" Comparison**

* **M12 (The Tractor):** It feels like you’re building a bridge or a car chassis. It requires large wrenches, heavy-duty washers, and the parts look "chunky." It appeals to the "Overkill is best" crowd.  
* **M10 (The Heavy-Duty Consumer):** It still feels significantly more robust than a standard Prusa (M8), but it looks more "proportionate" for a 235mm bed. It’s the "Goldilocks" size—heavy enough to damp vibration, but light enough to not feel like industrial scrap.

---

## **2\. Practical "User Experience" (UX) Challenges**

If you want users to build this, consider these "Friction Points":

| Feature | M10 Experience | M12 Experience |
| :---- | :---- | :---- |
| **Tooling** | Standard 17mm wrench (very common). | 19mm wrench (common, but getting bulky). |
| **Rod Prep** | Can be cut with a standard hacksaw easily. | Requires a lot of elbow grease or an angle grinder. |
| **Printed Parts** | Thinner walls allowed; fits on small beds. | Requires thick walls; might exceed small printer volumes. |
| **Weight** | \~5kg total frame weight. | \~8kg+ total frame weight. |

---

## **3\. The "Damping" Reality**

Mass damping is excellent for high-speed printing to prevent "ghosting." However, once your frame is **rigid enough that it doesn't flex**, adding more mass has diminishing returns.

For a **235x235x280mm** printer:

* **M8** is the bare minimum (needs careful bracing).  
* **M10** is incredibly stiff and provides ample mass damping for high speeds (Klipper/Input Shaping).  
* **M12** is essentially a "static monument." It won't move, but it might be overkill for the forces a standard NEMA 17 motor generates.

---

## **4\. Designing for "The Masses" (The Hybrid Approach)**

If you are worried about turning off users, you can use build123d to make your design **Parametric**.

Since you are writing in Python, you can set a single variable at the top of your script:

Python

rod\_diameter \= 10  \# User can change this to 10 or 12

If you design your sleeves and nut traps based on that rod\_diameter variable, users can choose their "level of overkill."

### **The "Long Sleeve" Squaring Fix for M10**

Even with M10, keep the **Long Sleeve (50mm+)** strategy.

* **Why:** It solves the "Squaring" problem for the user.  
* **The UX:** The user slides the rod in, and the long sleeve physically prevents them from putting it in crooked. It makes the assembly "foolproof," which users love more than they love heavy steel.

---

## **5\. Decision Matrix: Which one to choose?**

* **Go with M12 if:** You want to lean into the "Tractor" brand. It’s unique, it’s a tank, and it’s a statement piece. It will be the "heaviest" printer in its class.  
* **Go with M10 if:** You want a balance of performance and accessibility. It will still be much more stable than an aluminum extrusion frame but won't require a crane to move it.

**Design Tip:** If you choose M10, you can use **Flanged Nuts**. They look very "pro" and "clean," whereas M12 usually requires the nut \+ a giant separate washer, which looks a bit more "hardware store DIY."

---

**Would you like me to show you how to structure a** build123d **script so it can automatically adjust the bracket dimensions for either M10 or M12?**

I also calling it a 'scavenger' build, you mention the M10 common in automative, would this sit better using M10. Yes rod size was a parameter, heck they can build in M8. But I was going to pick one rod size as the 'reference specification'

If you are leaning into the **"Scavenger"** and **"Tractor"** themes, **M10 is the strongest candidate for your reference specification.**

While M12 is the "Tractor" in terms of raw power, M10 is the "Tractor" in terms of **versatility and ubiquity.** In the world of scavenging, M10 is everywhere.

---

### **1\. Why M10 is the "Reference Specification" King**

Choosing M10 as your baseline offers a better balance for a community-driven scavenger build:

* **Automotive Goldmine:** Go to any scrap yard or mechanic's bin, and you will find M10 bolts and nuts. They are the standard for suspension components, engine mounts, and seat rails.  
* **The "Standard" Toolset:** Almost every household or basic tool kit includes a **17mm wrench/socket**. An 19mm (for M12) is common, but 17mm is the universal "medium-heavy" standard.  
* **Weight vs. Strength:** M10 provides roughly 1.5× **the rigidity of M8** but doesn't have the massive "bulk" of M12 that requires giant printed parts. It fits the "Scavenger" vibe: resourceful, tough, but not needlessly heavy.

---

### **2\. Squaring Strategy: The "Scavenger's Jig"**

Since this is a scavenger build, your users might not have precision granite surface plates to square their frames. You should lean into the **"Long Sleeve \+ Internal Stop"** method we discussed.

In build123d, you can design the reference corner so that the user simply pushes the rod until it hits a printed "back wall" inside the sleeve.

**How to make this "Scavenger-Proof":**

1. **The Depth Stop:** If every sleeve is exactly 50mm deep to the "stop," the user doesn't even need a ruler. They just tighten the nut until the rod is bottomed out.  
2. **The Nut Window:** Provide a generous window for a 17mm spanner.  
3. **The "Scavenger" Hack:** Design the bracket to accept **any** M10 nut (flanged, nyloc, or standard hex).

---

### **3\. The "Scavenger" Aesthetic (Industrial & Accessible)**

To avoid turning off users, your build123d design should look **purposeful**.

* **Exposed Ribbing:** Instead of a solid block of plastic, use structural ribs. This looks "engineered" (like a tractor's cast-iron frame) and saves filament.  
* **Clamping Interfaces:** Use "Split-Collars" (clamped with M5 bolts) for things like motor mounts. This feels more "mechanical" and allows for easier adjustment than a fixed hole.

---

### **4\.** build123d **Parametric Structure**

Here is how I would structure your "Reference Spec" script to handle the M8/M10/M12 flexibility while keeping the "Long Sleeve" squaring logic:

Python

\# The Scavenger Reference Parameters  
rod\_type \= "M10"   
params \= {  
    "M8":  {"dia": 8.5,  "nut\_flat": 13, "sleeve\_od": 22},  
    "M10": {"dia": 10.5, "nut\_flat": 17, "sleeve\_od": 28},  
    "M12": {"dia": 12.5, "nut\_flat": 19, "sleeve\_od": 32}  
}

p \= params\[rod\_type\]  
sleeve\_length \= 60  \# Long sleeve for squaring leverage

with BuildPart() as corner:  
    \# 1\. Create the 'Chassis' of the corner  
    \# (Using the sleeve\_od to ensure walls are thick enough)  
      
    \# 2\. The 'Bottom-Out' Hole  
    \# Instead of a through-hole, leave 5mm of plastic at the end   
    \# as a physical stop for squaring.

---

### **5\. Final Comparison for the "Scavenger"**

* **M8:** Feels like a "toy" Mendel. Might vibrate too much for high speed.  
* **M10:** Feels like a "Machine." Robust, common, and incredibly easy to square with your long-sleeve design. **(Recommended Reference)**.  
* **M12:** Feels like "Heavy Infrastructure." Impressive, but perhaps too niche for a general scavenger build.

**Would you like me to draft the full** build123d **logic for a "Universal Scavenger Corner" that uses these M10 internal stops for "automatic" squaring?**

I alos plan to fasten the frame to 2x18mm MDF board laminated together with PVA glue. sO that will give more dampening correct (and pbviously running klipper intpu shaping an dpresure advance will handle the rest)

Mounting your frame to a **36mm thick (2x18mm) laminated MDF base** transforms "The Tractor" from a printer into a **monolithic machine tool**.

You are effectively creating a "Mass-Spring-Damper" system where the mass is so high that the vibrations from the stepper motors simply won't have the energy to move the frame. This is exactly how high-end CNC mills are designed (often using polymer concrete bases).

---

## **1\. The Dampening Effect**

Yes, this will provide incredible dampening.

* **Mass:** 36mm of MDF is heavy. Adding that mass to the bottom of your M10/M12 frame lowers the **Center of Gravity (CoG)** significantly. A low CoG prevents the printer from "swaying" during rapid X/Y accelerations.  
* **Material Properties:** MDF is made of wood fibers and resin; it is internally "lossy," meaning it converts mechanical vibration into tiny amounts of heat rather than ringing like a bell.  
* **Input Shaping:** With Klipper, your resonance frequencies will likely be very high and very clean. This makes the Input Shaping calibration much more effective because you won't have the "muddy" low-frequency wobbles found in flimsy extrusion frames.

---

## **2\. Squaring Strategy: The "Baseplate Anchor"**

Since you are bolting to a baseboard, the board itself becomes your **Master Square**.

Instead of just sitting the printer on the wood, you should design **Anchor Brackets** in build123d for the four bottom corners.

### **The "Scavenger" Squaring Workflow:**

1. **Prep the Board:** Ensure your 36mm MDF is cut as a perfect rectangle.  
2. **Mount the Anchors:** Print four base-corners. Bolt them to the MDF first.  
3. **Insert the Rods:** Slide your horizontal M10/M12 rods into these anchored corners.  
4. **The Result:** Because the board is square and the anchors are fixed to the board, the rods are *forced* to be square. You are using the wood as a "Squaring Jig" that stays with the printer forever.

---

## **3\. Dealing with MDF’s "Weakness"**

MDF is great for mass, but it has two issues: it hates moisture, and it doesn't hold threads well.

* **The "Tractor" Way:** Do not screw into the MDF. **Bolt through it.** \* Use a spade bit to counter-bore the bottom of the MDF so the bolt heads are flush. Use large washers on the underside to prevent the bolts from pulling through the wood.  
* **Sealing:** Since this is a "Scavenger" build, paint the MDF or coat it in a layer of cheap PVA glue/water mix to seal it. This prevents the board from warping if the humidity changes, which would otherwise pull your frame out of square.

---

## **4\.** build123d **Design: The Integrated Anchor**

Your bottom corner brackets should be different from your top ones. They need a "Flange" or "Foot" with bolt holes.

Python

\# build123d snippet for a Base Anchor  
with BuildPart() as base\_anchor:  
    \# 1\. Create the Sleeve (same as before)  
    \# 2\. Add a 'Floor Plate' (The Flange)  
    with BuildSketch(Plane.XY) as s\_base:  
        Rectangle(80, 80) \# Large footprint for stability  
    extrude(amount=10)  
      
    \# 3\. Add Mounting Holes for M6 or M8 bolts into the MDF  
    with BuildSketch(base\_anchor.faces().sort\_by(Axis.Z)\[0\]) as holes:  
        for loc in GridLocations(60, 60, 2, 2):  
            Circle(3.5) \# Holes for bolts  
    extrude(amount=-10, mode=Mode.SUBTRACT)

---

## **5\. Summary of "The Tractor" Scavenger Spec**

* **Rods:** M10 (Reference Spec) for the best balance of scavenging and strength.  
* **Base:** 36mm Laminated MDF (The "Anvil").  
* **Squaring:** Use the Long-Sleeve internal stops \+ the MDF base as the master jig.  
* **Software:** Klipper (Input Shaping will have a very easy time with this much mass).

This machine will be exceptionally quiet. Most of the "noise" from a 3D printer is the frame acting like a speaker cone; your heavy MDF and steel "Tractor" will vibrate so little that you'll mostly just hear the fans.

**Would you like me to help you design the "Z-Motor" mounts to be bottom-mounted so they can bolt directly through that 36mm MDF for maximum rigidity?**

Ummm I lkie the anchors, draw a square on the base board, mount the corners, build the base and wil be square and the vertical will be square to the base

This is the **definitive strategy**. You have hit on the exact methodology used to build precision CNC routers and heavy machinery.

By using your massive 36mm MDF base as the "Master Reference," you eliminate almost all the fiddly measurements up in the air. If the base is square, and your brackets are printed well, the printer *must* be square.

Here is the refined workflow for "The Tractor/Scavenger" build using this Base Anchor strategy.

---

### **1\. The New Philosophy: "Trust the Wood"**

Instead of trying to square a wobbly skeleton of rods in mid-air, you are building a foundation.

* **The MDF Baseboard is your jig.** You only need to measure precisely *once*—when drawing the layout lines on the wood.  
* **The 3D printed anchors are just connectors.** Their only job is to hold the rods rigidly relative to the wood.

### **2\. The Scavenger Assembly Workflow**

This is the easiest assembly path we've discussed so far.

#### **Step 1: The Master Layout (The hardest part)**

Take your 36mm laminated MDF board. You need to draw a perfect rectangle on it where the corners of the frame will sit.

1. Draw a baseline near the front edge.  
2. Draw two perpendicular lines going back.  
3. Draw the back line.  
4. **The Critical Check:** Measure the diagonals with a tape measure. Adjust your lines until the diagonals are *exactly* the same length down to the millimeter.

#### **Step 2: Mount the Anchors**

Print your four "Base Anchor" brackets. Place them precisely on the corners of your drawn rectangle.

* **Drill and Bolt:** Drill through the MDF. Use **M8 or M10 carriage bolts** from underneath (counter-bored so the bottom is flush) and tighten the anchors down hard from above with large washers and nuts.  
* *Result:* You now have four rigid plastic sockets fixed perfectly square to each other on an immovable base.

#### **Step 3: Drop-in Assembly**

1. **Verticals (Z):** Slide your M10 Z-rods into the vertical sockets of the anchors. Because the anchor bases are flat on the wood, these rods will stand perfectly plumb (90° to the base).  
2. **Horizontals (X & Y):** Slide your bottom X and Y rods through the horizontal sockets. Since the anchors are already fixed at the correct distances, you don't need to measure anything. Just put the nuts on and tighten them against the anchors.

---

### **3\. Designing the "Base Anchor" in** build123d

This bracket needs to be significantly different from the top corners. It needs a wide stance and massive rigidity.

**Design Requirements:**

* **Massive Flange:** A large, thick base plate (e.g., 100mm x 100mm x 15mm thick) to spread the load across the MDF.  
* **Through-Bolt Holes:** 4 holes in the flange for mounting to the wood.  
* **The "Engine Block":** A solid central block rising from the flange that holds the three offset M10 rods.  
* **Z-Rod Passthrough:** The Z-rod hole should go all the way through the flange so the steel rod rests directly on the MDF (or a small printed shim on the MDF) for maximum weight bearing.

**Conceptual** build123d **Script Structure:**

Python

\# "The Tractor" Base Anchor Concept  
\# M10 Reference Spec

flange\_thickness \= 15  
block\_height \= 70 \# Enough room for offset X and Y rods  
m10\_clearance \= 10.5

with BuildPart() as base\_anchor:  
    \# 1\. The Foundation Flange  
    with BuildSketch(Plane.XY) as flange\_sketch:  
        Rectangle(100, 100, align=(Align.MIN, Align.MIN))  
        \# Fillet corners for a cleaner look  
        fillet(vertices(), radius=10)  
    extrude(amount=flange\_thickness)  
      
    \# 2\. The Central "Engine Block" housing the rods  
    \# Sitting on top of the flange near the corner  
    with BuildSketch(Plane.XY.offset(flange\_thickness)) as block\_sketch:  
        Rectangle(60, 60, align=(Align.MIN, Align.MIN))  
    extrude(amount=block\_height)  
      
    \# 3\. Cut the Rod Paths (Using Offset Method)  
    \# Z-Rod: Goes vertically through EVERYTHING  
    with BuildSketch(Plane.XY.offset(-1)) as z\_hole:  
        Circle(m10\_clearance / 2)  
    extrude(amount=block\_height \+ flange\_thickness \+ 2, mode=Mode.SUBTRACT)  
      
    \# X and Y Rods: Horizontal cuts through the block at different heights  
    \# (Add logic here to cut horizontal cylinders)

    \# 4\. Mounting Holes for the MDF  
    with BuildSketch(Plane.XY) as bolt\_holes:  
        \# Create 4 holes in the corners of the flange  
        GridLocations(80, 80, 2, 2) \* Circle(4.5) \# for M8 bolts  
    extrude(amount=flange\_thickness, mode=Mode.SUBTRACT)  
      
    \# 5\. The "Tractor" Touch: Massive Fillets/Chamfers  
    \# Connect the block to the flange structurally  
    \# fillet(edges().filter\_by(Axis.Z), radius=20)

### **4\. The Ultimate "Tractor" Upgrade: Underslung Motors**

Since you have this massive base and you are bolting through it, you should absolutely mount your **Z-axis motors underneath the table.**

* **How:** Print separate motor mounts that bolt to the underside of the MDF, directly beneath the Z-rod holes in your anchors. Use a flexible coupler to connect the motor shaft to the M10 rod passing through the MDF.  
* **Why:**  
  1. It lowers the center of gravity even further.  
  2. It hides the motors and wiring, making the build look cleaner.  
  3. The MDF acts as a sound baffle, making the Z-moves near-silent.

This approach is solid. It uses the strengths of your materials (MDF for geometry and damping, Printed parts for complex connection geometry, Steel rods for rigid rails) in the best possible way.

OKay, the MDF was going to be optional, now its manadatory, some may not want to laminate, and may just do one layer 18mm or 25mm or 32mm. Being a scavenger build, ther is a donner printer, a Ender or Anet etc, I was plannign on taking the junkstrap approach, so use the donor to print the parts, use thos parte to build the prointer, then print new part (these will/should be more accurate than the doner printer, and once new parts are rpinted the old parts become spares)

That "junkstrap" or "bootstrap" methodology is exactly how the RepRap movement began. Using a lower-quality "donor" machine to print its successor is a rite of passage in 3D printing. It makes "The Tractor" a true evolution of the machine that came before it.

By making the MDF base mandatory, you turn a difficult mechanical assembly into a simple "construction" project.

---

## **1\. The MDF Thickness "Parametric" Base**

Since you're using build123d, you should make the **Anchor Flange** thick enough to handle various MDF thicknesses.

* **The Problem:** If a user uses a single 18mm board, a long bolt might poke out the bottom.  
* **The Solution:** Design the anchor with a **deep counter-bore** on the top side. This allows the user to use a standard bolt length regardless of whether their wood is 18mm or 36mm thick.  
* **Damping Note:** Even a single 18mm MDF sheet is significantly better than no base at all. If a user "scavenges" a piece of an old shelf or a heavy desktop, the strategy still works.

---

## **2\. The "Junkstrap" Printing Strategy**

When you are using a donor printer (like an Anet A8 or Ender 3\) to print parts for a much larger, heavier machine, you need to design for the donor's limitations:

### **Phase 1: The "Structural" Prints (Functional over Beautiful)**

Your first set of brackets should be printed with:

* **High Infill (40%+):** You need the compression strength for those M10/M12 nuts.  
* **More Walls (5-6 perimeters):** Strength in threaded rod frames comes from the walls of the "sleeves."  
* **Standard PLA/PETG:** Use whatever is easiest for the donor to print reliably.

### **Phase 2: The "Self-Evolution"**

Once "The Tractor" is alive, its massive frame and Klipper integration will likely produce much higher dimensional accuracy and less "ghosting" than the donor.

* **The Upgrade:** You can then print the final parts in a more durable material (like ASA or high-temp PETG) or simply use higher-quality settings to make the machine look "Pro."

---

## **3\. The "Baseboard Layout" Trick for Users**

To make the "Master Square" concept easy for someone with just a pencil and a ruler, you can print a **Layout Template**.

Instead of a full part, print a small **1cm thick corner guide** with a hole in the middle.

1. The user places these 4 guides on the MDF.  
2. They measure the diagonals between the holes.  
3. Once the diagonals match, they mark the holes through the guides.  
4. **Result:** Perfectly square drill points without needing complex carpentry skills.

---

## **4\.** build123d **Refined: The "Tractor" Anchor**

Here is how to code the anchor so it handles the "Scavenger" aspect (various bolts, various wood).

Python

\# build123d: Tractor Base Anchor  
\# Designed to be printed on a donor machine (Ender 3 size)

base\_dim \= 90  
block\_dim \= 55  
m10\_dia \= 10.5

with BuildPart() as anchor:  
    \# 1\. Wide Flange for wood mounting  
    with BuildSketch() as s:  
        Rectangle(base\_dim, base\_dim)  
    extrude(amount=12)  
      
    \# 2\. Main Sleeve Block  
    with BuildSketch(anchor.faces().sort\_by(Axis.Z)\[-1\]) as s2:  
        Rectangle(block\_dim, block\_dim, align=(Align.MIN, Align.MIN))  
    extrude(amount=60)  
      
    \# 3\. M10 Rod Holes (Offset Logic)  
    \# Vertical Z hole (through everything)  
    with BuildSketch(anchor.faces().sort\_by(Axis.Z)\[-1\]) as s3:  
        Circle(m10\_dia/2)  
    extrude(amount=-72, mode=Mode.SUBTRACT)

    \# 4\. Scavenger-Friendly Bolt Holes  
    \# Large 10mm holes to accommodate M6, M8, or even M10 lag bolts  
    with BuildSketch(anchor.faces().sort\_by(Axis.Z)\[0\]) as s4:  
        \# Places 4 holes for mounting to MDF  
        for loc in GridLocations(70, 70, 2, 2):  
            \# Includes a large counter-bore for the bolt head  
            Circle(12/2) \# Main hole  
    extrude(amount=12, mode=Mode.SUBTRACT)

---

## **5\. Integrating Donor Parts**

Since you are scavenging an Ender/Anet:

* **Motors:** NEMA 17s. Your M10/M12 frame will handle their torque with zero vibration.  
* **Electronics:** Mount the old mainboard and PSU directly to the MDF base. The wood acts as an insulator and a perfect mounting surface.  
* **Lead Screws:** You can use the standard 8mm lead screws from the donor for your Triple-Z. The M10/M12 rods act as the **frame**, while the donor's lead screws handle the **motion**.

---

## **6\. Squaring the "Pillars"**

Once your 4 base anchors are bolted to the MDF:

1. Insert your vertical M10 rods.  
2. Slide the **Top Corners** on.  
3. If the Top Corners are the same design as the Bottom Anchors (minus the flange), the geometry is forced to be a perfect rectangular prism.

**Next Step for you:** Does your donor printer have a specific bed size or rail system you want to reuse (like V-slot rollers or linear rods), or are you going full "Scavenger" with smooth rods and bearings for all axes?

WIll the donner be dimensional accurate enough? I more worried about the right angle. The hole size for the rod, we can print a test part first till we have the right size for the donner printer. But the right angle shuld be a righ angle correct?

This is the most common worry in the "bootstrap" process. To put your mind at ease: **Yes, the donor will be accurate enough**, provided we use a few clever design tricks to "absorb" its imperfections.

Here is the breakdown of why the donor’s right angles are usually fine, and how to handle it if they aren’t.

---

### **1\. The "Right Angle" Reality**

Most donor printers (Ender 3, Anet, etc.) are actually very good at the **90° angle** between the X and Y axes because that is determined by the factory-squared aluminum extrusions or the frame assembly.

What they are *bad* at is:

* **Dimensions:** A 100mm part might come out at 99.8mm or 100.2mm.  
* **Hole Geometry:** Holes usually print slightly smaller than designed because of how plastic shrinks and "squishes."

**The Solution:** In your build123d code, we won't design a "tight" hole. We will design a **Clearance Hole**. For an M10 rod (10mm), we will print a **10.6mm or 10.8mm hole**. This extra 0.8mm of "slop" allows the rod to slide in even if the donor printer is a bit messy. The **nuts and washers** are what actually lock the rod in place and provide the precision.

### **2\. Squaring the Donor (The "Pre-Flight" Check)**

Before you print your "Tractor" parts, do a 5-minute check on the donor:

1. **The Paper Test:** Ensure the bed is level.  
2. **The Belt Tension:** Tighten the belts. Loose belts cause "racking" (rectangles turning into rhombuses).  
3. **The "Square" Print:** Print a simple 100mm x 100mm L-shape (only 2mm thick). Check it against a cheap hardware store square. If it’s visually 90°, you are good to go.

### **3\. The "Self-Squaring" Bracket Design**

To ensure your "Tractor" isn't limited by the donor's inaccuracies, we use the **"Shoulder and Washer"** strategy.

Instead of the rod fitting tightly in the plastic (where a donor's error would tilt the rod), the rod sits loosely in a hole, and the **M10 washer sits against a flat, printed face.** \* Even if the hole is slightly off-center, the **flat face** of your bracket is what determines the angle.

* Printers are excellent at making flat faces. When you tighten the nut, the washer pulls the rod perfectly perpendicular to that flat face.

### **4\. Handling Dimensional Scale**

If your donor prints 100mm as 101mm, your "Tractor" frame will just be 1% larger. Since we are using **Threaded Rods**, this doesn't matter\!

* If the distance between holes in your brackets is 1mm too wide, you just move the nuts on the threaded rod by 1mm to compensate.  
* **Threaded rods are the ultimate "anti-accuracy" defense** because they are infinitely adjustable.

---

### **5\.** build123d **Test Part Strategy**

Don't print the whole 8-hour corner bracket first. Print a **"Calibration Slug"** to find your donor's "Magic Number" for M10/M12 rods.

Python

\# The Tractor Calibration Slug  
with BuildPart() as slug:  
    with BuildSketch() as s:  
        \# A simple block with 3 different hole sizes  
        Rectangle(60, 25)  
    extrude(amount=10)  
      
    with BuildSketch(slug.faces().sort\_by(Axis.Z)\[-1\]) as holes:  
        \# Test 10.4, 10.6, and 10.8mm  
        for i, size in enumerate(\[10.4, 10.6, 10.8\]):  
            with Locations((i\*20 \- 20, 0)):  
                Circle(size / 2)  
    extrude(amount=-10, mode=Mode.SUBTRACT)

**The Goal:** Pick the hole where the rod slides in easily with no friction, but doesn't "rattle" excessively. **That is your reference parameter.**

---

### **6\. The "Scavenger" Summary**

1. **Trust the Flats:** The flat surfaces of your brackets will be square.  
2. **Trust the Nuts:** The nuts/washers will force the rods to align with those flat surfaces.  
3. **Trust the MDF:** The MDF baseboard acts as the final "Correction Layer" that holds everything in the right place.

Your "Junkstrap" approach is very safe. Even a poorly tuned Ender 3 can print parts that, when combined with M10 steel and 36mm MDF, create a machine 10 times more rigid than the Ender itself.

**Would you like me to help you design the "Z-Axis Lead Screw Nut" housing?** This is the one part where the donor's accuracy matters most, as it needs to align with the motors you'll mount to the MDF.

I was goign to design a lumpy calibration cube-rectangle, print with three lumpy (slop) factors, see which fits the rod best, use that infromation to create the correct bracker

This is the classic engineer's approach—the "Calibration Slug." By testing the "Slop Factor" (tolerance) before committing to a 10-hour print, you are ensuring the success of "The Tractor."

Since you are using **build123d**, you can automate this. Instead of a simple block, I suggest a **"Lumpy Gauge"** that tests three critical things at once:

1. **Rod Clearance:** How easily the M10/M12 rod slides through.  
2. **Nut Fit:** How well the 17mm/19mm hex nut fits into your "Nut Trap" or window.  
3. **Washer Seating:** Whether the flat face is wide enough for your scavenger-found washers.

---

### **1\. The "Lumpy Gauge" Strategy**

In build123d, you can create a single script that generates three "lumps" on a rail. Each lump increases the clearance by **0.1mm**.

* **Lump A (Tight):** \+0.2mm over nominal (e.g., 10.2mm for M10). Likely too tight on a donor printer.  
* **Lump B (Standard):** \+0.4mm over nominal (10.4mm). Usually the "sweet spot" for Ender/Anet printers.  
* **Lump C (Slop):** \+0.6mm over nominal (10.6mm). Great for a "Scavenger" build where rods might have some rust or burrs.

---

### **2\. Squaring the "Pillars" vs. The Donor**

You mentioned worrying about the "right angle" of the donor. Here is the trick: **Even if your donor printer is slightly "out of square," your Tractor won't be.**

Because you are mounting your 4 Base Anchors to a **Master Square drawn on MDF**, the anchors are forced into position.

* If a bracket is printed with a 89.5° angle instead of 90°, the massive leverage of the M10/M12 rod and the force of the nuts will actually "flex" the plastic that final 0.5° into alignment as you bolt it to the wood.  
* **Steel wins over plastic every time.** The rigid MDF and steel rods will "correct" the minor inaccuracies of the donor-printed parts.

---

### **3\. Build123d: The "Lumpy" Calibration Script**

Here is a conceptual snippet for your "Tractor Gauge":

Python

from build123d import \*

\# Parameters  
rod\_nominal \= 10.0  \# Change to 12.0 for M12  
nut\_nominal \= 17.0  \# Change to 19.0 for M12  
test\_offsets \= \[0.2, 0.4, 0.6\]

with BuildPart() as gauge:  
    \# Create a base rail  
    with BuildSketch() as s:  
        Rectangle(100, 30)  
    extrude(amount=5)  
      
    \# Create three 'Lumps' (test blocks)  
    for i, offset in enumerate(test\_offsets):  
        with Locations((i \* 30 \- 30, 0, 5)):  
            with BuildPart() as lump:  
                \# The Block  
                with BuildSketch() as s2:  
                    Rectangle(25, 25)  
                extrude(amount=20)  
                \# The Rod Hole (Vertical)  
                with BuildSketch(lump.faces().sort\_by(Axis.Z)\[-1\]) as s3:  
                    Circle((rod\_nominal \+ offset) / 2)  
                extrude(amount=-25, mode=Mode.SUBTRACT)  
                \# The Nut Trap (Hexagon Window)  
                with BuildSketch(lump.faces().sort\_by(Axis.Y)\[-1\]) as s4:  
                    \# Hexagon slightly larger than nut  
                    RegularPolygon(radius=(nut\_nominal \+ offset) / 2, side\_count=6)  
                extrude(amount=-15, mode=Mode.SUBTRACT)

---

### **4\. The "Junkstrap" Reality Check**

Once you print this gauge on your donor:

1. **The "Push" Test:** Find the hole where the rod slides through with a firm push but doesn't "wiggle."  
2. **The "Drop" Test:** Find the hex trap where the nut drops in but doesn't spin when you apply torque with a wrench.  
3. **The Choice:** Use those specific offsets in your final build123d bracket script.

---

### **5\. Final Squaring Tip for the Base**

When you go to mount these "Lumpy-verified" brackets to your 36mm MDF:

* **The Diagonal Rule:** Don't just measure the sides of your rectangle. Measure from **Front-Left to Back-Right** and **Front-Right to Back-Left**.  
* If those two numbers are the same, your "Tractor" is perfectly square.  
* **The "Scavenger" Secret:** If they *aren't* the same, you can slightly enlarge the holes in the MDF to "shift" the anchor bracket a millimeter before tightening the big bolts.

**Would you like me to generate the "Top Corner" bracket logic next, which needs to mirror the bottom anchors but without the wood-mounting flange?**

Are M10 threaded rods scavengable? for example I can use a office photocopier to get M10 smooth rods. Any thin we can scavent M10 threaded rods off?

Scavenging **threaded** rods is significantly harder than scavenging **smooth** rods. While photocopiers and desktop printers are goldmines for precision ground smooth rods (used for the carriage rails), they rarely use long threaded rods because they rely on belts or high-lead screws for speed.

However, since you are looking for **M10 threaded rods** (all-thread), you need to look where heavy things are hung or braced.

---

## **1\. Top Scavenge Sources for M10 Threaded Rod**

If you are sticking to the "Scavenger" ethos, these are your best bets:

### **Commercial HVAC and Ducting (The Jackpot)**

In commercial buildings (offices, warehouses, malls), the large air ducts and cable trays hanging from the ceiling are almost always supported by **M10 or M12 threaded rods**.

* **Where to look:** Renovation sites or demolition skips. When an office is "gutted," miles of this rod are often thrown away because it’s cheaper to buy new than to clean the old ones.  
* **The Catch:** They might be dusty or have bits of insulation on them, but a wire brush fixes that instantly.

### **Heavy-Duty Flat-Pack Furniture**

While IKEA usually uses M6 or M8, higher-end or "heavy-duty" furniture (like solid wood loft beds, bunk beds, or large workbenches) often uses long M10 threaded sections to pull the frame together.

* **Where to look:** Roadside "hard rubbish" or "bulk waste" days. Look for the heavy timber frames of queen or king-sized beds.

### **Automotive Suspension and Exhausts**

You mentioned M10 is common in automotive. While you won't find 500mm lengths easily, you will find "Studs."

* **U-Bolts:** Large trucks and trailers use M10 or M12 U-bolts for their leaf springs. If you cut the "U" off, you have two straight lengths of very high-grade threaded rod.  
* **The Catch:** This steel is often "Grade 8.8" or higher (very hard), making it harder to cut with a hand saw, but excellent for "The Tractor's" rigidity.

---

## **2\. The "Scavenger's Reality Check"**

Because you are building a 3D printer, you need **straightness**.

* **The Problem:** Scavenged threaded rod from a demolition site might be slightly bent from being pulled down.  
* **The Test:** Roll the rod across your 36mm MDF baseboard. If it "wobbles" or light gaps appear underneath as it rolls, it’s bent.  
* **The Fix:** For the **frame** (the structural box), a slight bend doesn't matter much because the nuts will pull it into alignment. But for the **Z-axis movement**, you must have the straightest rods possible to avoid "Z-banding" in your prints.

---

## **3\. The "Junkstrap" Pivot: M10 vs. 3/8 Inch**

If you are in the US or Canada, scavenging **M10** (metric) is much harder than scavenging **3/8 inch** (imperial).

* **3/8" Rod** is nearly identical in size (\~9.5mm).  
* **The Scavenger Strategy:** In build123d, if you find 3/8" rod instead of M10, you only have to change **one variable** in your script. The "Lumpy Gauge" will tell you which version fits your found hardware.

---

## **4\. Why M10 Smooth Rods are different**

You mentioned getting M10 smooth rods from photocopiers. These are **perfect** for your X and Y axes (the parts the head slides on).

* **Frame:** Use threaded rod (scavenged from construction/HVAC).  
* **Rails:** Use smooth rod (scavenged from photocopiers).  
* **The Hybrid Bracket:** Your build123d corner brackets should be designed to hold the **Threaded M10** (with nuts) and provide a socket for the **Smooth M10** to sit in.

---

## **5\. Summary for "The Tractor" Scavenger**

| Part | Best Scavenge Source |
| :---- | :---- |
| **Horizontal/Vertical Frame** | Commercial HVAC hangars (Threaded M10/M12). |
| **Movement Rails (X/Y)** | Large office photocopiers (Smooth M10/M12). |
| **Fasteners** | Automotive bins (Flanged M10 nuts). |
| **Base** | Kitchen renovation skips (Laminated MDF countertops). |

**Would you like me to help you design a "Universal Rail/Rod Holder" in** build123d **that can take a smooth rod for the carriage and a threaded rod for the frame in the same part?**

M8,M10,M12 threaded rod is cheap at Bunnings (and now cheaper than using M12) and with M10 smooth rods (preferred/reference spec) will look cool.

Since you are in Western Australia (indicated by the Bunnings reference\!), you’re in a great position. Buying new threaded rod for the frame is a smart move—it’s one of the few things where "new" is better than "scavenged" because it ensures the rods are perfectly straight and the threads are clean.

Using **M10 Threaded Rods** for the frame and **M10 Smooth Rods** for the rails is a classic "Tractor" aesthetic. It looks unified, purposeful, and incredibly robust.

---

### **1\. The "Tractor" Rail Strategy**

Since you are using M10 smooth rods (scavenged from photocopiers) for your motion system, you have a slight challenge: **Smooth rods don't have threads to lock them into place.**

**How to mount them to the M10 Threaded Frame:** In build123d, you should design your corner brackets with a **Blind Socket** for the smooth rods.

* The smooth rod slides into a 30mm deep hole.  
* At the bottom of that hole, you can place a tiny blob of blue-tack or a small M3 "grub screw" (scavenged from the donor printer) to pinch the rod so it doesn't rotate or slide out.

---

### **2\. Squaring "The Tractor" on the MDF Base**

Since you are heading to Bunnings, you can pick up a few things that will make squaring the frame nearly effortless:

1. **A "Speed Square" or "Contractor Square":** Even a cheap plastic one is enough to check the vertical Z-rods against your MDF base.  
2. **M10 Flanged Nuts:** If Bunnings has these, grab them. They have a built-in washer that "bites" into the plastic bracket, making the joint much more rigid.  
3. **Laminated MDF (Shelving):** Look for the "pre-finished" white shelving. It’s usually 16mm or 18mm. Two layers of that glued together with PVA is the perfect "Scavenger's Anvil."

---

### **3\. Build123d Design: The "Hybrid" Corner**

Your corner brackets now need to do three things:

1. **Anchor to the MDF** (for the bottom 4 corners).  
2. **Clamp the M10 Threaded Frame.**  
3. **Hold the M10 Smooth Rail** for the X or Y carriage.

Python

\# build123d: Tractor Hybrid Anchor (Threaded \+ Smooth)  
from build123d import \*

m10\_threaded\_dia \= 10.5 \# Slop factor for Bunnings rod  
m10\_smooth\_dia \= 10.1   \# Tight fit for smooth rod

with BuildPart() as hybrid\_anchor:  
    \# 1\. The Base Plate (as we discussed for the MDF)  
    with BuildSketch() as s: Rectangle(90, 90)  
    extrude(amount=12)  
      
    \# 2\. The Main Body  
    with BuildSketch(hybrid\_anchor.faces().sort\_by(Axis.Z)\[-1\]) as s2:  
        Rectangle(60, 60, align=(Align.MIN, Align.MIN))  
    extrude(amount=70)  
      
    \# 3\. THREADED ROD Path (Pass-through with Nut Windows)  
    \# \[Insert horizontal hole and wrench window logic here\]  
      
    \# 4\. SMOOTH ROD Socket (Blind Hole)  
    \# This hole only goes 30mm deep so the rod sits firmly  
    with BuildSketch(hybrid\_anchor.faces().sort\_by(Axis.Y)\[-1\]) as s3:  
        with Locations((30, 50)): \# Positioned above the threaded rods  
            Circle(m10\_smooth\_dia / 2)  
    extrude(amount=-30, mode=Mode.SUBTRACT)

---

### **4\. The "Bootstrap" Advantage**

Because you are using an Ender/Anet donor, you can print the **"Lumpy Gauge"** we discussed earlier to test both the Bunnings M10 threaded rod and your photocopier M10 smooth rod.

**Pro Tip:** Photocopier rods are often induction-hardened. If they are too long, don't try to cut them with a hacksaw; you'll ruin the blade. You’ll need a thin "cutoff wheel" on an angle grinder or a Dremel.

---

### **5\. Final Assembly Logic**

1. **Glue the MDF:** Glue your two layers together. Put weights on them (buckets of water or your Bunnings rod bundles) and let it dry for 24 hours.  
2. **Mark the Square:** Draw your layout on the white melamine surface.  
3. **Bolt the Anchors:** Use the "Bootstrap" printed anchors.  
4. **Insert the "Bunnings" Frame:** Build the M10 threaded box.  
5. **Snap in the "Photocopier" Rails:** The smooth rods will now be perfectly parallel because they are being held by a frame that is bolted to a square piece of wood.

**Would you like me to help you design a "Carriage" in** build123d **that slides on those M10 smooth rods using scavenged bushings or 3D-printed bearings?**

So glueinf two laminated MDF is better than gluing two raw MDF? The smooth rod for x and y can sit on top of the box and do something like the do/dif with the MK2 and MK3. and for Z sit inside the frame. Ummm... are the smooth rods easy to cut? Vice \+ hacksaw?

To answer your first question: **Yes, gluing two pieces of laminated MDF (white shelving) is actually better for a 3D printer base than raw MDF.**

Even though wood glue (PVA) likes raw wood, the "Melamine" laminate on shelving is perfectly flat and extremely hard. When you glue the "raw" sides together (the particle board faces), the outer laminated faces provide a factory-smooth, moisture-resistant surface for your layout lines and anchor brackets. It is also much stiffer than raw MDF of the same thickness.

---

## **1\. The Smooth Rod Layout (MK2/MK3 Style)**

Your idea of placing the X and Y rods "on top" or "outside" the box, similar to how the Prusa MK2/MK3 handles the Y-axis, is excellent for a **"Tractor"** build.

### **The Layout Strategy:**

* **Y-Axis (Bed):** Sit these two M10 smooth rods **on top** of the bottom M10 threaded rods. You can print "cradles" that snap onto the threaded rod and hold the smooth rod at a specific height.  
* **X-Axis (Gantry):** These will move up and down on the Z-axis.  
* **Z-Axis (Vertical):** As you suggested, keep these **inside** the box frame. This protects the most critical alignment rods from being bumped and keeps the footprint compact.

---

## **2\. Can you cut Photocopier Rods? (The "Hard" Truth)**

This is where the "Tractor" gets tough. Most smooth rods salvaged from high-end photocopiers are **Induction Hardened and Ground (IHG) Steel.**

* **The Problem:** The outer "skin" of the rod (about 1-2mm deep) is hardened to HRC 60+. A standard **hacksaw will not bite into it.** The saw teeth will simply slide off and go blunt in seconds.  
* **The Test:** Take a metal file and try to scratch the end of the rod. If the file "skates" off without leaving a mark, it is hardened.

### **How to cut them:**

1. **Angle Grinder (Best):** Use a 1mm thin "Inox" cutting disc. It will slice through the hardened skin like butter.  
2. **Dremel/Rotary Tool:** Use a reinforced cutoff wheel. It takes longer but works well.  
3. **Hacksaw (The "Pro" Hack):** If you *must* use a hacksaw, you have to use a **grinding stone** or a file to grind away the hardened "skin" all the way around the rod until you reach the soft inner core. Once you are through the "crust," a hacksaw will cut the middle easily.

**Safety Tip:** Always wear eye protection when cutting hardened steel. The sparks and the tiny "shards" are very sharp.

---

## **3\. Designing the "MK2-Style" Cradles in** build123d

Since your smooth rods are sitting on the threaded rods, your brackets don't need to be massive blocks. They can be **Clips**.

Python

\# build123d: Threaded-to-Smooth Rod Adapter  
with BuildPart() as adapter:  
    \# 1\. Lower half: Clamps onto M10 Threaded  
    with BuildSketch() as s:  
        Circle(radius=15) \# Outer shell  
    extrude(amount=30)  
      
    \# Subtract the Threaded Rod hole  
    with BuildSketch(adapter.faces().sort\_by(Axis.Z)\[0\]) as s2:  
        Circle(radius=5.5) \# M10 threaded clearance  
    extrude(amount=-30, mode=Mode.SUBTRACT)  
      
    \# 2\. Upper half: Cradles the M10 Smooth  
    \# Positioned 20mm above the threaded rod  
    with BuildSketch(Plane.XZ.offset(15)) as s3:  
        Circle(radius=5.1) \# Tight fit for smooth rod  
    extrude(amount=30, both=True, mode=Mode.SUBTRACT)

---

## **4\. The "Tractor" Squaring Secret: The Z-Pillars**

Since the Z-rods sit **inside** the frame, you can use your build123d script to create a **"Z-Alignment Jig."** Instead of measuring the distance from the Z-rod to the frame, the bracket itself should have a "spacer arm" that touches the threaded rod. This locks the Z-rod into a fixed mathematical relationship with the frame. If the frame is square (thanks to the MDF), the Z-rods *have* to be parallel.

---

## **Summary of the "Tractor" Assembly Order:**

1. **Laminate the MDF:** PVA glue between the raw sides of the white shelving. Clamp well.  
2. **The Master Square:** Draw the layout on the melamine.  
3. **Bottom Frame:** Bolt the 4 corner anchors. Insert M10 threaded rods.  
4. **Z-Pillars:** Insert M10 vertical rods into the anchors.  
5. **Motion Rails:** Snap your "MK2-style" cradles onto the bottom rods and drop in your scavenged photocopier smooth rods.

**Would you like me to help you design the "X-Carriage" or the "Y-Axis Motor Mount" that needs to bridge the gap between your threaded frame and the smooth rods?**

I think I have the frame clear now. the x-carriage was goign to be the same as the Mendal i2 style, 'the plough' or something. I need to redesing to use clamp of the linera bearings and not zip ties. We settle on the Pitan, and for the suspended lengths, with Pitan mouinder direct drive using a E3D V6 (fan on fis ansd nozzel fan) the calcualtion some 'infite stiffness' for up to 300mm on M8 or M10 smooth rods.

"The Plough" is a fantastic name for the X-carriage of "The Tractor." Moving away from the zip-tie method of the original Mendel i2 is essential for this build; zip ties allow the bearings to "wiggle," which defeats the purpose of your heavy M10 frame and MDF base.

With an **E3D V6** and a **Titan (Pitan)** extruder, you have a concentrated mass of about 400g–500g. On a **300mm span of M10 smooth rod**, your calculations for "infinite stiffness" are practically correct—the deflection at the center will be measured in microns, far below the threshold of 3D printing layer inaccuracies.

---

## **1\. Redesigning "The Plough": From Zip-Ties to Clamps**

To match the "Tractor" aesthetic and mechanical rigidity, you should use **Split-Clamp Bearing Housings**.

### **The Design Logic:**

Instead of a solid hole that you force the bearing into, you print a C-shaped housing. You then use an M3 or M4 bolt to "pinch" the housing around the **LM10UU linear bearing**.

**Advantages:**

* **Zero Slop:** It accounts for any "lumpy" print inaccuracies from your donor printer.  
* **Serviceability:** You can swap bearings without breaking the carriage.  
* **Pre-load:** Tightening the bolt slightly deforms the plastic to grip the steel shell of the bearing perfectly.

---

## **2\. Structural Layout for the Pitan \+ V6**

Since you are using a Titan (Pitan) direct drive, the carriage needs to be deep enough to support the motor torque without twisting.

1. **Vertical Spacing:** Keep your two X-axis smooth rods spaced at least 40mm–60mm apart vertically. This "tall" carriage prevents the weight of the motor from "cantilevering" and twisting the rods.  
2. **The "Plough" Faceplate:** Since you are using build123d, you can create a thick "backplane" (10mm+) that the V6 mount and the Titan bolt onto.

---

## **3\.** build123d **Snippet: The Bearing Clamp**

This is the core component of "The Plough." It’s a parametric clamp for an LM10UU bearing (usually 19mm OD, 29mm length).

Python

\# The Plough: LM10UU Bearing Clamp  
bearing\_od \= 19.0 \+ 0.2  \# Nominal \+ slop for donor printer  
bearing\_len \= 29.0  
clamp\_bolt\_dia \= 3.5     \# For M3 bolt

with BuildPart() as bearing\_mount:  
    \# 1\. Main Block  
    with BuildSketch() as s:  
        Rectangle(bearing\_od \+ 10, bearing\_len)  
    extrude(amount=bearing\_od / 2 \+ 5)  
      
    \# 2\. The Bearing Bore  
    with BuildSketch(bearing\_mount.faces().sort\_by(Axis.Y)\[0\]) as s2:  
        Circle(radius=bearing\_od / 2)  
    extrude(amount=bearing\_len, mode=Mode.SUBTRACT)  
      
    \# 3\. The "Split" (to allow clamping)  
    with BuildSketch(Plane.XY.offset(bearing\_od / 2)) as s3:  
        Rectangle(2, bearing\_len)  
    extrude(amount=10, mode=Mode.SUBTRACT)  
      
    \# 4\. Bolt Ears  
    \# Add logic to extrude ears on the side for the M3 pinch bolt

---

## **4\. Why M10 Smooth Rod is the "Reference Spec"**

At a 300mm span:

* **M8 Rods:** Can vibrate (ringing) at high speeds because they act like a guitar string.  
* **M10 Rods:** Have a much higher natural frequency. Because they are stiffer, they don't "store" energy, meaning your **Klipper Input Shaping** results will be much cleaner. You will be able to push the "Tractor" to much higher accelerations than a standard Mendel i2 ever could.

---

## **5\. The "Tractor" X-Ends (Connecting X to Z)**

The "Plough" needs to sit on the X-rods, but the X-rods need to be held by the **X-Ends** which slide up and down the Z-rods.

**The Scavenger Trick:** Use your M10 threaded rod nuts to create the "Lift" mechanism.

* Most people use a brass lead screw nut.  
* If you are truly scavenging, you can use a **Standard M10 Nut** on a threaded rod for the Z-axis, but you will need **Anti-Backlash** logic.  
* **The Fix:** In build123d, design a pocket that holds *two* M10 nuts with a spring between them. This is the "Scavenger's Lead Screw" and it works surprisingly well for Z-axis movement.

---

## **6\. Final Polish: The Fans**

You mentioned a fan for the heatsink and a nozzle fan.

* **Ducting:** With the Titan and V6, space is tight. I recommend a **"Part Cooling Duct"** that wraps around the nozzle like a ring.  
* **Scavenging:** If you scavenged 4010 or 5015 blowers from the donor, make sure the build123d mount has "slots" rather than "holes" so you can adjust the height of the fan as you swap nozzles.

**The "Plough" is almost ready to tilt soil.** **Would you like me to focus on the "X-End" design where the X-axis smooth rods meet the vertical Z-axis rods and the lead screws?**

Here is the x-carrage I will be using as a initial design, the Pitan sits between the two X smoothe rods. I need redesign so there are cut-aways (more wall less infill) to make it structurally stronger. https://www.thingiverse.com/thing:3940673

That is a very clever "low-profile" carriage. By nesting the **Titan/Pitan** between the two smooth rods, you are keeping the center of mass closer to the axis of motion, which is ideal for "The Tractor." It reduces the "pendulum effect" during fast directional changes.

To redesign this for **"The Tractor"** philosophy—moving from zip-ties to clamps and optimizing for structural strength (using wall-count over infill)—we can use some specific build123d strategies.

---

### **1\. Structural Strength: The "Hollow Bone" Principle**

In 3D printing, strength doesn't come from solid plastic; it comes from **skin tension**.

* **The "More Wall" Rule:** 4–6 perimeters (walls) provide more rigidity than 100% infill.  
* **The Cut-away Strategy:** Instead of a solid block, we design a "truss" or a "web." In build123d, we can use the loft or shell functions, or simply subtract large "weight-saving pockets" that leave 3-5mm thick structural ribs.

### **2\. Redesigning for M10 Clamps**

Since your reference spec is **M10**, your bearing housings (for LM10UU) are larger than the original 8mm version.

* **Integrated Clamps:** Replace the zip-tie grooves with **Split-Block Clamps**.  
* **The "Tie-Down" Bridge:** Connect the top and bottom bearing housings with a thick vertical "spine" that also serves as the mount for the Pitan.  
* **Wrench Clearance:** Since you are using a direct drive, make sure the "Lumpy" verification for your donor printer is applied to the screw holes that hold the Pitan to the carriage.

---

### **3\.** build123d **Logic for the "Plough" Carriage**

Here is how you can structure the code to create a "Skeletonized" but ultra-rigid carriage:

Python

\# The Plough X-Carriage (Skeletonized for Pitan)  
rod\_spacing \= 50 \# Distance between X-rod centers  
bearing\_od \= 19.4 \# For LM10UU with slop  
wall\_thickness \= 4.0

with BuildPart() as plough:  
    \# 1\. Create two horizontal Bearing Cylinders  
    with BuildSketch(Plane.XZ) as s:  
        Circle(radius=(bearing\_od/2) \+ wall\_thickness)  
    \# Top Bearing  
    with Locations((0, rod\_spacing/2)):  
        extrude(amount=30, both=True)  
    \# Bottom Bearing  
    with Locations((0, \-rod\_spacing/2)):  
        extrude(amount=30, both=True)

    \# 2\. Add the 'Spine' (The truss connecting them)  
    with BuildSketch(Plane.YZ) as s2:  
        \# A rectangle that connects the outer tangents of the cylinders  
        Rectangle(15, rod\_spacing \+ bearing\_od)  
    extrude(amount=10) \# Central structural plate

    \# 3\. Cut-aways (The 'Lumpy' optimization)  
    \# Instead of a solid plate, subtract large triangles or slots  
    \# leaving only a 'X' or 'V' shaped truss.  
    with BuildSketch(plough.faces().sort\_by(Axis.X)\[0\]) as s3:  
        for loc in \[ (0, 15), (0, \-15) \]:  
            with Locations(loc):  
                SlotOverall(20, 10, rotation=90)  
    extrude(amount=-10, mode=Mode.SUBTRACT)

    \# 4\. Integrated Split-Clamps  
    \# Add a thin slot through the cylinders and holes for M3 pinch bolts

---

### **4\. Direct Drive "Plough" Considerations**

Since the Pitan sits *between* the rods:

* **Gravity Alignment:** Ensure the nozzle of the V6 is exactly centered between the two rods. This ensures that the weight is balanced and that any "torque" from the extruder motor doesn't tilt the head.  
* **Belt Path:** Don't forget to include the **belt grippers**. For "The Tractor," I suggest a "Screw-tensioned" gripper. Instead of just a slot for the belt, use a small M3 bolt to pinch the belt into a toothed cavity.

### **5\. Why the "Structural Web" is better than Infill**

When you print with 6 walls, the "web" parts become essentially solid plastic "beams." In a scavenger build, this is vital because:

1. **Vibration Absorption:** The voids in the truss help break up the resonance frequencies of the stepper motors.  
2. **Accuracy:** Thinner "ribs" of plastic cool more evenly than large solid blocks, which prevents the carriage from warping as it comes off the donor's bed.

---

### **6\. The "Scavenger" Belt Hack**

Since you are scavenging from an Ender or Anet, you likely have **GT2 6mm belts**.

* **The Upgrade:** For a 300mm span on M10 rods, your belts will be the "weakest" link in terms of stiffness.  
* **Tractor Tip:** Design the "Plough" so that the belts are as close to the smooth rods as possible. The further the belt is from the rod, the more "leverage" it has to twist the carriage during fast moves.

**Would you like me to help you refine the "Split-Clamp" logic in** build123d **so it perfectly integrates into the truss structure of the carriage?**

Now for bed slingers, well the better one, there are two smooth rods (or two linera rails) with a y-motor and a belt the sit in the middle between the rods. With my design I will have one at each side of the top box-frame. Do I need one stepper for each smooth rod? Will have enough drivers, as either using two board \+ laptop/pi with klipper MCU config, or a MKS SKIP board.

Since you are building **"The Tractor"** with a massive M10 frame and a heavy 36mm MDF base, you have a unique opportunity to choose between **Dual Y Steppers** or a **Single Stepper with a Sync Shaft**.

Given that you are using Klipper (which handles multiple MCUs and high driver counts flawlessly), the decision comes down to **Raw Power vs. Mechanical Synchronization.**

---

### **1\. Dual Y Stepper Motors (One per side)**

This is the "True Tractor" approach. You place a NEMA 17 at the back-left and back-right of the frame.

* **Pros:** \* **Incredible Torque:** You are doubling the force available to move the bed. This is great for high-speed printing with a heavy glass or magnetic spring-steel bed.  
  * **No Racking:** Because each side is driven independently, you don't rely on the bed's frame to "pull" the other side along.  
* **Cons:**  
  * **Sync Issues:** If one motor skips a step and the other doesn't, the bed will twist (rack).  
  * **Klipper Setup:** You will need to define them as \[stepper\_y\] and \[stepper\_y1\].

---

### **2\. The "Tractor" Alternative: Single Motor \+ Sync Shaft**

In heavy machinery (and the original Voron designs), instead of two motors, they use **one powerful motor** and a **transverse shaft** (an M8 or M10 rod) that spans the width of the printer.

* **How it works:** The motor drives the shaft. The shaft has a pulley on the left and a pulley on the right. Two belts go forward to the bed.  
* **Why this fits your build:** You already have the M10 hardware. You can use two of your scavenged bearings to hold a transverse "sync shaft."  
* **Benefit:** It is **physically impossible** for the left and right sides to get out of sync. It is a very "mechanical" and robust solution.

---

### **3\. Driver/Board Strategy (MKS SKIP)**

The **MKS SKIP** is a great choice. It has an onboard host (essentially a Pi) and usually 5 driver slots. If you go with **Triple-Z** and **Dual-Y**, you need:

* 3 drivers for Z.  
* 2 drivers for Y.  
* 1 driver for X.  
* 1 driver for Extruder.  
* **Total: 7 Drivers.**

Since the MKS SKIP only has 5 or 6 slots, you will likely need to:

1. **Use an expansion board:** Klipper makes it easy to add a cheap secondary board (like an SKR Pico or even an old Arduino/RAMPS) via USB to get the extra drivers.  
2. **Hard-wire the Y-motors:** You can run two Y-motors off a single driver in **series** (not parallel), but you lose the ability to auto-square them via software.

---

### **4\. Build123d: The Y-Motor Anchor**

Since your Y-motors sit on the corners of your top box-frame, your build123d design should integrate the motor mount directly into the corner bracket.

**Tractor Tip:** Design the motor mount to be **adjustable**. Use a "slot" for the motor bolts so you can slide the motor back and forth to tension the belt without needing a separate tensioner at the front.

Python

\# build123d: Integrated Y-Motor Mount  
with BuildPart() as y\_motor\_bracket:  
    \# 1\. Start with your standard M10 Corner Anchor logic  
      
    \# 2\. Add the 'Motor Plate'  
    \# NEMA 17 mounting holes are 31mm apart  
    with BuildSketch(Plane.XY.offset(50)) as motor\_plate:  
        Rectangle(42, 42) \# NEMA 17 size  
        \# Add 4 slots for tensioning  
        for loc in GridLocations(31, 31, 2, 2):  
            with Locations(loc):  
                SlotOverall(8, 4) \# 8mm long slot for M3 motor bolts  
    extrude(amount=8)

---

### **5\. Squaring the Y-Axis in Klipper**

If you go with **Dual Y motors** on separate drivers, Klipper can perform Z\_TILT\_ADJUST logic for your Z-axis, but for the Y-axis, it usually relies on **Endstops**.

* Place one endstop on the Left Y-rail and one on the Right Y-rail.  
* When the printer "Homes," each motor moves until it hits its own switch.  
* **This automatically squares the bed to the frame every time you start the printer.**

---

### **6\. Summary: Which way for "The Tractor"?**

If you want the most "Industrial" feel and have the extra drivers: **Go Dual Y motors with dual endstops.** It makes the machine feel unstoppable and ensures it is perfectly square every time it homes.

If you want to keep your electronics simple: **Go Single Motor with a Sync Shaft.** It uses the "mechanical advantage" of your steel hardware to keep things aligned.

**Would you like me to help you design the "Y-Carriage" (the part the bed bolts to) in** build123d**, ensuring it can bridge the gap between those two side-mounted smooth rods?**

Its not pulling the bed. The bed is on triple-z, think its called a z-dropdown design.

Ah, you are building a **CoreXY-style "Z-Drop"** or **Voron-style** layout, but using the "The Tractor" frame\! That changes the game significantly. In this design, the bed stays stationary in the X-Y plane and moves only vertically (Z), while the "Plough" (X-carriage) and the Y-gantry move at the top of the frame.

Since the bed is supported by **Triple-Z** and you mentioned the Y-axis motors are at the top, you are moving a **Gantry**, not a bed.

---

### **1\. The "Z-Dropdown" Gantry Strategy**

In a Z-drop design, the entire X-axis assembly (the "Gantry") moves up and down. This is usually more complex to square than a bed-slinger, but with your **M10 Threaded Frame** and **MDF Base**, you have the rigidity to pull it off.

Since you have the Y-motors at the top corners, you should use **Dual Y-Motors** to drive the Gantry.

---

### **2\. Dual Y-Motors for the Gantry**

Driving a gantry from both sides is superior to a center-pull for "The Tractor" because:

* **Cantilever Prevention:** If you pulled from the center, the heavy M10 smooth rods of the X-axis might "lag" at the ends.  
* **Synchronization:** By using two motors (one on each side of the top frame), you ensure the X-axis stays perfectly perpendicular to the Y-axis.  
* **Klipper Advantage:** You can use Klipper's \[stepper\_y\] and \[stepper\_y1\] to independently home each side, ensuring the gantry is square to the frame every single time.

---

### **3\. The Triple-Z Bed Support**

For a 235x235 bed in a "Z-Drop" design, the bed is usually suspended on three lead screws.

* **The Scavenger Layout:** \* Two lead screws at the front corners.  
  * One lead screw in the center of the back.  
* **Stability:** This creates a stable "tripod" that defines a perfect plane. With Klipper’s z\_tilt\_adjust, the printer will automatically probe the bed and turn those three M10 Z-motors until the bed is perfectly level relative to your nozzle.

---

### **4\.** build123d **Design: The Gantry "End-Stops"**

Since your X-axis (The Plough) needs to slide along the Y-axis, the "X-Ends" (the brackets at the end of the X-rods) are the most complex part of the build. They must:

1. Hold the LM10UU bearings for the Y-axis rods.  
2. Clamp the M10 smooth rods for the X-axis.  
3. Provide a mounting point for the Y-axis belts.

Python

\# build123d: Tractor Gantry X-End  
with BuildPart() as x\_end:  
    \# 1\. Y-Axis Bearing Housing (Clamped LM10UU)  
    \# This slides on the Y-rods fixed to the frame  
    with BuildSketch() as s1:  
        Circle(radius=15) \# Outer housing  
    extrude(amount=40)  
      
    \# 2\. X-Axis Rod Sockets (Perpendicular)  
    \# These hold the rods for "The Plough"  
    with BuildSketch(Plane.YZ.offset(20)) as s2:  
        \# Two M10 holes for the X-rods  
        for loc in \[(0, 25), (0, \-25)\]:  
            with Locations(loc):  
                Circle(radius=5.1)  
    extrude(amount=30, mode=Mode.ADD)  
      
    \# 3\. Belt Anchor  
    \# Teeth for the GT2 belt to loop back to the Y-motor

---

### **5\. Managing the Weight**

Because you are using M10 smooth rods for the X-axis, the Gantry is heavy.

* **The "Drop" Risk:** If the power goes out, a heavy Z-drop bed can sometimes slide down under its own weight.  
* **The Tractor Fix:** Since you are using M10 threaded rods or lead screws for the Z-axis, the "pitch" of the threads is usually steep enough that friction will hold the bed in place even without power.

---

### **6\. Summary of the "Tractor Z-Drop" Logic**

1. **Frame:** M10 Threaded Box on 36mm MDF.  
2. **Y-Axis:** Two M10 smooth rods fixed to the top of the frame, driven by dual NEMA 17s.  
3. **X-Axis (Gantry):** Two M10 smooth rods sliding on the Y-rods via "X-Ends."  
4. **Z-Axis (Bed):** Three lead screws/threaded rods moving the bed up and down inside the frame.

This setup is significantly more "Pro" than a standard bed-slinger. It allows for higher print speeds because the heavy bed isn't moving back and forth (causing "ringing"); it only moves slowly downward.

---

**Would you like me to focus the next** build123d **step on the "Triple-Z Bed Brackets" that connect your 235x235 bed to the three Z-axis rods?**

OKay, dual-y it is. So doner comes with X,Y,Z,E steppers. We need X, 2xY, 3xZ, E either two donners (cheapest way to get steppers) or one doner and buy three motors.

For "The Tractor," choosing **Dual-Y** is the right move. It aligns with the "overbuilt" philosophy and, as you noted, gives you the torque needed to move a gantry based on M10 smooth rods without any "racking" or twisting.

Since you need **7 motors** (1xX, 2xY, 3xZ, 1xE) and a typical donor only has 4, the "Double Donor" strategy is actually very clever. Not only do you get the extra motors, but you also get a second power supply (which you might need for a large heated bed) and a second set of endstops and cables.

---

## **1\. The Motor Strategy: Mixing and Matching**

Since you'll have a collection of NEMA 17s from different sources:

* **The Y-Axis (2x):** Use a matched pair from the same donor. Since they work together to move the gantry, having identical torque curves and step angles is ideal.  
* **The Z-Axis (3x):** Use three identical motors if possible. If you have to mix them, put the "strongest" motor at the back (where most of the bed weight usually sits if the cantilever is centered there).  
* **The X-Axis (1x):** This motor travels *on* the gantry. Use the lightest NEMA 17 you have (a "pancake" motor if one donor was a Titan-style setup) to keep the gantry's moving mass down.

---

## **2\. Powering "The Tractor"**

With 7 motors and potentially a large bed, a single "scavenged" 12V or 24V power supply (usually 250W–350W) might be pushed to its limit.

* **The Two-PSU Hack:** Since you have two donors, you can use one PSU for the Motherboard and X/Y/E motors, and the second PSU exclusively for the 3xZ motors and the heated bed.  
* **Wiring:** Connect the negative (V-) terminals of both power supplies together to ensure a common ground for the signals.

---

## **3\. Build123d: The "Dual-Y" Corner Hub**

Since the Y-motors are fixed to the frame at the top, we need a corner bracket that acts as a "Motor Clevis." This part needs to be the strongest in the machine because it handles the belt tension.

Python

from build123d import \*

\# Parameters for M10 Reference Spec  
rod\_dia \= 10.5  
motor\_mount\_holes \= 31.0  \# NEMA 17 standard

with BuildPart() as y\_motor\_corner:  
    \# 1\. The Base Block (Clamps the M10 Threaded Rods)  
    with BuildSketch() as s:  
        Rectangle(60, 60)  
    extrude(amount=50)  
      
    \# 2\. The Motor Mounting Plate (Extended out the side)  
    with BuildSketch(y\_motor\_corner.faces().sort\_by(Axis.X)\[-1\]) as s2:  
        Rectangle(50, 60)  
    extrude(amount=10)  
      
    \# 3\. NEMA 17 Bolt Pattern (Slots for belt tensioning)  
    with BuildSketch(y\_motor\_corner.faces().sort\_by(Axis.X)\[-1\].offset(10)) as s3:  
        for loc in GridLocations(motor\_mount\_holes, motor\_mount\_holes, 2, 2):  
            with Locations(loc):  
                \# 8mm slots allow you to slide the motor to tighten the belt  
                SlotOverall(8, 4.5, rotation=90)  
        \# Center hole for the motor shaft/pulley  
        Circle(12)   
    extrude(amount=-20, mode=Mode.SUBTRACT)

    \# 4\. M10 Threaded Rod Holes  
    \# Horizontal paths through the main block  
    with BuildSketch(y\_motor\_corner.faces().sort\_by(Axis.Y)\[0\]) as s4:  
        Circle(rod\_dia/2)  
    extrude(amount=60, mode=Mode.SUBTRACT)

---

## **4\. Squaring the "Z-Drop" Gantry**

In a Z-drop design, the vertical Z-rods are the most critical. If they aren't perfectly parallel, the bed will bind as it moves down.

* **The "Double Anchor" Strategy:** Use your **Base Anchor** logic (bolted to the MDF) for the bottom of the Z-rods, and use the **Top Corner Hubs** (the ones holding the Y-motors) for the top.  
* **The Adjustment:** Because you are using M10 threaded rods for the frame, if you find a Z-rod is "leaning," you just give the M10 nuts on the horizontal frame a half-turn. This "nudges" the top corner until the Z-rod is perfectly plumb.

---

## **5\. Klipper Configuration for 7 Motors**

When you set up your printer.cfg, remember that Klipper treats multiple motors for one axis as unique entities. This allows for "Mechanical Gantry Calibration."

* **Z-Axis:** Use \[z\_tilt\] to probe three points on the bed. Klipper will calculate how much to move each of the 3 motors to make the bed level with the nozzle.  
* **Y-Axis:** Use \[stepper\_y\] and \[stepper\_y1\]. If you have two endstops (one on each side), Klipper will home them independently, automatically squaring your gantry every time.

---

**Would you like me to help you design the "Triple-Z Bed Carrier"?** This is the frame that holds your 235x235 bed and connects it to the three lead screws, making sure it doesn't "tilt" as it drops down.

And a second mainboard, and if i3 Mega some smoothe rods (M8, but we can work with that.)

For Z, using a smooth rod and lead screw I am using a \*\*Kinematic Z-Joint\*\*.

While the Voron Trident uses \*\*GE5C spherical bearings\*\* (which act like a ball-and-socket joint to allow the bed to tilt without bending the rails), you can achieve the same "forgiveness" in a scavenger build using a single 3D-printed bracket that \*\*conceptually\*\* separates the smooth rod from the lead screw.

\#\#\# \*\*1\\. The "Two-Part" Bracket Design\*\*

In \*\*build123d\*\*, don't think of this as one solid block. Think of it as a \*\*base\*\* (the smooth rod carriage) and a \*\*floating insert\*\* (the lead screw nut holder).

\* \*\*The Smooth Rod Side (Rigid):\*\* This part of the bracket houses the linear bearing (LM8UU/LM10UU). It is bolted tightly to your bed. It ensures the bed stays in its X-Y position.

\* \*\*The Lead Screw Side (Floating):\*\* This part houses the T8 nut. Instead of being part of the solid bracket, the nut sits in a \*\*oversized pocket\*\* or is connected via a \*\*Wobble-X\*\* mechanism.

Building a **Kinematic Z-Joint** on a scavenger budget is a stroke of genius for "The Tractor." It solves the single biggest headache of Triple-Z systems: **binding.** If your three vertical rods aren't perfectly parallel to the nanometer, a rigid bed mount will fight the motors, cause skipped steps, and leave artifacts on your prints.

By decoupling the **movement** (the lead screw) from the **constraint** (the smooth rod), you ensure that "The Tractor" stays smooth even if the frame has a bit of "scavenger character."

---

### **1\. The Scavenger’s GE5C: The "Ball-and-Cup" Joint**

Since you don't want to buy specialized GE5C spherical bearings, you can print a **Kinematic Coupling**.

In build123d, you can design the bed mount so the lead screw doesn't "bolt" to the bed. Instead:

1. **The Nut Carrier:** The T8 lead screw nut is bolted to a small printed part that moves up and down.  
2. **The Ball:** A simple 6mm or 8mm steel ball (scavenged from a large bearing or bought cheap) sits on top of that carrier.  
3. **The Bed Bracket:** The bed has a "cup" (a conical hole) that simply rests on that ball.  
4. **The Logic:** Gravity holds the bed down. If the lead screw is slightly tilted, the ball just shifts slightly in the cup without bending the bed or the lead screw.

---

### **2\. Mixing M8 and M10: The Adapter Strategy**

Since your i3 Mega donor provides **M8 smooth rods** but your "Tractor" frame is **M10 threaded rod**, your brackets need to be "hybrid" designs.

* **Z-Verticals:** Use the M8 smooth rods for the Z-guides.  
* **Frame:** Stay with the M10 threaded rod for the structural box.  
* **The Design:** In build123d, your corner anchors will have a 10.5mm hole for the frame and an 8.2mm hole for the Z-rod.

**Tractor Tip:** Since M8 rods are thinner, they might flex more than M10. Because you are using Triple-Z, this is less of an issue, but ensure your **LM8UU bearing clamps** are ultra-rigid to compensate.

---

### **3\. The "Wobble-X" Scavenger Edition**

To prevent "Z-wobble" (where a bent lead screw pushes the bed side-to-side), your "Two-Part" bracket is exactly what you need.

* **The Smooth Rod Carriage (Rigid):** This holds the LM8UU. It is the "Anchor" that keeps the bed from moving in X and Y.  
* **The Lead Screw Nut (Floating):** This sits in a "cage." It can move a tiny bit left, right, front, and back, but it **cannot** move up or down relative to the carriage.

---

### **4\.** build123d **Logic: The Kinematic Bed Bracket**

This script creates the "Two-Part" system: a rigid bearing housing and a floating "cup" for the kinematic joint.

Python

\# The Tractor: Kinematic Z-Bracket (LM8UU \+ Floating Nut)  
bearing\_od \= 15.0 \# LM8UU diameter  
bearing\_len \= 24.0

with BuildPart() as z\_bracket:  
    \# 1\. The Rigid Carriage (Slides on M8 Smooth Rod)  
    with BuildSketch() as s:  
        Rectangle(bearing\_od \+ 10, bearing\_len \+ 10)  
    extrude(amount=20)  
      
    \# Bearing Bore (LM8UU)  
    with BuildSketch(z\_bracket.faces().sort\_by(Axis.Y)\[0\]) as s2:  
        Circle(radius=bearing\_od / 2)  
    extrude(amount=bearing\_len \+ 10, mode=Mode.SUBTRACT)

    \# 2\. The Floating Cup Interface  
    \# This is where the bed sits on the ball/screw  
    with BuildSketch(z\_bracket.faces().sort\_by(Axis.Z)\[-1\]) as s3:  
        with Locations((25, 0)): \# Offset from the smooth rod  
            \# The 'Cup' for the kinematic ball  
            Circle(10)  
    extrude(amount=10)  
      
    \# The conical 'Cup' subtraction  
    with BuildSketch(z\_bracket.faces().sort\_by(Axis.Z)\[-1\]) as s4:  
        with Locations((25, 0)):  
            \# A 90-degree countersink acts as the kinematic seat  
            Circle(6)  
    \# Using a revolve or a chamfer to create the cone

---

### **5\. Double Mainboard Setup: Klipper "Multi-MCU"**

Since you have two donor mainboards (e.g., two Trigorilla boards or an Ender board \+ a Mega board), Klipper is your best friend.

* **The Connection:** Plug both mainboards into your Laptop/Pi via USB.  
* **The Config:** In your printer.cfg, you simply define two MCUs:  
* Ini, TOML

\[mcu\]  
serial: /dev/serial/by-id/usb-board\_1

\[mcu aux\]  
serial: /dev/serial/by-id/usb-board\_2

*   
*   
* **Driver Allocation:**  
  * **Board 1:** X, Y1, Y2, E.  
  * **Board 2:** Z1, Z2, Z3.  
* **Sync:** Klipper handles the micro-second synchronization between the boards. To the user, it feels like one giant 7-driver board.

---

### **6\. Summary of "The Tractor" Z-Axis**

1. **Constraint:** 3x M8 Smooth Rods (Scavenged) held by the M10 Frame.  
2. **Drive:** 3x T8 Lead Screws driven by 3x NEMA 17s.  
3. **Interface:** Kinematic "Ball and Cup" joints to prevent binding.  
4. **Control:** Dual-Mainboard Klipper setup.

**Would you like me to help you design the "MDF Layout Jig" to ensure the three Z-axis lead screws are positioned in the perfect triangle on your 36mm baseboard?**

Gemini can make mistakes, so double-check it

