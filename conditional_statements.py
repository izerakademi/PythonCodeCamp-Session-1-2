# Conditional Statements - Koşullu İfadeler
number = int(input("Enter Number : "))

if number == 0:
    print("Number is equal to zero")

if number > 0:
    print("Number is positive")

if number < 0:
    print("Number is negative")

print("*************************")


if number == 0:
    print("Number is equal to zero")
elif number > 0:
    print("Number is positive")
else:
    print("Number is negative")

