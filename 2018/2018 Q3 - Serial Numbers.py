from collections import deque, defaultdict
import time

def allSwap(n):
    ans = set()
    for i in range(len(n) - 1):
        a = int(n[i])
        b = int(n[i+1])
        v = False
        if i > 0:
            c = int(n[i-1])
            if c > min(a,b) and c < max(a,b): v = True
        if i < len(n) - 2:
            c = int(n[i+2])
            if c > min(a,b) and c < max(a,b): v = True
        if v:
            m = list(n)
            m[i] = str(b)
            m[i+1] = str(a)
            ans.add("".join(m))
    return ans

n = int(input())
a = input()

start = time.time()

graph = defaultdict(set)

# create graph
def createGraph(a):
    global graph
    graph = defaultdict(set)
    seen = set()
    pending = deque([a])
    while pending:
        item = pending.popleft()
        w = allSwap(item)
        for order in w:
            graph[item].add(order)
            graph[order].add(item)
            if order not in seen:
                seen.add(order)
                pending.append(order)

#print(graph)

# find the furthest node
def findFurthest(a):
    global graph
    pending = deque([(a, 0)])
    furthest = 0
    node = ""
    seen = set()
    while pending:
        item, d = pending.popleft()
        seen.add(item)
        for i in graph[item]:
            if i not in seen:
                seen.add(i)
                pending.append((i, d+1))
        if d > furthest:
            furthest = d
            node = item
    return (node, d, seen)

createGraph(a)
node, d, seen = findFurthest(a)
#print(d)
#nodeEnd, d = findFurthest(node)

print(d)
#print(node, nodeEnd)



print("Time:", time.time() - start)

"""
b) 7 : 324165-326451
   16 : 865312479-136897542

c) 
"""
