import sys

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    print ' '.join(["{0}{1}".format(f[0].upper(), f[1::]) for f in l.split(' ')])
