class Number:
    def __init__(self,num):
        self.num = num
        
    
    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num 
    
    
    def __sub__(self, num2):
        print("Lets sub")
        return self.num - num2.num 
    
    
    def __mul__(self, num2):
        print("Lets mul")
        return self.num * num2.num 
    
    
    def __truediv__(self, num2):
        print("Lets div")
        return self.num / num2.num 
    
    
    def __floordiv__(self, num2):
        print("Lets rem")
        return self.num // num2.num
    
    
    
n1 = Number(10)
n2 = Number(4)

sum = n1 + n2
print(sum) 

sub = n1 - n2
print(sub) 

mul = n1 * n2
print(mul) 

div = n1 / n2
print(div) 

rem = n1 // n2
print(rem)    
    
    

        