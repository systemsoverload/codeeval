import sys

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    print int(all(l.count(str(i)) == int(ch) for i, ch in enumerate(str(l))))