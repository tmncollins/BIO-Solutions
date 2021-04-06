from collections import defaultdict
# Modifer, Position
player1 = []
pos = 1
mod = 0
player2 = []

# dicts of positions and num edges and positions and winner
squares = defaultdict(int)
wins = defaultdict(int)
lines = defaultdict(list)

# Process input
line = list(map(int, input().split()))
player1 = [line[1], line[0]]
player2 = [line[3], line[2]]
t = line[4]

def canU(p):
    return p > 6
def canD(p):
    return p < 31
def canL(p):
    return not (p % 6 == 1)
def canR(p):
    return not (p % 6 == 0)

# each line it is a turn
player1turn = True
count = 0
while count < t:

    # update info
    if player1turn:
        player1[pos] += player1[mod]
        if player1[pos] > 36: player1[pos] -= 36
        p = player1[pos]
    else:
        player2[pos] += player2[mod]
        if player2[pos] > 36: player2[pos] -= 36
        p = player2[pos]

    # Process Move
#    print(player1turn)
    while True:
        if len(lines[p]) < 4:
            if player1turn:
                # clockwise
                if canU(p) and "u" not in lines[p]:
                    # Put line up
                    lines[p].append("u")
                    lines[p-6].append("d")
#                    print(p, p-6)
                    break
                elif canR(p) and "r" not in lines[p]:
                    # Put line right
                    lines[p].append("r")
                    lines[p + 1].append("l")
#                    print(p, p + 1)
                    break
                elif canD(p) and "d" not in lines[p]:
                    # Put line down
                    lines[p].append("d")
                    lines[p+6].append("u")
#                    print(p, p+6)
                    break
                elif canL(p) and "l" not in lines[p]:
                    # Put line left
                    lines[p].append("l")
                    lines[p - 1].append("r")
#                    print(p, p - 1)
                    break
            else:
                # anti-clockwise
                if canU(p) and "u" not in lines[p]:
                    # Put line up
                    lines[p].append("u")
                    lines[p-6].append("d")
#                    print(p, p-6)
                    break
                elif canL(p) and "l" not in lines[p]:
                    # Put line left
                    lines[p].append("l")
                    lines[p - 1].append("r")
#                    print(p, p - 1)
                    break
                elif canD(p) and "d" not in lines[p]:
                    # Put line down
                    lines[p].append("d")
                    lines[p+6].append("u")
#                    print(p, p+6)
                    break
                elif canR(p) and "r" not in lines[p]:
                    # Put line right
                    lines[p].append("r")
                    lines[p + 1].append("l")
#                    print(p, p + 1)
                    break
        p += 1
        if p > 36: p -= 36

    if player1turn: player1[pos] = p
    else: player2[pos] = p

    # Check if any boxes have been captured
    hasCaptured = False
    for y in range(5):
        for x in range(5):
            if wins[(x,y)] == 0:
                # box is currently uncaptured
                topleft = y*6 + x + 1
                topright = y*6 + x + 2
                bottomleft = (y+1)*6 + x + 1
                bottomright = (y+1)*6 + x + 2
                if "d" in lines[topleft] and "l" in lines[topright] and "u" in lines[bottomright] and "r" in lines[bottomleft]:
                    # captured!
                    wins[(x,y)] = 1 if player1turn else 2
#                    print("player" + str(wins[(x,y)]) + "captured box " + str(x) + ", " + str(y))
                    hasCaptured = True

    if not hasCaptured:
        player1turn = not player1turn
    count += 1

count1 =0
count2=0
for y in range(5):
    for x in range(5):
        if wins[(x,y)] == 0:
            print("*", end="")
        elif wins[(x,y)] == 1:
            print("X", end="")
            count1 += 1
        else:
            print("O", end="")
            count2 += 1
    print()

print(count1, count2)


