# Write apython program to find out whether a student is pass or fail
# if it requires total 40% and at least 33%, in each subject to pass. Assume
# 3 subjects and take marks as an input from the user

sub1 = int(input("Enter number 1 subject marks : "))
sub2 = int(input("Enter number 2 subject marks : "))
sub3 = int(input("Enter number 3 subject marks : "))

if(sub1<33 and sub2<33 and sub3<33):
    print("You are fail because you have less than 33%")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail because you have less than 40%")
else:
    print("Congratulations!!! You passed the exam")

    