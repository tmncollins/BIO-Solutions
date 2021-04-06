from collections import deque

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def generateDial(n):
    letters = deque(alpha)
    dial = deque()
    while letters:
        letters.rotate(-(n-1))
        dial.append(letters.popleft())
    return dial

n,word = input().split()

dial = generateDial(int(n))
print("".join(list(dial)[:6]))

ans = ""
for letter in word:
    ans += list(dial)[alpha.index(letter)]
    dial.rotate(-1)

print(ans)

"""
b) LKBXIY

c) No. The nth letter of the word will be encrypted after n-1 rotations of the dial. The nth letter of the alphabet
will thus be encrypted as the 2i-1st letter on the second dial. It follows that the nth encrypted letter will always match the 
n+13th encrypted letter. As the letters repeat, only the letters on odd positions of the second dial will be expressed 
in the encrypted word, each appearing twice.

d) 1260
The letters within the word will return to the original letter in cycles. E.g. A -> B -> C -> A. To get the length of 
the longest cycle for the entire word, we must find a set of cycles that return a maximum longest cycle. As each letter 
must appear in a cycle, the lengths of the individual cycles must sum to 26. Cycles that are co-prime will give the
greatest total length. 
4 + 9 + 5 + 7 + 1 = 27
2 * 2 * 3 * 3 * 5 * 7 = 1260 
"""
