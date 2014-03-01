import sys

def solve(l):
    numbers = l.split()
    unique_numbers = [number for number in numbers if numbers.count(number) == 1]

    if unique_numbers:
        print numbers.index(str(sorted(map(int, unique_numbers))[0])) + 1
    else:
        print 0

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            solve(l)