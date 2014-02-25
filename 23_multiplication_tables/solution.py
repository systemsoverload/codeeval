for i in xrange(1, 13):
    print ''.join([str(x * i).rjust(4) for x in xrange(1, 13)]).strip()