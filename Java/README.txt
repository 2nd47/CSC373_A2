CSC373 Assignment 2
By :
  Daniil Kouznetsov
  Qingwei Li
  Julianna Paprakis

RandomMST:
RandomMST calculates the MST for some graph with a given size of vertices V using
a version of Prim's algorithm. We chose Prim's algorithm for both graphs because both are
complete graphs, which means that they have |V|^2 edges. Prim's algorithm runs in V^2 time,
while Kruskal's takes |E| log |V| time, which is equivalent to |V|^2 log |V| in this case, thus
will take longer than Prim's. 

We chose to store our graph data in simple data structures, and not classes in an attempt to
optimize space and runtime, at the expense of readability.

Our version of Prim's works in this way:
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

-----------------OUTPUT TABLE-------------------
------------------------------------------------
-- Input 10^i | MST weight | Runtime (seconds) -
------------------------------------------------
        i=1 | 1.1806798  | 0.1038634767770690918
        i=2 | 1.3039436  | 0.1246650218963623000
        i=3 | 1.1848867  | 0.1249768733978271500
        i=4 | 1.1954565  | 1.3109245300292969000

Table of V:
-----------OUTPUT TABLE (times run=15) ----------------------------------------
-------------------------------------------------------------------------------
- Input  | Mean MST Weight | Min MST Weight | Max MST Weight | Average Runtime - 
-------------------------------------------------------------------------------
    V=2  |          0.4459 |         0.1107 |         0.8772 |           0.0736
   V=10  |          1.0451 |         0.5162 |         1.5546 |           0.0693
   V=25  |          1.2368 |         0.8582 |         1.6812 |           0.0748
  V=1000 |          1.2208 |         1.1377 |         1.3061 |           0.0906
  V=20000|          1.1987 |         1.1784 |         1.2112 |           4.9578
  V=50000|          1.2003 |         1.1912 |         1.2127 |          31.2575


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

-----------------OUTPUT TABLE------------------
-----------------------------------------------
- Input 10^i | MST weight | Runtime (seconds) -
-----------------------------------------------
         i=1 | 2.749175   | 0.10774803161621094
         i=2 | 10.982569  | 0.15880990028381348
         i=3 | 34.161404  | 0.21111416816711426
         i=4 | 108.53012  | 1.00618290901184080

Table of V:
-----------OUTPUT TABLE (times run=15) ----------------------------------------
-------------------------------------------------------------------------------
- Input  | Mean MST Weight | Min MST Weight | Max MST Weight | Average Runtime - 
-------------------------------------------------------------------------------
    V=2  |          0.7674 |         0.1886 |         1.3249 |           0.0669    
   V=10  |          2.7822 |         2.1769 |         3.6950 |           0.0658    
   V=25  |          4.9596 |         4.3374 |         5.8197 |           0.0724
  V=1000 |         34.4248 |        33.8470 |        35.3149 |           0.1037   
  V=20000|        153.2719 |       152.8553 |       154.0963 |           3.6205 
  V=50000|        242.1439 |       241.4320 |       242.9703 |          23.5194 