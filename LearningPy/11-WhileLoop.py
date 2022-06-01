#while 1==1:
#    print("Infinite Loop!")

#userName = ""

#while len(userName) == 0:
    #userName = input("Enter your name: ")

#print("Hello " + userName)

userName = None

while not userName:
    userName = input("Enter your name: ")

print("Hello " + userName)