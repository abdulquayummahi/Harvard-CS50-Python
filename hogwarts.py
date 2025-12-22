# students = ["Hermione", "Harry", "Ron", "Draco"]

# print(students)
# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)

# for i in range(len(students)):
#     # print(students[i])
#     # print( i+1, students[i])
#     print(f"{i+1} {students[i]}")


# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
#
# for i in range(len(students)):
#     print(f"{students[i]}: {houses[i]}")


# students = {
#     "Hermione" : "Gryffindor",
#     "Harry" : "Gryffindor",
#     "Ron" : "Gryffindor",
#     "Draco" : "Slytherin",
# }
#
# # print(students)
# # print(students["Hermione"])
# # print(students["Harry"])
# # print(students["Ron"])
# # print(students["Draco"])
#
# for student in students:
#     # print(student)
#     print(student, students[student], sep=", ")
#     # print(f"{student} : {students[student]}")

students = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russel terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : ""},
]

# print(students)

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" : ")
    # print(f"{student["name"]} : {student['house']} : {student['patronus']}")