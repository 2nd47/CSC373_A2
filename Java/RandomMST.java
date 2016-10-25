import java.util.HashSet;
import java.util.Random;

public class RandomMST {

    public static void main(String[] args) {
        Random random = new Random();
        int size = Integer.parseInt(args[0]);
        HashSet<float[]> V = new HashSet<>();
        float[] minV = null;
        float ans = 0;

        //For each vertex, add it to the hashset V, with a unique
        //identifier of its index, and a cost of 1.1 
        for (int i = 0; i < size; i++) {
            //newVertex array structured as: {index, cost}
            float[] newVertex = new float[]{(float)i, 1.1f};
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
            minV = new float[]{-1.1f, 1.1f};

            //We create edges from each vertex not currently in the MST to
            //the current min vertex we just popped. We don't need to create
            //edges between curr and vertices already in the MST, because these
            //edges were already created and considered when we added these
            //vertices to the MST earlier.
            float newEdge;
            for (float[] j : V) {
                newEdge = random.nextFloat();

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