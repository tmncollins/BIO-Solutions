from collections import *
from cfractions import Fraction
from time import time
from itertools import product


def get_time(fuse):
    if fuse[1] == 0: return float("inf")
    return fuse[0] / fuse[1]

def get_smallest_time(fuses):
    t = float("inf")
    for fuse in fuses:
        t = min(t, get_time(fuse))
    return t

def count_ways(fuses):
    times = {0}
    q = deque()
    start = []
    for f in fuses: start.append((f, 0))
    start = tuple(start)
    state = (start, 0)
    seen = set()
    seen.add(state)
    q.append(state)
    c = 0

    while q:
        fuses, t = q.pop()
        times.add(t)
        c += 1

        for state in product([0,1,2], repeat=len(fuses)):
            if sum(state) == 0: continue
            new_fuses = []
            for f in range(len(fuses)):
                new_fuses.append((fuses[f][0], max(state[f], fuses[f][1])))
#            if new_fuses == fuses: continue
            dt = get_smallest_time(new_fuses)
            if dt == float("inf"):
                continue
            n_fuses = []
            for j in range(len(new_fuses)):
                fuse = (new_fuses[j][0] - dt * new_fuses[j][1], new_fuses[j][1])
                if fuse[0] > 0:
                    n_fuses.append(fuse)
            n_fuses = tuple(sorted(n_fuses))

            state = (n_fuses, 0)
            if state not in seen:
                seen.add(state)
                q.append(state)
            state = (n_fuses, t+dt)
            if state not in seen:
                seen.add(state)
                q.append(state)
#    print(sorted(list(times)))
#    print(c)
    return len(times)

fuses = list(map(int, input().split()))
fuses.pop(0)
start_time = time()
#for i in range(len(fuses)):
#    fuses[i] = Fraction(fuses[i], 1)
print(count_ways(fuses))
print(time() - start_time)

def c(MAX):
    ans = 0
    for a in range(1, MAX+1):
        print(a, ans)
        for b in range(1, a+1):
            ans = max(ans, count_ways([Fraction(a, 1), Fraction(b, 1)]))
    print("For 2 fuses:", ans)

    ans = 0
    for a in range(1, MAX + 1):
        print(a, ans)
        for b in range(1, a + 1):
            for c in range(1, b + 1):
                ans = max(ans, count_ways([Fraction(a, 1), Fraction(b, 1), Fraction(c, 1)]))
    print("For 3 fuses:", ans)

#c(100)


"""
b) 0, 1, 2, 3, 0.5, 2.5, 1.5, 0.75, 1.25

c) For 2: 17, For 3: 163
"""