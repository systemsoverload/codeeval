import sys

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    set1, set2 = l.split('|')
    #Remove extra padded space from list
    set1 = set1.split(' ')[0:-1]
    set2 = set2.split(' ')[1::]

    for i, v in enumerate(set1):
        sys.stdout.write("{0} ".format(int(v) * int(set2[i])))

    sys.stdout.write('\n')