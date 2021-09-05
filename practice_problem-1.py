# create a class programmer for storing info of
# few programmers working at microsoft

class Programmer:
    company = "Microsoft"
    
    def __init__(self,name,product):
        self.name = name
        self.product = product
        
    def getInfo(self):
        print(f"Company Name is {self.company}")
        print(f"Programmer name is {self.name}")
        print(f"He/She working on {self.product}")        


mrd = Programmer("Mahadi Rahman Dhrubo","Software Engineer")
mrd.getInfo()

print("\n")

srs = Programmer("Sadia Rahman Shanta","UI/UX Designer")
srs.getInfo()

