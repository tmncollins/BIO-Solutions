trees = set()
farmer = (0,0)
fdirection = "U"
pigs = (0,0)
fpigs = "U"

def boardToScreen(x,y):
    x += 1
    y = 10 - y
    return x,y

def screenToBoard(x,y):
    x -= 1
    y = 10 - y
    return x,y

def output():
    for y in range(10):
        for x in range(10):
            if (x,y) in trees:
                print("*", end="")
            elif (x,y) == farmer:
                if (x,y) == pigs: print("+", end="")
                else: print("F", end="")
            elif (x,y) == pigs:
                print("P", end="")
            else:
                print(".", end="")
        print()
    print()

def offboard(pos):
    x = pos[0]
    y = pos[1]
    return x < 0 or y < 0 or x >= 10 or y >= 10

def move(x,y,d):
    directions = {"U":(0,-1), "L":(-1,0), "R":(1,0), "D":(0,1)}
    rotate = {"U":"R", "R":"D", "D":"L", "L":"U"}
    dir = directions[d]
    next = (x + dir[0], y + dir[1])
    if next in trees or offboard(next):
        d = rotate[d]
        return (x, y), d
    return next, d

x,y = list(map(int, input().split()))
pigs = screenToBoard(x,y)
x,y = list(map(int, input().split()))
farmer = screenToBoard(x,y)

output()

m = 0
while True:
    val = input()
    if val == "X": break

    v, n = val.split()
    n = int(n)

    if v == "T":
        for i in range(n):
            x,y = list(map(int, input().split()))
            trees.add(screenToBoard(x,y))

    if v == "M":
        for i in range(n):
            m += 1

            # move farmer and pigs
            farmer, fdirection = move(farmer[0], farmer[1], fdirection)
            pigs, fpigs = move(pigs[0], pigs[1], fpigs)

            # check if pigs have been caught
            if farmer == pigs:
                x,y = boardToScreen(farmer[0], farmer[1])
                print("Farmer and pigs meet on move " + str(m) + " at (" + str(x) + "," + str(y) + ")")

    output()

"""
b) 1
   81

c) 19 moves.
Start at (1,10) and (1,9), both facing right

d) Yes, we will always be able to determine whether the pigs and the farmer meet. During the simulation, if it returns
to a state that has been seen before, the simulation will continue in an infinite repetition of states that have been 
seen before. Once all possible states have been simulated, we will know whether or not the pigs and the farmer will meet
and, if so, where. As the simulation only has a finite number of states, it must eventually reach a state that has already
been seen.
"""

