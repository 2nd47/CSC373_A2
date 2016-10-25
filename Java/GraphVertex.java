public class GraphVertex {
        public double cost = 2.1d;
        public int index;
        public double[] pos;

        public GraphVertex(int index) {
            this.index = index;
        }

        public GraphVertex(int index, boolean circle) {
            this.index = index;
            if (circle) {
                this.pos = randomWithinCircle();
            }
        }

        private double[] randomWithinCircle() {
            double z = 2 * Math.PI * Math.random();
            return new double[] {Math.cos((int) z), Math.sin((int) z)};
        }
}
