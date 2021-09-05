class Employee:
    company = "Google"
    
dhrubo = Employee()    
sadia = Employee()

print(dhrubo.company)
print(sadia.company)

Employee.company = "FaceBook"    

print(dhrubo.company)
print(sadia.company)    
    
    