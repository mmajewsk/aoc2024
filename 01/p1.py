#!/usr/bin/env python3
from icecream import ic
print = ic
import numpy

with open("inp.txt") as f:
    inp = f.read().strip().splitlines()
    left, right = [], []
    for element in inp:
        l,r = element.split("   ")
        left.append(l)
        right.append(r)


left = sorted(left)
right = sorted(right)

s = []
for l,r in zip(left, right):
    diff = abs(int(l) - int(r))
    s.append(diff)

print(sum(s))
