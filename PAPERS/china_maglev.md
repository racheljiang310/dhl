
## [Energy storage systems to exploit regenerative braking in DC railway systems: Different approaches to improve efficiency of modern high-speed trains](https://www.sciencedirect.com/science/article/pii/S2352152X17304140)

"Stationary/Infrastructure based Storage Systems. Main advantage is to avoid limitation regarding encumbrances. Main drawback regards additional losses, since energy flows move from the trains to the storage passing through the feeding line... Considering different storage technologies i.e. lithium batteries [11,12] or supercapacitors [13,14]. Energy storage systems are chosen and sized by considering their performance, aging and costeffectiveness"

"On the other hand, reduced number of braking phases and extended railway lines may reduce the costeffectiveness of the proposed solution, as confirmed by the low achieved interest, although today ever increasing"

equation of motion of the vehicle: <img width="200" src="https://github.com/user-attachments/assets/948cc0d7-702c-4aaf-8ed9-cc07d7e777a2" />

Considered high-speed train: Italian ETR 1000, a train equipped with a distributed traction system and able to operate both under DC and AC electrifications, thus being able to operate within the main European high-speed lines
- "More in detail, the 57% of the full amount of energy is converted in kinetic energy. Around 10% of energy is dissipated on the contact line, while electric drive losses and auxiliary loads spend, respectively, 18% and 4% respectively. Finally, 11% is adsorbed by motion resistance. It is particularly noticeable that large part of the supplied energy goes into trains’ kinetic energy, which is not yet lost and can be recovered during future braking actions."

To enhance energy recovery during braking...several variants of storage systems can be considered:

1) Stationary systems, interfaced with the feeding line by means of DC/DC converters:
- Systems based on supercapacitors.
- Systems based on high power lithium batteries.

<img height="250" alt="Screenshot 2025-02-11 at 13 39 29" src="https://github.com/user-attachments/assets/12c73563-6667-448d-afc0-e3c6b246ff48" />

<img height="250" src="https://github.com/user-attachments/assets/a81bc9bd-cdb6-4f5f-ba84-f21a6e212ba4" />

<img width="700" alt="Screenshot 2025-02-11 at 13 40 28" src="https://github.com/user-attachments/assets/f2948f11-cf79-4056-af99-bc8e4ccb9864" />

"The analysis has shown that braking energy recovery is able to provide significant energy and costs saving even in DC high-speed railway systems, opening new research opportunities for the future...It has been verified that supercapacitors, mainly because of the high energy-to-power ratio of this application, cannot compete in terms of costeffectiveness."

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

## [The Supercapacitor Energy Storage System is Applied to Shanghai Medium-low Speed Maglev Train Test Line](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9670830)

- "In regenerative braking, the linear induction motor has to overcome the running resistance of the train, the loss of the linear induction motor itself, the internal loss of the traction inverter, and the energy consumed in each link when converting kinetic energy into electric energy to feedback to the grid."

---

<img width="403" alt="Screenshot 2025-02-11 at 12 42 25" src="https://github.com/user-attachments/assets/288a2389-512f-44d1-b14d-6497b350b328" />

---

"The designed maximum operating speed of the Medium-low Speed Maglev Train test line is 100 km/h, and the formation form is composed of two cars with a coach
and four coaches without a coach in series in the middle. The total load of the whole train is 209.1t[6], and the technical requirements related to the braking performance of the maglev train are as follows: "
- "The emergency braking distance is less than 300m when the initial braking speed is 100 km/h;"
- "The average deceleration of service braking (regenerative braking) is greater than 1.1 m/s2."

"When train regenerative braking, the traction motor is transformed into a generator that converts the kinetic energy of the train into electric energy. In the meantime,the generated electric energy returns to the DC power grid and is used by the electric appliances on the train. It can be calculated that if the maximum DC grid voltage of this type of maglev train is not more than 1750V when braking, the maximum instantaneous current to be absorbed in the design of braking resistance or absorption energy storage system should be about 1200A, and the maximum instantaneous absorbed power should be about 3.6MW. Furthermore, it is estimated that the continuous current absorbed by the energy storage system or consuming resistor is about 800A under this condition"

---

2. [Positive Rail Voltage Rise Behavior and Inhibition Analysis of Regenerative Braking of Medium–Low-Speed Maglev Train](file:///Users/admin/Downloads/energies-17-01782%20(2).pdf#page=17&zoom=100,48,573)

"The current treatment method targeted for the MLS maglev is to release the excess RB energy in the form of heat energy via a ground resistance absorption device, but it results in energy waste and increases the temperature in the tunnel.

To better accommodate the RB energy, measures of energy storage (1) and energy feedback (2) have been proposed..." 
* energy feedback system exerts three advantages:
  - high efficiency: Excessive RB energy can be directly fed back to the AC system through the RBEFS, and the traction grid energy utilization rate can be greatly improved [17,18]
  - cheaper price: energy storage system is relatively large and expensive, and is more suitable for 600 V and 750 V traction grids at present; the price of the RBEFS is also becoming cheaper with the development of high-power semiconductor IGBTs.
  - smaller space: RB energy feedback system (RBEFS) can be considered a promising application for the MLS maglev
* energy storage systems and feedback systems have been compared to avoid the over-voltages

<img width="1470" alt="Screenshot 2025-02-11 at 13 14 15" src="https://github.com/user-attachments/assets/12481325-3cb1-4ce1-86dd-4d985ec4b784" />


