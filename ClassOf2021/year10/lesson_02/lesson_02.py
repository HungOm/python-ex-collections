age = input('What is your age ? ')

# try:
#     age = int(age)
#     # sls
# except:
#     print("Sorry, you need to input only numbers, not text.")
#     exit()

try:
    # age = int(age)
    if age > 12:
            print("you are older than twelve")
        else:
            print("please type only twelve")

except:
    print("Please try again")


# if age > 12:
#     print("you are twelve")
# else:
#     print("please type only twelve")