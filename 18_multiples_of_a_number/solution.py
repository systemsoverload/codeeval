import sys

def solve(l):
    floor, multiplier = map(int, l.split(','))

    count = 1
    while multiplier * count < floor:
        count += 1

    print(multiplier * count)

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            solve(l)