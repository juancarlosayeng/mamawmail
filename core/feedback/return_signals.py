'''
return_signals.py

Module: Delivery Feedback and Signal Handler
--------------------------------------------

Handles downstream signaling mechanisms in the Intelligent Fractal Propagation Protocol (IFPP).
Responsible for:
    - Receiving and interpreting delivery confirmations
    - Triggering upstream deletion of intermediate nodes after successful delivery
    - Sending failure or retry signals when propagation fails
    - Updating local relay logs and path memory
    - Supporting real-time pruning of active paths to preserve bandwidth and storage

Part of the MAMAWMAIL core protocol, this module supports a decentralized, self-cleaning
propagation model across a peer-to-peer swarm.

Usage:
    Called by `relay_manager.py` and optionally by path scoring or monitoring subsystems.

Author:
    Engr. Juan Carlos G. Ayeng
    Bacolod City, The Philippines
    © 2025

Version:
    0.1.0

License:
    MIT License (see LICENSE file)

Related:
    - relay_manager.py: initiates message propagation and tracks states    
    - tracer.py: optional plugin for debug tracing and feedback visualization
    - path_scores.db: for memory of past successful paths
    - scorer_gnn.py: AI plugin for adaptive path scoring
    - whitepaper: https://github.com/juancarlosayeng/mamawmail-whitepaper

Last updated:
    June 25, 2025
'''


