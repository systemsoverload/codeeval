import sys

def solve(l):
    haystack, needle = l.split(',')

    print(haystack.rfind(needle) )

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            solve(l)