# x = 5
# print('Before 5')
# if  x == 5:
#     print('Is 5')
#     print('Is Still 5')
#     print('Third 5')
# print('Afterwards 5')
# print('Before 6')
# if x == 6 :
#     print('Is 6')
#     print('Is Still 6')
#     print('Third 6')
# print('Afterwards 6')

# x = 42
# if x > 1 :
#     print('More than one')
#     if x < 100 : 
#         print('Less than 100') 
# print('All done')
# x = input("Enter a number: ")

# try:
#     x = int(x)
#     if x>10:

#         print("the number is greater than 10")
#     else:
#         print("the number is equal to or less than 10")
# except:
#     print("Please enter a number , Not a text.")
#     exit()

# x = 6
# if x < 2 :
#     print('small')
# elif x < 10 :
#     print('Medium')
# else :
#     print('LARGE')
# print('All done')
# x = input("type a number")
# try:
#     x = int(x)
#     if x > 5 :
#         print('Medium')
#     elif x>20:
#         print("Large")
#     else:
#         print('small')
# except:
#     print("this isnt a number")
# if x == 10 or x==3:


# No Else
# x = 5
# if x < 2 :
#     print('Small')
# elif x < 10 :
#     print('Medium')

# print('All done')
# x = 200

# if x < 2 :
#     print('Small')
# elif x < 10 :
#     print('Medium')
# elif x < 20 : 
#     print('Big')
# elif x < 40 : 
#     print('Large')
# elif x < 100:
#     print('Huge')
# else:
#     print('Ginormous')

# x = 0
# if x < 2 :
#     print('small')
# elif x < 10 :
#     print('medium')
# else : 
#     print('large')
# print('all done')


# height = input('type ur height in cm')
# try:
#     height = int(height)
#     if height < 150 :
#         print('you are short')
#     elif height < 160 :
#         print('you are average')
#     elif height <180 :
#         print('you are above average')
#     elif height > 180 :
#         print('you are Yao Ming')
#     else:
#         print('your a giant')
# except:
#     print('thats not a number')

# ans = str(input("What is your height in cm : "))
# if ans < 150 :
#     print("You are short")
# elif ans < 160 :
#     print("You are average")
# elif ans >= 160 and ans <= 180 :
#     print("You are average")
# elif ans > 180 :
#     print("You are Yao Ming")
# elif ans > 190 :
#     print("You are a Gaint")
# else :
#     print("write a value please")

# int()

# try:
#     height = int(input("whats ur height"))
#     if height < 150 :
#         print("u're short")
#     elif height < 160 :
#         print("you are average")
#     elif height == 180 :
#         print(" you are above average")
#     elif height > 180 and height <189:
#         print(" you are yao ming")
#     elif height > 190 :
#         print("you are giant")
#     else:
#         print("This will print if numbers are between 161 and 179")
# except:
#     print("Please enter number. Try again")

year = input("Type a year in numbers")
year = int(year)
if year % 4 < 1 :
  if year % 100 > 0 :
    print('this is a leap year')
if year % 4 < 1 :
  if year % 100 < 1 :
    if year % 400 < 1 :
      print('This is a leap year')
    else:
      print('This is not a leap year')
if year % 4 > 0 :
  print('This is not a leap year')