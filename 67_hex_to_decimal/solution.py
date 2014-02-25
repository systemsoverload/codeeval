import sys

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    print(int(l, 16))