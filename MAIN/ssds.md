# M.2 Solid State Drives
----

Define: compact, high-performance storage device commonly used in modern computing systems, including laptops, desktops, and data centers. Its small form factor and high-speed interface make it ideal for applications requiring fast **data access** and **low power consumption**

----
## M.2 Form Factor

Shape and Size: M.2 SSDs are rectangular with length (first two digits = the width in mm, last two represent the length). **They are installed directly to motherboard**

Keying: M.2 SSDs have notches (keys) on the edge connector to indicate their supported interfaces (e.g., SATA, PCIe NVMe).

|          |     |     |
|-------------------|-----------| -------- |
| <img width="200" src="https://github.com/user-attachments/assets/f536b552-a6ee-4d73-8c12-bd94e2309689" /> | <img width="200" src="https://github.com/user-attachments/assets/d1cc649f-d08d-4936-999a-4eb69d57b575" />| <img width="200" src="https://github.com/user-attachments/assets/0b98469a-e0fd-4692-8e35-8471d55d2743" /> |


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

**NOTE**: Don't remove
  
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
|  |            DRAM Cache                 |  |
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

| Component         |  Weight   |   Notes  |
|-------------------|-----------| -------- |
| NAND Flash Memory | 4-16 grams| 3D TLC   |
| Controller        | .5-1 gram |Phison E18|
| DRAM Cache        | .5-1 gram |  No      |
| PCB               | 2-4 grams |          |
| Voltage Regs      | .5-1 gram |          |
| Thermal Solutions | 5-10 grams| Heat sink / thermal pad|
| Interface Connect | .5-1 gram |          |
| Others            | .5-1 gram |          |
| Total             | 10-30 g   |          |

---

1. Removing Heatsink: saves 5-10 grams
2. Removing DRAM Cache: saves .5-1 gram (not really worth it in terms of mass) [future me: no]
3. Simplified controller: reduce power consumption/heat generation
  - removing ECC
  - removing heat sink management
  - remove cache management
4. Simplifying PCB: harder to do, but could still save a little

---

## Abstraction Layers

####  Way 1: Buy it [Micron’s 232-layer 3D NAND](https://dmassets.micron.com/is/image/microntechnology/gcm-1019003-infographic-232l-nand-540x340px-v2?ts=1730186089519&dpr=off)
- [Info](https://www.micron.com/products/storage/nand-flash/232-layer-nand)

#### Way 2: Custom SSD firmware

1. Architecture & Interfaces
* Host Interface: PCIe (NVMe)
* NAND Interface: ONFI/Toggle NAND

2. NAND Flash Management
* Wear Leveling: balance usage of NAND cells
* Garbage Collection
* Bad Block Management: Identify/remap bad NAND blocks
* ECC (Error Correction Code): can be simple

3. [Firmware & Optimization](https://codecapsule.com/2014/02/12/coding-for-ssds-part-1-introduction-and-table-of-contents/)
* **FTL(Flash Translation Layer): Maps logical addresses to physical NAND locations**
  * software layer in an SSD controller that translates logical block addresses (LBA) from the host system into physical locations on the NAND flash memory. 
    - Logical-to-Physical Address Mapping (L2P) 
      * OS sees the SSD as a traditional block storage device, with addresses in LBA format 
      * dynamically maps these logical addresses to physical NAND locations, maintaining a mapping table 
          - Page-Level FTL: Maps each page individually to an LBA => fast random writes, need large mapping table 
          - Block-Level FTL: Maps entire blocks => < memory overhead, write amplification 
          - Hybrid FTL (Log): page-level mapping for hot data and block-level mapping for cold data. 
    - Wear Leveling 
        * limited number of P/E (Program/Erase) cycles per block 
        * writes are evenly distributed across the NAND 
    - Garbage Collection: periodically moves valid data to new locations and erases old blocks to reclaim 
    - Bad Blocks: defects are marked and avoided, redirecting data storage 
    - Error Correction Handling: correct bit errors before returning data to the host 
* DRAM Cache Management: Not needed maybe? 
* Power Loss Protection: Ensures data integrity during unexpected power cuts 

4. Hardware Design
* FPGA Prototyping: test controller on an FPGA before moving to an ASIC design
* Custom PCB: Routing high-speed NAND and PCIe signals requires careful layout design

---

## [PCI Express](https://computer.howstuffworks.com/pci-express.htm)
> Peripheral Component Interconnect (PCI): bus is a channel or path between the components in a computer. Part of the slower bus that is responsible for communicating with hard disks and sound cards. Provides **direct access to system memory** for connected devices, but uses a **bridge to connect** to the frontside bus and, thus, to the CPU
 
- Peripheral Component Interconnect Express (PCIe):
  - Purpose: direct connection between two devices (nodes) on the bus is established while they are communicating with each other (point-to-point system)
    - better performance and scalable, enable parallel connections
    - <#>x connection: # lanes to carry data
    - AGP graphics card slots have PCI-Express 16x slots => more lanes


<img width="200" alt="PCIe" src="https://github.com/user-attachments/assets/b06c5f9a-e05e-468c-802a-28a9690e9b19" />

<img width="200" alt="PCIe" src="https://github.com/user-attachments/assets/48244d5a-e783-4053-9161-dd835dc78dbf" />

> Conclusion: Probably won't be able to connect all 64 SSDs to a server, nor should it since data won't be THAT big. We'll need a way to sort out the SSDs we don't need. Also, if we want parallel connections so that multiple servers can access the same data from the same rack, we need to consider the limitations of the SSD card. I'd estimate it ~ 4-16 parallel connections rn, but it's not a huge problem. 

---

## Meeting Notes

---
- 02/18: Journaling for rights
- 02/18: Fill as much, then load balance on last SSD
- 02/18: Replication of data (RAID)
- 02/18: Plug in all 64 SSDs into the server?
- 02/18: How does data transfer work? Which server knows what?
