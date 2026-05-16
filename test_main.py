# test_main.py

import unittest
from main import StudentManagementSystem


class TestStudentManagementSystem(unittest.TestCase):

    def setUp(self):
        self.system = StudentManagementSystem()
        self.system.students = ["Ali", "Ahmed"]

    # Test Add Student
    def test_add_student(self):
        result = self.system.add_student("Usama")
        self.assertIn("SUCCESS", result)
        self.assertIn("Usama", self.system.students)

    # Test Add Duplicate
    def test_add_duplicate(self):
        result = self.system.add_student("Ali")
        self.assertIn("already exists", result)

    # Test Search Found
    def test_search_found(self):
        result = self.system.search_student("Ali")
        self.assertIn("FOUND", result)

    # Test Search Not Found
    def test_search_not_found(self):
        result = self.system.search_student("Zain")
        self.assertEqual(result, "NOT FOUND")

    # Test Delete Student
    def test_delete_student(self):
        result = self.system.delete_student("Ahmed")
        self.assertIn("DELETED", result)
        self.assertNotIn("Ahmed", self.system.students)

    # Test Delete Not Found
    def test_delete_not_found(self):
        result = self.system.delete_student("Zain")
        self.assertEqual(result, "NOT FOUND")


if __name__ == "__main__":
    unittest.main()
