# text = input("Enter Name :")
# print("Name :", text)
# CTRL + K + D

number1 = float(input("Enter Number 1 : "))
number2 = float(input("Enter Number 2 :"))

print("Type of Number1 : ", type(number1))
print("Type of Number2 : ", type(number2))

print("Sum : ", number1 + number2)
print("Sub : ", number1 - number2)
print("Mul : ", number1 * number2)
print("Div : ", number1 / number2)
print("Pow : ", number1 ** number2)
print("Mod : ", number1 % number2)

print("Sum : {0}".format(number1 + number2))
print("Number 1 : {0} + Number 2 : {1} = Sum : {2}".format(number1, number2, number1 + number2))
print("Number 1 : {number1} + Number2 : {number2} = Sum : {sum}"
      .format(number1=number1, number2=number2, sum=number1 + number2))

avg = (number1 + number2) / 2
print("Avg : ", avg)
print("Avg : {0}".format(avg))
print("Avg : {avg}".format(avg=avg))
