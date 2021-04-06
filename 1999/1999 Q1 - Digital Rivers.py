import time

def generateRiver(n, l):
    river = set()
    for i in range(l):
        river.add(n)
        n +=  sum(list(map(int, list(str(n)))))
    return river

def nextRiver(n):
    return n + sum(list(map(int, list(str(n)))))

maxL = 9999

n = int(input())

start = time.time()

river1 = generateRiver(1,maxL)
river3 = generateRiver(3,maxL)
river9 = generateRiver(9,maxL)

while True:
    if n in river1:
        print("First meets river 1 at", n)
        break
    if n in river3:
        print("First meets river 3 at", n)
        break
    if n in river9:
        print("First meets river 9 at", n)
        break
    n = nextRiver(n)

print("Time:", time.time() - start)

"""
b) 416
"""

def b(n):
    rivers = []
    for i in range(n*5):
        rivers.append(generateRiver(i, 999))
    i = 8
    while True:
        c = 0
#        print(i)
        for river in rivers:
            if i in river: c += 1
        if c >= 100:
            return i
        i += 1
print(b(100))
