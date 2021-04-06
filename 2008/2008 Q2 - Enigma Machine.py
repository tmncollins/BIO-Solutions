from collections import deque

rotor1 = deque([0, 2, 3, 3])
rotor2 = deque([0, 1, 3, 0])
botor1 = deque([0, 1, 1, 2])
reflector = {0:3, 1:2, 2:1, 3:0}
letters = list("ABCD")

n = int(input())

rotor1.rotate(n % 4)
botor1.rotate(n % 4)
rotor2.rotate((n//4) % 4)

text = input()

for letter in text:
    q = letters.index(letter)
    q = (q + rotor1[q]) % 4
    q = (q + rotor2[q]) % 4
    q = reflector[q]
    q = (q + rotor2[q]) % 4
    q = (q + botor1[q]) % 4
    print(letters[q], end="")

    # rotate

    n += 1
    rotor1.rotate(1)
    botor1.rotate(1)
    if n % 4 == 0:
        rotor2.rotate(1)

"""
b) BCBCDB

c) 

d) No. Each port is connected to one wire, which is connect to a port on the other side. Therefore each letter is 
connected to exactly one other letter and because they are wired, the wirings go both ways. A letter is encrypted to 
the letter it is wired to. So if A was coded to B, then B would have to be coded to A. 
"""