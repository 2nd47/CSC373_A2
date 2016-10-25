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

        for (int i = 0; i < size; i++) {
            //newVertexZ is generating a random angle inside the circle
            float newVertexZ = 2 * (float)Math.PI * random.nextFloat();
            //newVertex array structured as:
            //{index, cost, position1, position2}
            float[] newVertex = new float[]{(float)i, 2.1f, (float)Math.cos(newVertexZ), (float)Math.sin(newVertexZ)};
            if (i == 0) {
                newVertex[1] = 0;
                minV = newVertex;
            }
            V.add(newVertex);
        }

        float[] curr;
        while (V.size() > 0) {
            curr = minV;
            V.remove(curr);
            ans += curr[1];
            minV = new float[]{-1.1f, 2.1f, -3f, -3f};

            float newEdge;
            for (float[] j : V) {
                // New edge dist is euclidean distance between the two vertices
                newEdge = dist(new float[]{j[2], j[3]}, new float[]{curr[2], curr[3]});
                if (j[1] > newEdge) {
                    j[1] = newEdge;
                }
                if (j[1] < minV[1]) {
                    minV = j;
                }
            }
        }
        System.out.println(ans);
    }
}