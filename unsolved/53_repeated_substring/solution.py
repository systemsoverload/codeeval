import sys

def solve(l):
    solutions = []
    for i in xrange(0, len(l)):
        for idx, val in enumerate(l):
            chunk = l[i:idx]
            if chunk and l.count(chunk) > 1 and chunk != l:
                cs = chunk.strip()
                if cs:
                    solutions.append((i, cs))

    if solutions:
        max_chunk_length = max(len(x[1]) for x in solutions)
        solutions = filter(lambda a: len(a[1]) == max_chunk_length, solutions)
        solutions.sort(key=lambda b: b[0])
        return solutions[0][1]
    else:
        return "NONE"

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            print solve(l)
