from collections import deque
import time
tape = deque([0 for i in range(1000000)])
state = 1

n = int(input())
states = [input().split() for i in range(n)]
m = int(input())

start = time.time()


for p in range(m):
    info = states[state - 1][tape[0]]
    tape[0] = int(info[0])
    if info[1] == "L": tape.rotate(1)
    else: tape.rotate(-1)
    state = int(info[2])
    if state == 0: break

# print out tape section
tape.rotate(3)
for i in range(7):
    print(tape.popleft(), end="")
print()
print(p+1)
print("Time:", time.time() - start)


"""
b) n+m 1s in a row (test it with a range of ns and ms to see) 
e.g. [1 for i in range(4)] + [0] + [1 for i in range(5)]

c)
2
1L2 1R2
1R1 1L0

d) No. A special rule is only necessary if both machines are attempting to write to the same cell. If the start machines
are a odd number of cells apart (i.e. adjacent) they will always be an odd number of spaces apart. This is because each
turn the machines move to an adjacent cell, and so must always be an odd number of spaces apart. 

"""