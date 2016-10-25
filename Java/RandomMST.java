import java.util.HashSet;

class RandomMST {

    public static void main(String[] args) {
        int size = Integer.parseInt(args[0]);

        HashSet<GraphVertex> V = new HashSet<>();

        GraphVertex minV = null;
        double ans = 0;

        for (int i = 0; i < size; i++) {
            GraphVertex newVertex = new GraphVertex(i);
            if (i == 0) {
                newVertex.cost = 0;
                minV = newVertex;
            }
            V.add(newVertex);
        }

        GraphVertex curr;
        while (V.size() > 0) {
            curr = minV;
            V.remove(curr);
            ans += curr.cost;
            minV = new GraphVertex(-1);

            double newEdge;
            for (GraphVertex j : V) {
                newEdge = Math.random();
                if (j.cost > newEdge) {
                    j.cost = newEdge;
                }
                if (j.cost < minV.cost) {
                    minV = j;
                }
            }
        }
        System.out.println(ans);
    }
}