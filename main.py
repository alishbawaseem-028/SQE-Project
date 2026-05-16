# main.py

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    # Normalize helper (avoids duplicate logic)
    def normalize(self, name):
        return name.strip().lower()

    # Add Student
    def add_student(self, name):
        name = name.strip()

        if name == "":
            return "ERROR: Name cannot be empty!"

        if self.normalize(name) in [self.normalize(s) for s in self.students]:
            return f"WARNING: '{name}' already exists!"

        self.students.append(name)
        return f"SUCCESS: '{name}' added successfully!"

    # View Students
    def view_students(self):
        if len(self.students) == 0:
            return "No students found."

        result = []
        for i, s in enumerate(self.students, 1):
            result.append(f"{i}. {s}")
        return result

    # Search Student
    def search_student(self, name):
        name = self.normalize(name)

        for s in self.students:
            if self.normalize(s) == name:
                return f"FOUND: {s}"

        return "NOT FOUND"

    # Delete Student
    def delete_student(self, name):
        name = self.normalize(name)

        for s in self.students:
            if self.normalize(s) == name:
                self.students.remove(s)
                return f"DELETED: {s}"

        return "NOT FOUND"


# ================= MAIN MENU =================
if __name__ == "__main__":
    system = StudentManagementSystem()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter name: ")
            print(system.add_student(name))

        elif choice == "2":
            result = system.view_students()
            if isinstance(result, list):
                print("\n".join(result))
            else:
                print(result)

        elif choice == "3":
            name = input("Enter name: ")
            print(system.search_student(name))

        elif choice == "4":
            name = input("Enter name: ")
            print(system.delete_student(name))

        elif choice == "5":
            print("Program exited.")
            break

        else:
            print("Invalid choice!")
