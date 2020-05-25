limit = int(input("Enter Number : "))
for number in range(1, limit + 1):
    if number % 2 == 0:
        print("Even Number : {0}".format(number))
    else:
        print("Odd Number  : {0}".format(number))
