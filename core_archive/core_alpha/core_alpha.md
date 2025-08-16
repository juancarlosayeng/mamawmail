# Core Alpha Log

## v0.1 – Initial Sketch
- Defined **Message Architecture** draft:  
  - Packet header format: {id, hop-count, been-here-flag}.  
  - Payload: full encrypted message.  
- Very basic crawler: random walk over neighbors.

## v0.2 – Propagation Model Test
- Introduced **Fractal Hop Spread (3^N)**.  
- Observed runaway packet growth; pruning not yet implemented.  

## v0.3 – Early Privacy Notes
- Explored onion-style encryption vs header-only obfuscation.
