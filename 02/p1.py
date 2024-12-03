
from icecream import ic
print = ic
import math
import numpy as np
from collections import Counter

levels = []
safe = 0
with open("inp.txt") as f:
    inp = f.read().strip().splitlines()
    for i in inp:
        l = [int(k) for k in i.split()]
        levels.append(l)
        lsafe = True
        ls = []
        print(l)
        for n1, n2 in zip(l, l[1:]):
            diff = n1 - n2
            diffa = abs(diff)
            print(diff, diffa)
            sig = np.sign(diff)
            ls.append(sig)
            if 1 <= diffa <= 3:
                continue
            else:
                print('greater')
                lsafe = False
                break
        if len(set(ls)) != 1:
            print('set', set(ls))
            lsafe = False
        if lsafe:
            safe += 1
print(safe)
