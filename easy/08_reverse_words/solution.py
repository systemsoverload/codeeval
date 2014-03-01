import sys

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    word_list = l.split(' ')
    word_list.reverse()

    print ' '.join(word_list)