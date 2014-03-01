import re
import sys


def solve(l):
    word, segment = l.split(',')
    # Apparently sometimes segment has some other non-standard/working regex char
    if re.findall(segment, word):
        return 'true'
    else:
        return 'false'


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            print solve(l)
