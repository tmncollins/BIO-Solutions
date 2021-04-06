a = int(input())
b = int(input())

def factors(n):
    f = set()
    for i in range(1,n//2+1):
        if n % i == 0:
            f.add(i)
            f.add(n//i)
    f.remove(n)
    return f

def amicable(a,b):
    A = sum(factors(a))
    B = sum(factors(b))
    if a == B and b == A:
        return True
    else:
        return False

if a != b and amicable(a,b):
    print("Amicable")
else:
    print("Not amicable")

"""
b) 220 284
"""

def b():
    for a in range(3,999):
        for b in range(3,999):
            if a != b:
                if amicable(a,b):
                    print(a,b)
#b()
