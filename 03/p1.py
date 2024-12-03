#!/usr/bin/env python3
from icecream import ic
import re
print = ic
import numpy

from collections import Counter

with open("inp.txt") as f:
    inp = f.read()
    pattern = "(do\(\))|(don't\(\))|(mul\((\d{1,3}),(\d{1,3})\))"
    matches = re.findall(pattern, inp)
    sum = 0
    enabled= True
    for row in matches:
        do, dont, mul, a, b = row
        if do:
            enabled = True
        elif dont:
            enabled = False
        if enabled and mul:
            sum += int(a)*int(b)
    print(sum)
