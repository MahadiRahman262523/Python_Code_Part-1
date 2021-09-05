# Write a program using function to convert celsius to fahrenheight

def far(cel):
    return (cel *(9/5))+32

c = int(input("Enter celsius value : "))
f = far(c)
print("Fahrenheit Temperature is "+ str(f))


