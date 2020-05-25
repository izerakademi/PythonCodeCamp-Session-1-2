# Loops - Döngüler

for number in range(1, 11):
    print(number)
    print("Hello World")

print("************************")
for number in range(11):
    print(number)

print("************************")
for number in range(1, 11, 2):
    print(number)

print("************************")
for number in range(0, 11, 2):
    print(number)

print("************************")
for number in range(10, 0, -2):
    print(number)

# WHILE
print("************************")
print("********WHILE***********")
print("************************")
number = 0
while number < 6:
    print(number)
    number += 1
    if number == 5:
        break
    if number == 3:
        continue
    print("Hello World")

print("************************")
for number in range(0,6):
    if number == 5:
        break
    if number == 3:
        continue
    print("Hello Word")
