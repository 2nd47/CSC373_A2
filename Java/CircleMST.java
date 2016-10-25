import java.util.HashSet;
import java.util.Random;

public class CircleMST {

    public static float dist(float[] pos1, float[] pos2) {
        return (float)Math.sqrt(
                Math.pow((pos1[0] - pos2[0]), 2.0d) +
                Math.pow((pos1[1] - pos2[1]), 2.0d));
    }

    public static void main(String[] args) {
        int size = Integer.parseInt(args[0]);
        Random random = new Random();
        HashSet<float[]> V = new HashSet<>();
        float[] minV = null;
        float ans = 0;

        //For each vertex, add it to the hashset V, with a unique identifier of
        //its index, a cost of 1.1, and the 2 coordinates denoting its position 
        for (int i = 0; i < size; i++) {
            //newVertexZ is generating a random angle inside the circle
            float newVertexZ = 2 * (float)Math.PI * random.nextFloat();
            float shrinkFactor = random.nextFloat();
            //newVertex array structured as: {index, cost, position1, position2}
            float[] newVertex = new float[]{
                    (float)i,
                    2.1f,
                    shrinkFactor * (float)Math.cos(newVertexZ),
                    shrinkFactor * (float)Math.sin(newVertexZ)};
            if (i == 0) {
                newVertex[1] = 0;
                minV = newVertex;
            }
            V.add(newVertex);
        }

        //Starting with the first vertice in V, go through and
        //remove the smallest cost vertice from V until V is empty
        float[] curr;
        while (V.size() > 0) {
            //remove current min, as it is the smallest cost vertice so
            //we will add it to our MST
            curr = minV;
            V.remove(curr);
            ans += curr[1];

            //Reset our min to a number larger than any other vertice cost
            minV = new float[]{-1.1f, 2.1f, -3f, -3f};

            //We find the edge length from each vertex not currently in the MST to
            //the current min vertex we just popped. We don't need to find the edge
            //length between curr and vertices already in the MST, because these
            //edges were already calculated and considered when we added these vertices
            //to the MST earlier.
            float newEdge;
            for (float[] j : V) {
                // New edge dist is euclidean distance between the two vertices
                newEdge = dist(new float[]{j[2], j[3]}, new float[]{curr[2], curr[3]});
                
                //If the edge between curr to vertex j is less than the current
                //minimum edge from some other vertex to j, we save the new edge
                //as the cost instead
                if (j[1] > newEdge) {
                    j[1] = newEdge;
                }

                //Keep track of the smallest cost edge we encounter in V, so we can
                //remove it next
                if (j[1] < minV[1]) {
                    minV = j;
                }
            }
        }
        System.out.println(ans);
    }
}