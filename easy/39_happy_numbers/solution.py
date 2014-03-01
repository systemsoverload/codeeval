import sys

def sum_square(number):
    count = 0
    for digit in str(number):
        count += int(digit) ** 2

    return count


def solve(l):
    sum_digits = sum_square(l)
    starting_digits = sum_digits

    #Gross, but its late...
    count = 0
    while sum_digits != 1:
        sum_digits = sum_square(sum_digits)
        count += 1

        if count > 50:
            break

    print int(count < 49 or sum_digits == 1)


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            solve(l)
