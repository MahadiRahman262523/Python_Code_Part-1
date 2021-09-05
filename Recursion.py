# def func_iterative(n):
#     fac = 1
#     for i in range(n):
#         fac = fac*(i+1)
#     return fac
#
# number = int(input("Enter any number : "))
# print("Factorial using iterative ",func_iterative(number))



# def func_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n * func_recursive(n-1)
#
# number = int(input("Enter any number : "))
# print("Factorial using recursive ",func_recursive(number))


# 0 1 1 2 3 5 8 13 21 34 55 89 144......
def fibinacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return  fibinacci(n-1) + fibinacci(n-2)

num = int(input("Enter any number : "))
print(fibinacci(num))



