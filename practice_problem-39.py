# Write a python function to print first n lines of 
# the following pattern :

# * * *
# * *             for n = 3
# * 

n = int(input("Enter any number to print pattern : "))

for i in range(n):
    print("*" * (n-i))
