'''
Python script to run the java programs and retrieve various statistics on it
'''

import argparse
import subprocess
import sys
import time
import pdb

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test MST functions')
    parser.add_argument('java', help='path to java program')
    parser.add_argument('n', help='number of times to run program')

    args = parser.parse_args()
    if not (args.java or args.n):
        print('Not enough arguments provided')

    sizes = [2, 4, 8, 10, 15, 25, 100, 1000, 10000, 20000, 50000]

    results = {}
    for i in sizes:
        results[i] = []
        results[i].append([])
        results[i].append([])

    for size in sizes:
        costs = []
        times = []
        for i in range(int(args.n)):
            t0 = time.time()
            cost = subprocess.check_output(["java", args.java, str(size)])
            t1 = time.time()
            timeTaken = t1 - t0
            costs.append(float(cost))
            times.append(timeTaken)

        #Time stored at results[size][0], cost stored at results[size][1]

        #Average (idx 0)
        results[size][0].append(sum(times)/int(args.n))
        #Max (idx 1)
        results[size][0].append(max(times))
        #Min (idx 2)
        results[size][0].append(min(times))

        #Average (idx 0)
        results[size][1].append(sum(costs)/int(args.n))
        #Max (idx 1)
        results[size][1].append(max(costs))
        #Min (idx 2)
        results[size][1].append(min(costs))

    #pdb.set_trace()
    with open('output.txt', 'w') as f:
    	f.write('Output of testing MST functions follows: \n\n')
    	f.write("Time:\n")
    	for size in sizes:
    		f.write("Size " + str(size) + ":\n")
    		f.write("Average: " + str(results[size][0][0] ) + '\n')
    		f.write("Max: " + str(results[size][0][1])+ '\n')
    		f.write("Min: " + str(results[size][0][2])+ '\n\n')

    	f.write('\n\n\n')
    	f.write("Cost:\n")    	
    	for size in sizes:
    		f.write("Size " + str(size) + ":\n")
    		f.write("Average: " + str(results[size][1][0]) + '\n')
    		f.write("Max: " + str(results[size][1][1])+ '\n')
    		f.write("Min: " + str(results[size][1][2])+ '\n\n')
