import csv
from sys import argv, exit

FIELDS = ["name", "phone", "email", "group"]

def load_students(file_name):
    """Завантажує студентів з CSV файлу та повертає список словників,
    відсортований за іменем. Назви стовпців не залежать від регістру,
    відсутні стовпці заповнюються порожніми значеннями."""
    students = []
    with open(file_name, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row = {(key or "").strip().lower(): (value or "").strip()
                   for key, value in row.items() if key is not None}
            student = {field: row.get(field, "") for field in FIELDS}
            if student["name"] != "":
                students.append(student)
    return sorted(students, key=lambda item: item["name"].lower())


def save_students(file_name, students):
    """Зберігає список студентів у CSV файл (з рядком заголовків)."""
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[field.capitalize() for field in FIELDS])
        writer.writeheader()
        for student in students:
            writer.writerow({field.capitalize(): student[field] for field in FIELDS})

def findInsertPosition(name, students):
    """Позиція, на яку треба вставити запис з іменем name,
    щоб список залишився відсортованим (без урахування регістру)."""
    insertPosition = 0
    for item in students:
        if name.lower() > item["name"].lower():
            insertPosition += 1
        else:
            break
    return insertPosition


def findElementPosition(name, students):
    """Позиція першого запису з іменем name або -1, якщо його немає."""
    for position, item in enumerate(students):
        if name.lower() == item["name"].lower():
            return position
    return -1


def insertStudent(students, student):
    """Вставляє студента, зберігаючи сортування. Повертає позицію вставки."""
    position = findInsertPosition(student["name"], students)
    students.insert(position, student)
    return position


def deleteStudent(students, name):
    """Видаляє студента за іменем. Повертає True, якщо запис було видалено."""
    position = findElementPosition(name, students)
    if position == -1:
        return False
    del students[position]
    return True


def updateStudent(students, name, new_values):
    """Змінює дані студента. Порожні значення в new_values не змінюють поле.
    Запис переставляється на правильну позицію (ім'я могло змінитись).
    Повертає True, якщо запис знайдено."""
    position = findElementPosition(name, students)
    if position == -1:
        return False
    updated = {}
    for field in FIELDS:
        value = new_values.get(field, "").strip()
        updated[field] = value if value != "" else students[position][field]
    del students[position]
    insertStudent(students, updated)
    return True


def formatStudent(student):
    return ("Student name is " + student["name"] +
            ",  Phone is " + student["phone"] +
            ",  Email is " + student["email"] +
            ",  Group is " + student["group"])

def printAllList(students):
    for elem in students:
        print(formatStudent(elem))


def inputName(prompt):
    while True:
        name = input(prompt).strip()
        if name != "":
            return name
        print("Name can not be empty")


def addNewElement(students):
    name = inputName("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    insertStudent(students, {"name": name, "phone": phone, "email": email, "group": group})
    print("New element has been added")


def deleteElement(students):
    name = input("Please enter name to be deleted: ")
    if deleteStudent(students, name):
        print("Element has been deleted")
    else:
        print("Element was not found")


def updateElement(students):
    name = input("Please enter name to be updated: ")
    position = findElementPosition(name, students)
    if position == -1:
        print("Element was not found")
        return
    old = students[position]
    print("Current data: " + ", ".join(field + "=" + old[field] for field in FIELDS))
    print("Enter new values (press Enter to keep the current value)")
    new_values = {}
    for field in FIELDS:
        new_values[field] = input("New " + field + " [" + old[field] + "]: ")
    updateStudent(students, name, new_values)
    print("Element has been updated")


def main(args):
    if len(args) < 2:
        print("Usage: python lab_02.py <input.csv> [output.csv]")
        return 1
    input_file = args[1]
    output_file = args[2] if len(args) > 2 else input_file

    try:
        students = load_students(input_file)
    except FileNotFoundError:
        print("File not found: " + input_file)
        return 1
    print("Loaded " + str(len(students)) + " students from " + input_file)

    while True:
        try:
            chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        except (EOFError, KeyboardInterrupt):
            print()
            chouse = "X"
        if chouse in ("C", "c"):
            print("New element will be created:")
            addNewElement(students)
            printAllList(students)
        elif chouse in ("U", "u"):
            print("Existing element will be updated")
            updateElement(students)
            printAllList(students)
        elif chouse in ("D", "d"):
            print("Element will be deleted")
            deleteElement(students)
        elif chouse in ("P", "p"):
            print("List will be printed")
            printAllList(students)
        elif chouse in ("X", "x"):
            save_students(output_file, students)
            print("Students were saved to " + output_file)
            print("Exit()")
            break
        else:
            print("Wrong chouse")
    return 0


if __name__ == "__main__":
    exit(main(argv))
