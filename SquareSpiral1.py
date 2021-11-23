# import turtle
# for x in range(100):
#   turtle.forward(x)
#   turtle.left(91)




message = 'this is string'

message2 = "Did you know? We run a special virtual machine to display the images and produce the sounds you here, then stream them to your browser. This server runs a full version of Python 3, like our Python 3 trinket, but also supports graphics, sound, and interactivity."



def changeCase(str):
    ar = str.split(' ')
    newAr = []
    for i in ar:
        newAr.append(i.upper())

    n = ' '.join(newAr)
    return n 




print(changeCase(message))

print("====================")
print(changeCase(message2))



