student = ("Max Müller", 22, "Informatik")

name, age, subject = student

# name = student[0]
# age = student[1]
# subject = student[2]

print(name)
print(age)
print(subject)

def get_student():
    return ("Max Müller", 22, "Informatik")

name, age, student = get_student()

print(name)
print(age)
print(subject)

students = [
    ("Max Müller", 22),
    ("Monika Mustermann", 23)
]

for name, age in students:
    print(name)
    print(age)