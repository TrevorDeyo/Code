#ChatGPT Optimization Pass 1
hrs = float(input("Enter Hours:"))
pay = float(input("Enter Hourly rate:"))

if hrs <= 40:
    print(hrs * pay)
else:
    normal_pay = 40 * pay
    over_pay = (hrs - 40) * (pay * 1.5)
    print(normal_pay + over_pay)