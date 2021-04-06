import time, math
from fractions import Fraction
from functools import lru_cache
import sys

"""
NOTE THAT THIS SOLUTION IS FAR TOO SLOW FOR SOME TEST CASES
"""

sys.setrecursionlimit(10**6)

top, bot = list(map(int, input().split()))

start = time.time()

V = Fraction(top, bot)

ans = []
allAns = []

seen = {}
mini = 1

def combine(a,b):
    if a == None or b == None: return None
    return a + b

def optimum(a,b):
    if a == None: return b
    if b == None: return a
    if len(a) < len(b): return a
    if len(b) < len(a): return b
    if max(a) < max(b): return a
    return b


def greedyEgypt(frac):
    frac = Fraction(frac)
    denom = []
    while frac.numerator != 0:
        x = math.ceil(frac.denominator / frac.numerator)
        denom.append(x)
        frac -= Fraction(1,x)
    return denom

@lru_cache(maxsize=None)
def egypt(v, i, d, maxa):
    global solution, shortest, largest

    print(v,i,d, shortest, largest)

    if v == Fraction(0,1):
        solution = True
        return tuple()

    if d > shortest: return None
    if i > largest: return None
    if v.denominator > 32000: return None
    if v.numerator == 1:
        solution = True
        d += 1
        maxa = max(maxa, v.denominator)
        if d <= shortest:
            shortest = d
            largest = min(maxa, largest)
        return (v.denominator,)
    if i > 32000: return None
    while Fraction(1,i) > v:
        i += 1
    return optimum(combine(egypt(v-Fraction(1,i), i+1, d + 1, max(i,maxa)),(i,)), egypt(v, i+1, d, maxa))


shortest = 9
largest = float("inf")

v = Fraction(V)
solution = False
print("Greedy", greedyEgypt(v))
print(egypt(v,2,0,0))

print("Time:", time.time() - start)

"""
b) 1/7
   31/32
   
c) There are no fractions which have unique egyptian fractions. All fractions can be written as an egyptian fraction, and
every unit fraction can be written as an egyptian fraction with more than 1 fraction. e.g. 1/7 = 1/8 + 1/56. Therefore,
given an egyptian fraction, an equivalent egyptian fraction can be created by expanding one its unit fractions into another
egyptian fraction with multiple terms.

d) 303791

"""

def d():
    seen = set()
    for a in range(1,1000):
        for b in range(1,1000):
            if a < b:
                seen.add(Fraction(a,b))
    print(len(seen))

d()