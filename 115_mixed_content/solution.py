import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line.strip():
            words = []
            numbers = []
            inputs = line.split(',')

            for i in inputs:
                i = i.strip()
                if str(i).isdigit():
                    numbers.append(i)
                else:
                    words.append(i)

            numbers_out = ','.join(numbers)
            words_out = ','.join(words)

            if numbers_out and words_out:
                print '|'.join([words_out, numbers_out])
            elif numbers_out:
                print(numbers_out)
            elif words_out:
                print(words_out)