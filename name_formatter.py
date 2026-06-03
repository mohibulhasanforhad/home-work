# biplob
#  Student Name Formatter

students = []

name1 = input("Enter name 1: ")
name2 = input("Enter name 2: ")
name3 = input("Enter name 3: ")

students.append(name1.title())
students.append(name2.title())
students.append(name3.title())

print("Students:", students)
print("Total students:", len(students))