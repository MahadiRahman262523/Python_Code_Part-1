# Faulty Calculator
# Design a calculator which will correctly all the except the following one :
# 45*3 = 555 , 56+9 = 77 , 56/6 = 4
# Your program should take operator and the two numbers as input from user
# and then return the result...

while(True):
    print("Enter first number")
    num1=int(input())
    print("Enter second number")
    num2=int(input())
    print("enter your operator")
    op=input()
    if op=='+' and num1==54 and num2==5 :
        print("64")
    elif op=='*' and num1==45 and num2==5 :
        print("555")
    elif op == '/' and num1 == 56 and num2 ==6:
        print("4")
    elif op=='+':
        print(num1+num2)
    elif op=='-':
        print(num1-num2)
    elif op=='*':
        print(num1*num2)
    elif op=='/' :
        print(num1/num2)
    else:
        print("Invalid Input")