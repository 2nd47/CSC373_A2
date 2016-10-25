from random import random
import math
import sys
import heapq
import time

def dist(pos1, pos2):
	'''return the distance between two points which are represented as
	a two-element, one-dimensional array
	'''
	return math.sqrt(
		(pos1[0] - pos2[0])**2 +
		(pos1[1] - pos2[1])**2
	)

def randomWithinCircle():
	''' Create a random position within the unit circle
	'''
	# create a random point along the circumfrence of the circle
	z = 2*math.pi*random()
	return (math.cos(z), math.sin(z))

class Vertex:
	def __init__(self, idx, posFunc, adj=None):
		# adj is a [list of (vertex, weight) pairs]
		self.adj = adj
		self.cost = 2
		self.prev = None
		self.idx = idx
		self.pos = posFunc()

	def __cmp__(self, other):
		return cmp(self.cost, other.cost)

def circleMST(size):
	# initial node 0
	v = set()
	minV = None
	ans = 0
	# create size vertices
	global t00
	t00 = time.time()
	for i in range(size):
		newVertex = Vertex(i, randomWithinCircle)
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
		minV = Vertex(-1, randomWithinCircle)
		global t40
		t40 = time.time()
		for j in v:
			newEdge = dist(j.pos, cur.pos)
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
	print(circleMST(int(sys.argv[1])))
	t1 = time.time()
	print('total time to execute: ' + str(t1 - t0))
	print('time to create vertices: ' + str(t01 - t00))
	print('time to add new vertices to set: ' + str(t21 - t20))
	print('time to find MST weight: ' + str(t11 - t10))
	print('time to remove from set: ' + str(t31 - t30))
	print('time to iterate to create new edges for a node: ' + str(t41 - t40))
	#create_graph(int(sys.argv[1]), None, randomWithinCircle)
