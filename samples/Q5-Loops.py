def Q1():
    number = int(input("Enter Number : "))
    sum = 0
    for i in range(1, number):
        sum = sum + i
    print("Sum : {0}".format(sum))


def Q2():
    number = int(input("Enter Number : "))
    mul = 1
    for i in range(1, number):
        mul = mul * i
    print("Mul : {0}".format(mul))


def Q3():
    number = int(input("Enter Number : "))
    evenCounter = 0
    oddCounter = 0
    for i in range(1, number + 1):
        if i % 2 == 0:
            evenCounter += 1
        else:
            oddCounter += 1
    print("Even Counter : {0}".format(evenCounter))
    print("Odd Counter : {0}".format(oddCounter))


def Q4():
    for i in range(1, 11):
        for j in range(1, 11):
            print("{i} * {j} = {result}".format(i=i, j=j, result=(i * j)))


def Q5():
    number = int(input("Enter Number : "))
    result = 1
    for i in range(number, 1, -1):
        result = result * i
    print("Fact : {0}".format(result))


# CTRL + ALT + L


# Q1()
# Q2()
# Q3()
# Q4()
Q5()
