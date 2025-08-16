'''
# test_crawler.py

Module: Test Suite — Device Crawler
-----------------------------------

Validates the peer crawler responsible for discovering candidate devices.
Responsible for:
    - Testing peer discovery across simulated networks
    - Checking adaptive aggregation and grouping logic
    - Ensuring duplicate device suppression
    - Validating memory of past successful hops
    - Confirming crawler scalability under high node counts

Usage:
    Run via pytest to ensure device crawler remains efficient and accurate.

Author:
    Engr. Juan Carlos G. Ayeng
    Bacolod City, The Philippines
    © 2025

Version:
    0.1.0

License:
    MIT License (see LICENSE file)

Related:
    - core/crawler.py
    - core/swarm_manager.py
    - core/path_scores.db

Last updated:
    August 16, 2025

'''
