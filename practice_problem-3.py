# create a class with a class attribute a ;
# create a object from it and set a set a directly using object a = 0.
# Does this change the class attribute.


class Sample:
    a = "Dhrubo"
    
obj = Sample()
obj.a = "Sadia"

print(Sample.a)
print(obj.a)    




