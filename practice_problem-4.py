# Add a static method in problem 2 to greet the user with Hello

class Calculator:
    def __init__(self,num):
        self.number = num
        
    def square(self):
        print(f"The Value of {self.number} suqare is {self.number **2}")
    
    def cube(self):
        print(f"The Value of {self.number} cube is {self.number **3}")
    
    def squareRoot(self):
        print(f"The Value of {self.number} suqare root is {self.number **0.5}")
        
    @staticmethod
    def greet():
        print("*****Hello there welcome to the best calculator*****")    
    

a = Calculator(3)
a.greet() 
a.square()
a.cube()
a.squareRoot() 


