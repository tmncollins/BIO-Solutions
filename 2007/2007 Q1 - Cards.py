from itertools import combinations

cards = list(map(int, input().split()))

sets = []
for i in range(2,5):
    sets += list(combinations(cards, i))

tot = 0
for item in sets:
    if sum(list(item)) == 15: tot += 1
    if len(item) == 2 and len(set(item)) == 1: tot += 1

print(tot)

"""
b) 10 9 8 1 2
c) 29. why is it not 29?????
"""

"""
code for c:

seen = []
tot = 0
for a in range(1,11):
    for b in range(1,11):
        for c in range(1,11):
            for d in range(1, 11):
                for e in range(1, 11):
                    l = [a,b,c,d,e]
                    if sum(l) == 15:
                        if sorted(l) not in seen:
                            seen.append(sorted(l))
                            print(l)
                            tot += 1
print(tot)

"""