import sys

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    set1, set2 = l.split(';')
    set1 = set1.split(',')
    set2 = set2.split(',')
    print ','.join([val for val in set1 if val in set2]) or ''