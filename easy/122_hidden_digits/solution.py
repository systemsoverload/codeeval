import sys

code = 'abcdefghij'

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    print ''.join([char if char.isdigit() else str(ord(char) - 97) for char in l if char.isdigit() or char in code]) or 'NONE'
