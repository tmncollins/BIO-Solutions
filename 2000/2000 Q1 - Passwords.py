import re

word = input()

def valid(word):
    for i in range(len(word)-1):
        for j in range(i+1, len(word)):
#            print(word[i:j])
            if len(re.findall(r"(" + word[i:j] + word[i:j] + r")+", word)) > 0: return False
    return True

if valid(word):
    print("Accepted")
else:
    print("Rejected")

"""
b) 7 letters: ABACABA
"""