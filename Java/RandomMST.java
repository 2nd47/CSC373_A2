import java.util.HashSet;

class RandomMST {

    public static void main(String[] args) {
        int size = Integer.parseInt(args[0]);

        HashSet<float[]> V = new HashSet<>();

        float[] minV = null;
        float ans = 0;

        for (int i = 0; i < size; i++) {
            float[] newVertex = new float[]{(float)i, 1.1f};
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
            minV = new float[]{-1.1f, 1.1f};

            float newEdge;
            for (float[] j : V) {
                newEdge = (float)Math.random();
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