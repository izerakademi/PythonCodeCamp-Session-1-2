limit = int(input("Enter Number : "))
sum = 0
for number in range(1, limit):
    sum = sum + number
    sum += number
    print("Number : {0}".format(number))
    print("Sum    : {0}".format(sum))

print("Sum : {0}".format(sum))
