# Write a program to find whether a given username contaoins less than 10
# characters or not


name = input("Enter your name : ")
length = len(name)

print("Your Name Length is : ",length)

if(length < 10):
    print("Your Name Contains Less Than 10 Characters")
else:
    print("Your Name Contains greater Than 10 Characters")