# Write a python program to create a dictionary of hindi words with values as their english
# translation. Provide user with an option to look it up.

myDict = {
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item",
    "Larkha" : "Boy",
    "Larkhi" : "Girl",
    "Vai" : "Brother",
    "Behen" : "Sister"
}

print("Options are : ", myDict.keys())
a = input("Enter hindi word : ")
print("The meaning of your word is : ",myDict.get(a))


