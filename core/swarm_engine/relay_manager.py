"""
relay_manager.py

Module: Fractal Propagation Relay Manager
-----------------------------------------

Implements the Intelligent Fractal Propagation Protocol (IFPP), responsible for:
    - Branch-based message forwarding across peer nodes
    - Hop control and redundancy-limited propagation
    - "Been-here" tagging to avoid circular paths
    - Success-based pruning and deletion signaling
    - Optional integration with AI-based path scoring

This module handles the core relay logic for MAMAWMAIL — a decentralized,
AI-assisted messaging protocol with no centralized servers.

Usage:
    Imported as part of the `core.swarm_engine` package.
    Run indirectly via `bootstrap_node.py` or node handler scripts.

Author:
    Engr. Juan Carlos G. Ayeng
    Bacolod City, The Philippines
    © 2025

Version:
    0.1.0

License:
    MIT License (see LICENSE file)

Related:
    - return_signals.py: for handling receipt and cleanup
    - path_scores.db: for memory of past successful paths
    - scorer_gnn.py: AI plugin for adaptive path scoring
    - whitepaper: https://github.com/juancarlosayeng/mamawmail-whitepaper

Last updated:
    June 25, 2025
"""
