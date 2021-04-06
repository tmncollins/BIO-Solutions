baktun, katun, tun, uinal, kin = list(map(int, input().split()))

# calibrate to 1 1 2000
baktun -= 13
katun -= 20
tun -= 7
uinal -= 16
kin -= 3

# convert to kins
katun += 20 * baktun
tun += 20 * katun
uinal += 18 * tun
kin += 20 * uinal

#print(kin % 7)
# find year
year = 2000
while True:
    days = 365
    if year % 100 == 0:
        if year % 400 == 0: days += 1
    elif year % 4 == 0: days += 1
    if kin < days:
        break
    year += 1
    kin -= days

# find month
m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year % 100 == 0:
    if year % 400 == 0: m[2] += 1
elif year % 4 == 0:
    m[2] += 1

month = 1
while True:
    if kin < m[month]:
        break
    kin -= m[month]
    month += 1

print(kin+1, month, year)

"""
b) 13 20 7 17 14, 13 20 8 16 9

c) 2,880,000 days
   1012737 days after 1 1 2000 (Sat) so 5 days after Sat so it is a Thursday
"""