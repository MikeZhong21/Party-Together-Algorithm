# Party Together Problem Solver

## Overview
The Party Together Problem (PTP) involves finding an optimal tour with least driving and walking cost to collect friends from their homes and return your home. 
The cost structure combines a driving cost (which is scaled by a constant α) and the walking distance for each friend to their pickup location.

## Problem Statement
The Party Together Problem (PTP) with inputs
 $(G,H,α)$. $G = (V,E)$ is an undirected graph where V is the set of nodes indexed from 0 to
 $|V | −1$ and each node represents a location in the city. The weight of each edge $(u,v)$ is the
 length of the direct road connection between location u and v, which is non-negative. <br/>
 Your house is at location 0. $H ⊂ V$ is the set of distinct locations that correspond to your friends’
 homes. If $F = {0,1,...,|F| − 1}$ is the set of friends, then each friend $m ∈ F$ has a house
 location hm ∈ H and each house location corresponds to exactly one friend. The constant α
 refers to the relative cost of driving vs walking. <br/>
 A possible pickup schedule specifies the locations where you will pick up your friends.
 More specifically, it will specify for each friend m a pickup location p<sub>m</sub> ∈ V , and you will
 need to drive your car starting from your home to pass from all the pickup locations to collect
 your friends and bring them back home (assume that the car has enough capacity to carry
 all your friends).
### Cost structure: 
Each friend incurs a walking cost equal to the distance traveled to get
from his home to his pickup location. You incur a driving cost equal to the distance traveled
by your car multiplied by the constant α, $0 ≤ α ≤ 1$. It is in general more efficient to travel
by car than walking, and the cost of the car does not depend on how many people it carries.

## Approach of PTP
The program initializes the tour: start from node 0, pass each home of friends, and end at node 0. <br/>
Then the program uses insert and delete heuristic to iteratively obtain the tour with shorter distance, eventually minimizing the cost (distance) of the tour.

### Insert Heuristic
1. Iterate through the tour and insert a node in any position of the tour (excluding index 0 and len(tour)-1)
2. Find the shortest path $p_{min1}$ between the inserted node and the predecessor of the inserted node $n_p$, and the shortest path $p_{min2}$ between the inserted node $n_s$ and the successor of the inserted node
3. Calculate the new path distance $p_{min} = p_{min1} + p_{min2}$
4. Replace the original path from node $n_p$ to node $n_s$ with $p_{min}$ to construct the new tour $t’$
5. Calculate and compare the cost of the current tour with the new tour $t’$
  * If the new tour $t’$ has lower cost, it will become the current tour.
  * If not, continue the loop to insert another node or insert the same node in another
    position and compare the cost.

### Delete Heuristic
1. Iterate through the tour and remove a node in any position of the tour (excluding index 0 and len(tour)-1)
2. Find the shortest path $p_{min}$ between the predecessor of the removed node and the successor of the removed node
3. Replace the original path from the predecessor to the successor that pass through the removed node with the path $p_{min}$ to construct the new tour $t’$
4. Calculate and compare the cost of the current tour with the new tour $t’$
  * If the new tour $t’$ has lower cost, it will become the current tour.
  * If not, continue the loop to remove another node and compare the cost.


