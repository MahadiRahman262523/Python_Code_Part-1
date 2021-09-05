#Write a program to calculate the factorial of a given number 
#using for loop

num = int(input("Enter any number : "))

fact = 1
for i in range(1,num+1):
    fact = fact*i
    
print(f"The Factorial of the number {num} is {fact}")    