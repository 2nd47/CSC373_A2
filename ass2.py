import sys
from random import random
import pdb

class Node:
	def __init__(self, val, size):
		self.value = val
		#A list of weights to each node w/ idx corresponding to val
		self.children = [None]*size

	def __getitem__(self, key):
		# Access a node with [] notation and you will access its children
		return self.children[key]

	def __setitem__(self, key, value):
		# Access a node with [] notation and you will access its children
		self.children[key] = value

def create_graph(size):
	nodelist = []
	for i in range(size):
		nodelist.append(Node(i, size))

	#set edges
	for i in range(size):
		for j  in range(size):
			if not nodelist[i][j]:
				if i == j:
					nodelist[i][j] = 0
				else:
					edgelen = random()
					nodelist[i][j] = edgelen
					nodelist[j][i] = edgelen

	pdb.set_trace()

if __name__ == '__main__':
	sizev = int(sys.argv[1])

	#size can be between 30 - 50k
	create_graph(sizev)
