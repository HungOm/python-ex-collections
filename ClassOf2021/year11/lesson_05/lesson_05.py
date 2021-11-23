# # total = 0
# # count = 0
# # while True :
# #     inp = input('Enter a number: ')
# #     if inp == 'done':
# #         break
# #     value = float(inp)
# #     total = total + value     
# #     count = count + 1

# # average = total / count
# # print('Average:', average)


# # numlist = list()
# # while True :
# #     inp = input('Enter a number: ')
# #     if inp == 'done' : 
# #         break
# #     value = float(inp)

# #     numlist.append(value)

# #     # print(numlist)

# # average = sum(numlist) / len(numlist)
# # print('Average:', average)



# # counts = dict()
# # names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# # for name in names :
# #     if name not in counts: 
# #        counts[name] = 1
# #     else :
# #         counts[name] = counts[name] + 1
# # print(counts)

# # # x = counts.get("john",0)
# # # if name in counts:
# # #     x = counts[name]
# # # else :
# # #     x = 0

# # print(counts)
# # # x = counts["John"]
# # x = counts.get("csev1",0)

# # print(x)

# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names :
#     counts[name] = counts.get(name, 0) + 1
# print(counts)


# Q1) Write a program that will let you enter as many different names as you want. Once you say “done”, the program should print out “Hello <name>” for every name that you entered. Like this:
# Enter a name: Jambo
# Enter a name: Jeremy
# Enter a name: done
# Hello Jambo
# Hello Jeremy

# Hint: Use a list to store the names. Use list.append() to add new names to the list.
# name_list = list()
# while True:
#     name = input("Enter your name: ")
#     if name == 'done':
#         break
#     name_list.append(name)

# try:
#     for name in name_list:
#         print('Hello {}, Welcome!'.format(name))

# except:
#     print("something went wrong")


# Q2) User your knowledge of dictionaries to make a “store”. You should have a dictionary that says what items your store sells, and how much they cost, like this:
# items = {
# “apples”: 0.5,
# “bananas”: 1.5
# }
# Your program should ask people what they want to buy, and how many. Then, it should tell them the price. It should say “Sorry, we don’t have that” if you try to buy something that is not in the store. When the user types in “done”, the program should stop:

# What would you like to buy? apples
# How many? 5
# Ok, that will be 2.5 dollars
# What would you like to buy? aliens
# Sorry, we don’t have that
# What would you like to buy? done
# Thank you, come again soon!


items = {'apples':1,'bananas':1.3,'orange':0.80}
totalPrice = list()
while True:
    item = input('What would you like to buy? ')
    if item == 'done':
        break
    if item not in items:
        print("Sorry, we dont have any of that")
    else:
        price = items[item]
        while True:
            num = input("How many {} do you want?".format(item))
            try:
                num = int(num)*price
                totalPrice.append(num)
                print("That will cost {} , do you want anything else sir/Madam?".format(num))
                break
            except:
                print("value/price must be digit")

print('Totoal cost is ',sum(totalPrice))
print("Thank you, come again!")