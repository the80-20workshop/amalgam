# Parts Sourcing & Replacement Guide

You've scavenged two donors. But things happen: a PSU dies, a leadscrew is bent, bearings are worn, or you discover a mainboard is unusable. This guide helps you **source replacement parts** from the secondhand market (AliExpress, Temu, eBay) without getting scammed or buying duds.

**Budget reality:** Expect to spend $80-150 on parts you can't scavenge, depending on donor condition and your frame path. Plan for contingencies.

---

## Parts You'll Likely Need to Source

| Part | Why Needed | Typical Cost | Notes |
|------|-----------|--------------|-------|
| **M10 Threaded Rods** | Darwin frame skeleton | $30-45 | 8 rods per set; check length |
| **M8 Lead Screws** | Z-axis motion (Triple-Z) | $15-25 | T8 2mm pitch standard; verify in photos |
| **8mm Smooth Rods** | X-Y motion (if donors lack) | $40-60 | 8× rods, check straightness |
| **IGUS RJ4JP-01-08** | Bearings (if donors worn) | $25-35 | Cheap alternative to LM8UU; check brand |
| **Power Supply** | If donor PSU dead | $40-80 | 24V preferred; verify wattage |
| **NEMA17 Motors** | If donor motors bad | $10-15 each | Usually abundant, but verify shaft |
| **Misc Bolts/Springs** | Assembly | $15-20 | M3, M4, M5 assortment; cheap |

---

## How to Assess Parts: Spot Fakes & Duds

**Before you buy anything, know exactly what you need:**

### 1. Know Your Specs

- **M10 threaded rods:** 1.5mm pitch, fully threaded (not partially)
- **M8 lead screws:** T8 2mm pitch (not 8mm pitch—yes, this confusion exists!)
- **8mm smooth rods:** 8.00 ±0.02mm diameter (not 8.5mm or "precision" variants)
- **LM8UU bearing:** 8mm bore, 15mm OD, 45mm length (not LM8, not generic "linear bearing")
- **IGUS RJ4JP-01-08:** Polymer, 8mm bore (cheaper than LM8UU, acceptable for Amalgam)
- **PSU:** Check voltage (12V vs. 24V) AND wattage (30A minimum for 24V systems = 720W)
- **NEMA17:** 1.8° step angle (not 0.9°), standard mounting face

### 2. Red Flags on Listings

🚩 **Avoid these:**
- Suspiciously cheap (99¢ for 8× rods? probably fake/short lengths)
- Zero reviews or only 1-2 reviews
- Fuzzy/low-quality photos or generic stock images (not showing the actual product)
- Vague descriptions ("linear bearing set" with no size spec)
- Photos don't match description ("shows 12mm rod but title says 8mm")
- Seller has low ratings on other items (pattern of problems)
- Shipping "from China" with "fast delivery" but actually 6-8 weeks

### 3. Green Flags

✅ **Look for these:**
- 10+ reviews with photos (shows real user experience)
- Reviews mention "fits perfectly," "exactly as described," "good quality"
- Photos show the actual product clearly (not stock images; you can see details)
- Seller specializes in 3D printer parts (high rating across multiple items)
- Clear specs in title + description (e.g., "8×250mm Smooth Rod, 8.00mm diameter")
- Honest shipping timeline (2-4 weeks from China, clearly stated)
- Seller responds to questions with clarification photos

### 4. Common Pitfalls & How to Avoid Them

| Pitfall | What Happens | How to Spot | Fix |
|---------|--------------|------------|-----|
| **Mixed pack sizes** | Order says "8 rods" but it's 2 long + 2 short + 4 medium | Check ALL photos carefully; count pieces | Message seller for specification |
| **Counterfeit bearings** | Fake IGUS or LM8UU logo; poor quality | Compare packaging to verified images; check seller history | Order from established 3D printer supplier |
| **Wrong lead screw pitch** | T8 comes in 2mm AND 8mm pitch; ordered wrong | Photos must show the pitch clearly; read reviews mentioning it | Verify with seller before ordering |
| **Wrong voltage PSU** | PSU says 12V but is actually 24V (or vice versa) | Check product photos for actual labels (not just title) | Message seller; ask for label photo |
| **Shipping takes forever** | "3-5 day shipping" actually takes 4-6 weeks | Read negative reviews about shipping time | Accept 2-4 weeks as realistic from China |
| **Broken on arrival** | Rod bent, bearing seized, PSU dead from shipping shock | Buy from sellers with good return policy; request protective packaging | Check AliExpress "buyer protection" or eBay returns |

### 5. Verification Tips

**Before you hit "buy":**

1. **Check seller profile**
   - How many items sold? (100+ = established)
   - What other products? (Do they specialize in 3D printer parts?)
   - Average rating? (4.5+ is good; <4.0 is risky)

