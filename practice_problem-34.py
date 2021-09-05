# Write a program to print  multiplication table of n
# using for loop in reversed order

tabl=int(input("Enter any number : "))
for i in range(10,-1,-1):
    print(tabl,"*",i,"=",i*tabl)



