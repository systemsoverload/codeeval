import sys

def solve(l):
    numbers, replacements = l.split(':')
    numbers = numbers.split()
    replacements = map(str.strip, replacements.split(','))

    for r in replacements:
        source, destination = map(int, r.split('-'))
        source_number = numbers[source]
        destination_number = numbers[destination]
        numbers[source] = destination_number
        numbers[destination] = source_number

    print ' '.join(numbers)


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            solve(l)