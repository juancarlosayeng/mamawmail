🌀 MAMAWMAIL Core — Pre-Alpha Snapshot

Date: 2025-06-20
Phase: Pre-Alpha (Exploratory Drafts)

🔹 Context

This archive contains the first experimental implementation of the MAMAWMAIL core logic.
It was created before the formal Alpha v1.0 specification (2025-08-16) and is preserved here for historical and technical reference.

At this stage, the design was unstructured and exploratory, testing ideas for:

Relay management

Swarm-level communication

Return signal feedback

Path scoring

These drafts were not compatible with the Alpha baseline, but they mark the earliest technical thinking behind MAMAWMAIL.

🔹 Archived Files

feedback/return_signals.py

Prototype for handling return acknowledgements in message hops.

ledger/path_scores.db

Early test database for path scoring metrics. Schema was experimental.

swarm_enginer/relay_manager.py

First attempt at a relay manager for swarm-like device hopping.

🔹 Notes

These files represent the pre-alpha exploratory phase.

Superseded by:
mamawmail/core/core_alpha_v1.0_2025_08_16.md

Retained only as historical design artifacts.

---------------------------------------------------------------------
# Core Pre-Alpha Snapshot – June 20, 2025

This directory contains the **first experimental implementation** of the MAMAWMAIL core logic.  
It was created before the formal Alpha specification (2025-08-16) and is kept here for historical and reference purposes.

## Files
- `feedback/return_signals.py`  
  Prototype for handling return signals in message hops.

- `ledger/path_scores.db`  
  Early database sketch for path scoring. Format and schema were experimental.

- `swarm_engine/relay_manager.py`  
  First attempt at a relay management engine. Contained basic swarm-like logic for device hops.

## Notes
- These files represent **initial concepts** and are **not compatible** with the current Alpha version.  
- They are archived here to preserve the development history.  
- The current active specification is:  
  `mamawmail/core/mamawmail/core_alpha_v1.0_2025_08_16.md`


