#students = ['Harry', 'Hermione', 'Ron']

# for i in range(len(students)):
#     print(i+1, students[i])  

students = {'Harry': 'Gryffindor', 'Hermione': 'Gryffindor', 'Ron': 'Gryffindor'}

for student in students:
    print(student, students[student], sep=', ')