from functools import lru_cache
from time import *

park, n = input().split()
park = park.lower()
n = int(n)

start = time()

alpha = "abcdefghijklmnopqrstuvwxyz"

@lru_cache(maxsize=None)
def count(filled, j):
    if j >= len(filled): return 1

    global park
    a = alpha[j]
    start = -1
    for i in range(len(park)):
        if filled[i] == "1":
            if start == -1:
                start = i
        elif park[i] != a:
            start = -1

        if park[i] == a:
            filled = list(filled)
            filled[i] = "1"
            filled = "".join(filled)
            options = 1
            if start > -1:
                options = i + 1 - start
            return options * count(filled, j+1)


@lru_cache(maxsize=None)
def construct(j, filled, n):
    if j >= len(filled): return ""
    global park
    a = alpha[j]
    start = -1

    for i in range(len(park)):
        if filled[i] == "1":
            if start == -1:
                start = i
        elif park[i] != a:
            start = -1

        if park[i] == a:
            filled = list(filled)
            filled[i] = "1"
            filled = "".join(filled)
            # this is where we are parked so we
            # could prefer any filled point congruent
            # to the left

#            if start == -1:
#                return alpha[i] + construct(j+1, filled, n)
            # there are options
            k = start
            if k == -1: k = i
            while True:
                n1 = count(filled, j+1)
                if n <= n1:
                    return alpha[k] + construct(j+1, filled, n)
                n -= n1
                k += 1

filled = "0" * len(park)

#print(count(filled, 0))
print(construct(0, filled, n).upper())
#print(time() - start)
