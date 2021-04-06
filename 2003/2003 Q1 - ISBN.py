isbn = list(input())

def isbnsolve(isbn):
    tot = 0
    index = 0
    for i in range(len(isbn)):
        item = isbn[i]
        if item != "?":
            if item == "X":
                item = 10
            else:
                item = int(item)
            tot += item * (10-i)
        else:
            index = (10-i)

    done = False
    for j in range(10):
        if ((j * index) + tot) % 11 == 0:
            return j
            done = True
            break

    if not done:
        return "X"

print(isbnsolve(isbn))

# part c
bn = "3201014525"
pos = set()
for i in range(10):
    for j in range(10):
        if i < j:
            a = list(bn)
            b = a[i]
            c = a[j]
            a[j] = b
            a[i] = c
            ans = a[-1]
            a[-1] = "?"
            x = "".join(a)
            print(x, ans, isbnsolve(x))
            if str(isbnsolve(x)) == ans:
                pos.add(x)
print(pos)



"""
b) 3540678654, 9514451570
c) 2301014525, 3401012525, 0201314525, 3200114525
"""



