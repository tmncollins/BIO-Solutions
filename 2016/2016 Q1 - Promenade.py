
l, m, r, s = 1, 0, 0, 1

q = input()

curr = (l + r, m + s)
for item in q:
    if item == "L":
        l = curr[0]
        m = curr[1]
    else:
        r = curr[0]
        s = curr[1]
    curr = (l + r, m + s)
print(curr[0], "/", curr[1])

"""
b) 3/5 + 1/5 = 4/5 = LRRR
c) 0 Rs, 999,999 Ls
d) No. A negative fraction needs a negative numerator or denominator. The sum of positive numbers is always positive.
The promenades always add positive numbers so a negative numerator or denominator is never produced
"""
