class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, вік: {self.age}"

    def __repr__(self):
        return f"Student({self.name!r}, {self.age})"


def main():
    students = [
        Student("Олена", 20),
        Student("Андрій", 19),
        Student("Максим", 22),
        Student("Софія", 18),
        Student("Богдан", 21),
    ]

    print("Початковий список:")
    for student in students:
        print(" ", student)

    print("\nСортування за іменем:")
    for student in sorted(students, key=lambda s: s.name):
        print(" ", student)

    print("\nСортування за віком (за зростанням):")
    for student in sorted(students, key=lambda s: s.age):
        print(" ", student)

    print("\nСортування за віком (за спаданням):")
    for student in sorted(students, key=lambda s: s.age, reverse=True):
        print(" ", student)


main()
