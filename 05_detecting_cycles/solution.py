import sys

with open(sys.argv[1], 'r') as f:
    lines = [ ( line.strip(), len(line)) for line in f.readlines() if line.strip()]
