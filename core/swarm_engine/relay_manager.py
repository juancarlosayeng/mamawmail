"""
relay_manager.py

Module: Fractal Propagation Relay Manager
-----------------------------------------

Implements: IFPProtocol – Intelligent Fractal Propagation Protocol

This module is responsible for:
    - Branch-based message forwarding across peer nodes
    - Hop control and redundancy-limited propagation
    - "Been-here" tagging to avoid circular paths
    - Success-based pruning and deletion signaling
    - Optional integration with AI-based path scoring

relay_manager.py handles the core decentralized relay logic for MAMAWMAIL —
an AI-assisted, serverless messaging protocol built for offline-first and
censorship-resistant communication.

Usage:
    Imported as part of the `core.swarm_engine` package.
    Typically invoked via `bootstrap_node.py` or node orchestration scripts.

Author:
    Engr. Juan Carlos G. Ayeng  
    Bacolod City, The Philippines  
    © 2025

Version:
    0.1.0

License:
    AGPLv3 (see LICENSE)

First Published:
    https://github.com/juancarlosayeng/mamawmail

Related Modules:
    - return_signals.py: Handles relay acknowledgements and deletion signals
    - path_scores.db: Records adaptive memory of successful paths
    - scorer_gnn.py: Plugin for AI-based dynamic scoring
    - Whitepaper: https://github.com/juancarlosayeng/mamawmail-whitepaper

Last updated:
    June 25, 2025
"""
