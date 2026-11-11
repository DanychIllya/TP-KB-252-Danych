FIELDS = ["name", "phone", "email", "group"]

list = [
    {"name":"Bob",  "phone":"0631234567", "email":"bob@example.com",  "group":"KB-252"},
    {"name":"Emma", "phone":"0507654321", "email":"emma@example.com", "group":"KB-252"},
    {"name":"Jon",  "phone":"0671112233", "email":"jon@example.com",  "group":"KB-251"},
    {"name":"Zak",  "phone":"0939998877", "email":"zak@example.com",  "group":"KB-252"}
]
 
def printAllList():
    for elem in list:
        strForPrint = ("Student name is " + elem["name"] +
                       ",  Phone is " + elem["phone"] +
                       ",  Email is " + elem["email"] +
                       ",  Group is " + elem["group"])
        print(strForPrint)
    return
 
def inputName(prompt):
    while True:
        name = input(prompt).strip()
        if name != "":
            return name
        print("Name can not be empty")
 
def findInsertPosition(name):
    insertPosition = 0
    for item in list:
        if name.lower() > item["name"].lower():
            insertPosition += 1
        else:
            break
    return insertPosition
 
def findElementPosition(name):
    for item in list:
        if name.lower() == item["name"].lower():
            return list.index(item)
    return -1
 
def addNewElement():
    name = inputName("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    insertPosition = findInsertPosition(name)
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return
 
def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = findElementPosition(name)
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del list[deletePosition]
    return
 
 
def updateElement():
    name = input("Please enter name to be updated: ")
    position = findElementPosition(name)
    if position == -1:
        print("Element was not found")
        return
 
    oldItem = list[position]
    print("Current data: name=" + oldItem["name"] + ", phone=" + oldItem["phone"] +
          ", email=" + oldItem["email"] + ", group=" + oldItem["group"])
    print("Enter new values (press Enter to keep the current value)")
 
    newItem = {}
    for field in FIELDS:
        value = input("New " + field + " [" + oldItem[field] + "]: ").strip()
        if value == "":
            newItem[field] = oldItem[field]
        else:
            newItem[field] = value

    del list[position]
    insertPosition = findInsertPosition(newItem["name"])
    list.insert(insertPosition, newItem)
    print("Element has been updated")
    return
 
def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        if chouse in ("C", "c"):
            print("New element will be created:")
            addNewElement()
            printAllList()
        elif chouse in ("U", "u"):
            print("Existing element will be updated")
            updateElement()
            printAllList()
        elif chouse in ("D", "d"):
            print("Element will be deleted")
            deleteElement()
        elif chouse in ("P", "p"):
            print("List will be printed")
            printAllList()
        elif chouse in ("X", "x"):
            print("Exit()")
            break
        else:
            print("Wrong chouse")
 
main()
 