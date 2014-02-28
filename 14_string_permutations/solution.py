import sys
from itertools import permutations


def solve(l):
    return ','.join(sorted([''.join(p) for p in permutations(l)]))


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            print solve(l)
