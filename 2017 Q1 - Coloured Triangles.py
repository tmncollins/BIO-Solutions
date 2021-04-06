row = list(input())

def triangle(row, size):
    while len(row) > size:
        newRow = []
        for i in range(len(row) - 1):
            if row[i] == row[i+1]: newRow.append(row[i])
            else:
                colours = [row[i], row[i+1]]
                if "G" not in colours: newRow.append("G")
                elif "B" not in colours: newRow.append("B")
                elif "R" not in colours: newRow.append("R")
        row = list(newRow)
    return row[0]

print(triangle(row, 1))
"""
b) there are 3
            RRRBBGGRG
            BGBRGBRGR
            GBGGRRBBB

c) There is only 1 way. Given a complete row, there are 3 different options for the row directly above, but only 1 option
   for each of the rows below. However, if 1 value in the row directly above is known, there is only 1 option for that row.
   If 1 colour in each row is known, then the bottom row must be fully known as it only contains 1 value. Therefore, 
   each row can be completed sequentially from the bottom.
   
d) Any value of the form 3^k + 1 as there are 3 possible values and the 2nd row must contain 3^k numbers?
   e.g. 10
   

d)

"""
