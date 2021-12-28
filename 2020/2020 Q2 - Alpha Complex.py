from collections import defaultdict
from time import time
from copy import deepcopy

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rooms = defaultdict(list)

plan, p, q = input().split()
plan = list(plan)
p = int(p)
q = int(q)
n = len(plan) + 2

start = time()

# generate graph from plan
# list of letters left to choose
to_choose = list(alphabet[:n])
for i in range(n - 2):
    for letter in to_choose:
        if letter not in plan:
            # connect these rooms
            rooms[letter].append(plan[0])
            rooms[plan[0]].append(letter)
            # update lists
            plan.pop(0)
            to_choose.remove(letter)
            break

# connect the two remaining rooms
rooms[to_choose[0]].append(to_choose[1])
rooms[to_choose[1]].append(to_choose[0])

# output graph
for i in range(n):
    output = ""
    rooms[alphabet[i]] = sorted(rooms[alphabet[i]])

    for room in rooms[alphabet[i]]:
        output += room

    print(output)

# main code

position = "A"
# initialise dictionaries
visited_odd = defaultdict(bool)
exited_odd = defaultdict(bool)

def move():
    global position, visited_odd, exited_odd

    # we have visited this room one more time
    visited_odd[position] = not visited_odd[position]

    if visited_odd[position]:
        # through first exit alphabetically
        # update exit information
        next_room = rooms[position][0]
        exited_odd[position + next_room] = not exited_odd[position + next_room]
        # update position
        position = next_room

    else:
        # find first exit alphabetically that has been
        # left through an odd number of times
        for i in range(len(rooms[position])):
            if exited_odd[position + rooms[position][i]]:
                # is this the last room?
                if i < len(rooms[position]) - 1:
                    i += 1
                # update exit information
                next_room = rooms[position][i]
                exited_odd[position + next_room] = not exited_odd[position + next_room]
                # update position
                position = next_room

                break



for _ in range(p):
#    print(_)
    move()

print(position, end="")

seen = []

for i in range(q - p):
#    print(i)
    if (position, visited_odd, exited_odd) in seen:
        index = seen.index((position, visited_odd, exited_odd))
        index += q - p - i
        index %= len(seen)
#        print(seen)
        position = seen[index][0]
        break
    else:
        seen.append((position, deepcopy(visited_odd), deepcopy(exited_odd)))
        move()

print(position)

print(time() - start)

"""
b) A 
   AAAA
   Letters in plan = Number of letters in complex - 2. As all rooms are connected only a A, the plan must only contain
   As

c) If the number of odd exits from the room is even, the room must have been visited an odd number of times. If it is odd,
the room must have been visited an even number of times. For example, the first time a spy is in a room, the number of 
odd exits is zero, which is even.

"""

