CSC373 Assignment 2
By :
  Daniil Kouznetsov
  Qingwei Li
  Julianna Paprakis

RandomMST:
RandomMST calculates the MST for some given graph G with vertices V using
Prim's algorithm and does it in this way:
   - Iterate from 0 to V-1:
      - Create a new vertex with some identifying index and a cost
      - Default cost to 1.1 (cost can at most be 1)
      - For the first vertex, set its cost to 0 and use it as the origin for the
        MST algorithm
   - Iterate over all vertices:
      - The current vertex (origin) will be the vertex with the minimum cost
      - Remove the current from the list of vertices
      - Add the cost of the current vertex to the overall answer
      - Iterate over all remaining vertices:
        - Create an outgoing edge
        - If the cost of the vertex is more than the weight of this edge, set
          the cost to be the edge weight
        - If the cost of the vertex is less than the minimum cost vertex, this
          is the new minimum cost vertex.
    - Return total cost
The main quirk of this algorithm is that the graph is generated on-the-fly
since edge weights are not retrieved from anywhere but, rather, are generated
as we move from vertex to vertex. This is correct as long as we create
one edge to and from every other edge in this complete graph. The asymptotic
runtime is identical to Prim's Algorithm.

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
CircleMST is programmed the same as RandomMST. However, the only real difference
 between the two programs is that CircleMST represents vertices in an array of
four floats, instead of two, where those two new elements represent the x,y
coordinates of each vertex. In turn, CircleMST takes less time to run than
RandomMST. One reason for this would be that the amount of calls to
Math.random() is much smaller since we only need one call for each vertex
rather than for each edge weight.

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
