from copy import copy, deepcopy
import math
import sys
from random import random
import pdb

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

def boruvkaStep(graph):
	'''
	From Wikipedia:
	Input: A graph G with no isolated vertices
		1 For each vertex v, select the lightest edge incident on v
		2 Create a contracted graph G' by replacing each component of G connected by the edges selected in step 1 with a single vertex
		3 Remove all isolated vertices, self-loops, and non-minimal repetitive edges from G'
 	Output: The edges selected in step 1 and the contracted graph G'
 	'''
	newGraph = [[] for i in len(graph)]
	supernodes = []
	for i in graph:
		for j in range(len(i.children)):
			if i <= j and i != j:
				

	return newGraph

def createMST(graph):
	'''
	From Wikipedia:
	Input: A graph G with no isolated vertices
		If G is empty return an empty forest
		Create a contracted graph G` by running two successive Borůvka steps on G
		Create a subgraph H by selecting each edge in G` with probability 1/2. Recursively apply the algorithm to H to get its minimum spanning forest F.
		Remove all F-heavy edges from G` (where F is the forest from step 3) using a linear time minimum spanning tree verification algorithm.
		Recursively apply the algorithm to G` to get its minimum spanning forest.
	Output: The minimum spanning forest of G` and the contracted edges from the Borůvka steps
	'''

	return

if __name__ == '__main__':
	# size can be between 30 - 50k
	if len(sys.argv) < 2:
		print('Please input a size argument!')
		exit()
	create_graph(int(sys.argv[1]), random, None)
	#create_graph(int(sys.argv[1]), None, randomWithinCircle)
