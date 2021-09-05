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
    
    
    def __str__(self):
        return f"Decimal number is {self.num}"
    
    def __len__(self):
        return 1
    
    
n = Number(9)
print(n)
print(len(n))    
    
    
    

        