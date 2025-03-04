
# Theme: Regenerative Breaking
----
## Research/Background
---

[Ideals](https://eprints.whiterose.ac.uk/2118/1/ITS105_WP471_uploadable.pdf) for a successful regenerative braking system:
- efficient energy conversion
- energy store with a high capacity per unit weight and volume
- high power rating (large amts of energy flow in a short space of time)
- smooth delivery of power
- absorb/store braking energy in direct propnrtion to braking, with < delay & loss over diff speeds and wheel torques

Look into: RB energy feedback system (RBEFS)
 
## Implementation (Research)
---

1. Maglev Motors = Generators
  - LIMs (our accelerators) = generators
  - cart slows down, linear motors reverse function
  - maybe regenerative suspension too?

**2. Energy Storage**
  - **Supercapacitors**: good for frequent charge/discharge (immediate use), less storage capacity, but long lifespan
  - **Batteries**: dense storage, but smaller lifespan, slower charge/discharge, and heat intensive at times
  - **Flywheel**: simple, fast charge/discharge, but requires weight & extra implementation to prevent loss of energy
  - on tracks, then ideal for start-stop operations can enable charge/discharge features
    - good idea bc energy can be distributed across tracks, fed into nearest storage system, central management via API

3. Power Management System
  - Use Options: power carts, power other parts of data center, or store
      - anay unused energy regenerated can be direted to power other parts of the data center
  - When Options: immediate, on-demand, hold until peak demands
  - Software API:
    - track stored energy in storage
    - track state of charge in carts
    - manage where energy goes

## LIMs as Generators

Papers:
- [Dynamic Models of Controlled Linear Induction Drives](https://www.eejournal.ktu.lt/index.php/elt/article/view/10447)
- Combined Propulsion and Levitation Control for Maglev/Hyperloop Systems Utilizing Asymmetric Double-Sided Linear Induction Motors
  - "On the other hand, the regenerative levitation principle described in [19] can be utilized during deceleration, which allows kinetic energy conversion to electricity and can be used to charge the battery during regenerative braking. In this case the DC mode is replaced by the AC generating mode combined with the AC motoring mode. Moreover, if the required braking force is high enough such that the generated primary current is able to maintain the required lift force, all ADSLIMs are operated in AC generating mode. As can be seen, the combination of AC motoring mode, DC mode and AC generating mode allows coverage for the full scope of operation including acceleration, cruising, and deceleration."
  - <img width="850" alt="Screenshot 2025-02-07 at 15 22 45" src="https://github.com/user-attachments/assets/df1d6637-fbb4-4520-87fb-adb62f560bea" />


## Power Manamgement System


## [Stationary and on-board storage systems to enhance energy and cost efficiency of tramways](https://www.sciencedirect.com/science/article/pii/S037877531400562X)

Context:
A. Trams dissipate all the braking energy in on-board resistors.
B. Trams send their braking energy into the catenary as long as the catenary voltage does not overcome the maximum limit of 900 V.
C. As per case B, but with addition on n-storage systems having the previously mentioned characteristics, in correspondence to the ESSs situated along the tramline route (C-1 to C-10).
- Cases B and C's two controls actions:
  - Baseline. In this case braking energy is sent into the catenary as long as the local voltage is within limits (for our application 900 V); As soon as the voltage reaches this limit, recovery is stopped.
  - Advanced. In this case when the contact line voltage reaches 900 V the energy recovery is not stopped, but reduced to exactly

#### Lithium battery configurations

<img width="691" alt="ESSs energy and recovered energy in case of stationary configuration with DC/DC
converter." src="https://github.com/user-attachments/assets/52aa4450-f364-459d-8edb-cfe30e7b6a77" />
- "an increase in the energy recovered does not automatically translate in a reduction in the energy absorbed by the railroad"

<img width="656" alt="Energy saving trend versus number of stationary storage units installed." src="https://github.com/user-attachments/assets/afba64e8-a703-4c06-bd3c-ea080a6bf7eb" />

- "energy saving guaranteed by the advanced control is comparable to that obtained by the installation of two storage systems, with the baseline control. equal # of storages, in case of advanced control the energy saving is three times respect to the baseline control using one storage, two times using two storages, around 1.4 times with three."
- "For the baseline control, the minimum recommended storage-tostorage distance is around 2.0 km."
- "For the advanced control, the minimum recommended storageto-storage distance is around 4.0 km."

#### Stationary Supercapacitators
<img width="687" alt="Screenshot 2025-02-11 at 13 58 00" src="https://github.com/user-attachments/assets/10a9e48c-b65a-4d4a-a698-a0b69a7831d9" />
- Annual energy saving, obtainable as weighted average of hourly consumptions, are therefore almost equivalent between the two storage configurations.

#### Cost-Benefit Analysis

<img width="688" alt="Screenshot 2025-02-11 at 14 02 16" src="https://github.com/user-attachments/assets/d0210724-05cb-4f97-8295-80109295ec37" />

---

## [Positive Rail Voltage Rise Behavior and Inhibition Analysis of Regenerative Braking of Medium–Low-Speed Maglev Train](https://www.researchgate.net/publication/379675421_Positive_Rail_Voltage_Rise_Behavior_and_Inhibition_Analysis_of_Regenerative_Braking_of_Medium-Low-Speed_Maglev_Train)

"The current treatment method targeted for the MLS maglev is to release the excess RB energy in the form of heat energy via a ground resistance absorption device, but it results in energy waste and increases the temperature in the tunnel.

To better accommodate the RB energy, measures of energy storage (1) and energy feedback (2) have been proposed..." 
* energy feedback system exerts three advantages:
  - high efficiency: Excessive RB energy can be directly fed back to the AC system through the RBEFS, and the traction grid energy utilization rate can be greatly improved [17,18]
  - cheaper price: energy storage system is relatively large and expensive, and is more suitable for 600 V and 750 V traction grids at present; the price of the RBEFS is also becoming cheaper with the development of high-power semiconductor IGBTs.
  - smaller space: RB energy feedback system (RBEFS) can be considered a promising application for the MLS maglev
* energy storage systems and feedback systems have been compared to avoid the over-voltages

<img width="1470" alt="Screenshot 2025-02-11 at 13 14 15" src="https://github.com/user-attachments/assets/12481325-3cb1-4ce1-86dd-4d985ec4b784" />

----

## [A New System of Combined Propulsion and Levitation for Maglev Transportation](https://ieeexplore.ieee.org/document/9124470)

"**The Inductrack system** demonstrates a high levitation efficiency since PMs require no power to produce the magnetic field and the only power loss originates from resistive losses due to currents induced in the track. The major drawback [...] requires huge and **expensive Neodymium-Iron-Boron (NdFeB) magnets which account for at least 2% of the total weight of the vehicle**"

Their proposal: "combines propulsion and suspension control in a series of asymmetric double sided linear induction motors (ADSLIMs) and allows each ADSLIM to work near its maximum efficiency operating point when producing desired propulsion and levitation forces."

Results: "The results show that the regenerative levitation case with maximum levitation efficiency demonstrates the best performance with 17.5% less power requirement compared to the zero thrust operation and 7.8% less power compared to the regenerative levitation case with maximum efficiency. "

<img width="1186" src="https://github.com/user-attachments/assets/99db0b53-0841-4f93-9097-25e5da036e5b" />





