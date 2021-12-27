from _collections import deque, defaultdict
from time import time

shortest = dict()
parent = dict()

def q3(t, c=False):
    if t == "A": return 1
    letters = list("ABCDEFGHIJKL")
    pending = deque([["A", 1]])
    best = 999999
    while pending:
#        print(pending)
        look, d = pending.popleft()
#        print(look)
        if d > best + 5: continue
        # add a letter
        if len(look) < len(t):
            i = letters[letters.index(max(look))+1]
            new = look + i
            if new not in shortest.keys() or d+1 < shortest[new]:
                shortest[new] = d+1
                parent[new] = [look]
                pending.append([new, d+1])
            elif d+1 == shortest[new]:
                parent[new].append(look)
            if new == t:
                if not c: return d+1
                else: best = d+1

        # swap
        if len(look) > 1:
            new = look[1] + look[0] + look[2:]
            if new not in shortest.keys() or d+1 < shortest[new]:
                shortest[new] = d+1
                parent[new] = [look]
                pending.append([new, d+1])
            elif d+1 == shortest[new]:
                parent[new].append(look)
            if new == t:
                if not c: return d+1
                else: best = d+1

        # rotate
        if len(look) > 1:
            new = look[1:] + look[0]
            if new not in shortest.keys() or d+1 < shortest[new]:
                shortest[new] = d+1
                parent[new] = [look]
                pending.append([new, d+1])
            elif d+1 == shortest[new]:
                parent[new].append(look)
            if new == t:
                if not c: return d+1
                else: best = d+1

    return best

def countWays(state):
    ways = 0
    if state not in parent: return 1
    for prev in parent[state]:
        ways += countWays(prev)

    return ways

def c(end):
    print(countWays(end))

a = input()
start = time()
print(q3(a, True))

c(a)
#print(time() - start)