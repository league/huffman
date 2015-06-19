#!/usr/bin/python
import sys
from bits import *

codes = {}
char = 0
for line in sys.stdin:
    xs = line.split()
    codes[xs[0]] = chr(char)
    char += 1

with open(sys.argv[1], 'rb') as inf:
    inb = BitInstream(inf)
    try:
        while True:
            buf = ''
            while buf not in codes:
                bit = inb.read1()
                buf += '1' if bit else '0'
            sys.stdout.write(codes[buf])
    except EOFError:
        pass
