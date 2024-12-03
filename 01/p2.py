#!/usr/bin/env python3
from icecream import ic
print = ic
import numpy

from collections import Counter

with open("inp.txt") as f:
    inp = f.read().strip().splitlines()
    left, right = [], []
    for element in inp:
        l,r = element.split("   ")
        left.append(l)
        right.append(r)


left = sorted(left)
right = sorted(right)


c = Counter(right)
ic(c)

s = 0
for l in left:
    s += int(l)* c.get(l, 0)
print(s)
