import sys

class Node:
	def __init__(self):
		#A list of tuples containing edge weight and child node
		self.children = []

	def __getitem__(self, key):
		# Access a node with [] notation and you will access its children
		return self.children[key]

	def __setitem__(self, key, value):
		# Access a node with [] notation and you will access its children
		self.children[key] = value

def create_graph(size):



if __name__ == '__main__':
	sizev = sys.argv[1]

	create_graph(sizev)
