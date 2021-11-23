# # Program:

# n = 5
# while n > 0 :
#     print(n)
#     n = n - 1
# print('Blastoff!')
# print(n)

# n = 5
# while n > 0 :
#     print('Lather')
#     print('Rinse')
# print('Dry off!')

# while True:
#     var = input("Enter <: ")
#     if var == '<':
#         print("Good job")
#         break
#     else:
#         print("try again:")
# print("done")

# while True:
#     line = input(">: ")
#     if line[0] == "#":
#         continue
#     if line == "done":
#         break
#     print(line)

    
# print("finally done")


# while True :
#     var = input("Enter < :")
#     if var == '<' :
#         print("Good Job")
#         break
#     else :
#         print("try again")
# Program:

# n = 5
# while n > 0 :
#     print(n)
#     n = n - 1
# print('Blastoff!')
# print(n)

# while True :
#     line = input("Enter password : ")
#     exit_code = ""
#     if line == "old123" : 
#         print("your pass has been changed .")
#         print("Please enter the new pass")
#         continue
#     if line == "12345" :
#         print("Logging in")
#         while True:
#             exit_1 = input("User Panel : ")
#             print("write exit to exit")
#             if exit_1 == "exit" :
#                 # print("ssss")
#                 exit_code = "exit"
#                 print("Exiting the nested while loop(the while loop inside while")
#                 break
#             # break
    
#     if exit_code == "exit":
#         print("You have assign exit_code value,thus exiting now")
#         print("Exiting the outer while")
#         break


# friends = ["Assad","Faraz","Ali","Sareh","Safa","Mariam"]
# print("Wishing my friend a happy new year")

# for i in friends:
#     print("Happy new year, ",i)
#     print("~~~~~~~~~~~~~~~~~")
# print("Done wishing")

# print("333333333333333333333")

# largest_num_sofar = -1


# for num in [9, 41, 12, 3, 74, 15]:
#     if 74 > largest_num_sofar:
#         largest_num_sofar = num
#     print("Largest number so far", largest_num_sofar)

# print("-----------")
# print("the largest number is ",largest_num_sofar)

# largest_so_far = -1
# print('Before', largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num > largest_so_far :
#       largest_so_far = the_num
#    print("The largest num so far is {}".format(largest_so_far, the_num))

# print('The final largest number', largest_so_far)
# count = 0
# items = [9, 41, 12, 3,  74, 15,1,2,4,5,5,6,6,7,6,787,8,3]
# # users = []

# for item in items:
#     print("counting..by 1 increment")
#     count = count +1

#     print(count)

# print('There are {} user in this set'.format(count))

# count = 0
# sum = 0
# print('Before', count, sum)
# for value in [9, 41, 12, 3, 74, 15] :
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# print('After', count, sum, sum / count)

# smallest = None
# # print('Before')
# for value in [9, 41, 12, 3, 74, 15] :
#     if smallest is None: 
#         smallest = value
#     elif value < smallest : 
#         smallest = value
#     # print(smallest, value)
# print('the smallest number is ', smallest)

# sum = 0
# numm = [9, 41, 12, 3, 74, 15]
# for num in numm:
#     sum = num + sum
# for num in numm:
#     if num < sum:
#         sum = num
# print(sum)

# smallest = []
# numbers = [9, 41, 12, 3, 74, 15]
# for num in numbers:
#     smallest = num + smallest
# for num in numbers:
#     if num < smallest :
#         smallest = num
# print(smallest)

# smallest = int()
# numbers = [9, 41, 12, 3, 74, 15]
# for num in numbers:
#     smallest = num + smallest
# for num in numbers:
#     if num < smallest :
#         smallest = num
# print(smallest)

# for value in [9, 41, 12, 3, 74, 15]:
#       if value < 9 :
#           print('smallest number', value)


# least = 0
# nums = [9, 41, 12, 3, 74, 15]
# for num in nums:
#     least = num + least
# for num in nums:
#     if num < least:
#         least = num
# # print(least)


# count = 0
# items = [9, 41, 12, 3,  74, 15,1,2,4,5,5,6,6,7,6,787,8,3]
# # users = []

# for item in items:
#     print("counting..by 1 increment")
#     count = count +1

#     print(count)


# def count(items):
#     count = 0
#     for item in items:
#         count = count+1

#     return count


# total = 0
# count = 0
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
        
#     value = float(inp)
#     total = total + value     
#     count = count + 1

# average = total / count
# print('Average:', average)


# Introduction to Python – Homework 4
# Q1) Write a program which asks the user to enter a number. The program should then add up all the numbers from 1 up to the number the user entered. Like this:
# Enter a number: 5
# 15
# Enter a number: 10
# 55
# Your program should also be able to deal with errors and mistakes, like this:
# Enter a number: bob
# Sorry, that’s not a number!

# Hint, use a “for” loop to write your program


# Q2) Write a program that:
# 1)	Asks me to enter numbers over and over until I enter “0”
# 2)	When I put in “0”, the program should stop and tell me the biggest number I put in
# The program should work like this:
# Enter a number: 28
# Enter a number: BOB
# Sorry, that’s not a number, please try again
# Enter a number: 1000
# Enter a number: 24
# Enter a number: 0
# The biggest number was 1000

# Hint: Use a “while” loop to write this program


line = "---------------------------"


print(line)

# try:
#     inp = int(input("Enter the number: "))
#     summ = 0
#     # print(type(inp))

#     for i in range(inp+1):
#         # print(i)
#         summ = summ + i
#     print(summ)


# except:
#     print("Sorry , enter number")

# biggest_num = None

# while True:
#     inp = input("Enter number: ")
#     try:
#         inp = int(inp)
    
#         if biggest_num is None:
#             biggest_num = inp

#         if biggest_num <inp:
#             biggest_num = inp

#         if inp ==0:
#             print(biggest_num)
#             break
#     except:
#         print("Sorry enter a number")

        


print(line)

