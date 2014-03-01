from operator import itemgetter
import sys

with open(sys.argv[1], 'r') as f:
    lines = [ ( line.strip(), len(line)) for line in f.readlines() if line.strip()]

#Pop off the first line which is the # of results to return
max_results = lines.pop(0)[0]

#Sort the words by length and then slice off N number of them
n_longest_words = sorted(lines, key=itemgetter(1))[(int(max_results) * -1)::]

#Parse the list in reverse order to print the longest words first
print('\n'.join([w[0] for w in reversed(n_longest_words)]))