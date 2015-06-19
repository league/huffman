#!/usr/bin/python
from sys import stdin
from heapq import *

tally = [1 for char in range(256)]
bs = stdin.buffer.read()
while len(bs) > 0:
    for b in bs:
        tally[b] += 1
    bs = stdin.buffer.read()

worklist = [(count, [char]) for char, count in enumerate(tally)]
heapify(worklist)

codes = ['' for char in range(256)]
while len(worklist) > 1:
    left = heappop(worklist)
    right = heappop(worklist)
    for char in left[1]: codes[char] = '0' + codes[char]
    for char in right[1]: codes[char] = '1' + codes[char]
    heappush(worklist, (left[0]+right[0], left[1]+right[1]))

for char, code in enumerate(codes):
    print(code, repr(chr(char)))
