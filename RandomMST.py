from random import random
import sys
import heapq
import time

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
	not_in_mst = set(range(1, size))
	edges = []
	nodes[0] = 1
	current = 0
	h = []
	weight = 0
	heaptime = 0
	poptime = 0

	while (len(edges) < size - 1):
		start = time.time()
		for i in not_in_mst:
			if (not nodes[i] and i != current):
				heapq.heappush(h, Edge(current, i, random()))
		end = time.time()

		heaptime += end - start
		min_edge = heapq.heappop(h)

		start = time.time()
		while (nodes[min_edge.vertices[0]] and nodes[min_edge.vertices[1]]):
			min_edge = heapq.heappop(h)
		end = time.time()

		poptime += end - start
		current = min_edge.vertices[1]
		nodes[current] = 1
		edges.append(min_edge)
		weight += min_edge.weight
		not_in_mst.remove(current)

	print("heaptime " + str(heaptime))
	print("poptime " + str(poptime))
	return weight

if __name__ == '__main__':
	# size can be between 30 - 50k
	if len(sys.argv) < 2:
		print('Please input a size argument!')
		exit()

	start = time.time()
	print(randomMST(int(sys.argv[1])))
	end = time.time()
	print(end - start)
	#create_graph(int(sys.argv[1]), None, randomWithinCircle)
