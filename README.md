-------
| REPO LINKS |
|----- |
| [MAMAWMAIL RESEARCH INITIATIVE](https://github.com/Mamawmail-Research-Initiative) : Github Organization  |
| [Intelligent Fractal Propagation Protocol](https://github.com/juancarlosayeng/mamawmail-intelligent-fractal-propagation-protocol-whitepaper) : IFPP Whitepaper  |
| [Mamawmail SYSTEM Whitepaper](https://github.com/juancarlosayeng/mamawmail-system-whitepaper) : IFPP Implementation/Application Whitepaper  |
| [Mamawmail](https://github.com/juancarlosayeng/mamawmail) : IFPP Implementation  |
-------

UPDATED: October 28 2025

### IFPP + MAMAWMAIL WHITEPAPER CURRENT STRUCTURE 

 
1. [x] [Intelligent Fractal Propagation Protocol Whitepaper](https://github.com/juancarlosayeng/mamawmail/blob/main/docs/The%20Intelligent%20Fractal%20Propagation%20Protocol%20(IFPP)%20A%20Protocol%20Originating%20from%20the%20MAMAWMAIL%20Project%20Whitepaper%20%E2%80%94%20September%2022%202025%20-%20Engr%20Juan%20Carlos%20G%20Ayeng%20-%20Bacolod%20City%20-%20Philippines.pdf)) 
   1. [x] Annex A [IFPP MESSAGE PACKET SPECIFICATION AND STATELESS TRANSPORT BEHAVIOR](https://github.com/juancarlosayeng/mamawmail-intelligent-fractal-propagation-protocol-whitepaper/blob/main/docs/ANNEX%20A%20-%20The%20Intelligent%20Fractal%20Propagation%20Protocol%20IFPP%20A%20Protocol%20Originating%20from%20the%20MAMAWMAIL%20Project%20Whitepaper%20%E2%80%94October%2015%202025%20-%20Engr%20Juan%20Carlos%20G%20Ayeng%20-%20Bacolod%20City%20-%20Philippines.pdf)
   2. [ ] Annex B - ONGOING - [IFPP PHYSICAL TRANSFER AND CARRIER LAYER EXPRESSIONS](https://github.com/juancarlosayeng/mamawmail/blob/main/docs/Annex_B-IFPP_Physical_Transfer_and_Carrier_Layer_Expressions.md) 
   3. [ ] Annex C - ONGOING - <b>Archangel Gabriel [AI]: Swarm Supra-Entity and Integrity Sentinel</b> 
  
      
2. [ ] Mamawmail Whitepaper - [ONGOING/Unfinished](https://github.com/juancarlosayeng/mamawmail/blob/main/docs/MAMAWMAIL%20-%20%20A%20Decentralized%20Communication%20System%20Updated%20Whitepaper%20%E2%80%94%20September%2027%202025%20(Original%20June%2020%202025)%20-%20Engr%20Juan%20Carlos%20G%20Ayeng%20-%20Bacolod%20City%20-%20Philippines.pdf)

  <br><br><br>
 SAMPLE ONGOING RESEARCH - adding more annexes, sections and research
## ANNEX-B Table: Projected Computational and Transmission Costs

This section quantifies the expected energy, storage, and bandwidth requirements during a full IFPP hop cycle between two devices.
The estimates are based on current-generation mobile hardware (ARM A53–A76 class CPUs, 4 GB RAM, 10 MB/s equivalent link) and optimized cryptographic operations (SHA3–256 and XChaCha20-Poly1305).
Values are averages designed for modeling and comparative evaluation with TCP/IP message delivery.
 <br>
| Stage                         | Description                                 | Device A (Sender)                                            | Device B (Receiver)    | Typical Duration | Notes                            |
|-------------------------------|---------------------------------------------|--------------------------------------------------------------|------------------------|------------------|----------------------------------|
| 1 – Payload Receipt           | App → Team Leader message load              |    8 KB RAM, 0.3 MB I/O                                      | -                      | 1ms              | No crypto; memory copy only      |
| 2 – Intel ↔ Gabriel           |    Candidate discovery, AI digest   sync    | 0.5 KB TX / 1 KB RX (≈1.5 KB total)                          | 0.5 KB RX / 1 KB TX    | 2–5 ms           |    Short JSON digest exchange    |
| 3 – Liaison Device Engagement | Candidate signal probe                      | < 2 KB RF signal frames                                      | 2 KB probe response    | 3-7 ms           | BLE/Wi-Fi beacon or UDP ping     |
| 4 – Point Binding             | Object binding + hash computation           | 32 KB RAM (SHA3) ≈ 2 ms CPU                                  | -                      | 2 ms             | 0.002 Wh compute cost            |
| 5 – Heavy Weapons Security    | Security update & verification              | 1 MB read + 64 KB write (≈2 MB I/O)                          | -                      | 15-25 ms         | Most expensive CPU stage (8%)    |
| 6 – Pre-Interaction Sync      | Angel team coordination                     | 128 KB RAM                                                   | 128 KB RAM             | 1 ms             | Negligible bandwidth             |
| 7 – Candidate Evaluation      | 3-node scoring and prioritization           |    1.5 MB RAM compute                                        | -                      | 5 ms             | Local AI inference vectorization |
| 8 – Recon Scouting            | Probe and verification on 3 targets         | 3 × 512 B TX                                                 | 3 × 512 B RX           | 8 ms             | Maintains micro-links            |
|    9 – Hop Decision           | Team Leader + Gabriel evaluation            | 64 KB RAM                                                    | -                      | <1 ms            | Decision matrix merge            |
| 10 – Security Instantiation   | Pre-arrival sandbox deploy                  | -                                                            | 0.5 MB disk write      | 5 ms             | Security sweep initialization    |
| 11 – Message Transfer         | Three-burst transmission                    | 2 KB (Ephemeral) + 4 KB (Metadata) + 10 KB (Core) = 16 KB TX | 16 KB RX               | 1-2 ms           | One-shot burst; no ACK cycle     |
| 12 – Post-Hop Deploy          | Angel re-spawn logic                        | 16 KB RAM                                                    | 32 KB RAM              | 2ms              | Code copy + hash verify          |
| 13 – Hop Confirm ↔ Gabriel    |    Hop status confirmation                  | 1 KB TX / RX                                                 | 1 KB TX / RX           | 1 ms             | Swarm ledger update              |
| 14 – All-Clear Signal         | Passive Gabriel confirmation                | -                                                            | < 0.1 KB RX            | Variable         | Triggered remotely               |
| 15 – Self-Deletion            | Memory release and cleanup                  |    32 KB RAM                                                 | -                      | 0.5 ms           | Garbage collection event         |
| 16 – Cycle Re-Instantiation   | Angel reload on next device                 | -                                                            | 64 KB RAM + 0.5 MB I/O | 2 ms             | Fresh process spawn              |


### Aggregate Resource Cost per Hop (One Device Pair)
| Metric                                         | Device A (Sender) | Device B (Receiver) |     Combined Total     |
|------------------------------------------------|-------------------|---------------------|------------------------|
|    Storage footprint (volatile + temp disk)    | ≈ 2.8 MB          | ≈ 1.1 MB            |    ≈ 3.9 MB            |
| Bandwidth usage (TX + RX combined)             | ≈ 25 KB           | ≈ 25 KB             | ≈ 50 KB per hop        |
| Energy draw                                    | ≈ 0.07 Wh         | ≈ 0.05 Wh           |    ≈ 0.12 Wh total     |
| Compute time (active CPU)                      | ≈ 70 ms           | ≈ 40 ms             | ≈ 110 ms total         |

<br><br><br><br>
## TCP/IP Transmission Baseline (10 KB Payload Example)
| Stage                    | Process                              | Device A (Sender) | Device B (Receiver) | Typical Duration |
|--------------------------|--------------------------------------|-------------------|---------------------|------------------|
| 1 – 3-Way Handshake      | SYN, SYN-ACK, ACK (3 packets × 60 B) | 180 B TX/RX       | 180 B TX/RX         | 15–30 ms         |
| 2 – TLS Handshake        | ECDHE + Certificate exchange         | 4 KB TX + 4 KB RX | 4 KB TX + 4 KB RX   | 120–200 ms       |
| 3 – Payload Transmission | 10.5 KB TX                           | 10.5 KB RX        | 10–20 ms            |                  |
| 4 – ACK & Keepalive      | 1 KB TX / RX                         | 1 KB TX / RX      | 5 ms                |                  |
| 5 – Session Close        | 0.5 KB TX / RX                       | 0.5 KB TX / RX    | 5 ms                |                  |

### Aggregate Cost (10 KB TCP Payload)
| Metric                             | Device A (Sender) | Device B (Receiver) |     Combined Total     |
|------------------------------------|-------------------|---------------------|------------------------|
| Bandwidth usage (over the air)     | 25 KB             | 25 KB               | ≈ 50 KB total          |
| Bandwidth usage (TX + RX combined) | 150–260 ms        | -                   | ≈ 200 ms average       |
| Energy draw                        | ≈ 0.30 Wh         | ≈ 0.25 Wh           | ≈ 0.55 Wh total        |
| Socket duration                    | 250 ms            | 250 ms              | -                      |

### Analytical Comparison
| Category           | IFPP [Per Hop]             | TCP/IP [10kb Message] | Relative Efficiency               |
|--------------------|----------------------------|-----------------------|-----------------------------------|
| Storage (volatile) | 3.9 MB                     | 4.0 MB                | ≈ Parity                          |
| Energy Draw        | 0.12 Wh                    | 0.55 Wh               | 4.5× more efficient               |
| Latency            | 110 ms                     | 200 ms                | ≈ 2× faster                       |
| Bandwidth          | 50 KB                      | 50 KB                 | Equal (IFPP includes AI metadata) |
| Security Overhead  | Self-authenticating digest | TLS cert chain        | ≈ 80% lighter                     |

<br>

## Interpretive Commentary  

### Compute Efficiency:
> IFPP’s event-driven architecture replaces persistent sockets with short-lived microtransactions, cutting power consumption by up to 75%.  

### Reduced Latency:
> Hop decisions overlap with Gabriel synchronization, enabling sub-100 ms behavior within three-hop swarm radius.  

### Stable Memory Pressure:  
> Because each angelic module self-deletes post-hop, per-device memory load remains constant even during heavy network churn.

### Security Simplicity:
> Eliminates TLS certificate dependencies — authentication occurs directly through device key digests.  

### Scalability Trend:
> As devices adopt multi-core AI accelerators (ARMv9 / RISC-V), IFPP’s efficiency gains scale sub-linearly with hop count, meaning greater network size yields higher relative throughput per watt.


<br><br><br><br>  
 




<hr>

UPDATED: October 14 2025

🧩 New Annex Added 

Annex A — IFPP Message Packet Specification and Stateless Transport Behavior
Defines the three-part IFPP message structure (Ephemeral Header, AI Metadata, Eternal Message Core) and outlines stateless, no-socket transport modes via UDP, Bluetooth, Wi-Fi, and TCP/IP bridge.

📘 Preview:
“Each IFPP message is composed of three interdependent yet independently storable components:
— Ephemeral Header – transient bootstrap and authentication data.
— AI Metadata – dynamic, self-evolving contextual information for learning and traceability.
— Eternal Message Core – immutable encrypted payload representing the true message.”


<details>
<summary>🧩 Annex A — IFPP Message Packet Specification and Stateless Transport Behavior</summary>

> Defines the three-part IFPP message structure (Ephemeral Header, AI Metadata, Eternal Message Core).  
>  
> 🔗 [Read Full Annex A (Markdown)](docs/Annex_A-IFPP_Message_Packet_Specification.md)  
> 📄 [Download PDF Version](docs/Annex_A-IFPP_Message_Packet_Specification.pdf)

</details>

<hr>


UPDATED: October 1 2025

# Submitted New IFPP Whitepaper to NLNET. 
- Separated IFPP from Mamawmail into its own Whitepaper.
<br><br>
- Github Repo about to be updated after finishing Mawmawmail Whitepaper.
<br><br>

-----------------------------------------------------



# WHATS NEW?
<br><br>
---
# UPDATE SUMMARY
UPDATED: August 24 2025

Part of the Mamawmail Research Initiative – practical implementation of the system.
----------------------------------------------------------------------
## Mamawmail Research Initiative – License Overview

The Mamawmail Research Initiative is a combined effort of theoretical research,  
system architecture design, and practical software implementation.  

It is organized into three connected repositories, each with its own license.  
The whitepapers provide the **research foundation** and theoretical framework,  
while the implementation repository translates those ideas into a working system.  

| Repository                                                | License                              | Purpose                                                   |
| --------------------------------------------------------- | ------------------------------------ | --------------------------------------------------------- |
| **mamawmail-intelligent-propagation-protocol-whitepaper** | CC BY-SA 4.0 (open research license) | Formal description of the Intelligent Fractal Propagation Protocol (IFPP), mathematical models, and comparisons |
| **mamawmail-system-whitepaper**                           | AGPL-3.0 (Community) + Commercial    | Broader system design, AI integrations, and saturation singularity theory |
| **mamawmail**                                             | AGPL-3.0 (Community) + Commercial    | Practical implementation of the Mamawmail system (Community & Enterprise editions) |


---------------------------------------------------------------------



<br><br>
---
# UPDATE SUMMARY
**August 20, 2025**  
<br><br>
<br>
*Intelligent Fractal Propagation Protocol [I.F.P.P] Technical Specification Defnition
<br><br>
<table align="center">
  <tr>
    <th align="center" style="font-size:20px;">I.F.P.P. Formal Description</th>
    <th align="center" style="font-size:20px;">I.F.P.P. Simplified Description</th>
  </tr>  
<tr>
<td width="50%" valign="top" >
<br>“In the initial propagation phase, nodes exhibit a fanout of \(k\), resulting in exponential reachability growth until the maximum fractal depth \(D\) is reached. For illustrative purposes, we select \(k=3\), a value chosen heuristically to approximate network saturation in a 1000-node environment without excessive redundancy. 
<br><br>This parameter is not fixed: in future iterations, the branching factor will be treated as a variable informed by network conditions and adaptive optimization.  
<br><br>In early simulations, IFPP behavior can be modeled within a TCP/IP framework for clarity of illustration, although the protocol itself is transport-agnostic.   
<br><br>Conceptually, equivalent behaviors could be observed in a theoretical UDP system or a Bluetooth mesh of 1000 devices.   
<br><br>These references are not implementations but testbeds for understanding propagation dynamics.”
<br><br><br><br>
</td>
<td width="50%" valign="top">
<br>“At the start, each device passes the message on to three others. 
  <br>This creates a branching, tree-like spread that grows very quickly, reaching most of the network in just a few steps. 
  <br><br>We chose the number three as a simple starting point because, in a group of about 1,000 devices, it lets the message spread widely without creating too many unnecessary duplicates. 
  <br><br>In later versions, this number will not be fixed — the system can adjust how many neighbors to pass the message to depending on how crowded or quiet the network is. 
  <br><br><br>For early testing, we can show this spreading pattern on common computer networks like the Internet (TCP/IP) or even imagine it working over wireless links such as Bluetooth. 
  <br><br>These examples are not finished systems, but just ways to picture how the spreading process works.”
<br><br><br><br>
</td>
</tr>
</table>
<br><br>
<br><br>
-------------------------
<br><br>
<br><br>

# UPDATE SUMMARY

**August 17, 2025**  

MAMAWMAIL Dual License
======================

MAMAWMAIL and the Intelligent Fractal Propagation Protocol (IFPP) are licensed under a dual-license model:

1. Community Edition
   Licensed under the GNU Affero General Public License, Version 3 (AGPL-3.0).
   You may use, modify, and distribute this software provided that:
   - Source code is made available for all derivative works.
   - Network-accessible versions of the software must also publish source code.
   - Attribution to the original author ("Juan Carlos Ayeng / Red Kamatis Virtual Studios") must be preserved.
See full license text below.

2. Enterprise Edition
   A **commercial license** is available for organizations that:
   - Wish to build proprietary modules without releasing source code.
   - Require enterprise support, advanced modules, or service-level agreements.
   Please contact: jcgayeng@protonmail.com for details.

---

## Attribution and Integrity

- No part of this project may be **relicensed, renamed, forked, or represented as an independent protocol** without proper attribution.  
- The name **MAMAWMAIL** and **IFPP (Intelligent Fractal Propagation Protocol)** are trademarks of the author.  

---

MAMAWMAIL Enterprise License Agreement
Copyright (C) 2025 Juan Carlos Ayeng
All rights reserved.

-------------------------------------------------
<br><br>
<br><br>

# UPDATE SUMMARY

**August 16, 2025**  

## Alpha v1.0 Release – Core Protocol Structure Finalized

MAMAWMAIL enters **Alpha stage (v1.0)** with a restructured codebase, modular headers, and evaluator-ready documentation.  
Focus of this release is on clean separation of modules, test coverage scaffolding, and documentation consistency.

---
<br><br>
<br><br>

### A. Core Restructuring
- Orchestration, propagation, AI, crawler, privacy, and singularity logic separated into clear submodules.  
- Archived pre-alpha work in `core_archive/` (snapshot preserved: June 20, 2025).  
- Introduced standardized headers across all `.py` files and test files.

- **Seven Architectures (Prototype — In Progress; Last Updated: 2025-08-13)**

1) **Message Architecture**  
   Messages are structured in three modular parts:  
   **Ephemeral Headers** (transit-only IDs) | **Path / AI Meta** (routing & scoring) | **Payload** (encrypted body for recipient only).

2) **Propagation Architecture**  
   Packets use a **fractal propagation pattern**. **Federated Learning** selects between  
   **Fractal hops** (redundant, multi-branch) vs **Singular hops** (shortest optimal route).

3) **Crawler Architecture**  
   **Primary locator:** IP. **Fallbacks:** Bluetooth radio, UDP hole punching, and proximity discovery.

4) **Intelligence Layer (AI) Architecture**  
   Stores **success/failure routing patterns without payloads**; learns from behavior and shares intelligence with the swarm.

5) **Self-Healing & Self-Pruning Architecture**  
   On **successful handoff**, transient packets are deleted from non-destination nodes.  
   If no known-good path exists, new paths are explored until one is found.

6) **Singularity Architecture**  
   **6A. Horizontal Singularity:** Map device-to-device paths to **maximize delivery** while **minimizing hops** (saturation when paths are fully mapped).  
   **6B. Vertical Singularity:** Minimize **packet size/count** to achieve **lowest latency**; continually reduce **failure decay**.

7) **Privacy Architecture**  
   Payloads are **not required** for AI scoring/routing and remain **ephemeral** in transit.  
   Decryption is possible **only** with the destination device’s matching hash.

<br><br>   

```
root/core/mamawmail/
│
├── orchestration/
│   ├── __init__.py
│   ├── workflow_controller.py        # Runs modules in sequence or parallel
│   ├── config_loader.py               # Reads YAML/JSON configs
│   ├── logging_monitor.py             # Unified log/metrics collector
│   └── dev_launcher.py                # Test launcher for specific modules
│
├── message_architecture/
│   ├── __init__.py
│   ├── packet_builder.py               # Creates encrypted message packets
│   ├── header_manager.py               # Handles addressing, 'been here' flags
│   └── integrity_validator.py          # Ensures packet consistency
│
├── propagation/
│   ├── __init__.py
│   ├── fractal_propagator.py           # Intelligent Fractal Propagation logic
│   ├── hop_manager.py                  # Manages multi-hop routing rules
│   └── redundancy_optimizer.py         # Controls exponential spread vs efficiency
│
├── crawler/
│   ├── __init__.py
│   ├── device_discovery.py             # Finds candidate devices
│   ├── candidate_scoring.py            # Scores for availability/reliability
│   └── neighborhood_mapper.py          # Maps device clusters
│
├── ai_engine/
│   ├── __init__.py
│   ├── relay_score_predictor.py        # Predicts best relay nodes (ML)
│   ├── anomaly_detector.py             # Flags strange traffic patterns
│   └── learning_manager.py             # Manages retraining & models
│
├── adaptive_topology/
│   ├── __init__.py
│   ├── topology_optimizer.py           # Prunes, merges, balances links
│   ├── topology_recovery.py            # Self-healing after disconnection
│   └── topology_history.py             # Tracks changes over time
│
├── singularity_manager/
│   ├── __init__.py
│   ├── convergence_detector.py         # Detects swarm-level synchronization
│   ├── singularity_resolver.py         # Decides actions when singularities occur
│   └── stability_predictor.py          # Predicts likelihood of singularity events
│
├── privacy/
│   ├── __init__.py
│   ├── encryption_manager.py           # Handles E2E encryption logic
│   ├── metadata_scrubber.py            # Removes identifying metadata
│   └── key_rotation.py                 # Periodic key regeneration
│
└── tests/
    ├── test_message_architecture.py
    ├── test_propagation.py
    ├── test_crawler.py
    ├── test_ai_engine.py
    ├── test_adaptive_topology.py
    ├── test_singularity_manager.py
    ├── test_privacy.py
    └── test_orchestration.py
```








### B. Testing Framework
- Created `tests/` directory with unit test scaffolds for each subsystem.  
- Added `tests/README.md` with clickable links to test files for evaluator navigation.  
- Ensures traceability: each test file maps to a corresponding module group.  


⚠️ **Notice (2025-08-16):**  
Automated execution of tests is **not yet available** in this alpha release.  
The scaffolding is complete and ready, but execution scripts and CI integration will be delivered in **Beta (Q4 2025)**.  

```bash
pytest core/mamawmail/tests/ -v   # (Planned availability in Beta)

-Tests are updated in parallel with core protocol modules.
-Designed to support continuous integration (CI/CD) pipelines.
-Some tests require mock relay peers and simulated swarm conditions.

---

## 🔹 Related Modules

| Test File                          | Target Module(s)                          |
|------------------------------------|-------------------------------------------|
| `test_message_architecture.py`     | `message_architecture.py`                  |
| `test_propagation.py`              | `propagation.py`, `relay_manager.py`       |
| `test_crawler.py`                  | `crawler.py`, `device_manager.py`          |
| `test_ai_engine.py`                | `ai_engine.py`, `scoring.py`               |
| `test_adaptive_topology.py`        | `adaptive_topology.py`                     |
| `test_singularity_manager.py`      | `singularity_manager.py`, `relay_manager.py` |
| `test_privacy.py`                  | `privacy.py`, `encryption.py`              |
| `test_orchestration.py`            | `orchestration.py`, integrates all modules |

---

```

### C. Documentation & Conventions
- Added naming/versioning rules for major checkpoints (`core_alpha_v1.0_YYYY-MM-DD.md`).  
- Defined release versioning scheme for evaluator clarity.  
- Established a **“What’s New”** log for incremental evaluator tracking.  

---

## Coming Soon
- Simulation-based integration testing.  
- Automated CI/CD pipeline integration.  
- Beta documentation layer with interactive visuals.  

<br><br>
 
---------------------------------------------------------------------

<br><br><br><br><br><br><br><br><br>

## UPDATE SUMMARY
July 20 2025

# Fractal Macro AI + Fractal Micro AI [Multi-Level AI]
> ### 1. Swarm-Level [System-Wide]
> ### 2. Device-Level [Device AI]


## A. Swarm-Level AI
MAMAWMAIL's decentralized network doesn't rely on one central AI. Instead, intelligence emerges from a swarm of devices: Micro AI handles routing and trust per device, while Macro AI learns across the entire swarm to guide propagation, optimize delivery, and control fractal behavior.
Monitors System of Devices, their info and knowledge of aggregated pathway lessons. Optimization for message success rate vs network load.

This architecture merges local autonomy and global learning into a self-improving system.


Swarm-Level AI can adjust:

> #### 1. Propagation Radius;
> #### 2. Max Fractal Hops per device, Start Singular Hops;
> #### 3. Grouping/Clustering, and other macro-level management;


## B. Device-Level AI
MAMAWMAIL's Device-Level AI Agent on each device [mainly] a lightweight scoring function.
Learns:

> #### 1. Best neighbors for routing.
> #### 2. Local traffic conditions. [Crawler AI]
> #### 3. Success/failure of past hops.

Output:
> #### 1. Propagation Control: Crawler 'Been Here' Packet Acceptance/Rejection
> #### 2. Transmit / Handoff Logic
> #### 3. Retrieval, Incorporation of System Learned Pathways





## AI Architecture Comparison: Gemini vs. MAMAWMAIL

While Google Gemini AI powers centralized, cloud-based intelligence for search tasks, **MAMAWMAIL** operates on a radically different model — a decentralized swarm where intelligence is distributed. Here's a side-by-side breakdown of how each system handles core AI components:

| **Component**       | **Google Gemini AI**                | **MAMAWMAIL AI Layer**                       |
|---------------------|-------------------------------------|----------------------------------------------|
| **Query Parsing**   | LLM on server                       | Micro AI classifies message priority         |
| **Context Awareness**| Gemini contextualizes search       | Micro AI analyzes device context             |
| **Synthesis**       | Gemini composes direct answer       | Macro AI guides swarm routing                |
| **Learning Loop**   | Feedback from user queries          | Feedback from packet delivery stats          |

In essence, **Gemini** operates as a cloud monolith with powerful but centralized intelligence. **MAMAWMAIL** flips the model: by embedding local learning into each node and coordinating behavior swarm-wide, it creates emergent intelligence without centralized servers.

This shift from **cloud AI** to **edge-swarmed AI** marks a foundational innovation in decentralized messaging and infrastructure resilience.


<hr>
 
# Summary
July 18 2025<br>

initial webpage design, ui and ux...ongoing
<br>
https://juancarlosayeng.github.io/mamawmail/
<br>
![Under Construction](webpage_july2025/images/underconstruction.png)
<br><br>
<p align="center">
  <img src="webpage_july2025/images/3123.PNG" alt="Screenshot" width="52%">
</p>



<hr>
July 13 2025

> ## SUMMARY

1. Identified, selected and informed initial TEAM Members;
2. Finalized System Architecture;
3. Creating and finishing Architecture Animations;
4. Creating and Finishing Github Website;
5. Mamawmail Packet Design, Preprocess, Handoff, Handshake, Return Trail Algorithm;
6. Web presence;
<ul>
  <li>[Facebook](https://www.facebook.com/profile.php?id=61577966164619&sk=about)</li>
  <li>[X](https://x.com/AyengJuan78960)</li>
  <li>[Youtube](https://www.youtube.com/@buhaykamatis1244)</li>
</ul>








> ## ARCHITECTURE
[Pre-Alpha] : More on Website. This system is what makes Mamawmail different, censorship-free, disasater-resilient, anonymous
> ### 1. Message Architecture
> ### 2. Propagation Architecture
> ### 3. Crawler Architecture
> ### 4. Intelligence Layer [AI] Architecture
> ### 5. Self-Healing | Self-Pruning Architecture
> ### 6. Singularity Architecture [MATH]
> ### 7. Privacy Architecture
Thank you JC Ayeng

<hr>
<br><br><br><br>
<hr>

> # MAMAWMAIL: An AI-Assisted Decentralized Messaging Protocol Using Fractal Propagation

## 📘 Abstract

**MAMAWMAIL** is a decentralized, peer-to-peer messaging protocol that delivers encrypted messages without central servers or permanent infrastructure.  
Using a fractal propagation model, messages branch through nearby devices and self-clean upon successful delivery. It integrates lightweight routing intelligence and prepares for optional AI-based learning to optimize delivery paths over time.

MAMAWMAIL is designed to be censorship-resistant, infrastructure-free, and suitable for use in disaster zones, offline environments, and sensitive field operations.

This repository contains the **source code implementation** of the protocol engine.

> 📘 Whitepaper, architecture rationale, and grant documentation:  
> https://github.com/juancarlosayeng/mamawmail-whitepaper

---

## 🎯 Project Goals

- Enable secure, serverless messaging using local device relays (Bluetooth, Wi-Fi Direct, UDP)
- Create a propagation system that is self-pruning, resilient, and scalable
- Add lightweight peer learning to improve routing over time
- Support future extensions like group messaging and swarm optimization
- Provide a modular open-source reference for mesh-based communication systems

---

## ✨ Key Features

- Fractal message propagation (3-way hops, 5-depth maximum or configurable)
- Self-cleaning message trails after successful delivery
- Local peer scorecard and memory optimization (SQLite)
- Optional AI-assisted routing (plugin-based: GNN, heuristics, etc.)
- Encrypted, end-to-end peer-to-peer delivery
- Plugin architecture for simulation, tracing, fleet control

---

## 📦 Use Cases

- Disaster zone communication without signal
- Military field coordination in disconnected areas
- Censorship resistance in restricted networks
- Messaging inside factories, ships, or campuses
- Educational use for decentralized learning and AI swarm modeling

---

## 🗂 Directory Overview

```text
mamawmail/
├── core/              # Main protocol components
│   ├── swarm_engine/  # Relay logic (e.g., relay_manager.py)
│   ├── encryption/    # E2E cryptography layer
│   ├── feedback/      # Handles receipts and cleanup
│   ├── ledger/        # Path memory via local SQLite
│   ├── ui/            # Console interface
│   └── config/        # System configuration
│
├── plugins/           # Optional AI, tracing, visual, enterprise tools
├── scripts/           # Bootstrap tools and CLI
├── tests/             # Unit and integration test cases
├── docs/              # Developer documentation
│   ├── architecture.md
│   ├── install_guide.md
│   └── plugin_specs/
└── README.md
```

---


## 📄 License
### 1. Source Code:
- Licensed under the MIT License — free for commercial and personal use.

### 2. Protocol & Documentation:
- See the mamawmail-whitepaper repo.
- Protocol design is AGPLv3; documentation is CC BY-NC-ND 4.0.

### 3. Commercial Use:
- Use of MAMAWMAIL or IFPProtocol in enterprise, military, or branded deployments requires a commercial license.
- The name, icon, and "MAMAWMAIL" trademark are not open source.

📩 For licensing inquiries: jcgayeng@protonmail.com



## 🧠 IFPProtocol – Intelligent Fractal Propagation Protocol
** Author: Engr. Juan Carlos G. Ayeng
** First Published: June 25, 2025
** Repository: mamawmail
** Whitepaper: mamawmail-whitepaper

Definition
The Intelligent Fractal Propagation Protocol (IFPProtocol) is the core relay system that powers MAMAWMAIL. It enables:

- Recursive 3-way branching with a default 5-hop maximum
- "Been-here" tagging to avoid circular delivery
- Success-based deletion and pruning of old paths
- Optional integration with AI-based peer scoring
- Designed for disconnected and infrastructure-hostile environments.

## 🤝 Contributions
We welcome testers, peer-to-peer developers, offline-first engineers, and mesh networking researchers.
Please open issues, submit pull requests, or share test scenarios and datasets.

## ✍️ Citation
** Author: Engr. Juan Carlos G. Ayeng
** 📄 Whitepaper: MAMAWMAIL: A Fractal, Serverless, Self-Optimizing Communication Protocol
** © 2025. All rights reserved.








