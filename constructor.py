class Student:
    # def __init__(self,name,dept,id):
    #     print("Student Deatils ->")
    #     print(f"Student name : {name}")
    #     print(f"Student Deprtment : {dept}")
    #     print(f"Student ID : {id}")
        
    def __init__(self,name,dept,id):
        self.name = name
        self.dept = dept
        self.id = id
        
    def getDetails(self):
        print("Student Deatils ->")
        print(f"Student name : {self.name}")
        print(f"Student Deprtment : {self.dept}")
        print(f"Student ID : {self.id}")        
        
        
mrd = Student("Mahadi Rahman Dhrubo","CSE","191-15-12177")
mrd.getDetails() 

print("\n")

srs = Student("Sadia Rahman Shanta","CSE","191-15-12444")
srs.getDetails()     
        
        
        