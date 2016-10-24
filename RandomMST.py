from ass2 import create_graph

if __name__ == '__main__':
	# size can be between 30 - 50k
	if len(sys.argv) < 2:
		print('Please input a size argument!')
		exit()
	create_graph(int(sys.argv[1]), random, None)
	#create_graph(int(sys.argv[1]), None, randomWithinCircle)
