import sys

def solve(l):
    stops = sorted([int(stop.split(',')[1]) for stop in map(str.strip, l.split(';')[:-1])])
    route = []

    for idx, distance in enumerate(stops):
        if not idx:
            route.append(distance)
        else:
            route.append(distance - stops[idx - 1])

    print ','.join(map(str, route))

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            solve(l)