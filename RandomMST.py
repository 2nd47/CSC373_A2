from ass2 import create_graph
from random import random
import sys
import heapq
import time

class Vertex:
	def __init__(self, idx, adj=None):
		# adj is a [list of (vertex, weight) pairs]
		self.adj = adj
		self.cost = 1
		self.prev = None
		self.idx = idx

	def __cmp__(self, other):
		return cmp(self.cost, other.cost)

def randomMST(size):
	# initial node 0
	v = set()
	minV = None
	ans = 0
	# create size vertices
	for i in range(size):
		newVertex = Vertex(i)
		# initialize cost of some vertex to 0
		if i == 0:
			newVertex.cost = 0
			minV = newVertex
		v.add(newVertex)
	while (len(v) > 0):
		cur = minV
		v.remove(cur)
		ans += cur.cost
		minV = Vertex(-1)
		for j in v:
			newEdge = random()
			if j.cost > newEdge:
				j.cost = newEdge
				j.prev = cur.idx
			if j.cost < minV.cost:
				minV = j


	return ans

if __name__ == '__main__':
	# size can be between 30 - 50k
	if len(sys.argv) < 2:
		print('Please input a size argument!')
		exit()
	t0 = time.time()
	print(randomMST(int(sys.argv[1])))
	t1 = time.time()
	print('total time to execute: ' + str(t1 - t0))
	#create_graph(int(sys.argv[1]), None, randomWithinCircle)
