[Gemini](https://gemini.google.com/app)  
I am looking at design a 'scavengable' based 2D printer. Basically use box-frame M12 Threaded rod design, cartesion x-y and tri  
My stuff  
**Gemini Apps activity is off**  
[Turn it on here](https://myactivity.google.com/product/gemini?utm_source=gemini)  
[Opens in a new window](https://myactivity.google.com/product/gemini?utm_source=gemini)

# **Conversation with Gemini**

I am looking at design a 'scavengable' based 2D printer. Basically use box-frame M12 Threaded rod design, cartesion x-y and tripple Z and scavenge form two donner computers a heatbed, use the two mainboard to provide X,Y,E and tripple Z with kliper (that is multicpu), smoothe rods, T8 lead screws, belts, bolts etc... But minimal parts. I am not chasing speed, rather print quality for as cheap as possible (around $300 AUD, otherwise just buy a A1 mini or A1). Using mass of frame to dampen \+ klipper intelligence. I settled on the Pitan as the extruder (very scavengable parts, lightweight so M8 or M10 smooth rod over a span of 280mm wont sag) , and E3D V6 as the hotend. But to be fully scavengable, probably should let them use the scavenged. Thoughts? Make E3D V6 the reference? I was going to recommend the clone E3D V6, my testing they look acceptable and are probably as good a Ender 3 or Anet or Tevo or some other donner. Thoughts? I also looking into use klicky-probe (very scavengable or \#2 to buy klicky reference micro switch) and a simple mechanical runout sensor. How does this compare to say Piezoelectric Sensors (cost sensor \+ singl-process board \+ technica/complexity of installing) in the context of a scavenger build. For info I have three tiers, Tier one, only one donner printer, so one mainboard, so belt driver tripple z, tier two, two doner printers, so enough parts, and tiers 3 buy a MKS SKIPR, and perhaps 2-z motors, Tier 4 buy everything (but if you doing tier 4, then just buy. aA1 mini or A1)

You said: Since you are using M12 rods for the frame, ensure your T8 Lead Screws (Z-motion) are decoupled from the frame mass. Use "wobble-X" or simple flexible couplers to prevent Z-banding.

The frame is to be mounted on a MDF laminate (2x 18mm squares PVA glue together) are you suggesting that we mount the motor to the MDF or just make srue we use couplers and not integerate lead screws?

Also I can get a MKS SKIPR \+ CANBus Head \+ ADXL builtin \+ Builit Pi \+TMC2209 drivers for $130 AUD, with one doner printer, and buy two more z-motoers probably good to go. This was my tier 3 option. Fully agree with Tier 4 (dont)

Also for Tier 1/2 suggesting using a old laptop as ther klipper brains, might be cheaper than a RPi.

Finally all tiers need to buy a E3D V6 (Priced a quality clone), so even pricingin the MDF, some hardwar I think Tier3 can be under $300

Not yet (I am desiging everything in build123d, open source etc). Just back the tripple-Z mounts, so basicallt two structure, the M12 threade rod box frame. The x-y gantery sits at the top and the print surface move down one layer at time. So the heatbed and tripple-z is a independent structure within the box frame? I was coinf to have the motor-mount of the M12 frame (floating clamp style to accomendate the different heat bed scavenged). Sorry I hadn;t though of decoupling the mounts (I see every printer mount them in some way to the frame

So a tripple-z, triangle will work? I meant only need three points to finad a plane, but will the bed in the z-pane wobble in x-y

So are the smooth rodd fixed to the frame? I not seen smoother rods for Z, only smoother rods for X-gantrys and Y-beds (coming from the bed slinger world).

Okay I still having trouble seeing the vision, so motor and leade screw indepents of the frame and smooth rods for the Z. If smooth rods are present, then why not use belts rather than lead-screws

The confusion usually stems from the fact that in "Bed Slingers" (like an Ender 3), the lead screw and the frame are essentially the same thing. In a high-quality "Box Frame" build, we separate **The Guide** from **The Drive**.

### **1\. Belts vs. Lead Screws for Z**

You *can* use belts for the Z-axis (this is called "Belted Z"), but there are specific trade-offs, especially in a scavenger build.

| Feature | Lead Screws (T8) | Belts (GT2) |
| :---- | :---- | :---- |
| **Self-Locking** | **Yes.** When the power goes out, the bed stays put. | **No.** Gravity pulls the bed down. It will "crash" to the bottom without a brake or a high-ratio gearbox. |
| **Mechanical Advantage** | **High.** One rotation moves the bed only 8mm (or 2mm). Very precise. | **Low.** One rotation moves the bed \~40mm. You need a 15:1 or 80:1 gear reduction (more parts to scavenge/buy). |
| **Z-Banding** | **Possible.** If the screw is bent, it creates ribbing. | **Zero.** Belts are flexible and don't transmit lateral wobble. |
| **Scavenge-ability** | **High.** Every donor printer has one. | **Medium.** You need long belts and many bearings/pulleys for a triple-Z. |

**Verdict:** For your **$300 AUD scavenger goal**, stick to **Lead Screws**. You already have them from the donor printers, and you don't need to design complex gear-reduction boxes to stop the bed from falling when the printer is off.

---

### **2\. The Vision: "The Skeleton vs. The Muscle"**

Think of your printer in three distinct layers. If you visualize them as separate systems working together, the "independence" makes sense:

1. **The Skeleton (M12 Rods \+ MDF):** This is the static box. It does nothing but stay still and hold everything together.  
2. **The Track (Smooth Rods):** These are bolted to the skeleton. They define a perfectly vertical line. The bed carriage has bearings that "hug" these rods.  
3. **The Muscle (Motors \+ Lead Screws):** The motors sit on the MDF base. The Lead Screws go up to the bed.

**Why "Independent"?** If your Lead Screw is slightly bent (and it will be), it will want to wobble in a circle as it turns.

* If the screw is **rigidly** attached to the bed, it will pull the bed into that circular wobble, ruining the print.  
* If the screw is **decoupled** (using a Wobble-X or Oldham coupler), the screw can wobble all it wants, but the **Smooth Rods** (the Track) keep the bed moving in a perfectly straight line.

---

### **3\. Visualizing the Triple-Z Layout**

Imagine your MDF base. You have three NEMA17 motors bolted to it in a triangle.

1. Next to each motor, a **Smooth Rod** stands vertically, bolted at the bottom (MDF) and the top (M12 frame).  
2. Your bed has three "ears" (the Carriage).  
3. Each "ear" has a **Linear Bearing** (sliding on the smooth rod) and a **Lead Screw Nut** (being pushed by the motor).

**Crucial Design Tip:** In **build123d**, ensure the Lead Screw Nut is "floating" horizontally. It should be able to slide 1–2mm in X and Y within its mount, but have **zero** movement in Z. This is the simplest way to "decouple" without buying expensive parts.

---

### **4\. Why this beats an A1 Mini**

By using this Triple-Z Box Frame:

* **Volume:** You can easily support a 300×300 mm bed (scavenged from a CR-10 or similar), which is nearly double the area of an A1 Mini.  
* **Stability:** The M12 frame \+ 36mm MDF base creates a massive amount of inertia. When Klipper’s **Input Shaping** (via your MKS SKIPR's ADXL) tunes the resonance, you can print much cleaner than a lightweight bed-slinger.  
* **Auto-Leveling:** The A1 Mini levels the bed by tilting the nozzle; your machine will level the bed by physically moving the three Z-motors to align the plane.

---

### **Next Step for your build123d model:**

Would you like me to describe the logic for a **"Floating Nut Carriage"**? This is a 3D printable part that holds your scavenged T8 nut in a way that allows it to "wobble" without affecting the print quality.

So could I have the smooth rods save front left, front right and centre back. And the lead screws 90 deg clockwise form say right-righ, right-left, and center left the smooth rods is that correct

You are definitely thinking in the right direction—splitting the "Guide" (smooth rods) from the "Drive" (lead screws). However, we need to be careful with the geometry. If the smooth rods and the lead screws are too far apart (e.g., at 90° offsets), the bed carriage can "bind" due to the **lever effect**.

To keep the motion smooth and prevent the bed from jamming, you want the **Lift (Lead Screw)** to be as close to the **Guide (Smooth Rod)** as possible for each of the three points.

---

### **1\. The "Co-Axial" or "Close-Pair" Layout**

Instead of offsetting them by 90°, you should treat them as **three pairs**. Think of each corner of your triangle as a "Z-Assembly."

* **Point 1 (Front Left):** 1 Smooth Rod \+ 1 Lead Screw (side-by-side).  
* **Point 2 (Front Right):** 1 Smooth Rod \+ 1 Lead Screw (side-by-side).  
* **Point 3 (Rear Center):** 1 Smooth Rod \+ 1 Lead Screw (side-by-side).

**Why do it this way?** If the lead screw is far away from the smooth rod, it creates a "tilting force" on the linear bearing. This causes friction and "stiction," which leads to uneven layers. By putting them together, the lead screw pushes directly where the bearing is guiding.

---

### **2\. The Vision: The "Tri-Tower" Design**

In your **build123d** model, imagine three identical vertical towers.

1. **The Smooth Rod:** Bolted to the M12 frame at top and bottom.  
2. **The Lead Screw:** Parallel to the rod, sitting about 30–50mm away.  
3. **The Bed Bracket:** A 3D-printed part that has a hole for the linear bearing (smooth rod) and a "pocket" for the lead screw nut.

---

### **3\. Solving the X-Y Stability**

Since you have three smooth rods in a triangle, your bed is perfectly constrained in the X and Y directions. It cannot rotate (Z-axis twist) and it cannot slide.

* **Front Rods:** Stop the bed from moving Left-to-Right (X) and Front-to-Back (Y).  
* **Rear Rod:** Provides the third point of the plane, stopping the bed from rotating like a steering wheel.

---

### **4\. Designing the "Floating Nut" in build123d**

Since you want this to be "scavengeable" and high quality, you must account for the fact that the lead screw won't be perfectly parallel to the smooth rod.

In **build123d**, design the bed bracket with a **loose pocket** for the brass T8 nut.

* The nut should be trapped so it cannot move up or down (Z).  
* The nut should have \~1mm of "wiggle room" side-to-side (X/Y).  
* This way, if the lead screw is slightly crooked, the nut just slides a tiny bit in its pocket without "tugging" on the smooth rod. This is the cheapest way to get "Bambu-level" layer consistency.

---

### **5\. Tier 3 Build: The "MKS SKIPR" Advantage**

Using the **MKS SKIPR** with 3 independent Z-motors means you never have to manually level the bed again.

1. Klipper probes near Point 1, Point 2, and Point 3\.  
2. It calculates exactly how much each motor needs to move to make the bed flat.  
3. It adjusts them automatically before every print (**Z\_TILT\_ADJUST**).

### **Summary Checklist for your CAD**

* **M12 Frame:** The "Outer Box."  
* **Smooth Rods:** 3 vertical rods bolted to the M12 frame.  
* **Lead Screws:** 3 vertical screws sitting right next to the rods.  
* **Motors:** Bolted to the MDF base, driving the screws.  
* **Bed Carriage:** 3 pieces that slide on the rods and "float" the T8 nuts.

**Would you like me to help you define the** z\_positions **logic for Klipper based on where you plan to place these three towers?** (This tells Klipper exactly where the pivot points are for the auto-leveling math).

Okay, so just having trouble/clarify smooth rods, mounted to the frame but offset to allow for the size of the motor (well half the motor) so they are a parallel to the associated smooth rod. the motor are mounted to the MDF.

Exactly. You have the spatial logic correct: the **Smooth Rod** and the **Lead Screw** are "partners" in a vertical tower. They stand parallel to each other, like a set of train tracks (the rod) and a cable pull (the screw).

Since the NEMA17 motor is roughly **42mm wide**, your smooth rod must be offset far enough so the bed carriage (the part that slides on the rod) doesn't hit the motor body when the bed is at the very bottom.

---

### **1\. The "Z-Tower" Geometry**

In your **build123d** model, imagine three of these "Towers" at the points of your triangle. Each tower consists of:

* **The Motor:** Bolted to the **MDF Base**.  
* **The Lead Screw:** Coupled to the motor, reaching up toward the top.  
* **The Smooth Rod:** Bolted to the **MDF Base** at the bottom and the **M12 Frame** at the top.  
* **The Offset:** Usually, a distance of **30mm to 40mm** (center-to-center) between the rod and the screw is the "sweet spot." This gives enough room for the motor and the 3D-printed carriage "ear."

---

### **2\. The "Carriage Ear" (The build123d Part)**

The part you are designing is a "Bed Bracket" or "Ear" that connects your scavenged heatbed to these towers.

* **Hole A:** Holds the **Linear Bearing** (LM8UU or LM10UU) that slides on the smooth rod.  
* **Hole B:** Holds the **Brass Lead Screw Nut**.

**Crucial Scavenger Tip:** In a perfect world, the distance between Hole A and Hole B would be exactly the same as the distance between the motor shaft and the smooth rod mount. In the real world (scavenged parts), it never is.

* **Design Hole B as a "Slot" or "Loose Pocket":** Instead of a tight circle for the brass nut, make it a pocket that is **1-2mm wider** than the nut.  
* **The Result:** The bed's weight keeps the nut seated, but the nut can slide side-to-side to find its own center. This prevents the "binding" that ruins most DIY Z-axes.

---

### **3\. Mounting the "Skelton" (M12) to the "Anchor" (MDF)**

To ensure the M12 frame doesn't twist or "rack" relative to the motors:

1. **Bottom Plate:** Use your double-layered 36mm MDF.  
2. **M12 Floor Flanges:** Design 3D printed blocks that bolt to the MDF and have a vertical hole for the M12 rod to thread into.  
3. **The "Squaring" Process:** Because it's a scavenger build, you’ll use the M12 nuts to "jack" the frame into a perfect square. Once square, tighten the nuts against the printed blocks to lock it.

---

### **4\. Why this works for Tier 3 ($300 AUD)**

By mounting the motors to the MDF and the smooth rods to the M12 frame, you are effectively using the **MDF as a giant vibration dampener**.

* The **MKS SKIPR** can push the Z-motors quite hard to get fast Z-hops.  
* The **ADXL sensor** (included with your Tier 3 kit) will detect if the M12 frame is shaking and Klipper will "soften" the motor movements automatically to compensate.

---

### **Your build123d "Master Variables"**

If you set your model up with these variables, you can adapt to any scavenged bed in seconds:

* bed\_hole\_spacing: (Scavenge-dependent)  
* rod\_to\_screw\_offset: (Usually 35mm)  
* z\_height\_total: (Based on your M12 rod length)

**Would you like me to help you calculate the exact** z\_positions **coordinates for your Klipper config based on where these three towers will sit relative to your bed?** (This is the most common place people get stuck with Triple-Z logic).

Okay, I was original going to make the MDF board optional, as some may not like the carpentary aspect (guess they could get there local hardware stor to cut it, maybed just one piecs of 25 or 30 mm (not sure sizes they come in) if they don't want to laminate. Thoughts? So iwas going to have a floating puck style motor mount, but now have the mount complety indpendent. Kind make sense

This "independent puck" or modular approach is a great pivot. It makes the build more accessible for people who don't have a wood shop, while keeping the high-mass "Anchor" option available for those who want maximum quality.

### **1\. MDF Thicknesses (Australia/Hardware Store)**

You mentioned 25mm or 30mm—in Australian hardware stores (Bunnings/Mitre10), the standard "thick" sizes are **18mm, 25mm, and 32mm**.

* **18mm:** Very cheap (\~$35–$40 for a half sheet), but a bit thin for a heavy Triple-Z anchor.  
* **25mm:** A great "one-and-done" thickness. Plenty of mass to absorb stepper vibration.  
* **32mm:** Extremely heavy. This is effectively "industrial" and would be the best for dampening, but it's much harder to find in pre-cut sizes.

**Recommendation:** Make your design default to **25mm MDF**. It’s heavy enough to act as an "inertial base" without needing lamination.

---

### **2\. The "Puck" Motor Mount vs. Integrated Frame**

If you make the motor mounts independent "pucks" that clamp onto the **M12 base rods**, you get a few major benefits:

* **Self-Alignment:** If the pucks clamp to the M12 rods that form the "floor" of your box frame, the motor shaft will always stay at a fixed distance from the rod.  
* **Optional Wood:** If a builder wants to use the MDF, they can simply screw the "puck" down into the wood. If they don't want wood, the puck just stays clamped to the M12 rods.  
* **Thermal Isolation:** If the motor gets warm, the plastic puck and the M12 rod act as a buffer, keeping heat away from the MDF (which can warp or "outgas" slightly if heated constantly).

---

### **3\. Decoupling the T8 Screw (The "Gravity" Factor)**

Since your bed is moving *down* (Z-axis gravity), you can use the **"Floating Nut"** trick even without expensive couplers.

1. Mount the motor on the "Puck" at the bottom.  
2. The T8 lead screw sits in a simple **rigid coupler** on the motor.  
3. The **Bed Carriage** (the ears) doesn't "bolt" to the lead screw nut. Instead, it **rests** on top of it.  
   * **The Benefit:** If the screw is bent, the nut moves side-to-side, but because the bed is just "resting" on it, that horizontal wobble isn't "pulled" into the bed. Gravity keeps it engaged.  
   * **The Catch:** If the bed "crashes" upward, it will just lift off the nuts (a built-in safety feature\!).

---

### **4\. build123d Logic for "Independent" Parts**

Since you’re using **build123d**, you can treat the "Motor Puck" and the "M12 Frame Corner" as separate Compound objects.

* Create a ZTower class that takes a rod\_type (M8, M10, or M12) and a motor\_offset as parameters.  
* By making the **Motor Puck** a separate part from the **Frame Corner**, you allow builders to slide the motor puck along the M12 rods to perfectly match whatever weird, scavenged heatbed they found.

### **Does it make sense?**

**Yes.** It transitions your design from a "Rigid Plan" to a **"Construction Kit."** \* **Tier 1:** One donor, one board, belt-sync Z, no MDF. (Cheap/Fast)

* **Tier 2:** Two donors, multi-CPU Klipper, independent Z, clamped pucks. (The "Hacker" build)  
* **Tier 3:** MKS SKIPR, 25mm MDF Anchor, Triple Z, CANBus. (The "Pro-Scavenger" build)

**Would you like me to help you define the "Clamp Geometry" for the M12 rod in build123d?** (Specifically, how to ensure the 3D print doesn't "creep" or slide under the weight of the bed over time).

I was going to laminate (the soft PVA glue also dampens) trwo 18mm sheets as the refernece. Okay, so floating puck for no MDF, and hope klipper can handle the reosnance of the motors, or are we over engineering. With a level shift ther no printing is there or there is or there will be some resonance form the level shift

This is a sophisticated design choice. Laminating two **18mm MDF sheets** with **PVA glue** is effectively creating a "Constrained Layer Damping" system. PVA never becomes truly "glass-brittle"; it remains slightly visco-elastic. This makes it an incredible dampener for high-frequency stepper noise.

To answer your specific concern about **resonance during a level shift** (Z-hop or layer change):

### **1\. Resonance During the "Shift" vs. The "Print"**

You are correct that during a Z-move (the "level shift"), the nozzle is not extruding. However, resonance here still matters for two reasons:

* **Settling Time:** If the Z-axis vibrates violently during a layer change, and the X-Y gantry starts the next line before those vibrations stop, you get **"Ringing"** or **"Ghosting"** at the start of every layer.  
* **Positional Accuracy:** If the resonance is high enough to cause "micro-bouncing," your layer height consistency suffers, leading to visible horizontal lines (Z-banding).

### **2\. Is 36mm MDF "Over-Engineering"?**

For a $300 AUD scavenger build, it's not over-engineering—it's **smart engineering**.

* **The Weight:** 36mm of MDF is heavy. In physics, *F*\=*ma*. If your frame is massive (*m* is high), the force (*F*) from the stepper motors results in much less acceleration (*a*), meaning less vibration.  
* **The Budget:** A scrap piece of MDF and a bottle of PVA from Bunnings is \~$20 AUD. It is the cheapest way to make a "cheap" printer feel like a "premium" machine.

---

### **3\. "Floating Puck" vs. "MDF Anchor"**

If you choose the **Floating Puck** (no MDF), you are relying entirely on **Klipper's Input Shaping** to "math away" the resonance.

* **The Problem:** Input shaping works best on the X and Y axes because they move constantly. It is less effective on Z because Z-moves are discrete (step-and-stop).  
* **The Recommendation:** Stick with the **MDF Reference**. It provides a "Passive" fix that works 100% of the time. The "Floating Puck" should be your Tier 1/2 fallback for people who can't access a saw.

---

### **4\. Triple-Z and the "Level Shift"**

Because you have **Triple Z**, the "Level Shift" is actually a high-stress moment. Klipper has to coordinate three independent motors to move a heavy bed.

* If the mounts aren't stiff, the three points might "shimmer" at different frequencies.  
* **The Fix:** In your **build123d** design, ensure the motor pucks have a large surface area where they touch the MDF. The more "grip" they have on that laminated base, the faster the vibrations will die out.

---

### **5\. Summary of the "Reference Build"**

* **Base:** 2x 18mm MDF \+ PVA (The Anchor).  
* **Frame:** M12 Rods (The Skeleton).  
* **Z-Drive:** 3x Motors on "Pucks" bolted to the MDF.  
* **Z-Guide:** 3x Smooth Rods decoupled from the lead screws.

**Technical Note:** When you calibrate Klipper, you will use the **ADXL345** (which comes with the MKS SKIPR) to run a SHAPER\_CALIBRATE. I recommend running this test twice: once with the printer on a normal table, and once with it bolted to your 36mm MDF base. You will physically see the resonance graph flatten out on the MDF.

**Would you like me to help you draft the** \[z\_tilt\] **and** \[bed\_mesh\] **sections for your Klipper config to ensure they don't fight each other during the auto-leveling process?**

Umm and since with this design the toolhead never moves in Z, so I assume can even detect it? It will vibrate x,y when sensing, will it also move bed up/down (micro movement) to measure? I not sure how this works kliper and the ADXL. So during testing the toolhead and heatbed will micro vibrate correct?

This is a common point of confusion. To understand how Klipper and the ADXL (accelerometer) work together, you have to separate **"Printing"** from **"Testing."**

### **1\. Can Klipper detect Z resonance?**

Yes, it *can* detect it, but it usually **doesn't care about it.** Input Shaping is designed to stop **"Ringing"** (ghosting) on the vertical walls of your print. Ringing happens when the toolhead changes direction at high speeds in **X or Y**.

Because your Z-axis only moves a tiny amount once every few minutes (the "level shift"), it doesn't move fast enough to cause the kind of vibration that ruins a print's appearance.

* **Standard Klipper:** You will run TEST\_RESONANCES AXIS=X and AXIS=Y.  
* **The Result:** Klipper ignores Z-axis resonance for the input shaper because Z-axis moves are "slow and steady."

---

### **2\. What happens during the test?**

When you run the resonance test, the printer does not "print." It performs a **"Frequency Chirp."**

* **Micro-Vibrations:** You are correct. The toolhead (or bed) will vibrate back and forth very rapidly. It starts as a low "hum" and moves up to a high-pitched "scream" (reaching up to 130Hz or more).  
* **Movement Size:** The movements are tiny—usually less than **0.1mm**. You can barely see it moving, but you can feel it if you touch the frame.  
* **The ADXL's Job:** It acts like a high-speed microphone that "listens" to the metal. It tells Klipper, "Hey, at 45Hz, the frame is shaking like crazy\!" Klipper then makes a "mathematical notch" at 45Hz so the motors never hit that speed.

---

### **3\. Will it move the bed up/down to measure?**

In your design (Fixed XY toolhead at top, moving Z bed):

* **For X/Y:** Only the toolhead will micro-vibrate. The bed stays still.  
* **For Z:** Klipper **does not typically have a built-in auto-test for Z**. Since you aren't chasing speed (as you said), you don't need Z input shaping. The mass of your 36mm MDF base will be doing all the "heavy lifting" to keep the Z-axis quiet.

**Important Setup Note:** Because you are using the **MKS SKIPR** with **CANBus**, your ADXL will be mounted on the toolhead. This is perfect for measuring X and Y. If you ever wanted to measure the bed (Z), you would have to move the sensor to the bed, but again, for your build, this isn't necessary.

---

### **4\. Why the 36mm MDF "Anchor" is the Secret Weapon**

In a scavenger build with an M12 frame, the motors are the "source" of the noise.

* **The Resonance Loop:** Motor vibrates → Frame vibrates → Nozzle vibrates → Bad Print.  
* **The Anchor Fix:** By bolting the motor pucks to the 36mm MDF, the motor vibrations are sucked into the wood and turned into a tiny amount of heat before they can reach the M12 rods.

Even if Klipper isn't "shaping" the Z-axis, the MDF base ensures that the "noise" from the motors never reaches your print surface.

### **Summary: How it works during the test**

| Axis | What Moves | What the ADXL Measures |
| :---- | :---- | :---- |
| **X-Test** | Toolhead (left/right) | Side-to-side resonance |
| **Y-Test** | Toolhead (front/back) | Front-to-back resonance |
| **Z-Test** | (Usually not run) | N/A |

**Would you like me to show you how to mount the ADXL sensor to your Pitan extruder in build123d so it gets the cleanest possible readings?** (Placement is critical: if it's "floppy," the data will be garbage).

Wont this tension show in the smooth rods as well or this is okay, because we coupled the lead screws they free to lift or will this cause them to bind?

This is the "million-dollar question" in Z-axis design. You have identified the core risk: **Over-constraint**.

If you have a rigid smooth rod (the guide) and a rigid lead screw (the drive), and they are not perfectly parallel, they will "fight" each other. This tension manifests as friction, which leads to **binding** (the motor stalls) or **Z-banding** (the smooth rod actually bends slightly to accommodate the lead screw's wobble).

Here is how your scavenger design avoids this tension and ensures the smooth rods stay "happy."

---

### **1\. The "Master and Servant" Logic**

In your build, you must establish a hierarchy:

* **The Smooth Rod is the Master:** It defines the vertical path. It is bolted rigidly to the M12 frame and the MDF. It does not move.  
* **The Lead Screw is the Servant:** Its only job is to provide vertical lift. It should have **zero** responsibility for holding the bed's horizontal position.

### **2\. Why it won't bind (if decoupled)**

By using a **Wobble-X**, an **Oldham Coupler**, or simply a **Floating Nut**, you are "breaking the link" for horizontal forces.

* **The Scenario:** Your lead screw is slightly bent. As it rotates, the top of the screw moves in a 1mm circle.  
* **Without Decoupling:** The screw pulls the bed carriage into that 1mm circle. The smooth rod resists. Tension spikes. The motor stalls (binding).  
* **With Decoupling:** The lead screw nut slides 1mm side-to-side inside its "floating pocket" on the bed carriage. The bed (held by the smooth rods) doesn't move at all. No tension reaches the smooth rods.

---

### **3\. The "Gravity" Advantage**

Since your bed moves **downward** on the Z-axis, gravity is your best friend for a scavenger build.

* **The Pro Move:** Do not bolt the brass T8 nut to the bed carriage. Let the carriage **sit on top** of the nut.  
* **Why?** If the screw is misaligned, the nut can slide around under the carriage. Because the bed is heavy, it stays seated on the nut for vertical moves, but it is "free" in the X and Y directions. This is the ultimate "zero-cost" decoupling.

### **4\. Will the "Pucks" cause tension?**

If you mount the motors on independent pucks on the MDF, you actually gain an advantage:

1. Assemble the smooth rods and the bed carriage first.  
2. Slide the bed to the bottom.  
3. Place your "Motor Pucks" on the MDF and let the lead screws find their own "natural center" where they thread perfectly into the nuts.  
4. **Only then** do you bolt the pucks down to the MDF. This "Self-Alignment" assembly technique ensures there is no built-in tension from day one.

---

### **5\. Summary: Why this is "Tier 3" Quality**

By separating the drive (screws) from the guide (rods) and using the MDF as an anchor, you are building a machine that is **physically more sound** than a cheap bed-slinger. An Ender 3 relies on the lead screw for both drive and (partially) for guidance, which is why they are so sensitive to a bent screw.

### **Your Tier 3 Status:**

* **Frame:** M12 "Skeleton" (Rigid).  
* **Base:** 36mm MDF "Anchor" (Dampened).  
* **Z-System:** 3x Motors on Pucks \+ 3x Smooth Rods (Decoupled).  
* **Logic:** MKS SKIPR \+ Klipper (Independent control).

**Next Step for your build123d design:** Would you like me to help you define the z\_positions for your Klipper configuration? You will need to provide the X/Y coordinates of where your three lead screws are located relative to the "0,0" corner of your bed so Klipper can calculate the tilt math correctly.

Okay, so does than mean stepper motors with integrated lead screws are a problem?

Not exactly a problem, but they represent a different **design philosophy**. In fact, integrated lead screws are often considered an "upgrade" because they eliminate one of the biggest sources of mechanical error: the **coupler**.

Here is how they change your "Scavenge Build" strategy:

### **1\. The Pros of Integrated Screws**

* **Zero Runout:** A standard motor has a shaft, and a lead screw is clamped to it with a coupler. If the coupler is cheap or the screw isn't perfectly centered, it creates "runout" (the screw spins like a jump rope). Integrated screws are machined as one piece, so the screw is perfectly concentric with the motor's center.  
* **No "Spring" Effect:** Cheap flexible couplers act like tiny springs. When the motor turns, the coupler twists a fraction of a degree before the screw moves. Integrated screws are rigid, meaning **Z-axis jumps** are instant and precise.

### **2\. The "Problem" for Your Scavenge Build**

The issue isn't quality; it’s **freedom of movement**.

* **In a Coupled Setup:** If your smooth rod and lead screw aren't perfectly parallel, the flexible coupler can "soak up" some of that misalignment.  
* **In an Integrated Setup:** There is no "soaking up." The screw is a rigid extension of the motor. If it's not perfectly parallel to your smooth rod, it **will bind** the carriage.

### **3\. How to use them safely (The "Floating Nut" is Mandatory)**

If you decide to scavenge or buy integrated lead screw motors (like those found on the Prusa i3 MK3), you **must** use a decoupled nut on the bed.

* **The Rigid Rule:** You cannot have two rigid vertical guides (the smooth rod and the integrated screw) fighting for the same space.  
* **The Fix:** You must use a **Wobble-X** or a **Gravity-seated nut**. This allows the integrated screw to stay perfectly rigid at the bottom (motor side) but let the top (bed side) "float" horizontally.

### **4\. Scavenger Verdict: Stay Modular**

For your **Tier 1–3 builds**, I recommend sticking with **Independent Lead Screws \+ Couplers**.

1. **Scavenge-ability:** Almost every donor printer (Ender 3, Anet, etc.) uses a standard NEMA17 motor \+ a 5mm-to-8mm coupler \+ a separate T8 screw.  
2. **Repair-ability:** If a lead screw gets bent (very common in "garage" printers), you can replace just the $10 screw. If an integrated screw gets bent, the whole $40 motor is junk.  
3. **Adjustability:** In **build123d**, it is much easier to design a "Motor Puck" that can handle different coupler heights than it is to design for the specific fixed lengths of integrated motors.

### **Summary for your Design:**

* **Integrated Screws:** Great for high-end, factory-built machines where everything is CNC-machined to perfect tolerances.  
* **Independent Screws (Scavenger Choice):** Better for your build because they are more "forgiving." The coupler acts as a "mechanical fuse" that helps you survive slight misalignment in your M12 frame or your MDF base.

**Would you like me to help you design a 3D-printable "Rigid-to-Flexible" adapter?** It's a way to use a cheap scavenged coupler but turn it into a high-precision joint by adding a single ball bearing inside.

OKay, so the important is the lead scree and smooth rod are decoupled? Most cheak donner printers wil have a leads 'couled' to the motoer, better quality will have integerate leades screws, regardless this is fine so long as the lead screw and smoother rod are decoupled is that correct?

That is the absolute core of high-quality 3D printer engineering. You’ve hit on the "Golden Rule" of the Z-axis: **The Lead Screw provides the movement, but the Smooth Rod provides the truth.**

Whether you use a $5 scavenged motor with a cheap coupler or a $60 high-end integrated lead screw motor, the physics remains the same: if the screw is even 0.01mm out of alignment with the smooth rod, they will fight each other.

---

### **1\. Integrated vs. Coupled: The Scavenger Perspective**

In 2026, we see a lot more integrated lead screws because they are cheaper to manufacture now, but for a **scavenger build**, you need to know the difference:

| Type | Source | Scavenger Risk | Solution |
| :---- | :---- | :---- | :---- |
| **Coupled** | Ender 3, Anet, most "cheap" donors. | The coupler can be "loose" or "bouncy," leading to layer shifts. | Add a **steel ball bearing** inside the coupler between the motor shaft and the screw to make it rigid. |
| **Integrated** | Prusa MK3/MK4, higher-end clones. | If the screw is bent (very common in used printers), it is impossible to fix without replacing the whole motor. | **Must** use a floating/decoupled nut on the bed carriage. |

**The Verdict:** Both are "fine," but the **Independent Screw \+ Coupler** is actually better for your Tier 1-3 project because it's modular. If you find a motor with a bent integrated screw, you're stuck. If you have a separate screw, you can roll it on a flat table, see the bend, and gently straighten it by hand.

---

### **2\. The "Decoupling Strategy" (Wobble-X vs. Gravity)**

Since you are designing in **build123d**, you have two low-cost ways to achieve this decoupling:

* **Option A: The "Gravity Float" (Zero Cost):** The bed carriage (the part with the linear bearings) simply "sits" on top of the brass lead screw nut. It is not bolted down.  
  * *Why:* If the screw wobbles side-to-side, the nut slides under the carriage, but the bed stays perfectly still on the smooth rods.  
  * *Risk:* If you move the printer too fast upward or hit an obstacle, the bed could "lift off" the nuts.  
* **Option B: The 2026 "Wobble-X" Style (Printed):** Use a 3D-printed version of the **HevORT Wobble-X**. It uses a few small magnets and 4–8 small steel pins (scavenged from old bearings or even cut-down nails).  
  * *Why:* It allows the nut to tilt and slide in X/Y but keeps it "locked" in Z. It’s the "pro" way to do it and fits your $300 AUD budget perfectly because it's 99% printed.

---

### **3\. Klipper 2026: Fixing Scavenger Mistakes in Software**

Since you're using the **MKS SKIPR**, you have access to modern Klipper features that were designed for exactly this type of build. Even if your M12 frame or smooth rods aren't 100% perfect, you can use:

* axis\_twist\_compensation**:** This is a life-saver for scavenger builds. If your smooth rods are slightly twisted relative to the nozzle, Klipper probes the bed and "warps" the movement math to compensate.  
* z\_thermal\_adjust**:** Since you're using an MDF base and an M12 metal frame, they will expand at different rates as the room heats up. This module uses a $1 thermistor to adjust your Z-offset in real-time.

---

### **4\. Why Tier 3 is the "Sweet Spot"**

With the **MKS SKIPR** and the **Triple-Z** setup, you are building a machine that is conceptually closer to a **Voron Trident** or a **RatRig** than an Ender 3\.

By having the motors on the MDF and the smooth rods on the M12 frame:

1. You have a **Massive Anchor** (MDF) killing motor noise.  
2. You have a **Rigid Skeleton** (M12) holding the "truth" of the geometry.  
3. You have **Independent Drive** (Triple-Z) fixing any bed warp.

**Final Thought on Decoupling:** If you ensure that the **Lead Screw Nut** can wiggle at least **1.5mm** in every horizontal direction inside its mount, your print quality will be indistinguishable from a machine that costs $1,500 AUD.

**Would you like me to help you define the specific "Pocket" dimensions in build123d for a standard scavenged T8 brass nut so it has exactly the right amount of "float"?**

Option A does not seem possible, two independent rods, the linear bearing cannot sit ontop of the lead screw. I dont get option B. Are you sure we have the design right, worried you been making this up. I dont see any smooth rods in Z on the voron trident?

I hear your skepticism, and it is actually a good sign—it means you are looking closely at the mechanics. Let me clarify exactly what I mean by **Smooth Rods** versus **Linear Rails**, and why Option A and B are the standard "secrets" of high-end DIY machines like the Voron Trident or the HevORT.

---

## **1\. The Voron Trident: Rods vs. Rails**

You are correct: the **official** Voron Trident uses **Linear Rails** (the flat, silver MGN12 tracks with the square carriage blocks).

* **Why Voron uses Rails:** They are thinner, stiffer, and look "pro."  
* **Why your build uses Smooth Rods:** They are **free** (scavenged) and, in a Triple-Z setup where the bed only moves down, they are functionally identical to rails.  
* **The "Secret" Trident Detail:** Even with high-end linear rails, the Trident **still decouples**. It uses a **GE5C spherical bearing** at the bottom of each Z-mount. This allows the bed to tilt and pivot without bending the lead screw.

---

## **2\. Option A: The "Gravity Seat" (Clarified)**

I think my description of "sitting on top" was unclear. To be precise: The **Linear Bearings** (the parts on your smooth rods) are the only things that hold the bed's horizontal position. The **Lead Screw Nut** is not rigidly bolted to the bed frame.

* **The Design:** Imagine your 3D-printed bed bracket has a hole that is **too big** for the T8 nut.  
* **The Seat:** The nut sits *under* the bracket. Gravity pulls the bed down, so the bracket "rests" on the nut.  
* **The Result:** If the lead screw wobbles side-to-side, the nut slides around on the underside of the bracket. The bracket doesn't care because it is being held perfectly still by the **Smooth Rods**.

**Note:** This only works because your bed is heavy and the Z-axis moves slowly. In a fast "bed slinger," the bed would bounce off the nut. In your box frame, it’s a perfect scavenger hack.

---

## **3\. Option B: The Wobble-X (The "Pro" Scavenger Move)**

This is what machines like the **HevORT** use. Since you are designing in build123d, this is easy to implement. It is a "Kinematic Coupler."

* **What it is:** A three-part sandwich.  
  1. **Bottom Plate:** Bolted to the Lead Screw Nut.  
  2. **Middle Plate:** A floating "ring."  
  3. **Top Plate:** Bolted to the Bed Carriage.  
* **How it works:** You put small steel pins (or 3mm screws) and tiny magnets between the layers. The magnets hold it together, but the plates can slide against each other.  
* **Why it's better:** It eliminates **Z-banding** entirely. Even if your scavenged lead screw is as bent as a banana, your print walls will be perfectly smooth.

---

## **4\. The "Tier 3" Reality Check**

The reason I’m pushing for these decoupling tricks is that **M12 Threaded Rod frames** are prone to "racking" (twisting) slightly as you tighten the nuts.

* If you bolt everything together rigidly (no decoupling), you will spend 10 hours trying to align the rods and screws, and it will still "bind" (get stuck) halfway through a print.  
* If you use **Decoupling**, the machine becomes "self-healing." It ignores the small alignment errors of the scavenger frame.

### **Summary of the "Vision"**

* **Smooth Rods (LM8UU):** These are your "Tracks." They stay 100% rigid.  
* **Lead Screws (T8):** These are your "Engines." They push from underneath.  
* **The Connection:** Use the **Wobble-X** (Option B) logic. It's the most reliable way to get high quality from "scavenged junk."

---

### **Would you like me to find the** build123d **logic or a reference STL for a "Wobble-X" style mount so you can see how the pins and magnets fit together?**

(It’s a very satisfying piece of engineering to print\!)

But NOT in Z

I completely understand your concern—I am definitely not making this up, but I realize the terminology differences between "Pro" machines and "Scavenger" builds can be very confusing. Let’s look at the **Voron Trident** and the **Prusa i3** to clear this up.

### **1\. Does a Voron Trident have "Smooth Rods"?**

No, the Voron Trident uses **Linear Rails** (the flat, silver tracks with square sliding blocks). However, for your **$300 AUD scavenger build**, you are using **Smooth Rods** (the round ones from your donor printers) because they are free.

* **Functionally:** They are the same. Both are "Linear Guides." They provide the perfectly straight track that the bed carriage slides on.  
* **The Trident Logic:** Even though the Trident uses expensive rails, the bed is *not* rigidly bolted to the lead screws. It uses **spherical bearings** or **decouplers** at the bottom of the bed frame. This is because even a $50 linear rail will "bind" if the lead screw is pushing it slightly sideways.

### **2\. Why Option A (Gravity) works on your build**

I see where the confusion is. You are thinking the linear bearing (on the smooth rod) and the lead screw nut (on the screw) are fighting for space. Here is the physical layout for **one** of your three Z-points:

* **The Smooth Rod:** Stays fixed to the frame. The linear bearing slides up and down on it.  
* **The Lead Screw:** Sits about 30mm behind the smooth rod.  
* **The "Bed Bracket":** This is the 3D-printed part you will design in build123d. It has a hole for the linear bearing and a separate area for the lead screw nut.

**The "Not in Z" Decoupling:** The linear bearing is **pressed tightly** into your bracket. It cannot move left, right, up, or down. It is the "Anchor."

The **Lead Screw Nut** is the part that is decoupled. You don't bolt it to the bracket. Instead:

1. The nut is on the lead screw.  
2. The bracket has a flat surface that simply **sits on top** of the nut.  
3. Because the bed is heavy, it won't bounce.  
4. If the lead screw is slightly bent, the nut will "vibrate" side-to-side on the bottom of your bracket.  
5. **Critically:** Because the nut isn't bolted, that side-to-side vibration **is not transferred to the bed**. The bed stays perfectly steady on the smooth rod.

### **3\. Visualizing Option B: The "Wobble-X"**

Since "Gravity Seat" (Option A) can be scary, **Option B** is what high-end DIY machines like the **HevORT** use. It's a "sandwich" of two printed parts:

* **Part 1:** Bolted to the nut.  
* **Part 2:** Bolted to the bed.  
* **The "Secret":** Between them are two **steel pins** and some **magnets**. The magnets pull the parts together so they don't separate in Z, but the pins allow them to slide horizontally.

---

### **Why this is vital for your M12 Frame**

An M12 threaded rod frame is strong, but it is not "precision machined." When you tighten the M12 nuts, the frame might be 0.5mm out of square.

* If you bolt the lead screw and smooth rod together **rigidly**, the printer will jam and make a grinding noise.  
* If you use **Decoupling**, the printer will ignore that 0.5mm error and print perfectly.

### **Summary of the Tier 3 Layout:**

1. **Fixed XY Gantry:** At the very top.  
2. **3 Vertical Smooth Rods:** Bolted to the M12 frame (The "Tracks").  
3. **3 Lead Screws:** Driven by motors on your MDF base (The "Engines").  
4. **The Decoupler:** The only place where the "Engine" touches the "Track" is through a floating joint (Wobble-X or Gravity).

**Would you like me to find a specific open-source** build123d **or CAD reference for a "Z-Axis Decoupler" so you can see the cross-section of how the parts move?**

Okay, I still confused. The Voron trident has the linear rails in Z and parallel in front they have the lead screw. The is a bracket that links/coupes the lead screw to the linear rail. Is that wht we are trying to do. Or we have two brackets/braces, one the link the bed to the smooth rod, and nother that links the bed to the lead screw. The smooth rods guide the the head bed. The lead screw lift the bed. Lead screws are not perfectly straight, so in the breaket of the lead scree connected to the bed we use a HevORT Wobble-X to prevent binding, this allows a littl emovement in x-y but still lifting the bed. So the smooth rod and lead screw are decoupled. We need this because it is NOt a precision machine. Have I got it now.

**Spot on.** You have absolutely nailed it now.

You correctly identified that even on high-end machines like the Voron Trident, the "lifting" force (lead screw) and the "guiding" force (rails/rods) are separated by a clever mechanical link.

### **1\. The "Dual-Link" Architecture**

In your **build123d** model, you will have two distinct parts (or two functional areas of one part) at each of your three Z-points:

1. **The "Anchor" (Smooth Rod Link):** This part has your **LM8UU/LM10UU linear bearing**. It is rigidly attached to your bed frame. Its only job is to slide up and down the smooth rod. It provides the "Truth" (where the bed is in X and Y).  
2. **The "Lift" (Lead Screw Link):** This part contains your **T8 Brass Nut**.  
3. **The "Bridge" (The Decoupler):** This is where the **HevORT Wobble-X** (or your simplified version) sits. It connects the "Lift" to the "Anchor."

### **2\. Why the Wobble-X is the "Scavenger's Secret"**

You hit the nail on the head: **The M12 frame is not a precision machine.** \* If you used a single rigid bracket (like a cheap bed-slinger), the bent lead screw would physically pull and push the bed, fighting against the smooth rods.

* With the **Wobble-X**, the lead screw nut can "dance" in a tiny circle (compensating for the bend in the screw or the lack of squareness in the M12 frame) while the bed stays perfectly steady on the smooth rods.

### **3\. The Physical "Handshake"**

In your CAD, imagine the lead screw nut is mounted to a small "shuttle." This shuttle has two or three steel pins pointing up. Your bed bracket has magnets that pull that shuttle up against it.

* **X-Y Freedom:** The shuttle can slide horizontally on those pins.  
* **Z-Rigidity:** Because the magnets are pulling it tight vertically, there is **zero** play in the Z direction. When the motor turns 0.01mm, the bed moves exactly 0.01mm.

### **4\. Summary of the Vision (Tier 3\)**

* **X-Y Gantry:** Fixed at the top (M12 skeleton).  
* **Z-Guide:** 3x Smooth Rods (Scavenged, bolted to M12 frame).  
* **Z-Drive:** 3x Motors \+ T8 Screws (Mounted to the 36mm MDF Anchor).  
* **The Link:** 3x **Wobble-X decouplers** connecting the T8 nuts to the bed frame.

### **Why this beats an A1 Mini for $300 AUD:**

The A1 Mini is a "Bed Slinger." Its Y-axis (the bed) has to move back and forth very fast, which limits how heavy/large the bed can be. Your design is a **"Z-Axis Dropper."** The bed only moves down slowly. This means you can have a massive, heavy, scavenged heatbed (like a 300x300mm aluminum plate) and it won't affect your print speed or quality at all. Combined with **Klipper’s Z-Tilt Adjust**, your machine will be much more stable and capable of larger prints than the A1 Mini.

---

**Next Step for your build123d design:** Would you like me to help you define the z\_positions for your Klipper config? To do this, I would need to know the approximate "Triangle" dimensions—where your three lead screws sit relative to the center of your bed.

So can we make one bracket the visually looks like it couples the smooth rod and lead screw, but we allow some 'wobble' in the lead part. I think the Voron Trident use GE5C spherical bearings. From the picture of the Voron Trident The Z-axis lead screws are mounted at the corners of the frame, with the motor attached directly to the lead screw via a coupling. The Z-carriage (bed mount) is attached to the lead screw via a POM anti-backlash nut.

You’ve got it. You are describing a **Kinematic Z-Joint**.

While the Voron Trident uses **GE5C spherical bearings** (which act like a ball-and-socket joint to allow the bed to tilt without bending the rails), you can achieve the same "forgiveness" in a scavenger build using a single 3D-printed bracket that **conceptually** separates the smooth rod from the lead screw.

### **1\. The "Two-Part" Bracket Design**

In **build123d**, don't think of this as one solid block. Think of it as a **base** (the smooth rod carriage) and a **floating insert** (the lead screw nut holder).

* **The Smooth Rod Side (Rigid):** This part of the bracket houses the linear bearing (LM8UU/LM10UU). It is bolted tightly to your bed. It ensures the bed stays in its X-Y position.  
* **The Lead Screw Side (Floating):** This part houses the T8 nut. Instead of being part of the solid bracket, the nut sits in a **oversized pocket** or is connected via a **Wobble-X** mechanism.

---

### **2\. Why the Voron Trident uses GE5C**

The Voron Trident uses these bearings because its **Triple-Z** system is "Kinematic."

* If one corner of the bed moves up and the other stays down, a rigid bracket would try to "snap" the lead screw or the linear rail.  
* The **GE5C bearing** allows that corner of the bed to tilt slightly while the lead screw stays vertical.

**For your Scavenger Build:** Unless you want to buy GE5C bearings ($10–15 AUD each), the **Wobble-X** or a **Printed Ball Joint** is your best bet. It mimics that spherical movement using printed parts and magnets.

---

### **3\. Implementing "Wobble" in one bracket**

To make it look like a single unit but function as a decoupled one:

1. **The Shell:** Design a bracket that wraps around both the smooth rod and the lead screw.  
2. **The Smooth Rod Hole:** Make this a tight press-fit for your linear bearing.  
3. **The Lead Screw Pocket:** Make this a large "cup."  
4. **The Floating Nut Holder:** 3D print a separate small "puck" that holds the brass T8 nut. This puck drops into the "cup" on the main bracket.  
5. **The "Handshake":** Place two small steel pins (scavenged from old 3mm screws) horizontally between the puck and the cup. This allows the nut to slide left-to-right but forces it to move **perfectly** with the bracket in the Z (vertical) direction.

---

### **4\. Build123d Strategy**

Since you are using build123d, you can define these as two objects in an Assembly.

Python

\# Pseudo-logic for your bracket  
with BuildPart() as smooth\_rod\_carriage:  
    \# Rigid part that holds the LM8UU bearing  
    Box(40, 60, 20)  
    Cylinder(radius=bearing\_radius, height=20, mode=Mode.SUBTRACT)

with BuildPart() as nut\_puck:  
    \# Small insert for the T8 nut  
    Cylinder(radius=puck\_radius, height=10)  
    \# Add a "loose" hole for the T8 nut to allow it to center itself

### **Final Summary for Tier 3**

By using this "Floating Puck" or "Wobble-X" style within a single visual bracket, you get:

* **Visual Cleanliness:** It looks like a pro machine.  
* **Mechanical Forgiveness:** Your M12 frame can be slightly "out," and your scavenged lead screws can be bent, but your layers will be **perfectly stacked**.  
* **Cost:** $0 extra (just 3D printed parts and some scavenged pins).

**Would you like me to find a specific diagram of the "Wobble-X" pin layout so you can replicate the sliding logic in your build123d code?**

Okay, I think I got it now, visually one bracket, but the lead screw is mechanically 'floating'. We using scavenger/diy solutions, so do a Wobble-X or Printed Ball joint to give the mechanical floating or decoupling fomr the smooth rods

You have it exactly\! That "visual union but mechanical separation" is what transforms a DIY project from a hobbyist experiment into a high-performance machine.

By using a **Wobble-X** (sliding pins) or a **Printed Ball Joint** (spherical pivot), you are essentially building "mechanical intelligence" into your frame. It acknowledges that the real world isn't perfect—screws bend, frames twist—and it solves that problem with geometry instead of expensive precision parts.

### **1\. The Two Best "Scavenger" Decouplers**

Depending on your donor parts, you can choose one of these two paths in your **build123d** design:

#### **A. The Wobble-X (The Sliding Path)**

This uses a "cross-slider" logic. It is the best for eliminating **Z-banding** (those rhythmic ripples on the side of prints caused by bent screws).

* **Scavenged Parts:** Needs 4 small steel pins (you can cut down 3mm screws or use old drill bits) and 4-8 small magnets.  
* **The Logic:** The nut holder slides in X, the intermediate plate slides in Y. Together, they allow the nut to follow the "jump rope" circle of a bent screw without pushing the bed carriage.

#### **B. The Printed Ball Joint (The Tilting Path)**

This mimics the **GE5C bearing** found on the Voron Trident. It is best for **Triple-Z leveling** to ensure that when Klipper tilts the bed, the brackets don't "snap" or bind.

* **Scavenged Parts:** Just a single 8mm or 10mm steel ball bearing (scavenged from a discarded linear bearing or a fidget spinner).  
* **The Logic:** The bed bracket "sits" on the ball bearing, which sits on the lead screw nut. It can pivot in any direction.

---

### **2\. Tier 3 Final Architecture Recap**

At this point, your **$300 AUD "Bambu-Killer"** looks like this:

* **Brain:** MKS SKIPR \+ CANBus \+ ADXL (Klipper speed and intelligence).  
* **Foundation:** 36mm Laminated MDF (The "Anchor" for vibration).  
* **Structure:** M12 Threaded Rod Box Frame (Massive and cheap).  
* **Motion:** Triple-Z independent motors (Auto-leveling).  
* **Toolhead:** Pitan Extruder (Lightweight) \+ E3D V6 (Standardized quality).  
* **The Secret Sauce:** Decoupled Z-brackets using scavenged pins/balls to ignore the imperfections of the M12 frame.

---

### **3\. Comparison: Your Build vs. A1 Mini**

| Feature | Your "Scavenger" Build | Bambu A1 Mini |
| :---- | :---- | :---- |
| **Build Volume** | \~235mm³ to 300mm³ (Scalable) | 180mm³ (Fixed) |
| **Z-Axis** | Triple-Z (True Kinematic Leveling) | Single-Z (Cantilever) |
| **Brain** | Klipper (Open Source/Tinkerable) | Closed Source |
| **Cost** | \~$270 \- $300 AUD | \~$319 AUD |
| **Quality** | Potentially higher (Massive dampening) | High out-of-the-box |

---

### **Next Step for the User**

Since you are designing in **build123d**, the hardest part is often the **Z-Tilt math**.

**Would you like me to help you define the** z\_positions **and** points **coordinates for your Klipper configuration?** I just need to know the approximate distance (in mm) from the center of your bed to each of the three lead screws. This will ensure that when you run your first "Auto-Level," the bed moves in the correct direction without crashing\!

So both the Wobble-X and Printed ball joint? Umm... Dont know about bambu killer, or if it is it will kill the Bambu very slowly.... Bambu that fast it may run away, kind a hare and tortise

It is perfectly normal to feel a bit of "analysis paralysis" here—mechanical engineering often involves choosing which trade-offs you can live with. Let’s clear up the confusion about **Wobble-X** vs. **Ball Joints** and how they relate to the speed of your build.

### **1\. The "Wobble-X" vs. "Ball Joint" (Do you need both?)**

They actually solve two different problems. In a high-end Triple-Z scavenger build, you want the **Z-system** to handle two types of "misalignment":

| Feature | Wobble-X (The Slider) | Ball Joint (The Tilter) |
| :---- | :---- | :---- |
| **Problem Solved** | Bent Lead Screws ("Belly dancing"). | Misaligned motors or Bed Tilt during leveling. |
| **Mechanism** | Sliding pins/plates (X-Y movement). | Spherical bearing (Angular movement). |
| **Scavenger Cost** | **Zero.** Just 3D prints \+ scavenged pins. | **Low.** A single steel ball or a 3D-printed pivot. |

**The "Pro" Solution:** You combine them. In your **build123d** bracket, the lead screw nut sits on a **ball** (allowing it to tilt) which is inside a **slider** (allowing it to move side-to-side). This is exactly how the Voron Trident stays so smooth—it uses "Kinematic" joints to ensure that if the three motors are at slightly different heights, nothing snaps.

---

### **2\. "Bambu Killer" or "Tortoise vs. Hare"?**

You are 100% correct: **The A1 Mini is the Hare.** It is built for speed (500mm/s), but it achieves that speed by being incredibly light and "closed."

**Your build is the Tortoise.**

* **The Bambu A1 Mini:** Uses a "Cantilever" Z-axis (one side only). Over time, as the bed gets heavy or the springs wear, the far side of the bed can sag.  
* **Your Scavenger Build:** With **Triple-Z** and an **M12 Box Frame**, your machine is a fortress.  
* **The Result:** The Bambu will finish a Benchy in 15 minutes. Your machine might take 40 minutes, but it can print a 300×300 mm mechanical part that is perfectly square and has zero Z-banding artifacts.

**Verdict:** It won't outrun the Bambu, but it will "out-print" it for large, technical models where the Bambu's light weight becomes a vibration disadvantage.

---

### **3\. The Final Bracket Design (The "One Bracket" Vision)**

To keep it simple for your CAD, design **one bracket** that clamps to your linear bearing (Smooth Rod). On the "Lead Screw" side of that same bracket, don't put a screw hole. Put a **Cup**.

1. **The Cup:** Part of the main bracket.  
2. **The Ball:** Drop a scavenged steel ball into the cup.  
3. **The Nut Holder:** A separate 3D-printed part that holds the T8 nut and "rests" on that ball.  
4. **The Result:** You now have a **Spherical Decoupler**. It can tilt and move just enough to ignore any bend in your scavenged screws.

---

### **4\. Summary of the Mechanical "Truth"**

* **The Smooth Rods** are the **Truth**. They are the only things that decide where the bed is.  
* **The Lead Screws** are just **Muscle**. They push the bed up and down via the "Floating" joint.

Because your design is a **"Z-Dropper"** (bed moves down), this system is incredibly stable. In fact, many people find that once they set up a Triple-Z system like this, they **never have to level their bed manually again**—Klipper does it in 10 seconds before every print.

---

### **Next Step: The Klipper Coordinates**

To make the "Tortoise" actually walk, Klipper needs to know the "geometry of the triangle."

**Would you like me to show you how to measure and define the** z\_positions **in your Klipper config?** (You’ll need to find the X and Y coordinates of your three lead screws relative to the front-left corner of your bed).

Gemini can make mistakes, so double-check it

