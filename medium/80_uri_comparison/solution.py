from urllib import unquote
import sys


def get_octets(uri):
    proto, address = uri.split('://')
    host, schema = address.split('/')[0].lower().strip(':80'), [unquote(s.lower().strip()) for s in address.split('/')[1:]]

    return proto.lower(), host, schema

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for l in lines:
    uri1, uri2 = l.strip().split(';')

    print(get_octets(uri1) == get_octets(uri2))
