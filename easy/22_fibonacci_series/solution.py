import sys

def solve(l):
    n = int(l)
    if n == 0:
            return (0, 1)
    else:
        a, b = solve(n // 2)
        c = a * (2 * b - a)
        d = b * b + a * a
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            print(solve(l)[0])