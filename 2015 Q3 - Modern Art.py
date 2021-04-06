from functools import lru_cache
import time

a,b,c,d,n = list(map(int, input().split()))

start = time.time()

@lru_cache(maxsize=None)
def factorial(n):
    t = 1
    while n > 1:
        t *= n
        n -= 1
    return t

@lru_cache(maxsize=None)
def perms(a,b,c,d):
    top = factorial(a+b+c+d)
    bottom = factorial(a) * factorial(b) * factorial(c) * factorial(d)
    return top / bottom

letters = "ABCD"

def order(word, pos, n):
#    print(word, pos, n)
    if sum(pos) == 1:
        for i in range(len(pos)):
            if pos[i] == 1:
                return word + letters[i]

   # check if A
    if pos[0] > 0:
        if n <= perms(pos[0] - 1, pos[1], pos[2], pos[3]):
            return order(word + "A", [pos[0] - 1, pos[1], pos[2], pos[3]], n)
        else:
            n -= perms(pos[0] - 1, pos[1], pos[2], pos[3])
    # check if B
    if pos[1] > 0:
        if n <= perms(pos[0], pos[1] - 1, pos[2], pos[3]):
            return order(word + "B", [pos[0], pos[1] - 1, pos[2], pos[3]], n)
        else:
            n -= perms(pos[0], pos[1] - 1, pos[2], pos[3])
    # check if C
    if pos[2] > 0:
        if n <= perms(pos[0], pos[1], pos[2] - 1, pos[3]):
            return order(word + "C", [pos[0], pos[1], pos[2] - 1, pos[3]], n)
        else:
            n -= perms(pos[0], pos[1], pos[2] - 1, pos[3])
    # check if D
    if pos[3] > 0:
        if n <= perms(pos[0] , pos[1], pos[2], pos[3] - 1):
            return order(word + "D", [pos[0], pos[1], pos[2], pos[3] - 1], n)
        else:
            n -= perms(pos[0], pos[1], pos[2], pos[3] - 1)

#print(factorial(0))
print(order("", [a,b,c,d], n))
print("Time:", time.time() - start)

"""
b) 10

c) No. If every position has changed then the left-most position must have moved, meaning that in the nth position, 
the other positions where in reverse alphabetical order. Since the left-most position has changed, in the n+1st position,
all of the other positions are now in alphabetical order. The only way for all positions to change at once is if they are
in reverse alphabetical order. The only way for an order to be both alphabetical and reverse alphabetical is if there
is only 1 artist. If there was only 1 artist (ignoring the left-most position) there would be no n+2nd position after the
n+1st position. 
"""
