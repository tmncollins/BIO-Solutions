h,m = list(map(int, input().replace(":", " ").split()))
hours = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
minutes = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
           "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty",
           "Twenty-one", "Twenty-two", "Twenty-three", "Twenty-four", "Twenty-five", "Twenty-six", "Twenty-seven", "Twenty-eight",
           "Twenty-nine"]
if m < 30:
    h = hours[h - 1]
    if m == 0:
        print(minutes[hours.index(h)] + " o'clock")
    elif m == 15:
        print("Quarter past " + h)
    elif m == 1:
        print("One minute past " + h)
    else:
        print(minutes[m-1] + " minutes past " + h)
elif m == 30:
    print("Half past " + h)
else:
    h = hours[h%len(hours)]
    m = 60 - m
    if m == 15:
        print("Quarter to " + h)
    elif m == 1:
        print("One minute to " + h)
    else:
        print(minutes[m-1] + " minutes to " + h)

"""
b) 11:23, 11:27, 11:28, 12:23, 12:27, 12:28
Longest forms will be x minutes past y, why x and y are maximum lengths.
x = 23, 27, 28
y = 11, 12

"""
