# can you change the elg parameter inside a class to something else(say"harry").
# try changing self to 'slf' or 'harry' and see the effects.


class Sample:
    def __init__(self,name):
        self.name = name
        
obj = Sample("Dhrubo")
print(obj.name)        

# N.B :- we are obviously writing slf or anything in place of self
#        but we are not writing this because its confused other programer who's 
#        see the this source code

