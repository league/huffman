#!/usr/bin/python
import sys
from bits import *

code = []
for line in sys.stdin:
    xs = line.split()
    code.append(xs[0])

with open(sys.argv[1], 'rb') as inf:
    outb = BitOutstream(sys.stdout.buffer)
    buf = inf.read()
    while len(buf) > 0:
        for ch in buf:
            for bit in code[ch]:
                outb.write1(bit == '1')
        buf = inf.read()
    outb.close()
