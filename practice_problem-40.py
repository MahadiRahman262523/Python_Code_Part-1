# Write a python function to remove a given word 
# from a list and strip if at the same time

def remove_and_strip(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()


name = "     Mahadi Rahman Dhrubo    "
n = remove_and_strip(name , "Dhrubo")
print(n)


