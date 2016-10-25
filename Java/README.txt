CSC373 Assignment 2

RandomMST:
RandomMST calculates the MST for some given graph G with vertices V as such:
 - From 0 to V-1, create a new vertex stored 

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
