# print('hello')

# x = 5
# if x < 10:
#     print("smaller")
# if x >20:
#     print("bigger")

# print("finish")

# Program:
age = input("Please enter your age: ")

print(type(age))


try:
    age = int(age)
    if age < 10:
        print("You are younger than ten")
    elif age == 10:
        print("You are ten")
    elif age == 11:
        print("You are eleven")
    elif age == 12:
        print("You are twelve")
    else:
        print("You are older than twelve")
except:
    print("somthing went wrong")


print(type(age))
