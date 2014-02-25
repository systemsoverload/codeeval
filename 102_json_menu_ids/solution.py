import json
import sys

with open(sys.argv[1], 'r') as f:
    lines = [json.loads(line.strip()) for line in f.readlines() if line.strip()]

for l in lines:
    print(sum([item.get('id') for item in l.get('menu').get('items') if item and item.get('label')]))
