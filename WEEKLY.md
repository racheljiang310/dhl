# Weekly Research Progress Update
---
**Name:** [Rachel Jiang]  
**Research Topic:** [DHL]  
**Week:** [10]: Mar 14 🥧

---

## 1. **Overview of Progress**

This week progress: Happy 🥧 Day!

- pause on simulation
- updated Cart Mass Calculations spreadsheet:
  - targeting Rocket 4 Plus SSD (8TB), specific mass is really hard to find, so I estimated based on finding common density and dimensions of some parts
  - calculated estimations for power consumption and recovery via tweaking parameters
  - link to [calculations](https://docs.google.com/spreadsheets/d/1-Co3nxuuoy1GcUiEevEvnTI8xphWBnEozjH-1yfd05E/edit?gid=0#gid=0)
- Studied SCMaglev vs China's Shanghai Maglev: different implementations, consider how we can boost regenerative breaking capabilities & reduce power consumption

---

## 2. **Next Steps**
For the upcoming week, I plan to:
- look into raw NAND memory like Apple Studio
- do research on SCMaglev's implementation & find ways we can boost power recovery to power usage ratio
  - consider issues that SCMaglev is currently facing: cooling, regenerative breaking, wheels-then-levitate
- expand spreadsheet such that we can find optimal parameters to maximize the power recovery to power usage ratio

---

**Name:** [Rachel Jiang]  
**Research Topic:** [DHL]  
**Week:** [9]: Mar 7

---

## 1. **Overview of Progress**

This week progress: 👵🏼

- continuing work on overall [simulation](https://github.com/racheljiang310/dhl/blob/main/MAIN/simulation.md) (using Unity)
- received feedback from Prof on network switches, modified ideas & open to more feedback [link](https://github.com/racheljiang310/dhl/blob/main/MAIN/meta_rails.md)
- more research into SSDs, specifically into the datasheets and specs for a Rocket 4 Plus SSD (8TB)

Prof feedback on SSDs
- cache and control logic doesn't have to be in the carts, we can move them to servers & just keep raw flash mem in carts
- reference: Apple Studio

---

## 2. **Next Steps**
For the upcoming week, I plan to:
- Create a mapping for server to access data with the addition of inserting carts in the middle. Potentially adding to FTL or adding to existing cache
- pause on simulation, need to confirm final schema with team before continuing
- SSDs figure out how to detatch SSD controller from SSD & still have things work when server accesses data
- some calculations with respect to energy, speed, and efficiency when using a Rocket 4 Plus SSD (8TB)

---

**Name:** [Rachel Jiang]  
**Research Topic:** [DHL]  
**Week:** [8]: Feb 29

---

## 1. **Overview of Progress**

This week progress: 🌊

- continuing work on network switching [simulation](https://github.com/racheljiang310/dhl/blob/main/MAIN/simulation.md) (using Unity bc Unreal Engines takes 56 GB to download)
- continued working on diagrams on datacenter and sever-cart communication, definitely open to feedback and modifications [link](https://github.com/racheljiang310/dhl/blob/main/MAIN/integration.md)
- read more papers on regenerative breaking, this time on one developed by China, where a team used a super capacitor storage system for their regenerative breaking link
regenerative breaking cost-benefit analysis between battery & super capacitor storage system link
- visualization of [network switching](https://github.com/racheljiang310/dhl/blob/main/MAIN/meta_rails.md), currently trying to make multiple versions and weighting the pros and cons
- researching more into SSDs and how it communicates with the host server

---

## 2. **Next Steps**
For the upcoming week, I plan to:
- PCIe: figure out how the connections will be made between server and SSD [link](https://github.com/racheljiang310/dhl/blob/main/MAIN/ssds.md)
- Simulation: Continue working on Network Switches/Docking
- More Statistics & Paper Reading

---

**Name:** [Rachel Jiang]  
**Research Topic:** [DHL]  
**Week:** [7]: Feb 21

---

## 1. **Overview of Progress**

This week progress: 🌊

- SSD Research and [Findings](https://github.com/racheljiang310/dhl/blob/main/MAIN/ssds.md)
  - found cool video for learning about memory mapping, controller interfacing with SSDs
- Schema for communication between servers, carts, and metadata server lookups
  - what sends what to what and when to carry out a cart data access request
  - [Schema](https://github.com/racheljiang310/dhl/blob/main/MAIN/communication_schemas.md)
- Regenerative Breaking: got stats! and experiment studies
  - [Main Doc](https://github.com/racheljiang310/dhl/blob/main/PAPERS/maglev_cobra.md)
- Network Switching Simulation: basic 3D cubes that move along a rail

---

## 2. **Next Steps**
For the upcoming week, I plan to:
- API: work on some diagrams for this
- Simulation: Continue working on Network Switches/Docking
- More Statistics & Paper Reading

---
---

**Name:** [Rachel Jiang]  
**Research Topic:** [DHL]  
**Week:** [6]: Feb 11

---

## 1. **Overview of Progress**

This week progress: 🔥

- SSD Research and [Findings](https://github.com/racheljiang310/dhl/blob/main/MAIN/ssds.md)
  - found cool website for learning
- Regenerative Breaking: got stats! and experiment studies
  - [Main Doc](https://github.com/racheljiang310/dhl/blob/main/MAIN/regenerative_breaking.md)
  - [Papers](https://github.com/racheljiang310/dhl/tree/main/PAPERS)

---

## 2. **Next Steps**
For the upcoming week, I plan to:
- API: how is data mapped into carts? Data mapped into ssds?
  - need data, does it know which cart to access? Mapping table?
  - distributed, parallel, threaded?
  - research how distributed datasets are used in ML models?
  -  Network Switches/Docking: simple simulation? (Unreal Engines / Unity)
  - This week: cost of supercapacitor storage system + other regenerative breaking
    
---

**Name:** [Rachel Jiang]  
**Research Topic:** [DHL]  
**Week:** [5]: Feb 07

---

## 1. **Overview of Progress**
This week progress:
- Brainstorm Network Switching / Docking [More Braindump](https://github.com/racheljiang310/dhl/blob/main/MAIN/meta_rails.md)
  - Met with Yarwin: Discussed how we could do Rails on Rails
- SSD Research and [Findings](https://github.com/racheljiang310/dhl/blob/main/MAIN/ssds.md)
  - Potentially take off cache?
  - Remove heat sink fs (takes up a lot of weight afterall)
  - think about stacking & mapping memory to id
- Regenerative Breaking
  - [Main Doc](https://github.com/racheljiang310/dhl/blob/main/MAIN/regenerative_breaking.md)
  - Reading papers: [Papers](https://github.com/racheljiang310/dhl/tree/main/PAPERS)
    - Maglev-Cobra & Yamanashi Test Line have maglev regenerative breaking initiatives => need to look into specific stats on how much % energy regained
---

## 2. **Next Steps**
For the upcoming week, I plan to:
- [Rail on Rails]: do the math, maybe find a simulation software for it
- [Regenerative Breaking]: look into stats
- [Identify Cart]: further designing
- [SSDs]: learn more about SSDs, and figure out memory mapping if we stack them 3D

---

**Name:** [Rachel Jiang]  
**Research Topic:** [DHL]  
**Week:** [4]: Jan 31 

---

## 1. **Overview of Progress**
This week progress:
- Brainstorm Network Switching / Docking [Braindump](https://docs.google.com/drawings/d/1rsbkDRbqh8WbcEoA0NRzeHCZfSCtXhhv3560oUPtj4M/edit?usp=sharing)
- Met with Yarwin: Discussed network switching & card identification process
- Potential no contact data transfer?
  - Free-Space Optical Communication (FSOC): lasers to transmit data at speeds comparable to optical fiber. (Tbps) speeds over short distances.
  - Terahertz Wireless Communication: THz frequency range, enabling ultra-high-speed wireless data transfer (experimental stage)
  - Millimeter-Wave (mmWave) Wireless: (Gbps) speeds, good for real-time data streaming
- Pre-existing [Braindump Doc](https://docs.google.com/document/d/12Eglz0b-QdzZEQDLx2L2KOPlc13EjNpj-NsEMbnBi9Q/edit?tab=t.0)

---

## 2. **Next Steps**
For the upcoming week, I plan to:
- [Rail on Rails]: consider mass of rails, how this would work, etc
- [Regenerative Breaking]: look into
- [Identify Cart]: further designing
- [Reduce mass]: learn more about SSDs
- [Reduce power]: can DHL carts be more energy efficient?
