class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f'{self.name} from {self.house}'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        self._name = name

    @property
    def house(self):
        return self._house
    
    # House setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("House must be one of Gryffindor, Hufflepuff, Ravenclaw, or Slytherin.")
        self._house = house

    @classmethod
    def get_student(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get_student()
    # if student[0] == "Alice":
    #     student['house'] = "Gryffindor"
    # student.house = "Gryffindor"
    print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# def get_student():
#     # student = Student()
#     # student.name = input("Name: ")
#     # student.house = input("House: ")
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house) 

if __name__ == "__main__":
    main()