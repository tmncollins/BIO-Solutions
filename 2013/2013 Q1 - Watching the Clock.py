from functools import lru_cache
import time


a,b = list(map(int, input().split()))
t1 = [0,0]
t2 = [0,0]

start = time.time()

#@lru_cache(maxsize=None)
def incrementTime(t, n):
    t[1] += n
    t[0] = (t[0] + t[1] // 60) % 24
    t[1] = t[1] % 60
    return t

def printTime(t):
    h = str(t[0])
    m = str(t[1])
    if len(h) != 2: h = "0" + h
    if len(m) != 2: m = "0" + m
    print(h + ":" + m)


t1 = incrementTime(t1, 60 + a)
t2 = incrementTime(t2, 60 + b)
while t1 != t2:
    t1 = incrementTime(t1, 60 + a)
    t2 = incrementTime(t2, 60 + b)

printTime(t1)
print("Time:", time.time() - start)

"""
b) 8 (12:00), 9 (16:00), 16 (18:00), 18 (08:00), 0 (01:00)

c) greatest difference = 24 * 60 = 1440 so 1440 hours

"""
