# Meta-Rails (aka _RAILS ON RAILS_)

---

## Switches

---

### [OLD] Idea 1: Diagonal Movement (Not my favorite)

1. Cart 1 is on Track 1, Track 2 next to Track 1
3. Cart 1 reaches switch area
4. Cart 1's top Rail 1 detaches from bottom Rail 1, and same thing happens for Rail 2
5. Rail 1 and Rail 2 converge, one in front of other
6. Cart 1 moves to Rail 2's top fully, continues vertical movement
8. Rail 1 and Rail 2 diverge, return to original tracks, back to normal

![ROR](https://github.com/user-attachments/assets/18ded2d9-2f01-49f0-98cf-2911a123bb98)

---

### Idea 2: 1-Cart Hovering Roundabouts (A little imaginative, but not impossible)

1. Cart 1 at intersection, leaves rail track
3. Cart 1 enters roundabout, where it's momentarily levitating, roundabout locks entry to intersection (1 cart only)
4. Cart 1 leaves roundabout, roundabout controller frees locks, invites next cart to cross intersection

<img width="300" alt="Hovering Roundabout" src="https://github.com/user-attachments/assets/b9766f91-ade2-4047-a16c-8946bd444001" />

> Note: We'd need something that acts like a multi-directional peashooter that can apply EMFs that will ultimately propel the cart out of the roundabout as it's continuously hovering in circles. Some controller will need to direct the peashooter and time it correctly, also we'd need to makes sure the cart doesn't bang on the walls of the tube. Hence, this idea is a little out there, not impossible, but has a lot of risk

---

### Idea 3: Pre-Configured MagLev switching (the straight-est)
1. 2 Cart "homes" that will face opposite of one another from left and right ends of the data center
2. Meta rails in cart homes. As cart server deploys a cart, it will pre-configure the exact row it should be headed towards, thus moving the cart sideways via meta rails
3. Once in the right row, the cart is shot from left to right (or right to left) and will only move in the directions of that row.
4. Once it reaches close to docking station, it will slow down and step onto the meta rail that the docking station will push out via EMF
5. As docking station detects the cart on the meta rail, it will retract, thus giving way to other carts that move on the same row.
6. Data sharing occurs now
7. Once cart is done, docking station pushes meta rail out and cart will continue its same direction/motion until it reaches the right end, in which the right end cart home will preconfigure its next route back to the cart home on the left OR a new destination if a server requests for it

![Lazy Carts](https://github.com/user-attachments/assets/b80e05ad-d458-47c2-9ced-8e01c07cc761)

<img width="400" alt="Most Straight" src="https://github.com/user-attachments/assets/2768c2d2-470b-4a24-9ab3-48e28d3f7c81" />

> Note: This one might be easiest to implement because we don't have to worry about switching en-route. However, this also means the path the cart takes isn't going to be the most optimal (especially for return trips), but we can trade this off for a faster cart speed since we can just send it without need to worry about slowing down to make a network switch

---

### Idea 4: Complex and Sort of not Optimal Network Switches (based off real switches)

1. Intersections = a network switch for MagLev
2. Once a cart reaches a network switch, enter a race condition to contend for slot in switch (aka everyone else in line)
3. Each network switch has 4 freely rotating meta rails. Each rotating meta rail will be pre-configured to rotate in a direction based on the directions from the controller for the switch.
4. Once cart gets a turn at the switch, it will go onto the meta-rail and be rotated towards the direction it needs to be rotated towards and shot to the destination rotating meta-rail.
5. Destination meta rail will be the final "node" that cart travels within the network switch, so cart will step off meta-rail and be shot from the switch to its configured route along the normal maglev rails.

<img width="400" alt="Complex" src="https://github.com/user-attachments/assets/2c40a857-33cd-4047-84b8-3e518d1c67d3" />

> Note: I'm not a huge fan of this one because it can be very slow and can cause quite a lot of traffic. We shouldn't have to model DHL switches after real network switching because it would limit the capabilities of DHL. So I'm not a huge advocate for this idea, but just putting it out there to leave options open or bring inspo.

---

## Docking

Personally, I like the meta rails being applied here because we can just have the meta rail be pulled out and pulled in when the cart arrives or leaves the docking station. 

---

1. Cart arrives at docking station (still on rails)
2. Electromagnetic force applied sideways to shift the perpendicular platform towards the docking area
3. New rails replace position of initial rails (that the docked cart is on top of)
4. Ongoing traffic uses new rails
5. When docked cart returns, electronagnetic force applied to shift it back in place, replacing new rails with old

