n, m = list(map(int, input().split()))
from math import comb

def order(word, zeros, ones, n):
#    print(word)
    if ones == 0:
        return word + "0" * zeros
    if zeros == 0:
        return word + "1" * ones

    c = comb(zeros + ones - 1, ones)
    if n > c:
        n -= c
        word += "1"
        return order(word, zeros, ones - 1, n)
    else:
        word += "0"
        return order(word, zeros - 1, ones, n)


def getZeroes(n, ones):
    z = 0
    while True:
        if comb(ones - 1 + z, ones-1) >= n:
            break
        n -= comb(ones - 1 + z, ones-1)
        z += 1
    return z,n

def ans(n,m):
    if m == 0:
        return "0"
    z,n = getZeroes(n,m)
#    print(z, n)
    return order("1", z, m-1, n)

a = ans(n,m)

for i in range(len(a)):
    if i % 6 == 0 and i > 0: print(" ", end="")
    print(a[i], end="")
print()

"""
b) 10
   0
   11111
   111010 001100 00
   110100011000011111000
   
c) 62 

d) At most, m digits can change at once. When m is odd, moving from the final number containing (m-1)/2 ones to the next 
number changes all m digits. Similarly, when m is even, moving from the final number containing m/2 ones to the next number
also changes all m digits. 
"""

# pass a = 1000001, b = 11000001 for part c
def b(n, m, A=-1, B=-1):
    if n == 1: return "0"
    ones = 1
    i = 1
    c = 1

    while True:
        a = ans(i, ones)
        if a == A:
            start = c
        if a == B:
            return c - start - 1
        if len(a) <= m:
            c += 1
            i += 1
        else:
            ones += 1
            i = 1
#            print(ones)
        if c == n:
            return a

#print(b(n,m,"1000001", "11000001"))
