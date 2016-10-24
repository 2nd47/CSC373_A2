from ass2 import create_graph
from random import random
import sys
import heapq

class Edge:
	def __init__(self, v1, v2, weight):
		self.vertices = (v1, v2)
		self.weight = weight

	def hasVertice(self, vertice):
		return vertice in self.vertices

	def __cmp__(self, other):
         return cmp(self.weight, other.weight)

def randomMST(size):
    nodes = [None] * size
    edges = []
    nodes[0] = 1
    current = 0
    h = []
    weight = 0

    while (len(edges) < size - 1):
        for i in range(size):
            if (not nodes[i] and i != current):
                heapq.heappush(h, Edge(current, i, random()))
        min_edge = heapq.heappop(h)
        while (nodes[min_edge.vertices[0]] and nodes[min_edge.vertices[1]]):
            min_edge = heapq.heappop(h)
        current = min_edge.vertices[1]
        nodes[current] = 1
        edges.append(min_edge)
        weight += min_edge.weight

    return weight

if __name__ == '__main__':
	# size can be between 30 - 50k
	if len(sys.argv) < 2:
		print('Please input a size argument!')
		exit()
	print(randomMST(int(sys.argv[1])))
	#create_graph(int(sys.argv[1]), None, randomWithinCircle)
