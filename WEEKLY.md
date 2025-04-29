# Weekly Research Progress Update
---
# Week 5
---
**Name:** [Rachel Jiang]  
**Research Topic:** [DHL UGrad Research]  
**Week:** [5]: May 2 🥧

## 1. **Overview of Progress**

This week progress: 👾
- found freely-distributed f2fs via cloning `https://kernel.googlesource.com/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools`
  - not sure what I can do with this for now, but will be taking notes
  - intro link: [guide](https://docs.kernel.org/filesystems/f2fs.html)
- ROS

## 2. **Next Steps**
For the upcoming week, I plan to:
- continue digging through ewaste bins

## 3. **Weekly Notes**
- [X] I need to read this article: [optimize regen break](https://www.sciencedirect.com/science/article/pii/S235214652300279X)
- [ ] More links: [learn ssd](https://github.com/mikeroyal/SSD-Guide?tab=readme-ov-file#SSD-learning-resources)
---
# Week 4
---
**Name:** [Rachel Jiang]  
**Research Topic:** [DHL UGrad Research]  
**Week:** [4]: Apr 25 🥧

## 1. **Overview of Progress**

This week progress: 👾
- met with team, setup weekly meeting time
- e-waste digging: unfortunately no ssds, so looked towards simulators/emulators online
- found: [MQSim](https://github.com/CMU-SAFARI/MQSim), [SSD-Guide](https://github.com/mikeroyal/SSD-Guide), and [SimpleSSD](https://docs.simplessd.org/en/v2.0.12/instructions/start.html)
- on the contray, SimpleSSD is in fact NOT easy for those using MacOS + Docker containers, lots of build issues (TypeErrors, etc)
  - ultimately was not able to get it building, kept throwing errors, need to look into why this is happening
- found: ROS (Robot Operating System) for carts: [link](https://articulatedrobotics.xyz/tutorials/ready-for-ros/what-you-need-for-ros)
- created [orchestrator](https://github.com/racheljiang310/dhl/tree/main/orchestrator) directory to start thinking about how we want cart server to work

## 2. **Next Steps**
For the upcoming week, I plan to:
- continue digging for open source resources while
- continue digging through ewaste bins

## 3. **Weekly Notes**
- I need to read this article: [optimize regen break](https://www.sciencedirect.com/science/article/pii/S235214652300279X)
- Look into what `gem5` dependencies are
  
---
# Week 3
---
**Name:** [Rachel Jiang]  
**Research Topic:** [DHL UGrad Research]  
**Week:** [3]: Apr 18 🥧

## 1. **Overview of Progress**

This week progress: 👾
- outlining how software could look like (what is inventory, what is the response/request protocol, etc)
- see [doc](https://github.com/racheljiang310/dhl/blob/main/MAIN/software_ideas.md)
- not much done relative to other weeks, but will be picking up more next week as we finalize on group meeting date

## 2. **Next Steps**
For the upcoming week, I plan to:
- set up with weekly meeting with DHL team
- continue working on software api ideas

## 3. **Weekly Notes**
- Interesting article: [optimize regen break](https://www.sciencedirect.com/science/article/pii/S235214652300279X)
  
---
# Week 2
---
**Name:** [Rachel Jiang]  
**Research Topic:** [DHL UGrad Research]  
**Week:** [2]: Apr 11 🥧

---

## 1. **Overview of Progress**

This week progress: 🏁
- Signed up for research units
- SCMaglev (the [pictures](https://global.jr-central.co.jp/en/company/_pdf/superconducting_maglev.pdf) really helped me understand how the EDS system works)
- Read into Paper #2 on [maglev_cobra.md](https://github.com/racheljiang310/dhl/blob/main/PAPERS/maglev_cobra.md) and extracted more specific conclusions about how we can maximize regenerative breaking (reduce deceleration, reduce incline, etc)

---

## 2. **Next Steps**
For the upcoming week, I plan to:
- Get in touch with DHL team, get set up with weekly meeting

---

## 3. **Weekly Notes**
Raw Nand from Mac Studio: memory chips used for storage without an integrated controller
- Where: mounted directly onto the logic board
- Controller? built into Apple’s custom processor (M1/M2 SoC)
- Why?
  - allows for bypass of standard SSD form factors
  - higher bandwidth & power efficiency
  - more control over performance and thermals

SCMaglev's [implementation](https://global.jr-central.co.jp/en/company/_pdf/superconducting_maglev.pdf)

<img width="670" src="https://github.com/user-attachments/assets/8f7b8259-a8fe-4358-872b-84112855c2bc" />

| Propulsion  | Levitation  | Guidance |
|---|---|---|
| <img width="200" src="https://github.com/user-attachments/assets/a6f53b4e-9a4e-409b-a7c9-6a4250459c96" />| <img width="200" src="https://github.com/user-attachments/assets/6971b76e-41d0-4421-b489-fe42d13ac129" /> | <img width="200" src="https://github.com/user-attachments/assets/a6397fa5-bfb5-481f-b8dc-20b6b8ca7c18" />|
- coil made of a Niobium-titanium alloy
- electrodynamic suspension (EDS) system
- cooled down to reach superconductivity

Regenerative Breaking
- electric torque changes direction, but the velocity maintains the same orientation
- motor velocity is greater than synchronous velocity $v > v_s$
- maximal regenerated energy formula: $P_{rotor} = \frac{V^2s}{R_2}$
  - power transfer between rotor & stator
  - stator loss & flux leakage are negligible
  - $s = \frac{w_1}{w_2}$ where $w_1$ is the motor angular velocity and $w_2$ is the synchronous angular velocity
  - $V$ is voltage
  - $R_2$ is sum of the secondary resistance (due to the losses in copper, with the element that is the conversion of elec into mech energy)

---

---
# WINTER 2025 WEEKLY PROGRESS UPDATES
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
  - chart results [link](https://github.com/racheljiang310/dhl/blob/main/MAIN/simulation.md)
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
