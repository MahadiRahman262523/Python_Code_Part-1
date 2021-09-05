class Person:
    designation = "Programmer"
    
    def getDesignation(self):
        print(f"Person's Designation is {self.designation}")
        
        
       
class ProgrammerInfo(Person):
    name = "Mahadi Rahman"
    favLang = "Python & PHP"
    designation = "Software Developer"
    
    def showDetails(self):
        print(f"Person's name is {self.name}")
        print(f"Person's favourite language is {self.favLang}")
        
        
    def getDesignation(self):
        print(f"Person's Designation is {self.designation}")    
        
        
p1 = Person()
p1.getDesignation()

print("\n")

p2 = ProgrammerInfo()
p2.getDesignation()
p2.showDetails()

print("\n")

print(f"programmer designation {p2.designation}") 
print(f"person designation {p1.designation}")              
       
       
        