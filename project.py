
students = []
def studentDetails():
    name = input("Enter the name of the student:: ")
    age = int(input("Enter the age of the student:: "))
    class_ = input("Enter the class of the student:: ")
    subjects = input("Enter the subjects of the student:: ")
    address = input("Enter the address of the student:: ")
    hobbies = input("Enter the hobbies of the student:: ")
    student = {"name": name, 
                 "age": age, 
                "class": class_,
                 "subjects": subjects,
                 "address": address,
                 "hobbies": hobbies}
    return student
def add_student():
    student = studentDetails()
    for s in students:
        if s["name"] == student["name"]:
            print(f"Student {student['name']} is already present...")
            return
    students.append(student)
    print(f"{student['name']} is added...")
def delete_student():
    name = input("Enter the name of the student to delete:: ")
    for s in students:
        if s["name"] == name:
            students.remove(s)
            print(f"{name} is deleted...")
            return
    print(f"Can't delete Student {name}, No student with {name}")

def display_students():
    if not students:
        print("No students added...")
        return
    for s in students:
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Class: {s['class']}")
        print(f"subjects: {s['subjects']}")
        print(f"Address: {s['address']}")
        print(f"Hobbies: {s['hobbies']}")
        print()
def display_menu():
    print("Menu:")
    print("1. Add a student")
    print("2. Delete a student")
    print("3. Display the students' data")
    print("4. Exit")
    choice = int(input("Enter your choice:: "))
    return choice
while True:
    choice = display_menu()
    if choice == 1:
        add_student()
    elif choice == 2:
        delete_student()
    elif choice == 3:
        display_students()
    elif choice == 4:
        print("Thank you for using the application...")
        break
    else:
        print("Invalid choice.")

