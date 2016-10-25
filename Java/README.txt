CSC373 Assignment 2
By :
  Daniil Kouznetsov
  Qingwei Li
  Julianna Paprakis

RandomMST:
RandomMST calculates the MST for some graph with a given size of vertices V using
Prim's algorithm and does it in this way:
   - Iterate from 0 to V-1:
      - Create a new vertex with some identifying index and a cost
      - Default cost to 1.1 (cost can at most be 1)
      - For the first vertex, set its cost to 0 and use it as the origin for the
        MST algorithm
   - Iterate over all vertices that are not in the MST (at first they are all not in the MST):
      - The current vertex (origin) will be the vertex with the minimum cost
      - Remove the current vertex from the set of vertices which are not in the MST (V)
        -The current vertex will now be in our MST
      - Add the cost of the current vertex to the total cost answer
      - Iterate over all remaining vertices (j) in V:
        - Create a random outgoing edge from the origin vertex to j
        - If the cost of the j is more than the weight of this new edge, set
          the cost to be the new edge weight
        - Keep track of the minimum cost vertex in V so we can pick the next origin:
          if the cost of the j is less than the current minimum cost vertex, j
          is the new minimum cost vertex.
    - Return total cost 
The main quirk of this algorithm is that the graph is generated on-the-fly
since edge weights are not retrieved from anywhere but, rather, are generated
as we move from vertex to vertex. This is correct as long as we create and check
one edge to and from every other edge in this complete graph. The asymptotic
runtime is identical to Prim's Algorithm. The first for loop to set each V takes |V| time. 
While we are calculating the edges and cost of the MST, we attempt to speed this up by only 
looping through each vertex currenly not in the MST.

This takes about |V| + |V|-1 + ... + 1 + 0 = |V|(|V|+1)/2 time, which still simplifies 
to |V|^2 time. As such, our runtime is O(|V|^2).

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
CircleMST is programmed the same as RandomMST. The only real difference
 between the two programs is that CircleMST represents vertices in an array of
four floats, instead of two, where those two new elements represent the x,y
coordinates of each vertex. The edges for each vertex are calculated by finding
the Euclidian Distance between the 2 vertex points, instead of being calculated 
randomly. In turn, CircleMST takes less time to run than
RandomMST. One reason for this would be that the amount of calls to
Math.random() is much smaller since we only need one call for each vertex
rather than for each edge weight, and there are V^2 edges in this graph since it
is a complete graph.

As both loops take the same time as the function above (the only difference is constant time calculations),
the runtime of this function is also O(|V|^2).

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
