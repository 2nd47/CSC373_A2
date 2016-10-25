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
	global t00
	t00 = time.time()
	for i in range(size):
		newVertex = Vertex(i)
		# initialize cost of some vertex to 0
		if i == 0:
			newVertex.cost = 0
			minV = newVertex
		global t20
		t20 = time.time()
		v.add(newVertex)
		global t21
		t21 = time.time()
	global t01
	t01 = time.time()
	global t10
	t10 = time.time()
	while (len(v) > 0):
		cur = minV
		global t30
		t30 = time.time()
		v.remove(cur)
		global t31
		t31 = time.time()
		ans += cur.cost
		minV = Vertex(-1)
		global t40
		t40 = time.time()
		for j in v:
			newEdge = random()
			if j.cost > newEdge:
				j.cost = newEdge
				j.prev = cur.idx
			if j.cost < minV.cost:
				minV = j
		global t41
		t41 = time.time()
	global t11
	t11 = time.time()

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
	print('time to create vertices: ' + str(t01 - t00))
	print('time to add new vertices to set: ' + str(t21 - t20))
	print('time to find MST weight: ' + str(t11 - t10))
	print('time to remove from set: ' + str(t31 - t30))
	print('time to iterate to create new edges for a node: ' + str(t41 - t40))
	#create_graph(int(sys.argv[1]), None, randomWithinCircle)
