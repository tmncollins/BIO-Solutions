import time
"""

seen = set()
def func(items):
    if len(items) == 1: return
    for i in range(len(items)):
        for j in range(len(items)):
            if i < j:
                for a in range(len(items) - 1):
                    q = list(items)
                    A = q[i]
                    B = q[j]
                    if A+B < 10:
                        q.remove(A)
                        q.remove(B)
                        q.insert(a, A+B)
                        if tuple(q) not in seen:
                            seen.add(tuple(q))
                            func(q)

w = [1 for i in range(int(input()))]

func(w)
seen.add(tuple(w))
#print(seen)
print(len(seen))
order = sorted(list(seen))
print(order[int(input()) - 1])
print(order.index((2,1,1,2,1,1)))
"""

def getTot(n):
    if n < 10:
        return max(1,2**(n-1))
    n -= 10
    s = 2**9 - 1
    c = -1
    k = 1
    while n > 0:
        n -= 1
        c += 1
        s *= 2
        s -= getTot(k)
        k += 1
    return s

q, p = list(map(int, input().split()))

start= time.time()

#print(getTot(q))

o = q

Q = q
ans = []
curr = 1
while p > 0 and sum(ans) < o:
#    print(curr, p, q, getTot(q-1))
    if p <= getTot(q-1):
        ans.append(curr)
        q = o - sum(ans)
#        Q -= 1
        curr = 1
    else:
        p -= getTot(q-1)
        q -= 1
        curr += 1

for item in ans: print(item, end=" ")
print()
print("Time:", time.time() - start)

"""
b) 88 blocks
32 * 1, 16 * 2, 10 * 3, 8 * 4, 6 * 5, 5 * 6, 4 * 7, 4 * 8, 3 * 9
32 + 16 + 10 + 8 + 6 + 5 + 4 + 4 + 3 = 88

c) They are the reverse of the other. The last entry in the dictionary starts with as many 9s as possible. If there is a 
digit that it contains that is not a 9 at is at the end. The first entry in the numeric order must be as small (short) as
possible. The number with the most nines is also the shortest number. If there is a digit that it contains that is not a
9 at is at the start.

d) 

"""