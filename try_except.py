print("Enter number 1 : \n")
num1 = input()
print("Enter number 2 : \n")
num2 = input()

try:
    print("The sum of two values is ",int(num1)+int(num2))

except Exception as e:
    print(e)