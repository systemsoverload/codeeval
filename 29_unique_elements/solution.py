import sys

def solve(l):
    unique_numbers = sorted(set(int(number) for number in l.split(',')))
    print(','.join([str(number) for number in unique_numbers]))

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            solve(l)