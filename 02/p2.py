
from icecream import ic
print = ic
import math
import numpy as np
from collections import Counter
import tqdm

levels = []
safe = 0

def issafe(l):
    lsafe = True
    ls = []
    for n1, n2 in zip(l, l[1:]):
        diff = n1 - n2
        diffa = abs(diff)
        sig = np.sign(diff)
        ls.append(sig)
        if 1 <= diffa <= 3:
            continue
        else:
            lsafe = False
            break
    if len(set(ls)) != 1:
        lsafe = False
    return lsafe

# with open("ex.txt") as f:
with open("inp.txt") as f:
    inp = f.read().strip().splitlines()
    for i in tqdm.tqdm(inp):
        l = [int(k) for k in i.split()]
        levels.append(l)
        if issafe(l):
            safe += 1
        else:
            for i in range(len(l)):
                if issafe(l[:i] + l[i+1:]):
                    safe += 1
                    break
print(safe)
