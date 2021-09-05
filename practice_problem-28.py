#write a program to print multiplication table of a given number
#using for loop

# num = int(input("Enter any number : "))

# for i in range(1,11):
#     # print(str(num) + " X " + str(i) + " = " + str(i*num))
#     print(f"{num} X {i} = {i*num}")



#write a program to print multiplication table of a given number
#using while loop


print ("Enter a number")
num = int(input())
i = 1
while i<11:
    m = num*i
    print (f"{num} × {i} = {m}")
    i = i+1


