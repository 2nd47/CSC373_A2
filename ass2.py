import math
import sys
from random import random
import pdb
import time

class Node:
	def __init__(self, size, pos=(0,0)):
		self.pos = pos
		# a list of weights to each node w/ idx corresponding to weight
		self.children = [None]*size

	def __getitem__(self, key):
		'''# access a node with [] notation and you will access its children
		'''
		return self.children[key]

	def __setitem__(self, key, value):
		'''access a node with [] notation and you will access its children
		'''
		self.children[key] = value

	def __str__(self):
		'''string representation of some node
		'''
		return 'Node with ' + str(self.children) + '\n'

	def __repr__(self):
		return self.__str__()

class Edge:
	def __init__(v1, v2, weight):
		self.vertices = (v1, v2)
		self.weight = weight

	def hasVertice(vertice):
		return vertice in self.vertices

	def __getitem__(self, key):
		'''# access a node with [] notation and you will access its vertices
		'''
		return self.vertices[key]

	def __setitem__(self, key, value):
		'''access a node with [] notation and you will access its vertices
		'''
		self.vertices[key] = value

	def __cmp__(self, other):
         return cmp(self.weight, other.weight)

'''
REMINDER : THESE FILES MUST BE SPLIT UP BEFORE SUBMISSION
'''

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

def create_graph(size, edgeFunc, posFunc):
	# create an empty array of length 'size' with empty nodes
	nodelist = []
	if posFunc:
		nodelist = [Node(size, posFunc()) for i in range(size)]
	else:
		nodelist = [Node(size) for i in range(size)]

	# for every node in the nodelist
	for i in range(size):
		# and every one of its children (don't need all nodes)
		for j in range(i, size):
			# if not already initialized
			if i <= j and (not nodelist[i][j]):
				# if the edge is to itself, the weight must be 0
				if i == j:
					nodelist[i][j] = 0
				# otherwise, initialize some random weight for the edge
				else:
					# initialize the edge weight given some positions
					if posFunc:
						edgelen = dist(nodelist[i].pos, nodelist[j].pos)
					# initialize the edge weight given some function
					else:
						edgelen = edgeFunc()
					nodelist[i][j] = edgelen
					nodelist[j][i] = edgelen
	print(nodelist)
	pdb.set_trace()

def mstByMatrix(size):
	'''get the mst of a complete size-sized graph with random edges of weight
	uniformly distributed between [0...1)
	'''
	def inGraph(graph, edge):
		'''check if a vertex is in the graph
		'''
		pass

	t0 = time.time()
	nodes = [[None for j in range(i, size)] for i in range(size)]
	edges = []
	ans = 0

	for i in range(size):
		for j in range(i, size):
			if not nodes[i][j-i]:
				if i == j:
					nodes[i][j-i] = 0
				else:
					nodes[i][j-i] = random()
		# looped over all j
	# looped over all i

	t1 = time.time()
	print(str(t1-t0))
	# fully connected graph created, iterate over to create mst

	nodeMap = [False for i in range(size)]
	nodeMap[0] = True

	nextVert = 0

	# add the remaining vertices
	while nextVert > -1:
		break

	return ans

if __name__ == '__main__':
	# size can be between 30 - 50k
	if len(sys.argv) < 2:
		print('Please input a size argument!')
		exit()
	print(mstByMatrix(int(sys.argv[1])))
	#create_graph(int(sys.argv[1]), random, None)
	#create_graph(int(sys.argv[1]), None, randomWithinCircle)
