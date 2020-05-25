list1 = []
print(list1)
print(type(list1))

list2 = list()
print(list2)
print(type(list2))

list3 = [3, 12, 22, 33, 55, 10]
print(list3)

list4 = [12, 44, 67, 11, 89, "Apple", "Orange"]
print(list4)
print(type(list4))
print(len(list4))

print(list4[0])
print(list4[2])
print(list4[5])
print(list4[len(list4) - 1])
print(list4[-1])
print(list4[-2])

print("*************************")
print(list4)
print(list4[:4])
print(list4[1:4])
print(list4[3:])
print(list4[::2])
print(list4[::-2])

print("*************************")
numberList1 = [1, 2, 3, 4, 5, 6]
numberList2 = [89, 12, 55, 78, 32, 43]
print(numberList1)
print(numberList2)
print(numberList1 + numberList2)
numberListResult = numberList1 + numberList2
numberListResult = numberListResult + ["Apple"]
print(numberListResult)

print("*************************")
numberListResult[1] = 22
print(numberListResult)
numberListResult[-1] = "Orange"
print(numberListResult)

numberListResult[:2] = [20, 40]
print(numberListResult)

print(numberListResult * 3)

print("**********Methods***************")
print("************Append**************")
numberListResult.append("English")
numberListResult.append("German")
print(numberListResult)

print("************Pop**************")
numberListResult.pop()
print(numberListResult)
numberListResult.pop(2)
print(numberListResult)

print("************Count**************")
numberListResult.append(20)
print(numberListResult)
print(numberListResult.count(20))

print("************Insert**************")
numberListResult.insert(1, 98)
print(numberListResult)

print("************Remove**************")
numberListResult.remove("Orange")
print(numberListResult)

print("************Extend**************")
numberListResult2 = [1, 2, 67, 97, 213]
numberListResult.extend(numberListResult2)
print(numberListResult)

print("************Reverse**************")
numberListResult.reverse()
print(numberListResult)

print("************Clear**************")
numberListResult.clear()
print(numberListResult)

del numberListResult
numberListResult