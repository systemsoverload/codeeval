import sys

def solve(l):
    solution = None
    for idx, val in enumerate(l):
        chunk = l[0:idx]
        if chunk and chunk == l[idx:idx + len(chunk)]:
            solution = chunk
            break

    try:
        return len(solution)
    except:
        return len(l)

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            print solve(l)
