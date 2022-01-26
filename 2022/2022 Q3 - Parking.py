from functools import lru_cache
from time import *
from math import *

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

def get_num_prefs(parked, car):
    position = parked.index(car)
    preferences = 1

    while position > 0:
        position -= 1
        if parked[position] == ".":
            break
        preferences += 1

    return preferences

def count_pref_lists(park):
    parked = ["." for _ in range(len(park))]
    prefs = 1
    for car in range(len(park)):
        position = park.index(alpha[car])
        parked[position] = alpha[car]
        # get the car's preferred positions
        preferred = get_num_prefs(parked, alpha[car])
        # update total number of valid preference lists
        prefs *= preferred
    return prefs

from itertools import permutations as perms

def c(i):
    ans = 0
    for a in perms(alpha[:i]):
        a = "".join(a)
    #    print(a, count("".join(a)))
        if count_pref_lists(a) == 2:
            ans += 1
    print(ans)

"""
Triangle Numbers, so 16 is 15th triangle number = 120
2 1
3 3
4 6
5 10
6 15
7 21 
8 28
"""

def d():
    ans = 0
    fact = factorial(15)
    for a in range(1,16):
        for b in range(1,a):
            ans += fact // (a*b)
    output = ""
    ans = str(ans)[::-1]
    for i in range(0, len(ans), 3):
        output += ans[i:i+3] + ","
    output = output[::-1][1:]
    print(output)
#d()
