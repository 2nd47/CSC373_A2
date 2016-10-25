'''
Python script to run the java programs and retrieve various statistics on it
'''

import argparse
import subprocess
import sys
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test MST functions')
    parser.add_argument('java', help='path to java program')
    parser.add_argument('n', help='number of times to run program')

    args = parser.parse_args()
    if not (args.java or args.n):
        print('Not enough arguments provided')

    sizes = [2, 10 , 25, 100]

    results = {}
    for i in sizes:
        results[i] = []

    for size in sizes:
        costs = []
        times = []
        for i in range(int(args.n)):
            t0 = time.time()
            cost = subprocess.check_output([args.java, str(size)])
            t1 = time.time()
            timeTaken = t0 - t1
            costs.append(cost)
            times.append(timeTaken)
        results[size]['time']['average'] = sum(times)/int(args.n)
        results[size]['time']['min'] = max(times)
        results[size]['time']['max'] = min(times)

        results[size]['cost']['average'] = sum(costs)/int(args.n)
        results[size]['cost']['min'] = max(costs)
        results[size]['cost']['max'] = min(costs)

    with open('output.txt', 'w+') as f:
        f.write('Output of testing MST functions follows: \n\n')
