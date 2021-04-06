from collections import defaultdict
import time
from functools import lru_cache


complex = defaultdict(list)
visited = defaultdict(int)
exits = defaultdict(int)
pos = "A"

def generateComplex(plan):
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    letters = alpha[:len(plan) + 2]
    plan = list(plan)
    while plan:
        for l in letters:
            if l not in plan:
                complex[l].append(plan[0])
                complex[plan[0]].append(l)
                plan.pop(0)
                letters.remove(l)
                break
    for l in letters:
        for l2 in letters:
            if l != l2:
                complex[l].append(l2)


def printComplex():
    for room in sorted(complex.keys()):
        print("".join(sorted(complex[room])))

#@lru_cache(maxsize=None)
def move(pos, n):
    global visited, complex, exits

    if n == 1:
        next = complex[pos][0]
        exits[pos + next] += 1
        return next
    else:
        next = complex[pos]
        for j in range(len(next)):
            i = next[j]
            if exits[pos + i] % 2 == 1:
                if i == next[-1]:
                    exits[pos+i] += 1
                    return i
                else:
                    i = next[j+1]
                    exits[pos+i] += 1
                    return i


plan, p, q = input().split()
p, q = int(p), int(q)
start = time.time()

generateComplex(plan)
printComplex()

for item in complex:
    complex[item] = sorted(complex[item])

for i in range(p):
    visited[pos] += 1
    pos = move(pos, visited[pos] % 2)
print(pos,end="")
for i in range(q-p):
    visited[pos] += 1
    pos = move(pos, visited[pos] % 2)
print(pos)

print("Time:", time.time() - start)

"""
b) A 
   AAAA
   Letters in plan = Number of letters in complex - 2. As all rooms are connected only a A, the plan must only contain
   As

c) If the number of odd exits from the room is even, the room must have been visited an odd number of times. If it is odd,
the room must have been visited an even number of times. For example, the first time a spy is in a room, the number of 
odd exits is zero, which is even.

"""

