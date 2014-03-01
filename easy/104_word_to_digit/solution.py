import sys

digit_map = {
	"zero": 0, "one": 1, "two": 2, "three": 3,
	"four": 4, "five": 5, "six": 6, "seven": 7,
	"eight": 8, "nine": 9
}

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    print ''.join([str(digit_map[digit]) for digit in l.split(";")])
