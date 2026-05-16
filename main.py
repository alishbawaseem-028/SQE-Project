students = []

# Add Student
def add_student():
    # .strip() removes accidental extra spaces
    name = input("Enter student name: ").strip()

    if name == "":
        print("\n❌ ERROR: Name cannot be empty!")
    elif name.lower() in [s.lower() for s in students]:
        print(f"\n⚠️ WARNING: '{name}' already exists in the system!")
    else:
        students.append(name)
        print(f"\n✅ SUCCESS: '{name}' added successfully!")

# View Students
def view_students():
    if len(students) == 0:
        print("\n📭 Notice: No students found in the database.")
    else:
        print("\n===============================")
        print(f"📊 STUDENT LIST ({len(students)} Total)")
        print("===============================")
        for index, student in enumerate(students, 1):
            print(f"{index}. {student}")
        print("===============================")

# Search Student
def search_student():
    if len(students) == 0:
        print("\n📭 Notice: Database is empty. Nothing to search.")
        return

    search_name = input("Enter student name to search: ").strip()
    
    # Case-insensitive search
    found_students = [s for s in students if s.lower() == search_name.lower()]

    if found_students:
        print(f"\n🔍 RESULT: Student '{found_students[0]}' was found in the system!")
    else:
        print(f"\n❌ RESULT: Student '{search_name}' NOT found!")

# Delete Student
def delete_student():
    if len(students) == 0:
        print("\n📭 Notice: Database is empty. Nothing to delete.")
        return

    delete_name = input("Enter student name to delete: ").strip()
    
    # Find the exact match in the list regardless of how it was typed
    match = None
    for s in students:
        if s.lower() == delete_name.lower():
            match = s
            break

    if match:
        students.remove(match)
        print(f"\n🗑️ SUCCESS: '{match}' has been deleted from the system!")
    else:
        print(f"\n❌ ERROR: Could not delete. '{delete_name}' not found!")

# Main Menu Loop
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("=====================================")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("\n🚪 Program Closed. Goodbye!")
        break
    else:
        print("\n❌ Invalid choice! Please enter a number from 1 to 5.")