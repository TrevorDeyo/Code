# Promt the user for a score
while True:
    try:
        score = float(input("Enter a score between 0.0 and 1.0: "))
        if score < 0.0 or score > 1.0:
            print("Error: Score is out of range.")
        else:
            break
    except ValueError:
        print('Error: Invalid input. Please enter a numeric value.')
    
# Calculate the grade
if score >= 0.9:
    grade = "A"
elif score >= 0.8:
    grade = "B"
elif score >= 0.7:
    grade = "C"
elif score >= 0.6:
    grade = "D"
else:
    grade = "F"

print('Grade:', grade)