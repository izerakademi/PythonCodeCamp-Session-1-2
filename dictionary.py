dictionaryList = {}
print(type(dictionaryList))
print(dictionaryList)

dictionaryList = dict()
print(type(dictionaryList))
print(dictionaryList)

dictionaryList = {"Lang1": "English", "Lang2": "German", "Lang3": "Spanish"}
print(dictionaryList)

print("Value of Lang1 : {0}".format(dictionaryList["Lang1"]))
print("Value of Lang2 : {0}".format(dictionaryList["Lang2"]))
print("Value of Lang3 : {0}".format(dictionaryList["Lang3"]))
dictionaryList["lang4"] = "Spanish"
print(dictionaryList)

print("**************Nested Dictionary*****************")
dictionaryList = {
    "Plates": {"Plate1": 35, "Plate2": 6, "Plate3": 34},
    "Cities": {"City1": "Izmir", "City2": "Ankara", "City3": "Istanbul"}
}
print(dictionaryList)
print("**************Plates*****************")
print("Plates : {0}".format(dictionaryList["Plates"]))
print("Plate 1 : {0}".format(dictionaryList["Plates"]["Plate1"]))
print("Plate 2 : {0}".format(dictionaryList["Plates"]["Plate2"]))
print("Plate 3 : {0}".format(dictionaryList["Plates"]["Plate3"]))
print("**************Cities*****************")
print("Cities : {0}".format(dictionaryList["Cities"]))
print("City 1 : {0}".format(dictionaryList["Cities"]["City1"]))
print("City 2 : {0}".format(dictionaryList["Cities"]["City2"]))
print("City 3 : {0}".format(dictionaryList["Cities"]["City3"]))

print("**************Get*****************")
print("**************Plates*****************")
print("Plates : {0}".format(dictionaryList.get("Plates")))
print("Plate 1 : {0}".format(dictionaryList.get("Plates").get("Plate1")))
print("Plate 2 : {0}".format(dictionaryList.get("Plates").get("Plate2")))
print("Plate 3 : {0}".format(dictionaryList.get("Plates").get("Plate3")))
print("**************Cities*****************")
print("Cities : {0}".format(dictionaryList.get("Cities")))
print("City 1 : {0}".format(dictionaryList.get("Cities").get("City1")))
print("City 2 : {0}".format(dictionaryList.get("Cities").get("City2")))
print("City 3 : {0}".format(dictionaryList.get("Cities").get("City3")))

productList = {
    "1": {"ProductName": "Computer",
          "ProductDescription": "Computer Test Description",
          "Quantity": 10,
          "Price": 5700,
          "Specification": {"Cpu": "9700K",
                            "Motherboard": "Asus Z370",
                            "Ram": "16GB"}},
    "2": {"ProductName": "Macbook Pro",
          "ProductDescription": "Mac Test Description",
          "Quantity": 20,
          "Price": 15700,
          "Specification": {"Cpu": "9900K",
                            "Motherboard": "Asus Z390",
                            "Ram": "32GB"}},
}
print("Product 1   : {0}".format(productList.get("1")))
print("ProductName : {0}".format(productList.get("1").get("ProductName")))
print("Product Description : {0}".format(productList.get("1").get("ProductDescription")))
print("Quantity : {0}".format(productList.get("1").get("Quantity")))
print("Price : {0}".format(productList.get("1").get("Price")))
print("Specification : {0}".format(productList.get("1").get("Specification")))
print("Specification=>CPU : {0}".format(productList.get("1").get("Specification").get("Cpu")))
print("Specification=>Motherboard : {0}".format(productList.get("1").get("Specification").get("Motherboard")))
print("Specification=>Ram : {0}".format(productList.get("1").get("Specification").get("Ram")))

print("*******************************************************************************")

print("Product 2   : {0}".format(productList.get("2")))
print("ProductName : {0}".format(productList.get("2").get("ProductName")))
print("Product Description : {0}".format(productList.get("2").get("ProductDescription")))
print("Quantity : {0}".format(productList.get("2").get("Quantity")))
print("Price : {0}".format(productList.get("2").get("Price")))
print("Specification : {0}".format(productList.get("2").get("Specification")))
print("Specification=>CPU : {0}".format(productList.get("2").get("Specification").get("Cpu")))
print("Specification=>Motherboard : {0}".format(productList.get("2").get("Specification").get("Motherboard")))
print("Specification=>Ram : {0}".format(productList.get("2").get("Specification").get("Ram")))

print("*********Pop**********")
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)

print("*********PopItem**********")
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.popitem())
print(squares.popitem())
print(squares)

print("*********Clear**********")
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squares.clear()
print(squares)

print("*********Del**********")
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
del squares[4]
print(squares)

print("*********Items**********")
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.items())

print("*********SetDefault**********")
person = {"Name": "Ali", "Age": 20}
age = person.setdefault("Age", 25)
print("Person : {person}".format(person=person))
print("Age : {age}".format(age=age))

person = {"Name": "Ali"}
age = person.setdefault("Age", 25)
print("Person : {person}".format(person=person))
print("Age : {age}".format(age=age))

print("*********Update**********")
person = {"Name": "Ali", "Age": 20}
person.update({"Name": "Mehmet"})
print("Person : {person}".format(person=person))

print("*********Values**********")
print("Values : {values}".format(values=person.values()))

print("*********Keys**********")
print("Keys : {keys}".format(keys=person.keys()))

people = {
    1: {"Name": "Ali", "Age": 20},
    2: {"Name": "Mehmet", "Age": 30},
    3: {"Name": "Gizem", "Age": 25}
}

for key, value in people.items():
    print("Person Key : {0}".format(key))
    for k in value:
        print("{k} : {v}".format(k=k, v=value[k]))
    print("*************")