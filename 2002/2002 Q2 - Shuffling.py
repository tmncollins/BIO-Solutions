import time
data = input()
start = time.time()

def expand(N):
    ans = ""
    n = list(N)
    while len(n) > 0:
        look = n.pop(0)
        if look in list("bio"): ans += look
        else:
            look = int(look)
            b = 0
            c = 0
            info = ""
            while b > 0 or c == 0:
                info += n[c]
                if n[c] == ")": b -= 1
                elif n[c] == "(": b += 1
                c += 1
            if info[0] == "(":
                info = info[1:-1]
            ans += look * info
            n = n[c:]

    return ans

def expandFully(data):
    while True:
        new = expand(data)
        if new == data: return data
        data = new

data = expandFully(data)
#print(data)

end = 8
cards = [i+1 for i in range(end)]

for item in data:
    if item == "b":
        c = cards.pop(0)
        cards.append(c)
    else:
        a = cards[:end//2]
        b = cards[end//2:]
        d = []
        if item == "o":
            for i in range(end//2):
                d.append(a[i])
                d.append(b[i])
        else:
            for i in range(end//2):
                d.append(b[i])
                d.append(a[i])
        cards = list(d)
#    print(cards)

for item in cards: print(item, end=" ")
print()
print("Time:", time.time() - start)

"""
b) 12 17 2 7 13 18 3 8 14 19 4 9 15 20 5 10 16 1 6 11
c) 8 breaks, 6 in shuffles, 3 out shuffles
d) Yes, it is always possible to restore a deck to its original state using only in riffles
   For an even sized deck, all cards change position, for an odd sized deck the last card never moves
   The in shuffle always changes the ordering, and there are only a finite number of possible orderings,
   thus the deck must always return to its original state.
   Each in riffle shuffle on a unique deck gives creates a unique deck and so each ordering can only be created by
   riffle shuffling a certain unique ordering. Therefore, a circular loop of orderings is created and the first ordering
   that is returned to is the original state.
"""