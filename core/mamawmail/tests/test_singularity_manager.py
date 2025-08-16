'''
# test_singularity_manager.py

Module: Test Suite — Singularity Manager
----------------------------------------

Validates the system’s handling of propagation singularities and control thresholds.
Responsible for:
    - Testing fractal hop limit enforcement
    - Checking prevention of uncontrolled propagation loops
    - Validating "max fractal" threshold switching to single-hop
    - Ensuring proper clean-up after singularity conditions
    - Measuring stability under high-volume swarm traffic

Usage:
    Run via pytest to ensure singularity management prevents runaway propagation.

Author:
    Engr. Juan Carlos G. Ayeng
    Bacolod City, The Philippines
    © 2025

Version:
    0.1.0

License:
    MIT License (see LICENSE file)

Related:
    - core/singularity_manager.py
    - core/propagation_engine.py
    - core/return_signals.py

Last updated:
    August 16, 2025

'''
