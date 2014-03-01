import sys

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    s, _ = l.split(',')
    for i in _.strip():
        s = s.replace(i, '')

    print(s)
