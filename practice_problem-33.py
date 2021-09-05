# Write a program to print the following star pattern :

# *
# **          for n = 3
# ***

n = int(input("Enter any to print star pattern : "))

for i in range(n):
    print("*" * (i+1))

