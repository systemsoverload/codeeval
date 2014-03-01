import sys

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    binary_string = "{0:b}".format(int(l))
    print(binary_string.count('1'))
