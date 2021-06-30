def calculateOAD():
    price = float(input('enter price: '))
    price_under_25 = float(input('enter price -25bps: '))
    price_above_25 = float(input('enter price +25bps: '))
    accrued = float(input('enter accrued from OAD or BQNT App: '))

    OAD = 100*(price_under_25 - price_above_25) / (2*(25/100)*(price + accrued))

    return print('OAD: {}'.format(OAD))

calculateOAD()
