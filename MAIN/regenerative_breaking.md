
# Theme: Regenerative Breaking
----
## Research/Background
---
Article: **Energy-saving Carriages for Tokaido Shinkansen Trains**

Define: converts kinetic energy into electric energy (power generation) by using electric motors as generators during braking
- channel the generated power to the overhead line for use by other trains
- idea: run motor forward => create mech energy; run backwards => vehicle's momentum = mech energy

Examples of use cases:
- JR Tokai put power regenerative braking to Series 300 - Series 700 and N700 trains.
  - Series 700 trains, 12 of the normal 16 carriages were equipped with the brake system
  - Series N700, 14 carriages to acquire all the braking force usually required for a train
 
## Implementation (Research)
---

1. Maglev Motors = Generators
  - LIMs (our accelerators) = generators
  - cart slows down, linear motors reverse function

2. Energy Storage
  - within cart or along tracks to store recovered energy
  - Options: batteries, supercapacitors (faster charge/discharge)
      - Supercapacitors: good for frequent charge/discharge (immediate use), less storage capacity, but long lifespan
      - Batteries: dense storage, but smaller lifespan, slower charge/discharge, and heat intensive at times
      - Flywheel: simple, fast charge/discharge, but requires weight & extra implementation to prevent loss of energy
  - Idea: on tracks, then ideal for start-stop operations can enable charge/discharge features
    - good idea bc energy can be distributed across tracks, fed into nearest storage system, central management via API
  - Idea: within cart, then on-demand charge/discharge, but at the cost of a heavier cart (not a fan)
  - **Bonus: stores mechanical energy, reducing heat waste, and increasing cooling load :D**
    - could be another factor to consider when deciding between placing the supercapacitors on/off cart
    - consider: if LIM accelerators and cart don't touch, then we can't auto-transfer the regenerated energy

3. Power Management System (How recovered energy is used?)
  - Use Options: power carts, power other parts of data center, or store
      - anay unused energy regenerated can be direted to power other parts of the data center
  - When Options: immediate, on-demand, hold until peak demands
  - Software API:
    - track stored energy in storage
    - track state of charge in carts
    - manage where energy goes

## LIMs as Generators
## Power Manamgement System
## Cooling

