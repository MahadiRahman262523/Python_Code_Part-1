d1 = {}
print(type(d1))

d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "David":"jam-bread",
      "Shuvam":{
            "B":"Maggie",
            "L":"Roti-Vat",
            "D":"Chiken"
         },
      "Marks":[78,89,90]
      }

print(d2)
print(d2["Harry"])
print(d2["Shuvam"])
print(d2["Shuvam"]["D"])

d2["Ankit"] = "Junk-food"
d2["Aurangazeb"] = "Kabab"
d2[420] = "Khoka Babu"
print(d2)

del d2[420]
print(d2)

d3 = d2.copy()
print(d3)

del d3["Harry"]

print(d2)
print(d3)

print(d2.get("David"))
print(d2.update({"Dhrubo":"Pizza"}))
print(d2)

del d2["Rohan"]
print(d2)

print(d2.keys()) # Print the keys of the dictionary
print(type(d2.keys()))
print(d2.items()) # Print the (key,value) for all contents of the dictionary
print(type(d2.items()))
print(d2.values()) # Print the values of the dictionary

