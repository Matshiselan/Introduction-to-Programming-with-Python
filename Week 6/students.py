       
import csv


students = []
with open('students.csv') as file:
    reader = csv.reader(file)
    for name, age in reader:
        # name, age = line.strip().split(',')
        # students.append(name)
        # print(f'{name} is {age} years old')
        students.append({'name': name, 'age': int(age)})

for student in sorted(students, key=lambda s: s['name']):
    print(f"{student['name']} is {student['age']} years old")    