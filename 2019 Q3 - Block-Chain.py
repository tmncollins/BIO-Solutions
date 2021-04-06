import time
from functools import lru_cache

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
l, p = input().split()
l = int(l)

start = time.time()

@lru_cache(maxsize=None)
def chains(length, smaller, middle, larger):
    if length >= 3: return 0
    if sum([smaller, middle, larger]) == 0: return 1
    ans = [0]
    if length == 1:
        for i in range(smaller):
            ans.append(chains(length, i, middle, larger + smaller - i - 1))
    else:
        for i in range(smaller):
            ans.append(chains(length, i, middle+smaller-i-1, larger))
    for i in range(middle):
        ans.append(chains(length, smaller, i, larger+middle-i-1))
    for i in range(larger):
        ans.append(chains(length + 1, smaller, middle+i, larger-i-1))
    return sum(ans)

def generateStart(l, p):
    r = list(alpha[:l])
    for item in p:
        r.remove(item)
    return r

def getSeconds(word):
    s = []
    for a in range(1,len(word)):
        if word[a] > min(word[:a]):
            s.append(word[a])
    return s

remaining = generateStart(l,p)
seconds = getSeconds(p)
length = 1 if len(seconds) == 0 else 2
smaller = 0
middle = 0
larger = 0
for item in remaining:
    if item < min(p):
        smaller += 1
    elif seconds and item < min(seconds):
        middle += 1
    else:
        larger += 1

print(chains(length, smaller, middle, larger))

print("Time:", time.time() - start)

"""
b) BOI, OBI, OIB, IBO, IOB

c) Both of the original block chains were in reverse alphabetical order. If the combined blocks chains were not a block 
chain then at least one of the original block chains must have contained 2 letters in alphabetical order. Thus neither 
of the original block chains could have had 2 letters in order as the combined block chain would have had at least 3 
letters in alphabetical order. The only way for no 2 letters to be in alphabetical order in a block chain is for the
block chain to be in reverse alphabetical order. This means that the resultant block chain only has a maximum of 2 
letters in alphabetical order: one from each of the original block chains.

d) ASRQPONMLKJIHGFEDCB
   RPSMJQHOFEDNLKICGBA
   
"""

def d(r, n, L):
    if len(r) == l: return r
    if n == 0: return r
    for a in alpha:
        if a in r: continue
        word = r + a
        remaining = generateStart(L, word)
        seconds = getSeconds(word)
        length = 1 if len(seconds) == 0 else 2
        smaller = 0
        middle = 0
        larger = 0
        for item in remaining:
            if item < min(word):
                smaller += 1
            elif seconds and item < min(seconds):
                middle += 1
            else:
                larger += 1
        m = chains(length, smaller, middle, larger)
        if n <= m:
            return d(word, n, L)
        n -= m

#print(d("", 1000000000, 19))
