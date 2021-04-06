import time
import math

word = input()
s, p = list(map(int, input().split()))

start = time.time()

def wordToList(word):
    return [word.count("A"), word.count("B"), word.count("C"), word.count("D"), word.count("E")]


def combine(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c


def rewrite(word=str, n=1):
    for i in range(n):
        word = word.replace("E", "EE").replace("C", "Cd").replace("D", "DC").replace("B", "aB").replace("A", "B").replace("a", "A").replace("d", "D")
    return word


def getLen(word, n):
    for i in range(n):
        word = nextLen(word)
    return word

def nextLen(word):
    a = word[1]
    b = word[0] + word[1]
    c = word[2] + word[3]
    d = word[2] + word[3]
    e = word[4] * 2
    return [a,b,c,d,e]


def func(word, count, s, p, c):
#    print(c)
#    print(word, count, s)
    if s == 0:
#        print(word)
#        print(p-sum(count))
        return combine(count, wordToList(word[:p-sum(count)]))
    tot = sum(getLen(count, s))
    for i in range(1, len(word)+1):
        curr = getLen(wordToList(word[:i]), s)
        if tot + sum(curr) >= p:
#            print("curr", curr)
            # all this can be handled numerically
            i -= 1
#            print(word[i:i+c], i+c, i)
            return func(rewrite(word[i:i+c], 1), combine(getLen(count, 1), getLen(wordToList(word[:i]), 1)), s-1, p, c+1)
    return combine(count,getLen(wordToList(word), s))

ans = func(word, [0,0,0,0,0], s, p, 2)
for item in ans:
    print(item, end=" ")
print()

print("Time:", time.time() - start)

"""
b) ABBABBABABBABBABABBABABBABBABABBAB, 34 (starting A)
   256 (starting C)
   CDDCDCCDDCCDCDDCDCCDCDDCCDDCDCCDDCCDCDDCCDDCDCCDCDDCDCCDDCCDCDDCDCCDCDDCCDDCDCCDCDDCDCCDDCCDCDDCCDDCDCCDDCCDCDDCDCCDCDDCCDDCDCCDDCCDCDDCCDDCDCCDCDDCDCCDDCCDCDDCCDDCDCCDDCCDCDDCDCCDCDDCCDDCDCCDCDDCDCCDDCCDCDDCDCCDCDDCCDDCDCCDDCCDCDDCCDDCDCCDCDDCDCCDDCCDCDDC

c) No. Every C is generated from either a D or a C in the previous string. After each rewriting, every C is replaced with
a C followed by a D and every D is replaced with a D followed by a C. Thus, every C must be adjacent to a D (either before
or after). If there are 2 Cs next to each other then the first C must follow a D and the second C must be followed by a D
So there can never be more than 2 Cs next to each other.

d) A -> AA
   B -> A
"""


