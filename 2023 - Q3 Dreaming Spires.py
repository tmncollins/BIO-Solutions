from itertools import permutations
from _collections import deque

start = "-".join(input().split()).replace("0", "")
end = "-".join(input().split()).replace("0", "")

q = deque()
q.append((start, 0))

seen = set()

while q:
    curr, d = q.popleft()
#    print(curr, d)

    if curr == end:
        print(d)
        break

    curr = curr.split("-")

    for a in range(4):
        if curr[a] != "":
            for b in range(4):
                if a != b:
                    # move top from a to b
                    next_state = list(curr)
                    move = next_state[a][-1]
                    next_state[a] = next_state[a][:-1]
                    next_state[b] += move
                    next_state = "-".join(next_state)
                    if next_state not in seen:
                        seen.add(next_state)
                        q.append((next_state, d+1))

"""
b) ball arrangement is 1 1 2 0 balls on each peg in some order to give 9 possible moves. 
There are 4!/2! = 12 ways to arrange 1 1 2 0 and 4! = 24 ways of arranging the balls in each arrangement, 
giving 288 game states

check with code:

states_9 = set()

for item in permutations(("1", "1", "2", "0")):
    for perm in permutations(("1","2","3","4")):
        perm = "".join(perm)
        state = perm[:int(item[0])] + "-" + perm[int(item[0]):int(item[0]) + int(item[1])] + "-" + perm[int(item[0])+int(item[1]):int(item[0])+int(item[1])+int(item[2])] + "-" + perm[int(item[0])+int(item[1])+int(item[2]):]
        print(state)
        states_9.add(state)

print(len(states_9))

"""

"""
c) 73 after 2 moves; 375 after 4 moves

"""

def part_c(start, moves):
    q = deque()
    q.append((start, 0))

    seen = set()
    end = set()
    last = -1

    while q:
        curr, d = q.popleft()

        if d != last:
            last = d
            seen.clear()

        if d == moves:
            end.add(curr)
            continue

        curr = curr.split("-")

        for a in range(4):
            if curr[a] != "":
                for b in range(4):
                    if a != b:
                        # move top from a to b
                        next_state = list(curr)
                        move = next_state[a][-1]
                        next_state[a] = next_state[a][:-1]
                        next_state[b] += move
                        next_state = "-".join(next_state)
                        if next_state not in seen:
                            seen.add(next_state)
                            q.append((next_state, d+1))

    return end

c = part_c("1-2-3-4", 2)
print(c, len(c))


from itertools import combinations_with_replacement as combi
from functools import lru_cache

def part_d():

    @lru_cache(maxsize=None)
    def count_states(heights, balls=8, i=0):
#        print(heights, balls, i)
        if i >= len(heights):
            return balls == 0

        ans = 0
        for j in range(heights[i]+1):
            ans += count_states(heights, balls - j, i+1)
        return ans

    print(count_states((3,2,2,2), 4))

    for heights in combi([1,2,3,4,5,6,7,8], 8):
        x = count_states(heights)
        if x == 2023: print(heights)


part_d()

