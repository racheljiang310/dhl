
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

1. Maglev Motors = LIMs (our accelerators) = generators
  - cart slows down, linear motors reverse function
  - regenerative suspension?

2. Energy Storage
  - **Supercapacitors**: good for frequent charge/discharge (immediate use), less storage capacity, but long lifespan
  - **Batteries**: dense storage, but smaller lifespan, slower charge/discharge, and heat intensive at times
  - **Flywheel**: simple, fast charge/discharge, but requires weight & extra implementation to prevent loss of energy
  - on tracks, then ideal for start-stop operations can enable charge/discharge features
    - good idea bc energy can be distributed across tracks, fed into nearest storage system, central management via API

3. Power Management System
  - use cases: immediate, on-demand, hold until peak demands
  - Software API:
    - track stored energy in storage
    - track state of charge in carts
    - manage where energy goes

---

## LIMs as Generators

- [Dynamic Models of Controlled Linear Induction Drives](https://www.eejournal.ktu.lt/index.php/elt/article/view/10447)
- "regenerative levitation principle described in [19] can be utilized during deceleration, which allows kinetic energy conversion to electricity and can be used to charge the battery during regenerative braking. In this case the DC mode is replaced by the AC generating mode combined with the AC motoring mode. Moreover, if the required braking force is high enough such that the generated primary current is able to maintain the required lift force, all ADSLIMs are operated in AC generating mode. As can be seen, the combination of AC motoring mode, DC mode and AC generating mode allows coverage for the full scope of operation including acceleration, cruising, and deceleration."

<img src="https://github.com/user-attachments/assets/df1d6637-fbb4-4520-87fb-adb62f560bea" />

---

## Power Manamgement System

### [Stationary and on-board storage systems to enhance energy and cost efficiency of tramways](https://www.sciencedirect.com/science/article/pii/S037877531400562X)

> study inspired by a real tramline located in the northern part of Italy (Bergamo)
> total line length ~ 12 km, 10 Substations (ESSs)
> no. of operating trams: rush hours (10 trains), low load hours (5 trains), holidays (3 trains)

| <img src="https://github.com/user-attachments/assets/a2162207-cc9c-4a45-aac1-c92860b616d9" />  |<img src="https://github.com/user-attachments/assets/be74b769-4d0c-43ac-b5dd-26b9cba9f9f2" /> |<img src="https://github.com/user-attachments/assets/0e5de3f6-9771-4ee1-a958-6582937056af" /> |
|--|--|--|

This paper analyses and compares the following variants:
- Stationary high-power lithium batteries
- Stationary supercapacitors
  - may require the presence of the DC/DC converter, since the charge/discharge processes imply rather large voltage variations
- High-power lithium batteries on-board trains. (We won't be entertaining this idea)
- Supercapacitors on-board trains. (We won't be entertaining this idea)

### Configuration with/without the DC/DC converter

#### Lithium Battery Configurations

A. Trams dissipate all the braking energy in on-board resistors.

B. Trams send their braking energy into the catenary as long as the catenary voltage does not overcome the maximum limit of 900 V.

C. As per case B, but + n-storage systems, in correspondence to the ESSs situated along the tramline route (C-1 to C-10).
- controls actions:
  - Baseline: braking energy is sent into the catenary as long as the local voltage is **within** limits (for our application 900 V)
  - Advanced: when the contact line voltage reaches 900 V the energy recovery is not stopped, but **reduced to exactly**

##### _Lithium Battery Results_
- "an increase in the energy recovered does not automatically translate in a reduction in the energy absorbed by the railroad"
- with equal # of storages => "advanced control the energy saving is **three times** respect to the baseline control using one storage, two times using two storages, around 1.4 times with three."
- "baseline control, the minimum recommended storage-tostorage distance is around 2.0 km."
- "advanced control, the minimum recommended storageto-storage distance is around 4.0 km."

| <img src="https://github.com/user-attachments/assets/52aa4450-f364-459d-8edb-cfe30e7b6a77" />  |   <img src="https://github.com/user-attachments/assets/afba64e8-a703-4c06-bd3c-ea080a6bf7eb" /> |
|---|---|
> “Total ESS Energy”, i.e. the total energy absorbed by the railroad summing up the absorptions of all the ESS’s, and the “Recovered energy”, i.e. the total flow of energy recovered into catenary by trains


#### Stationary Supercapacitators Configurations

##### _Stationary Supercapacitators Results_

- Annual energy saving, obtainable as weighted average of hourly consumptions, are therefore almost equivalent between the two storage configurations.

| <img src="https://github.com/user-attachments/assets/10a9e48c-b65a-4d4a-a698-a0b69a7831d9" />  |   <img src="https://github.com/user-attachments/assets/e1483809-63ca-412c-b02c-f7dee207164c" /> |
|---|---|

### Cost-Benefit Analysis

<img src="https://github.com/user-attachments/assets/d0210724-05cb-4f97-8295-80109295ec37" />

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

----

## Regenerative Breaking in EVs

Equations

$\eta_{gen} = \frac{W_{out}}{W_{in}}$ \\
$P_{gen} = \frac{\eta_{gen}mv^2}{2\Delta t}$ \\




