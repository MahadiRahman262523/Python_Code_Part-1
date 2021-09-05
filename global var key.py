# a = 10
#
# def func(n):
#     # a = 22
#     b = 33
#
#     global a
#     a = a+22
#
#     print(a,b)
#     print(n)
#
# func("Mahadi Rahman")
# print(a)


x = 100
def dhrubo():
    x = 20
    def sadia():
        global x
        x = 880
    #print("Before calling sadia()",x)
    sadia()
    print("After calling sadia()",x)

dhrubo()
print(x)