student = ("Pedro", 19, "male")

print(student.count("Pedro"))
print(student.index("male"))

for i in student:
    print(i)

if("Pedro" in student):
    print("Ok!")