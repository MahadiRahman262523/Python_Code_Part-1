# A spam comment is defined as a test containsing following keywords:
#     "make a lot of money","buy now","subscribe this",
#     "click this". Write a program to detect this spam

text = input("Enter the text : \n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False
    
if(spam):
    print("This Text is Spam")
else:
    print("This Text is not Spam")   

