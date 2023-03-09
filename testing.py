numbers = []
while True:
    num = input("Enter a number (or 'done' to finish): ")
    if num == "done":
        break
    try:
        number = int(num)
        numbers.append(number)
    except ValueError:
        if num == "":
            print("Error: Please enter a number or 'done'")
        else:
            print("Error: '{}' is not a valid number".format(num))

if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print("Minimum is", smallest)
    print("Maximum is", largest)
else:
    print("No valid numbers were entered")
