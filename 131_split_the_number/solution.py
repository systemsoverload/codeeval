import sys

def solve(l):
    number, pattern = l.split()
    operator_idx = [pattern.find(i) for i in ('+', '-') if pattern.find(i) > 0][0]
    operator = pattern[operator_idx]

    #Probably a safer way to do the math, but it was fast...
    return eval( ''.join([number[:operator_idx], operator, number[operator_idx:]]) )


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            print(solve(l))