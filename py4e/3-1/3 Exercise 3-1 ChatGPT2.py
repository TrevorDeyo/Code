#ChatGPT Optimization Pass 2
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

if hours_worked <= 40:
    print(f"Total pay: {hours_worked * hourly_rate:.2f}")
else:
    normal_pay = 40 * hourly_rate
    overtime_pay = (hours_worked - 40) * (hourly_rate * 1.5)
    total_pay = normal_pay + overtime_pay
    print(f"Total pay: {total_pay:.2f}")