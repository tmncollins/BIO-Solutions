from functools import lru_cache

def score_word(word):
    global ALPHA
    s = 0
    for i in word:
        s += ALPHA.index(i) + 1
    return s

@lru_cache(maxsize=None)
def count_words(score, number):
    if score < 0: return 0
    if score == 0: return 1
    ans = 0
    for i in range(min(score, 26)):
        j = i+1
        if j != number:
            ans += count_words(score - j, j)
    return ans

def get_word(n, score):
    word = ""
    n -= 1
    s = 0
    last = -1
    while s < score:
        for i in range(26):
            j = i+1
            if j == last: continue
            x = count_words(score - s - j, j)
            if n < x:
                s += j
                last = j
                word += ALPHA[i]
                break
            n -= x
    return word

def get_pos(word):
    global ALPHA

    pos = 1
    last = -1
    score = score_word(word)
    for l in word:
        for j in range(ALPHA.index(l)):
            i = j+1
            if i != last:
#                print(i, score-i, count_words(score-i, i))
                pos += count_words(score-i, i)
        j = ALPHA.index(l) + 1
        score -= j
        last = j
#        print(pos)
    return pos


ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

word = input()
print(get_pos(word))
print(score_word(word))
print(get_word(get_pos(word), score_word(word)))

"""
b) ABABAB
c) 954658
d)
The longest word with a score of 54 is either AB * 18 or BA * 18, which have 36 letters
The word that follows AB * 18 is ABABABABABABABABABABABABABABABABABC, which has 35 letters
The word that follows BA * 18 is BABABABABABABABABABABABABABABABABAC, which has 35 letters
The word that precedes BA * 18 is AZYB, which has 4 letters, giving a difference of 32
To achieve a better difference we either need a longer longest word (which there isn't) or a shorter word to be 
adjacent to. 
Several 3 letter words exist (e.g. CYZ) brute forcing these gives a difference of no greater than 31
        e.g. CZY and DABABABABABABABABABABABABABABABACA
No 2 or 1 letter words exist.
Thus, this difference of 32 is the greatest and only occurs once.


"""
"""
# part b
print(get_word(1, score_word("ACE")))

# part c
print(count_words(26, -1))

# part d brute force part
MAX_LEN = 0
end = count_words(54, -1)
for a in range(26):
    for b in range(26):
        for c in range(26):
            if a == b or b == c or a == c: continue
            total = a + b + c + 3
            if total != 54: continue
            word = ALPHA[a] + ALPHA[b] + ALPHA[c]
            i = get_pos(word)
            if i > 1:
                word_left = get_word(i-1, 54)
                if len(word_left) - 3 > MAX_LEN:
                    MAX_LEN = len(word_left) - 3
                    print(word, word_left, MAX_LEN)
            if i < end:
                word_left = get_word(i+1, 54)
                if len(word_left) - 3 > MAX_LEN:
                    MAX_LEN = len(word_left) - 3
                    print(word, word_left, MAX_LEN)
print("MAX_LEN", MAX_LEN)
"""
