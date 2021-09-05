# create a class pet from a class animal and
# further create class dog from pets. add a
# method bark to class dog 


class Animal:
    animalType = "Mammal"
    

class Pets(Animal):
    color = "white" 
    
    
class Dog(Pets):
    @staticmethod
    def bark(): 
        print("Bow Bow Bow !!!")
        
d = Dog()
d.bark()              


