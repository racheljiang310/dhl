
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

## [Efficient Regenerative Braking Strategy Aimed at Preserving Vehicle Stability by Preventing Wheel Locking](https://pdf.sciencedirectassets.com/308315/1-s2.0-S2352146523X00040/1-s2.0-S235214652300279X/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIEgAY%2FbWhyHR34Vygv%2BzQ8GROcpwaOlG3DYZtgUhv%2FqQAiB3lhXENxiQJeCLRPTZVtNPYd4lDnDQUzA2ZQ6CTAwQ9iq7BQiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAUaDDA1OTAwMzU0Njg2NSIMnLidBHlHYJ5BeChSKo8FIwqfjg%2BfFjsit2UlPvwjMSvHMk7U3v5%2BOeOJh80YnyOuhRagHe4g3afHBSYs2%2Fe%2BGmFcVBkdZXB2YFzjJop5U5I4t%2FwrbY%2FuqEk8YiKFfMBvI0PW2FHKX35d2Cf2xsIOiWp%2FwSUIjBCZ%2BIRCRSF82sLSmP4WA%2BrOq9gU%2BJ2iZyvJiI5bsZb1jdGw9TXrwV0wpnXbjlhZNbarUKAHfUMkdu2toaxaWOC2rp%2BWRvAW0eNxLiK0rAwGTgBoVAfqHKNXnioV1GXqCGOWaIJoEGbhbKNgNknn1Vxu0vR5eOnZRT2%2FY4u%2BisTPOK%2F8AL1VlC3PRUVhEARu%2BuVOymO5QntB3mzo%2BMn56D%2Fk7t%2B%2FwVWrdFzI4fL8MxEZek%2BxPp1RjNGP3oQ%2B6baycJE8OJ6Rlc580AiPiN5H7SKHuK5iELuWX%2FukcGY4x9HQoIH3RfOmyWRnbgwhdo0AFB5ntt%2Byk8tuFvL51sOFaaZ67bNKkJq1SreVeA9OihBQr2FD1cqvqvTlEGVDpKsQP%2FqebcihyN%2BYH8Hn95ayGGiQL5tXVzDQVnYFDzwVt%2FhmLk4uma8YTuq4eGfOpeuKZyvZqwAN4Cso9iNH9mnVqJoBIvL44lByg8G5kDq6tMfbLlvP4yaap%2FUX3r00HQyEmOEGwyENpFFRklQFluxdjvnj86yFsBbVA3RYri0rREjsgZu7jUCSLL3cz%2BorVcf0cxkhAa53ew8uT3JubhcX%2BkkfORzMJZdILwp%2BmfUor46MZy%2Bp6w4i7Vo%2Blxo%2BYo67p4gCfmNwVTuYXaiTc8Uu1Io7UJAtJzfUmu%2BCbpuqazM2IIXNtGSvZLYeJhMC8%2FBJC4iag0DqRkdZnXLur1BHEPyyoXtSkkiPHzDCx8TABjqyARwdc28OSGaX9Up%2FLyY9ERK7XkGkCM%2FIM8FhLWge6nK515OBmvBxGSDYpO9PnUibq7otcflXu3d2cwNiHS4zauN8cA3Eug6Npe%2Fez%2B9zDzCsXKxgYhUZZe8ENteWTRqcLxDRQMcXnZ8JYLKuYegHGlAoiaJHYfD%2FXBNP7Zi%2BvkVmtEHiTpnv6XuTFwKWR2uc38exH39RStXziumtY5powPFpkxVrMfy7NSUG%2Fi8R32fCCeA%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250429T195015Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYRWHLYD7V%2F20250429%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e2521b11bf2232a0b8fa678750e02f627a1e7906ecd63387375815d6f85aa692&hash=3593282926a59fc7f8f74c12e2de5577377348cf96c0470fb4f0f02113ccd9a7&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S235214652300279X&tid=spdf-2a43cd9f-8b83-4413-8004-95ea8caccdbf&sid=097828c788064941193a2c765c6aabc154a7gxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&rh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=0f155a5d5a525654045652&rr=938153c80895cb7a&cc=us)

Conclusions from their methodology: "This logic was tested via simulation, and it emerged that, on the WLTC driving cycle, the logic saved about 30% in consumption compared to the same vehicle without regenerative recovery, and about 23% compared to a logic commonly adopted on the market. On cycle US06, it saves about 24% and 19%, respectively"

Goal: max regen motor torque during braking, min action of traditional brakes which dissipate energy"
Limitations: 
1. locking limitation of the drive axle wheels (when electric motor can't sat the regen torque req).
   - Brake force required are imposed as the min of total braking force req by the driver and max total braking force that avoid wheel locking multiplied by a safety coefficient => LIM motors don't have to worry about this
2. Current that the motors must send to the battery can't exceed the max current that can be absorbed by battery pack
   - $Volt \times Curr_{max}$ We do have to worry about this too

----

## Regenerative Breaking in EVs

Equations

- $\eta_{gen} = \frac{W_{out}}{W_{in}}$
  - $eta_{gen}$ = efficieny of the generator
  - Work out : Work in
- $P_{gen} = \frac{\eta_{gen}mv^2}{2\Delta t}$
  - $P_{gen}$ = power produced by generator
  - t = amount of time car takes to break
  - m = mass of car
  - v = initialixe velocity
- $n_{batt} = \frac{P_{out}}{P_{in}}$
  - $P_{in} = P_{gen}$
  - $P_{out} = \frac{W_{out}}{\Delta t}$
  - $W_{out} =  \frac{n_{batt}n_{gen}mv^2}{2}$




