import sys

def solve(l):
    total = 0
    pwr = len(l)

    for digit in l:
        total += int(digit) ** pwr

    return int(l) == total

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            print solve(l)