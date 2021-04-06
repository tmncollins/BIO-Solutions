from collections import deque, defaultdict
from functools import lru_cache
import time

VALUES = list("A23456789TJQK")
CLUBS = [i + "C" for i in VALUES]
HEARTS = [i + "H" for i in VALUES]
SPADES = [i + "S" for i in VALUES]
DIAMONDS = [i + "D" for i in VALUES]
CARDS = CLUBS + HEARTS + SPADES + DIAMONDS

order = list(map(int, input().split()))
startTime = time.time()

piles = []

def printPiles():
    global piles
    for pile in piles:
        print(pile[0], end=" ")
    print()

def size(arr):
    size = 0
    for item in arr:
        size += len(item)
    return size

def reset():
    global piles, CARDS
    cards = deque(CARDS)
    piles = []
    c = 0
    while cards:
        cards.rotate(-(order[c%len(order)]-1))
        piles.append(cards.popleft())
        c += 1

@lru_cache(maxsize=None)
def validMoves(piles):
    moves = defaultdict(list)
    for i in range(len(piles)):
        for j in range(len(piles)):
            if i == j-1 or i == j-3:
                if piles[i][0] == piles[j][0] or piles[i][1] == piles[j][1]:
                    moves[j].append(i)
    return moves

reset()
#print(piles)
print(piles[0], piles[-1])

# strategy 1
reset()
while len(piles) > 1:
    moves = validMoves(tuple(piles))
    if len(moves) == 0: break
    p = max(moves.keys())
    q = piles[max(moves[p])]
    p = piles.pop(p)
    q = piles.index(q)
    piles[q] = p
print(len(piles), piles[0])

# strategy 2
reset()
while len(piles) > 1:
    moves = validMoves(tuple(piles))
    if len(moves) == 0: break
    largest = 0
    l = 0
    for start in sorted(moves.keys()):
        for end in sorted(moves[start]):
            if len(piles[start]) + len(piles[end]) >= largest:
                largest = len(piles[start]) + len(piles[end])
                l = (start, end)
    q = piles[l[1]]
    p = piles.pop(l[0])
    q = piles.index(q)
    piles[q] = p
print(len(piles), piles[0])

# strategy 3
reset()
while len(piles) > 1:
    moves = validMoves(tuple(piles))
    if len(moves) == 0: break
    largest = 0
    l = 0
    for start in sorted(moves.keys()):
        for end in sorted(moves[start]):
            # check how many moves this move will leave
            pil = list(piles)
            q = pil[end]
            p = pil.pop(start)
            q = pil.index(q)
            pil[q] = p
            m = size(validMoves(tuple(pil)).values())
#            print(m, largest)
            if m >= largest:
                largest = m
                l = (start, end)
    q = piles[l[1]]
    p = piles.pop(l[0])
    q = piles.index(q)
    piles[q] = p
#    printPiles()
print(len(piles), piles[0])

print("Time:", time.time() - startTime)



"""
b) 2C, KC, 3H, KH, 4S, KS, 2D, KD, 4C, 2H, 7H, 5S

c) 531434
   998284

d) Yes. The first pile that was moved in the first game, only contained 1 card. If a pile with only 1 card is moved onto
another pile then that card and the card beneath it will be adjacent in the second game. If the tiles piles were combined
then the 1 card was a math for the top card of the pile it was moved onto so the 2 adjacent cards will also match and 
so they can be combined in the second game. 

"""


def c():
    global CARDS
    n = 10
    seen = set()
    for a in range(0,n):
        for b in range(0,n):
            for c in range(0,n):
                for d in range(0,n):
                    for e in range(0,n):
                        for f in range(0,n):
                            cards = deque(CARDS)
                            ca = set()
                            cards.rotate(-a)
                            ca.add(cards.popleft())
                            cards.rotate(-b)
                            ca.add(cards.popleft())
                            cards.rotate(-c)
                            ca.add(cards.popleft())
                            cards.rotate(-d)
                            ca.add(cards.popleft())
                            cards.rotate(-e)
                            ca.add(cards.popleft())
                            cards.rotate(-f)
                            ca.add(cards.popleft())
                            ca = tuple(sorted(ca))
                            if ca not in seen:
                                seen.add(ca)
    print(len(seen))
#c()
