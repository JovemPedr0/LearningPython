temperature = int(input("What is the temperature outside? "))

if not(temperature >= 0 and temperature <= 30):
    print("the temperature is bad today :(")
    print("stay inside!")
elif not(temperature < 0 or temperature > 30):
    print("the temperature is good today!")
    print("go outside!")