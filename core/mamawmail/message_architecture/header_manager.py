'''
Module: Header Manager
----------------------

Handles packet headers including addressing and traversal flags.  

Responsibilities:
    - Assign sender/receiver metadata
    - Track "been here" propagation markers
    - Control TTL (hop depth)
    - Support multi-device routing

Usage:
    Imported by `packet_builder.py` and `fractal_propagator.py`.  

Author: Engr. Juan Carlos G. Ayeng  
Version: 0.1.0  
License: MIT License  
Last updated: Aug 16, 2025  

'''
