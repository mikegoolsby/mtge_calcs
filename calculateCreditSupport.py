def calculateCreditSupport():

    raw_input = (input("enter suboordinate tranche balances separated by a space: "))
    reserve_bal = int(input("enter reserve balance: "))
    
    tranche_bal = raw_input.split()

    for i in range(len(tranche_bal)):
        tranche_bal[i] = int(tranche_bal[i])


    tranche_sums = sum(tranche_bal)

    group_bal = int(input("enter group balance: "))

    collat_bal = int(input("enter overall collateral balance: "))

    oc = (collat_bal - group_bal) / collat_bal

    oc_dollar = oc * collat_bal

    print("\n")
    return print((reserve_bal + tranche_sums + oc_dollar) / collat_bal)

calculateCreditSupport()
