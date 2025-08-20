# WHATS NEW?
<br><br>
---
# UPDATE SUMMARY

**August 20, 2025**  
<br><br>
<br>
*Intelligent Fractal Propagation Protocol [I.F.P.P] Technical Specification Defnition
<br><br>
<table>
<tr>
   <td style="text-align: justify;"><b></b>**I.F.P.P. Formal Description**</b></td>
   <td style="text-align: justify;"><b></b>**I.F.P.P. Simplified Description**</b></td>
</tr>   
<tr>
<td width="50%" valign="top" 
   style="
       padding: 2rem 3rem;
       line-height: 2.6rem;
       text-indent: 3.6rem;
       text-align: justify;
    ">



“In the initial propagation phase, nodes exhibit a fanout of 
\(k\), resulting in exponential reachability growth until the maximum fractal depth \(D\) is reached. For illustrative purposes, we select \(k=3\), a value chosen heuristically to approximate network saturation in a 1000-node environment without excessive redundancy. This parameter is not fixed: in future iterations, the branching factor will be treated as a variable informed by network conditions and adaptive optimization. In early simulations, IFPP behavior can be modeled within a TCP/IP framework for clarity of illustration, although the protocol itself is transport-agnostic. Conceptually, equivalent behaviors could be observed in a theoretical UDP system or a Bluetooth mesh of 1000 devices. These references are not implementations but testbeds for understanding propagation dynamics.”

</td>
<td width="50%" valign="top"
   style="
       padding: 2rem 3rem;
       line-height: 2.6rem;
       text-indent: 3.6rem;
       text-align: justify;
    ">



“At the start, each device passes the message on to three others. This creates a branching, tree-like spread that grows very quickly, reaching most of the network in just a few steps. We chose the number three as a simple starting point because, in a group of about 1,000 devices, it lets the message spread widely without creating too many unnecessary duplicates. In later versions, this number will not be fixed — the system can adjust how many neighbors to pass the message to depending on how crowded or quiet the network is. For early testing, we can show this spreading pattern on common computer networks like the Internet (TCP/IP) or even imagine it working over wireless links such as Bluetooth. These examples are not finished systems, but just ways to picture how the spreading process works.”

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








