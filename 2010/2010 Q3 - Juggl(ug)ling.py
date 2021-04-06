from collections import deque
import time
startTime = 0

"""
NOTE THAT THIS SOLUTION IS A BIT TOO SLOW FOR SOME TEST CASES
"""

def juggling():
    global startTime
    j, n = list(map(int, input().split()))
    jugs = list(map(int, input().split()))

    startTime = time.time()

    start = tuple([0 for i in range(j)])

    pending = deque([(start, 0)])

    seen = set()

    while pending:
        check = pending.popleft()
#        print(check, pending)
        item, d = check

        # we can either fill, move or empty
        # fill jugs
        for i in range(j):
            this = list(item)
            this[i] = jugs[i]
            this = tuple(this)
            if n in this:
                print(d + 1)
                return
            if this not in seen:
                seen.add(this)
                pending.append((this, d+1))
        # empty jugs
        for i in range(j):
            if item[i] > 0:
                this = list(item)
                this[i] = 0
                this = tuple(this)
                if n in this:
                    print(d + 1)
                    return
                if this not in seen:
                    seen.add(this)
                    pending.append((this, d+1))
        # pour jugs
        for a in range(j):
            for b in range(j):
                if a != b and item[a] > 0:
                    this = list(item)
                    diff = min(jugs[b] - this[b], this[a])
                    this[b] = min(jugs[b], this[a] + this[b])
                    this[a] = max(0, this[a] - diff)
                    this = tuple(this)
                    if n in this:
                        print(d + 1)
                        return
                    if this not in seen:
                        seen.add(this)
                        pending.append((this, d + 1))


juggling()
print("Time:", time.time() - startTime)

"""
b) 1. Fill B. 
   2. Pour B into A. 
   3. Empty A. 
   4. Pour B into A. There will be 2 oz remaining in B
   
c) 2 & 20, 4 & 20, 

d) No. When liquid is poured from jug A to jug B, either jug A is emptied, jug B is filled, or both. Therefore,
every operation either fills or empties a jug, so after each operation that must be at least one jug which is either
full or empty. If there are no 1 oz jugs then a jug containing 1 oz of liquid is not full or empty. If every jug is
neither full or empty, then there is no set of steps which will achieve this outcome.
"""