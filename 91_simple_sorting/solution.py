import sys
from decimal import Decimal

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            print ' '.join(map(str, sorted([Decimal(number) for number in l.split()])))