# write a class calculator capable of finding 
# square,cube and squareroot of a number

class Calculator:
    def __init__(self,num):
        self.number = num
        
    def square(self):
        print(f"The Value of {self.number} suqare is {self.number **2}")
    
    def cube(self):
        print(f"The Value of {self.number} cube is {self.number **3}")
    
    def squareRoot(self):
        print(f"The Value of {self.number} suqare root is {self.number **0.5}")
    

a = Calculator(3) 
a.square()
a.cube()
a.squareRoot()       


