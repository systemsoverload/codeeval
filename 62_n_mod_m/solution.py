import sys


def solve(l):
    n, m = map(int, l.split(','))
    print (n - m * int(n / m))


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
           solve(l)