# Write a program to print the following star pattern :

    #       *
    #     * * *               for n = 3
    #   * * * * *    

n = int(input("Enter any number to print star pattern : "))

for i in range(n):
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (n-i-1))


    