largest = -999999999
smallest = 999999999
while True:
    num = input("Enter a number: ")

    if num == "done":
            break

    try:
        number = int(num)
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    except:
        print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)