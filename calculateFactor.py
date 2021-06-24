def calculateFactor():
    orig_bal = int(input("original balance: "))
    curr_bal = float(input("current balance: "))

    factor = curr_bal / orig_bal

    print("factor = {}".format(factor))

calculateFactor()
