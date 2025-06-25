# MAMAWMAIL

**AI-Assisted Decentralized Messaging Protocol Using Fractal Propagation**

MAMAWMAIL is a no-server, peer-to-peer messaging protocol designed to deliver encrypted messages through a resilient fractal propagation system. It eliminates centralized infrastructure by using intelligent, self-pruning message hops across a device mesh network.

This repository contains the source code implementation of the protocol engine.

> 📘 Whitepaper, architecture rationale, and grant documentation:  
> https://github.com/juancarlosayeng/mamawmail-whitepaper

---

## 🔧 Features

- Fractal-based message propagation (3⁵ or configurable branch depth)
- Self-cleaning message trails after successful delivery
- Path scoring and memory optimization (SQLite-based)
- Support for optional AI-guided routing (plugin)
- Encrypted, end-to-end peer-to-peer delivery
- Plugin architecture for simulation, tracing, and enterprise features

---

## 📄 License

This codebase is released under the [MIT License](LICENSE). You are free to use, modify, and distribute this implementation for personal and commercial projects without restriction.

> ⚠️ For licensing of the protocol theory, documentation, or brand name, see the MAMAWMAIL whitepaper repository.


---

## 🗂 Directory Overview
mamawmail/
├── core/ # Main protocol components
│ ├── swarm_engine/ # Relay logic (e.g., relay_manager.py)
│ ├── encryption/ # E2E cryptography layer
│ ├── feedback/ # Handles receipt confirmations
│ ├── ledger/ # Local SQLite path database
│ ├── ui/ # Terminal/console interface
│ └── config/ # Settings and system parameters
│
├── plugins/ # Optional AI, fleet control, visual tools
├── scripts/ # Dev tools, bootstrap scripts
├── tests/ # Unit and integration tests
├── docs/ # Internal dev documentation
│ ├── architecture.md
│ ├── install_guide.md
│ └── plugin_specs/



## 👤 Author

- **Engr. Juan Carlos G. Ayeng**  
  Bacolod City, The Philippines  
  GitHub: [@juancarlosayeng](https://github.com/juancarlosayeng)  
  Contact: jcgayeng@protonmail.com

