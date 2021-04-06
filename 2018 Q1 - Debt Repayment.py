from math import ceil


interest, repayment = list(map(int, input().split()))

def payOffDebt(interest, repayment):
    debt = 100 * 100
    paid = 0

    interest /= 100
    repayment /= 100
    numPayments = 0
    lastDebt = debt

    while debt:
    #    print(debt, interest, repayment)
        debt += debt * interest
        debt = ceil(debt)
        pay = min(debt, max(debt * repayment, 5000))
        pay = ceil(pay)
        debt -= pay
        debt = ceil(debt)
        paid += pay
        numPayments += 1

        if debt >= lastDebt: return 0
        lastDebt = debt


    return paid / 100

print(payOffDebt(interest, repayment))
#print(numPayments)

"""
b) 5

c) 96% interest, 49% repayment, gives 107296.43 repaid 

"""

def c():
    largest = 0
    ans = (0, 0)
    for i in range(0,100):
        print(i)
        for r in range(1,100):
            tot = payOffDebt(i, r)
#            print(tot, i, r)
            if tot > largest:
                largest = tot
                ans = (i,r)
    print(ans[0], ans[1])

#c()

