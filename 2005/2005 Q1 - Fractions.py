n = input()
q = len(n) - 2
n = int(n[2:])
b = 10 ** q
primes = [2]


def primeFactorise(n):
    ans = []
    while n not in primes:
        for prime in primes:
            if n % prime == 0:
                ans.append(prime)
                n /= prime
                break
    ans.append(int(n))
    return ans


def convertToFraction(a,b):

    for i in range(3, 10000):
        prime = True
        for p in primes:
            if p > i**0.5: break
            if i % p == 0:
                prime = False
                break
        if prime: primes.append(i)

    top = primeFactorise(n)
    bottom = primeFactorise(b)

    t = []
    #print(top, bottom)

    for item in top:
        if item in bottom:
            z = bottom.count(item)
            z -= 1
            bottom.remove(item)
    #        for i in range(z): bottom.append(item)
        else:
            t.append(item)

    #print(n, b)
    #print(t, bottom)

    numerator = 1
    denominator = 1
    for item in t: numerator *= item
    for item in bottom: denominator *= item

    return str(numerator) + " / " + str(denominator)
print(convertToFraction(n, b))

"""
b) 24 (Number of factors of 10000 excluding 1 

c) 0.9584
Greatest Product is Denominator: 625
Greatest Product of Numerator contains as many 9s as possible: 599
5*9*9*6*2*5 = 24300
"""

print("C!")
# code for c
best = 0
high = 0
for i in range(2, 10000):
    if i % 100 == 0:
        print(i)
        print(high, best)
    a = convertToFraction(i, 10**4)
    score = 1
    for j in a:
        if j in "0123456789":
            score *= int(j)
    if score > high:
        high = score
        best = i
print(high, best)