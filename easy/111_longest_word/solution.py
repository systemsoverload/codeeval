import sys

def solve(l):
    longest_word = ""

    for word in l.split(' '):
        if len(word) > len(longest_word):
            longest_word = word

    print longest_word

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            solve(l)