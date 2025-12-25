import csv

# with open("students.csv") as file:
#     for line in sorted(file):
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]}: {row[1]}")
#
#         name, house = line.rstrip().split(",")
#         print(f"{name}: {house}")

# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append((name, house))
#
# for student in sorted(students):
#     print(student)

# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name, "home": home}
#         # student["name"] = name
#         # student["house"] = house
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} : {student['home']}")



# students = []
#
# with open("students.csv") as file:
#     # reader = csv.reader(file)
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} : {student['home']}")


name = input("Enter your Name   : ")
home  = input("Where is your Home: ")

with open("students.csv", "a", newline="") as file:
    # writer = csv.writer(csvfile)
    writer = csv.DictWriter(file, fieldnames=("name", "home"))
    writer.writerow({"name": name, "home": home})