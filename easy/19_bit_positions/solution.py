import sys

def solve(l):
    number, b1, b2 = map(int, l.split(","))
    bits = bin(number)[2:]

    if b1 > len(bits) or b2 > len(bits):
        bits = '0' * (max(b1, b2) - len(bits)) + bits

    if bits[-b1] == bits[-b2]:
        return "true"
    else:
        return "false"

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            print(solve(l))