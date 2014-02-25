import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            print sum([int(c) for c in line])