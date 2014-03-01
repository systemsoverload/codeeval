import sys

with open(sys.argv[1], 'r') as f:
    lines = [int(line.strip()) for line in f.readlines() if line.strip()]

print sum(lines)
