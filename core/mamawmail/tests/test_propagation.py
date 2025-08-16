'''
# test_propagation.py

Module: Test Suite — Propagation Engine
---------------------------------------

Validates packet propagation under the Intelligent Fractal Propagation Protocol (IFPP).
Responsible for:
    - Verifying correct multi-hop forwarding
    - Testing propagation termination with "been here" flags
    - Checking redundancy and fractal expansion limits
    - Measuring delivery times under simulated topologies
    - Ensuring deletion signals are correctly propagated upstream

Usage:
    Run via pytest to benchmark swarm-level delivery performance.

Author:
    Engr. Juan Carlos G. Ayeng
    Bacolod City, The Philippines
    © 2025

Version:
    0.1.0

License:
    MIT License (see LICENSE file)

Related:
    - core/relay_manager.py
    - core/return_signals.py
    - core/propagation_engine.py

Last updated:
    August 16, 2025


'''
