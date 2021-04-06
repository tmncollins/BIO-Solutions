from collections import deque
n = int(input())
w = int(input())

circle = deque([i+1 for i in range(n)])

def game(circle, w, clock=True):
    if not clock: circle.rotate(-1)
    while len(circle) > 1:
        if clock:
            circle.rotate(-w)
            q = circle.pop()
        else:
            circle.rotate((w-1))
            q = circle.pop()
#        print(q)
    return circle[0]
print(game(deque(circle), w))

# part c
"""
for i in range(1,1000):
    circle = deque([i + 1 for i in range(100)])
    circle2 = deque([i + 1 for i in range(100)])

    if game(deque(circle), i) == game(deque(circle2), i, False):
        print(i)
"""



"""
b) 5, 10, 3, 9, 4, 12, 8, 7, 11, 2, 6, 1
c) 64 words

"""
