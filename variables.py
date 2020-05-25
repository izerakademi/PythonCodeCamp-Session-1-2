# ALT GR + 3
# CTRL + ALT + L
# Variables - Değişkenler

# Integer Numbers - Tam Sayılar
print("************************")
print("Integer Numbers - Tam Sayılar")
print("************************")
number = 5
print("Number :", number)
print(type(number))

# Floating Numbers - Ondalıklı Sayılar
print("************************")
print("Floating Numbers - Ondalıklı Sayılar")
print("************************")
number = 5.7
print("Number :", number)
print(type(number))

# Integer Numbers - Tam Sayılar
number = 6
print("Number :", number)
print(type(number))

# Strings - Metinsel İfadeler
# CamelCase  => firstName => Kotlin, Java, Python
# PascalCase => FirstName => C#
print("************************")
print("Strings - Metinsel İfadeler")
print("************************")
firstName = "Ali"
lastName = "Solmaz"
print("FistName : ", firstName)
print("LastName :", lastName)
print("Type of FirstName :", type(firstName))
print("Type of LastName :", type(lastName))

# Basic Casting  - Basit Tip Dönüşümü
print("************************")
print("Basic Casting  - Basit Tip Dönüşümü")
print("************************")
number = 10.6
print("Number :", number)
print("Type of Number :", type(number))

newNumber = int(number)
print("New Number :", newNumber)
print("Type of Number :", type(newNumber))

newNumber = str(number)
print("New Number :", newNumber)
print("Type of Number :", type(newNumber))

# Bool - Mantıksal Yapılar
print("************************")
print("Bool - Mantıksal Yapılar")
print("************************")
isCorrect = True
print("Is Correct : ", isCorrect)
print("Type of Number :", type(isCorrect))

isCorrect = False
print("Is Correct : ", isCorrect)
print("Type of Number :", type(isCorrect))

print("************************")
number1 = 5
number2 = 10
number3 = 15
print(number1, number2, number3)
print(number1, number2, number3, sep="+")
print(number1, number2, number3, sep="\n")
print(number1, number2, number3, sep="+", end="=")
print(number1 + number2 + number3)
print("Sum : " + str(number1 + number2 + number3))
print("Sum :", number1 + number2 + number3)
print("İzer" + "Akademi")
