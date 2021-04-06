import time

target = list("1234567")

order = list(input())

start = time.time()

pending = [(order, 0)]

ans = set()
seen = set()
while True:
    item, d = pending.pop(0)

    # code for part b
    """
    if d == 6:
        ans.add("".join(item))
    if d > 6: break
    """

    if item == target:
        print(d)
        break

    # 1
    q = list(item)
    a = q.pop(0)
    q.insert(3, a)
    if "".join(q) not in seen:
        seen.add("".join(q))
        pending.append((q, d+1))

    # 2
    q = list(item)
    a = q.pop(-1)
    q.insert(3, a)
    if "".join(q) not in seen:
        seen.add("".join(q))
        pending.append((q, d+1))

    # 3
    q = list(item)
    a = q.pop(3)
    q.insert(0, a)
    if "".join(q) not in seen:
        seen.add("".join(q))
        pending.append((q, d+1))

    # 4
    q = list(item)
    a = q.pop(3)
    q.append(a)
    if "".join(q) not in seen:
        seen.add("".join(q))
        pending.append((q, d+1))

#print(len(ans))
print("Time:", time.time() - start)

"""
b) 11 for 2
functions 1 and 3, 2 and 4 are inverse of each other. So both of those next to each other result in the same ordering.
1 + 3 * 4 = 13
Also the orders of functions 1 and 2, 3 and 4 don't matter, they result in the same ordering
13 - 2 = 11
Why is it not 334???


c) 

d) No. It is possible to get to the given starting order from any other starting order and so finishing in a different
order is equivalent to freely rearranging the shirts in some way. Thus, choosing the start and finishing orders has 
no bearing on the length of the hardest ordering as the changing of the arrangements is equivalent.
"""
