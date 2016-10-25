CSC373 Assignment 2
By :
  Daniil Kouznetsov
  Qingwei Li
  Julianna Paprakis

RandomMST:
RandomMST calculates the MST for some given graph G with vertices V as such:
   - Iterate from 0 to V-1:
      - Create a new vertex with some identifying index and a cost
      - Default cost to 1.1 (cost can at most be 1)
      - For the first vertex, set its cost to 0 and use it as the origin for the
        MST algorithm
   - Iterate over all vertices:
      - Remove the origin from the list of vertices
      - 

------------OUTPUT TABLE-------------
-------------------------------------
- Input 10^i | MST weight | Runtime -
-------------------------------------
         i=1 |            |
         i=2 |            |
         i=3 |            |
         i=4 |            |

Table of V:
-----------OUTPUT TABLE-------------
------------------------------------
- Input | Mean MST Weight (n=1000) -
------------------------------------
    V=2 |
   V=10 |
   V=25 |
  V=100 |


CircleMST:
CircleMST is programmed the same as RandomMST.

CircleMST takes less time to run than RandomMST. One reason for this would
be that the amount of calls to Math.random() is much smaller since we only
need one call for each vertex rather than for each edge weight.

------------OUTPUT TABLE-------------
-------------------------------------
- Input 10^i | MST weight | Runtime -
-------------------------------------
         i=1 |            |
         i=2 |            |
         i=3 |            |
         i=4 |            |

Table of V:
-----------OUTPUT TABLE-------------
------------------------------------
- Input | Mean MST Weight (n=1000) -
------------------------------------
    V=2 |
   V=10 |
   V=25 |
  V=100 |
