import sys

def solve(l):
    numbers = l.split(' ')
    counter = 1

    for idx, number in enumerate(numbers):
        try:
            next_number = numbers[idx + 1]
        except IndexError:
            next_number = None

        if number == next_number:
            counter += 1
        else:
            print counter, number,
            counter = 1

    print '\n',

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            solve(l)