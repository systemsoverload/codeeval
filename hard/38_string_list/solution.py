import sys
from itertools import permutations

#Permutations returns MANY duplicates which causes set/list comprehension to fail with memory errors
def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p


def solve(t):
    word_length, word = t.split(',')
    word_length = int(word_length)

    return ','.join(sorted([''.join(p) for p in unique_permutations(''.join([letter * len(word) for letter in word]), word_length)]))

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            print solve(l)
