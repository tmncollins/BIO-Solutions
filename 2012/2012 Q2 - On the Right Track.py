import time

network = {"DA":["E","F"], "CB":["G","H"], "BC":["I","J"], "AD":["K","L"], "AE":["M","N"], "AF":["N","O"], "BG":["O","P"],
           "BH":["P","Q"], "CI":["Q","R"], "CJ":["R","S"], "DK":["S","T"], "DL":["T","M"], "VU":["M","N"], "UV":["O","P"],
           "WX":["S","T"], "XW":["Q","R"], "EM":["U"], "EN":["U"], "FN":["U"], "FO":["V"], "GO":["V"], "GP":["V"], "HP":["V"],
           "HQ":["W"], "IQ":["W"], "IR":["W"], "JR":["W"], "JS":["X"], "KS":["X"], "KT":["X"], "LT":["X"], "LM":["U"],
           "MU":["V"], "NU":["V"], "OV":["U"], "PV":["U"], "QW":["X"], "RW":["X"], "SX":["W"], "TX":["W"], "UM":["L","E"],
           "UN":"EF", "VO":"FG", "VP":"GH", "WQ":"HI", "WR":"IJ", "XS":"JK", "XT":"KL", "ME":"A", "NE":"A", "NF":"A", "OF":"A",
           "OG":"B", "PG":"B", "PH":"B", "QH":"B", "QI":"C", "RI":"C", "RJ":"C", "SJ":"C", "SK":"D", "TK":"D", "TL":"D", "ML":"D",
           "EA":"D", "FA":"D", "GB":"C", "HB":"C", "IC":"B", "JC":"B", "KD":"A", "LD":"A"}

flipflop = list(input())
train = list(input())
n = int(input())
start = time.time()

for _ in range(n):
    s,e = train
    t = "".join(train)
    train = e + network[t][0]
    if e in flipflop:
        network[t] = network[t][::-1]
    else:
        if len(network[t]) == 1:
            reverse = network[t][0] + e
            # switch if not already facing
            if network[reverse][0] != s:
                network[reverse] = network[reverse][::-1]
#            print("Changed", reverse, "to", network[reverse])

print(train)

print("Time:", time.time() - start)

"""
b) V,U,M,L,D,A,E,M,U,V,P

c) After the train leaves P->V it will enter an infinite loop of 8 points, irrelevant of type of the points or how they
are set. However, the exact location of the cycle is unknown without this information as there are 2 possible cycles it 
could enter, as the rail layout is symmetrical:

d) 
"""