class Person:
    name = None
    age = None
    
    def talk(self):
        print("Person can be talk each other")
        
        
class Student(Person):
    name = "Mahadi Rahman"
    age = 20
    ID = "191-15-12177"
    
    def study(self):
        print("Every Student study everyday")
        
        
class Teacher(Student):
    name = "Zakia Zaman"
    age = 35
    empID = 700256378
    
    def teach(self):
        print("Every teacher teaching their student")
        
        
        
p = Person()
print(p.name)
print(p.age)
p.talk()

print("\n")

s = Student()
print(s.name)
print(s.age)
print(s.ID)
s.study()
s.talk()

print("\n")

t = Teacher() 
print(t.name)
print(t.age)
print(t.empID)
t.teach()
t.study()
t.talk()       
        
        
        
        
                        