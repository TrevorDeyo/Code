hrs = float(input("Enter Hours:"))
pay = float(input("Enter Hourly rate:"))

def computepay(hrs, pay):
    if hrs <= 40 :
        result = hrs * pay
    else :
        NormalPay = 40 * pay
        OverPay = (hrs - 40) * (pay * 1.5)
        result = NormalPay + OverPay
    return result

computed_pay = computepay(hrs, pay)
print('Pay', computed_pay)