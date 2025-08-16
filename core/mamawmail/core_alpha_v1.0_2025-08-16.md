# 🌀 MAMAWMAIL Core — Alpha Phase (v1.0)

**Date:** 2025-08-16  
**Phase:** Alpha  
**Version:** 1.0  

---

## 🔹 Overview

This document represents the **first formalized architecture draft** of the MAMAWMAIL system.  
It establishes both:
- The **baseline architecture and design goals** for Alpha.  
- The **naming/archival convention** that will be used across all future phases.  

The **Alpha Phase** is exploratory, meaning assumptions may change.  
The goal is to establish a working model of the **Intelligent Fractal Propagation Protocol (IFPP)** and verify minimum viable functionality.

---

## 🔹 Phase Intent

- Define **minimum viable architecture** for the relay system.  
- Test **device-to-device propagation** using fractal logic.  
- Create a **baseline workflow** for packet hopping, redundancy, and deletion.  
- Identify pain points to refine in the upcoming **Beta Phase**.  

---

## 🔹 Key Components (Alpha v1.0)

1. **Packet Structure**  
   - Header, payload, propagation markers (`been here`, fractal depth).  
   - Includes deletion signals after confirmed delivery.  

2. **Relay Engine**  
   - Implements hopping (3^n fractal spread).  
   - Applies **temporary storage + redundancy** rules.  
   - Deletes transient packets when handoff is successful.  

3. **Fractal Threshold Control**  
   - Expansion up to hop-depth 5 (≈ 3⁵ spread).  
   - Beyond threshold → switches to single-hop propagation.  

4. **Message Lifecycle**  
   - Creation → Fractal Spread → Redundancy → Delivery → Cleanup.  

---

## 📌 Naming Convention for Core Files

Each core documentation file follows this pattern:

