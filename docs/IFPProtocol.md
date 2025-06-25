# IFPProtocol – Intelligent Fractal Propagation Protocol

**Author**: Engr. Juan Carlos G. Ayeng  
**Date Created**: June 25, 2025  
**Repository**: [mamawmail](https://github.com/juancarlosayeng/mamawmail)  
**License**: AGPLv3 with additional commercial terms  
**Status**: Draft v0.1 (subject to refinement with implementation)

---

## ✨ Overview

The Intelligent Fractal Propagation Protocol (IFPProtocol) is a decentralized message relay protocol designed for peer-to-peer delivery without central servers, persistent storage, or global routing.

Inspired by fractal growth patterns, the protocol propagates messages outward through trusted local relays using recursive 3-way hops with limited depth and memory tagging to prevent loops.

IFP is designed for:
- Censorship resistance
- Offline operation
- Disaster recovery and field communication
- AI-assisted learning and pruning

---

## 🔁 Core Mechanisms

### 1. **Fractal Branching**
Each message propagates via 3 trusted peers per hop. After 5 hops, the message is considered expired.

### 2. **"Been-Here" Tagging**
Each node marks seen headers to prevent reprocessing or circular propagation.

### 3. **Success-Based Pruning**
Once a delivery confirmation ("hit") is received, previous hops self-delete local copies.

### 4. **Redundancy Control**
The system supports exponential spread at early hops, then falls back to single-hop propagation once coverage stabilizes.

---

## 🔒 Message Anatomy

Each message packet includes:

- `header_id`: Unique hash or nonce identifying the message
- `payload`: Encrypted body (E2E encrypted)
- `path_meta`: Encrypted relay chain or scoring info
- `time_to_live`: Hop counter (5 max by default)

---

## 🧠 AI Routing Integration (Optional)

IFP supports integration with routing intelligence via:
- Peer scoring (trust, response time, reliability)
- Graph-based models (GNN or reinforcement learning)
- Data source: `path_scores.db` + plugin `ai_routing/scorer_gnn.py`

---

## 🧾 Licensing & Attribution

This protocol is © 2023–2025 by Juan Carlos G. Ayeng, released under AGPLv3 with additional terms for commercial use and branding.

> All implementations must include attribution and comply with licensing conditions.  
> For enterprise licensing or adaptation, contact: **jcgayeng@protonmail.com**

---

## 📎 Related Files

- `core/swarm_engine/relay_manager.py`: Main propagation logic
- `plugins/ai_routing/scorer_gnn.py`: Optional AI routing module
- `docs/architecture.md`: Full system design overview
- `mamawmail-whitepaper`: Theoretical foundations

---
