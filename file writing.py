# f = open("Dhrubo_1.txt","w")
#f = open("Dhrubo_1.txt","a")

# a = f.write("Name : Mahadi Rahman Dhrubo\n")
# print(a)
# f.write("ID : 191-15-12177\n")
# f.write("Favrt. Prog. Lang. : Python\n")
# f.write("section : O-6\n")
# f.write("Designation : CR\n")


# Handle read and write Both
f = open("Dhrubo_1.txt","r+")
print(f.read())
f.write("Thank you")

f.close()
