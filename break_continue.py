# i = 0

# while(i<45):
#     print(i+1 , end= " ")
#     if i == 17:
#         break
#     i = i+1



# i = 0

# while(i<45):
#     if i+1 < 5:
#         i = i+1
#         continue
#     print(i+1 , end= " ")
#     # if i == 17:
#     #     break
#     i = i+1



while(True):
    a = int(input("Enter integer number : "))

    if a > 100:
        print("Congrats you have entered a number greater than 100")
        break

    else:
        print("try again!!!")
        continue