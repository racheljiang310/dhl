# M.2 Solid State Drives
----

Define: compact, high-performance storage device commonly used in modern computing systems, including laptops, desktops, and data centers. Its small form factor and high-speed interface make it ideal for applications requiring fast **data access** and **low power consumption**

----
## M.2 Form Factor

Shape and Size: M.2 SSDs are rectangular with length (first two digits = the width in mm, last two represent the length).
Keying: M.2 SSDs have notches (keys) on the edge connector to indicate their supported interfaces (e.g., SATA, PCIe NVMe).

----
## M.2 Components [1TB storage]

#### A. NAND Flash Memory [4-8 grams]
> primary storage medium where data is stored; non-volatile, 3D NAND to > storage density
- SLC, MLC, TLC, WLC
- high -> low endurance
- low -> high capacity
- - scaling up > mass, by a lot

#### B. Controller (Microcontroller) [0.5-1 gram]
> manages data storage & retrieval
- read/write operations
- error correction, wear leveling, garbage collection (invalidations, free space)
- interfaces with host system via SATA/PCIe NVMe protocols
- DRAM Cache for frequent data access & mapping tables
**Note**: ECC (Advanced Error Correction)
  - ECC usually used to ensure data integrity over long periods
  - we use it for short-term data transport, so we can just reply on the host system's error checking
  - not a huge issue bc its scalable size doesn't change much

#### C. DRAM Cache (Optional) [0.5-1 gram]
> speeds up operations
- mapping tables (FTL: Flash Translation Layer)
- buffer for read/write ops
- scaled up weight not huge

**NOTE**: Not a huge part of the weight though
  - Reason 1: we're doing sequential read/write operations for data transport, not random access
  - Reason 2: we're won't create a big enough speedup to give us a reason to keep it
  
#### D. Interface Connector [0.5-1 gram]
> edge connector that plugs into M.2 slot on motherboard
- electrical/data connections between SSD & host
- protocols

#### E. PCB (Printed Circuit Board) [2-4 grams]
> holds all componenents together
- electrical connections between the components above
- withstand thermal/mechanical stress
- scaling up > mass
**NOTE**: we could find a way to reduce the width/length of the PCB, potentially

#### F. Voltage Regulators [0.5-1 grams]
> regulates power supply to SSD
- 3.3V input voltage converted to required 

#### G. Thermal Solutions [1-5 grams]
> manages heat dissipation
- thermal pads, heatsinks, thermal throttling (scaling up > mass)
**Note**:
  - we could create our own heat sinks outside of the SSD, potentially at the docking stations
  - maybe we don't really need them in the SSD?

---

## Diagram

```
+---------------------------------------------+
|                    M.2 SSD                  |
|                                             |
|  +---------------------------------------+  |
|  |            NAND Flash Memory          |  |
|  | (Multiple chips for storage capacity) |  |
|  +---------------------------------------+  |
|                                             |
|  +---------------------------------------+  |
|  |               Controller              |  |
|  | (Manages data storage and retrieval)  |  |
|  +---------------------------------------+  |
|                                             |
|  +---------------------------------------+  |
|  |            DRAM Cache (Optional)      |  |
|  | (Speeds up data access and mapping)   |  |
|  +---------------------------------------+  |
|                                             |
|  +---------------------------------------+  |
|  |          Voltage Regulators           |  |
|  | (Regulate power for components)       |  |
|  +---------------------------------------+  |
|                                             |
|  +---------------------------------------+  |
|  |          Interface Connector          |  |
|  | (Connects to M.2 slot on motherboard) |  |
|  +---------------------------------------+  |
|                                             |
|  +---------------------------------------+  |
|  |          Thermal Solutions            |  |
|  | (Heat dissipation and management)     |  |
|  +---------------------------------------+  |
+---------------------------------------------+
```

---

## Sabrent Rocket 4 Plus SSD Example

---

| Component         |  Weight   |
|-------------------|-----------|
| NAND Flash Memory | 4-16 grams|
| Controller        | .5-1 gram |
| DRAM Cache        | .5-1 gram |
| PCB               | 2-4 grams |
| Voltage Regs      | .5-1 gram |
| Thermal Solutions | 5-10 grams|
| Interface Connect | .5-1 gram |
| Others            | .5-1 gram |
| Total             | 10-30 g   |

---

1. Removing Heatsink: saves 5-10 grams
2. Removing DRAM Cache: saves .5-1 gram (not really worth it in terms of mass)
3. Simplified controller: reduce power consumption/heat generation
  - removing ECC
  - removing heat sink management
  - remove cache management
4. Simplifying PCB: harder to do, but could still save a little


