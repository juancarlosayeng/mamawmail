'''
Module: Configuration Loader
----------------------------

Reads YAML/JSON configuration files and injects runtime parameters.  

Responsibilities:
    - Load configs for modules
    - Validate schema and defaults
    - Allow dynamic overrides via CLI or API
    - Ensure consistency across distributed nodes

Usage:
    Imported by `workflow_controller.py` and all major modules needing configs.  

Author: Engr. Juan Carlos G. Ayeng  
Version: 0.1.0  
License: MIT License  
Last updated: Aug 16, 2025  

'''
