from ass2 import create_graph
from random import random
import sys
import heapq

class Edge:
    def __init__(self, v, w, other=None):
        self.vert = v
        self.weight = w
        self.next = other

class Vertex:
	def __init__(self, adj=None):
        # adj is a [list of (vertex, weight) pairs]
		self.adj = adj
        self.cost = 1
        self.prev = None

    def __cmp__(self, other):
        return cmp(self.cost, other.cost)

    def addEdge(self, edge):


def randomMST(size):
    # initial node 0
    h = []
    # create size vertices
    for i in range(size):
        heapq.heappush(h, Vertex())
    # initialize cost of some vertex to 0
    h[0].cost = 0
    while (curvyCurryVertex = heapq.heappop(h)):



if __name__ == '__main__':
	# size can be between 30 - 50k
	if len(sys.argv) < 2:
		print('Please input a size argument!')
		exit()
	print(randomMST(int(sys.argv[1])))
	#create_graph(int(sys.argv[1]), None, randomWithinCircle)
