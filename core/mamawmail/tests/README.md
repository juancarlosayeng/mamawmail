# 🧪 MAMAWMAIL Test Suite

**Directory:** `core/mamawmail/tests/`  
**Phase:** Alpha v1.0 (2025-08-16)  

---

## 🔹 Overview

This directory contains **unit tests and integration tests** for the  
MAMAWMAIL Intelligent Fractal Propagation Protocol (IFPP).  

The test suite ensures that all **core components** of the relay engine,  
crawler, AI scoring layer, and adaptive swarm logic behave as expected.  

---

## 🔹 Test Files

- `test_message_architecture.py`  
  Validates message packet structure, headers, and encryption integrity.

- `test_propagation.py`  
  Tests fractal propagation behavior, hop limits, pruning, and redundancy.

- `test_crawler.py`  
  Ensures device discovery, candidate aggregation, and swarm-level crawling.

- `test_ai_engine.py`  
  Verifies adaptive AI scoring of paths and feedback loop integration.

- `test_adaptive_topology.py`  
  Confirms real-time adjustment of relay topology under swarm changes.

- `test_singularity_manager.py`  
  Tests detection and handling of propagation singularities (deadlocks/loops).

- `test_privacy.py`  
  Validates encryption, anonymity guarantees, and local-only message retention.

- `test_orchestration.py`  
  Integration-level orchestration across relay, crawler, and AI components.

---

## 🔹 Usage

⚠️ **Notice (2025-08-16):**  
Automated tests are not yet available in this alpha release.  
The test suite directory and specifications are prepared, but execution scripts will be enabled in upcoming updates once the **core protocol stabilizes**.  

Planned availability: **Beta Release (Q4 2025)**  
```bash
pytest core/mamawmail/tests/ -v


🔹 Notes

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


Maintainer:
Engr. Juan Carlos G. Ayeng
Bacolod City, The Philippines
© 2025 — MIT License

