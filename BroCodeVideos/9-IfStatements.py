userAge = int(input("How old are you? "))

if(userAge == 100):
    print("you are a century old!")
elif(userAge >= 18):
    print("you are an adult!")
elif(userAge < 0):
    print("you haven't been born yet!")
else:
    print("you are a child!")