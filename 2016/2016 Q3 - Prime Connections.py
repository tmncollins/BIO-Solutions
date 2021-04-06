import time

primes = set()
notPrimes = set()

def isPrime(n):
    for i in range(2, int(n**0.5) +1):
        if n % i == 0: return False
    return True

ppaths = set()
pdist = dict()
qdist = dict()
qpaths = set()

l, p, q = list(map(int, input().split()))

start = time.time()

ppending = [(p, 1)]
qpending = [(q, 1)]
pdist[p] = 1
qdist[q] = 1


# start from p and q
while True:
    # start with p
    item = ppending.pop(0)
#    print(item)
    exp = 0
    while True:
        c = 0
        v = item[0] - 2**exp
        if v > 1:
            if v in primes and v not in pdist:
                ppending.append((v, item[1] + 1))
                ppaths.add(v)
                pdist[v] = item[1] + 1
            elif v in notPrimes:
                pass
            else:
                p = isPrime(v)
                if p and v not in pdist:
                    primes.add(v)
                    ppending.append((v, item[1] + 1))
                    ppaths.add(v)
                    pdist[v] = item[1] + 1
                else: notPrimes.add(v)
        else:
            c += 1
        v = item[0] + 2**exp
        if v <= l:
            if v in primes and v not in pdist:
                ppending.append((v, item[1] + 1))
                ppaths.add(v)
                pdist[v] = item[1] + 1
            elif v in notPrimes:
                pass
            else:
                p = isPrime(v)
                if p and v not in pdist:
                    primes.add(v)
                    ppending.append((v, item[1] + 1))
                    ppaths.add(v)
                    pdist[v] = item[1] + 1
                else: notPrimes.add(v)
        else:
            c += 1

        if c == 2: break

        exp += 1

    # now q
    # start with p
    item = qpending.pop(0)
    exp = 0
    while True:
        c = 0
        v = item[0] - 2 ** exp
        if v > 1:
            if v in primes and v not in qdist:
                qpending.append((v, item[1] + 1))
                qpaths.add(v)
                qdist[v] = item[1] + 1
            elif v in notPrimes:
                pass
            else:
                p = isPrime(v)
                if p and v not in qdist:
                    primes.add(v)
                    qpending.append((v, item[1] + 1))
                    qpaths.add(v)
                    qdist[v] = item[1] + 1
                else:
                    notPrimes.add(v)
        else:
            c += 1
        v = item[0] + 2 ** exp
        if v <= l:
            if v in primes and v not in qdist:
                qpending.append((v, item[1] + 1))
                qpaths.add(v)
                qdist[v] = item[1] + 1
            elif v in notPrimes:
                pass
            else:
                p = isPrime(v)
                if p and v not in qdist:
                    primes.add(v)
                    qpending.append((v, item[1] + 1))
                    qpaths.add(v)
                    qdist[v] = item[1] + 1
                else:
                    notPrimes.add(v)
        else:
            c += 1

        if c == 2: break
        exp += 1

    # check
    if len(ppaths.intersection(qpaths)) > 0: break


#print(pdist, qdist)

if q in pdist:
    print(pdist[q])
elif p in qdist:
    print(qdist[p])
else:
    shortest = float("inf")
    for item in ppaths.intersection(qpaths):
        d = pdist[item] + qdist[item] - 1
    #    print(item, d)
        if d < shortest: shortest = d
    print(shortest)
    print("Time:", time.time() - start)

"""
b) 12
c) 41041
d) As there are 2 different paths with the same number of primes in between p and q, the shortest 
path between p and q must be less than n
"""

"""
Code for part c:

paths = set()

pending = [[2]]

primes = [2]

for i in range(3, 250000):
    prime = True
    for p in primes:
        if p > i**0.5: break
        if i % p == 0:
            prime = False
            break
    if prime: primes.append(i)
pairs = set()

print("Got primes")

for a in primes:
    if primes.index(a) % 100 == 0:
        print("At: " + str(primes.index(a)) + " out of " + str(len(primes)))
    exp = 0
    while True:
        c = 0
        v = a + 2**exp
        if v > 250000: c+= 1
        elif v in primes:
            pairs.add((v,a))
        v = a -2**exp
        if v < 1: c += 1
        elif v in primes:
            pairs.add((v,a))
        if c == 2: break
        exp += 1

print(len(pairs), len(pairs) / 2)

"""
