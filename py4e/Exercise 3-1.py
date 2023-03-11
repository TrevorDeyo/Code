hrs = input("Enter Hours:")
h = float(hrs)

pay = input("Enter Hourly rate:")
p = float(pay)

if h <= 40 :
    print(h * p)
else :
    NormalPay = 40 * p
    OverPay = (h - 40) * (p * 1.5)
    print(NormalPay + OverPay)