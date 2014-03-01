import sys

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    e = int(l) + int(l[::-1])
    i = 1
    while str(e)[::-1] != str(e):
        e = int(e) + int(str(e)[::-1])
        i += 1

    print "{0} {1}".format(i, e)
