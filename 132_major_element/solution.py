import sys

def solve(l):
    numbers = l.split(',')
    row_hash = {}

    for num in numbers:
        count = row_hash.setdefault(num, 0)
        row_hash[num] = count + 1
        if row_hash[num] > len(numbers) / 2:
            return num

    return None

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print solve(line.strip())
