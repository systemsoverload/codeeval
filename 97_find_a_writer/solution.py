import sys

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    encoded_str, c = l.split('|')
    code = c.split(' ')
    author = []
    for key in code:
        if key:
            author.append(encoded_str[int(key) - 1])

    print ''.join(author)

