from collections import defaultdict
import time as TIME

n = int(input())
astronauts = list(map(int, input().split()))

start = TIME.time()

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

modes = defaultdict(int)
speeds = {alpha[i]:astronauts[i] for i in range(n)}
astro = set(alpha[:n])

pending = [(n, 0, astro, set())]
while len(pending) > 0:
    pending = sorted(pending)
    curr = pending.pop(0)
#    print(curr, pending)
    for a1 in curr[2]:
        for a2 in curr[2]:
            if a1 < a2:
                time = max(speeds[a1], speeds[a2])
                time += curr[1]
                remaining = set(curr[2])
                crossed = set(curr[3])
                remaining.remove(a1)
                remaining.remove(a2)
                crossed.add(a1)
                crossed.add(a2)
                fastest = float("inf")
                f = "A"
                for a in crossed:
                    if speeds[a] < fastest:
                        fastest = speeds[a]
                        f = a
                crossed.remove(f)
                remaining.add(f)
                time += speeds[f]

                if (len(remaining)) == 1:
                    final = list(remaining)[0]
                    time -= speeds[final]
                    key = frozenset()
                    if modes[key] == 0 or time < modes[key]:
                        modes[key] = time
#                    print(time)
                else:
                    key = frozenset(remaining)
                    if modes[key] == 0 or time < modes[key]:
                        modes[key] = time
                        pending.append((len(remaining), time, remaining, crossed))

print(modes[frozenset()])
print("Time:", (TIME.time() - start))

"""
B) AB (2) cross then A (1) crosses back. CD (5) cross then B (2) crosses back. Finally AB cross (2) = 12 min
"""