2. **Read reviews carefully**
   - Skim positive reviews for specific product praise
   - Read negative reviews for patterns (e.g., "shipping took 2 months" vs. "bent on arrival")
   - Look for reviews with photos (shows real users tested it)

3. **Message seller if unclear**
   - Ask: "Is this [specific spec]?"
   - Ask for: Measurement photos, close-ups of packaging
   - Some sellers respond helpfully; others ignore you (red flag)

4. **Use buyer protection**
   - AliExpress: "Buyer Protection" covers most cases
   - eBay: "Item Not As Described" protection (good return policy)
   - Temu: Less reliable; avoid for critical parts

5. **Cross-check specs across listings**
   - If multiple sellers have the same product, do they all say the same spec?
   - If one says 8mm and another says "8.5mm precision rod," they're different
   - Trust the one with more reviews + photos

---

## Sourcing Strategy by Platform

### AliExpress
- **Pros:** Generally reliable, good buyer protection, low prices, photos often accurate
- **Cons:** Slow shipping (2-6 weeks), sometimes vague specs, disputes can take time
- **Tips:** Filter by "Free Shipping" (often built into price); read reviews for realistic times
- **Best for:** Common parts (rods, bearings, bolts); bulk orders

### Temu
- **Pros:** Aggressive pricing, fast initial delivery sometimes, growing inventory
- **Cons:** Newer platform, lower review counts, inconsistent quality, fewer detailed specs
- **Tips:** Stick to established sellers; avoid unique/critical items
- **Best for:** Non-critical items (bolts, misc hardware); budget sourcing

### eBay
- **Pros:** Fast local shipping (1-7 days), easy returns, verified sellers
- **Cons:** Higher prices, smaller selection of cheap parts
- **Tips:** Filter by "Ships from [your country]"; pay slightly more for speed/reliability
- **Best for:** Critical items (PSU, mainboard) where reliability matters more than cost

### Secondhand (Facebook Marketplace, Gumtree, Local)
- **Pros:** Inspect in person, negotiate price, immediate pickup
- **Cons:** Limited selection, condition varies, no returns
- **Tips:** Ask for photos of the actual item; test before buying if possible
- **Best for:** Motors, PSU, electronics (inspect for damage); larger items (reduces shipping)

---

## Budget: What to Expect

**Baseline donor pair assumption:**
- Two donors at $50-100 each: $100-200
- MDF base: $15-20
- Misc (bolts, wires): ~$30

**Add contingencies (parts you'll likely need to source):**
- M10 rods (Darwin path): $30-45
- M8 lead screws (1-2 extra): $15-25
- Extra bearings (if worn): $20-35
- Replacement PSU (if needed): $40-80
- Misc parts (springs, connectors, etc.): $20-30

**Total realistic budget:** $250-380 AUD

If you're hitting $300+ on donors + parts, reconsider (see [When NOT to Scavenge](donor-printer-guide.md#when-not-to-scavenge-enclosed--proprietary-printers)).

---

## Quick Decision Tree: Source or Scavenge?

When you find a part is missing/broken, decide quickly:

```
Is the part scavengeable from second donor?
  ├─ YES → Use it; inspect quality before assembly
  └─ NO → Go to next question

Is it a common part (rod, bearing, bolt)?
  ├─ YES → Source cheap from AliExpress/Temu; wait 3-4 weeks
  └─ NO → Go to next question

Is it critical (mainboard, PSU, hotend)?
  ├─ YES → Buy from eBay/local (faster, more reliable)
  └─ NO → Source cheap; can wait

Is your total cost (donors + parts) approaching $300?
  ├─ YES → Reconsider; just buy Bambu A1 Mini or Ender 3 V3 SE
  └─ NO → Proceed; you're in good budget territory
```

---

## Tips for Successful Sourcing

1. **Order early, expect delays** — Plan 3-4 weeks for AliExpress/Temu; 1 week for eBay local
2. **Buy spares of common wear items** — Get 2 sets of bearings/rods; they're cheap
3. **Verify measurements in photos** — Don't trust title specs alone; measure from photos
4. **Keep receipts & tracking** — In case you need to return/dispute
5. **Join communities** — Ask on 3D printing forums which sellers are reliable (this changes monthly)
6. **Test before assembly** — Roll rods on glass, spin motors by hand, measure diameters
7. **Account for shipping shock** — Order breakable items from sellers who use protective packaging

---

## Red Alert: When to Give Up and Buy New

If your sourced parts cost + donor cost exceed $320 AUD, **stop and recalculate.**

You're better off:
- **Bambu A1 Mini:** ~$180 AUD, brand new, warranty, proven print quality
- **Ender 3 V3 SE:** ~$150 AUD, budget option, great community support
- **Just Klipperize a single donor:** You already have one; upgrade it instead of Amalgam

Scavenging is about **smart reuse**, not **budget creativity**.

---

*"The parts you source should cost less than your donors. If not, you've lost the economics game."*
