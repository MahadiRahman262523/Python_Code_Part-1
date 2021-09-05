# Write a python program to calculate the sum of first n natural numbers

def natural_num(n):
    sum1 = 0
    while(n > 0):
        sum1=sum1+n
        n=n-1
    return sum1    
        
n=int(input("Enter a number: "))        
print("The sum of first n natural numbers is",natural_num(n))

