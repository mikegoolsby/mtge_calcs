def calculateAccruedInterest():
    orig_face = int(input("enter orig face amt: "))
    factor = float(input("enter factor: "))
    price = float(input("enter price: "))
    coupon = float(input("enter coupon: "))
    curr_face = orig_face * factor
    settle_day = int(input("enter day of month of settle (ie if july 4th, enter 4): \n"))

    if settle_day <= 31 and settle_day != 0:
        settle_day -= 1
    elif settle_day == 1:
        settle_day = 1

    prin_value = (price / 100) * curr_face 
    accruedIntMonthly = (curr_face * coupon) / 1200
    accruedDaily = (accruedIntMonthly / 30) * settle_day
    total_accrual = prin_value + accruedDaily
    print("**Trade Numbers**\nOriginal Face: {}\nCurrent Factor: {}\nCurrent Face: {}\nPrincipal Value: {}\n+ Accrued *{} days* {}\n=Total: {}".format(orig_face,factor,curr_face,prin_value, settle_day, accruedDaily, total_accrual))


calculateAccruedInterest()
