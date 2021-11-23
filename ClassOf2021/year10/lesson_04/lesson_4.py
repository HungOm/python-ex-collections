# n = 5
# while n > 0 :
#     print('Lather')
#     print('Rinse')
# print('Dry off!')
# n = 5
# while n > 0 :
#     print("n is {}".format(n))
#     n = n - 1
# print('Blastoff!')
# print(n)


# while True:
#     line = input('enter anything:  ')
#     if line == 'done' :
#         break
#     print(line)

# print(" --printing done ---")
# print('Done!')


# while True:
#     line = input('Enter somthing: \n')
#     if line[0] == '#' :
#         continue
#     if line == 'done' :
#         break
#     print(line)
# print('Done!')


# while True:
#     line = input("Enter Something: \n")
#     if line[0] == "#":
#         continue
#     if line == "done":
#         break
#     print(line)

# definite loops 
line = '----------------------'
# print(line)

# for i in [5,4,3,2,1]:
#     print('this is {}'.format(i+10))

# print("end of loops")
# print('done')
# print(line)


# # definite loops
# line = '--------------'
# print(line)

# for i in [5,4,3,2,1]:
#     print('this is {}'.format(i+10))
    
# print("end of loops")
# print('done')
# print(line)


# print(line)

# friends = ['Ali','Ayatulla','Sareh','Meerab','Phyo Ih San',' Van Lian','Ak Nasir','Anas Ramans']
# for friend in friends:
#     print('Good Luck with your coming Exam {}!'.format(friend))
# print('done')

# print(line)

print(line)

# largest_num = 0
# numbers = [9, 41, 12, 3, 74, 15,345,345,435,345,2,2,34,2143,658,6,3,3,3,3,5,4,45,34,34,34,3,52,52,53245,3245,325,23,453,78,645,3252,121121231,432,4,23424334,242,54,5,2,23,45435,2,32,]

# for number in numbers:
#     if largest_num< number:
#         largest_num = number

# print(largest_num)
# print(line)

# largest_so_far = -1
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num > largest_so_far :
#       largest_so_far = the_num
# print('After', largest_so_far)
# largest_s0_far =-1
# print('Before', largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far the_num)
# print('After',largest_so_far)

# smallest_num = 890
# for the_big in[899,8923,23232,4345,3453,656]:
#     if the_big< smallest_num:
#         smallest_num= the_big
# print("the smallest of all",smallest_num)

# largest_so_far =74

# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num < largest_so_far :
#       smallest_so_far = the_num


# print('After', smallest_so_far)

# smallest_num = 900

# for num in [94564, 43431, 33312, 343433, -100990, 1343435]:
#     if smallest_num is None:
#         smallest_num = num
#     if num<smallest_num:
#         smallest_num=num 

# print(smallest_num)

print(line)
# numbers = [9, 41, 12, 3, 74, 15,345,345,435,345,2,2,34,2143,658,6,3,3,3,3,5,4,45,34,34,34,3,52,52,53245,3245,325,23,453,78,645,3252,121121231,432,4,23424334,242,54,5,2,23,45435,2,32,342,234,41, 12, 3, 74, 15,345,345,435,345,2,2,34,2143,658,6,3,3,3,3,5,4,45,34,34,34,3,52,52,53245,3245,325,23,453,78,645,3252,121121231,432,4,23424334,242,54,5,2,23,45435,2,32,342,234,
# 24,121,12,1,1,1,1,1,3,3,3,2]
# count = 0
# # print("start counting ...")

# for number in numbers:
#     count = count + 1
#     # print("current count:",count)
# # print("~~~~~~~~~~~~")
# print("Final count:",count)



# found = False
# print('Before', found)
# for value in [9, 41, 12, 3,3,5,7,2,74, 15] : 
#     print("do something")
#     if value == 3 :
#        found = True
#        print(found, value)


# if found == True:
#     print("Yayyy the number you're looking for is in the list!!! Rejoy!!")

# print('After', found)

# smallest = None
# print('Before')
# for value in [9, 41, 12, 3,5,6,7,1, 74, 15] :
#     if smallest is None : 
#         smallest = value
#     elif value < smallest : 
#         smallest = value
#     print(smallest, value)
# print('After', smallest)



# print(line)\\\




# while True:
#     user = input("Enter a number.. ")  
#     try:
#         user = int(user)

#     except:
#         print("Sorry that's not a number")

#     if user == 0 :
#         break
# print("Largest number is")

# numbers = [9, 41, 12, 3, 74, 15,345,345,435,345,2,2,34,2143,658,6,3,3,3,3,5,4,45,34,34,34,3,52,52,53245,3245,325,23,453,78,645,3252,121121231,432,4,23424334,242,54,5,2,23,45435,2,32,342,234,41, 12, 3, 74, 15,345,345,435,345,2,2,34,2143,658,6,3,3,3,3,5,4,45,34,34,34,3,52,52,53245,3245,325,23,453,78,645,3252,121121231,432,4,23424334,242,54,5,2,23,45435,2,32,342,234,
# 24,121,12,1,1,1,1,1,3,3,3,2]


# while True:
#     user=input("enter number")
#     if user == 0:
# #         break


# Q1) Write a program which asks the user to enter a number. The program should then add up all the numbers from 1 up to the number the user entered. Like this:
# Enter a number: 5
# 15
# Enter a number: 10
# 55
# Your program should also be able to deal with errors and mistakes, like this:
# Enter a number: bob
# Sorry, that’s not a number!







# number = input("Enter any number")
# count = 0
# summ =0

# try:
#     number = int(number)
#     while number > 0:
#         count = count+ 1
#         summ = summ + count
#         if number-1 <count:
#             print("The final answer is {} ".format(summ))
#             break

# except:
#     print("Sorry, that's not a number")


# Q2) Write a program that:
# Asks me to enter numbers over and over until I enter “0”
# When I put in “0”, the program should stop and tell me the biggest number I put in
# The program should work like this:
# Enter a number: 28
# Enter a number: BOB
# Sorry, that’s not a number, please try again
# Enter a number: 1000
# Enter a number: 24
# Enter a number: 0
# The biggest number was 1000


largest_num = -1

while True:
    try:
        userNumber = int(input("Enter a number: "))
        if userNumber>largest_num:
            largest_num = userNumber

        if userNumber==0:
            print("the largest number so far is ",largest_num)
            break
    except:
        print("Sorry, pls enter a number. Enter 0 if you want to exit().")


# largest_so_far = -1
# print('Before', largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num > largest_so_far :
#       largest_so_far = the_num
#    print(largest_so_far, the_num)

# print('After', largest_so_far)
