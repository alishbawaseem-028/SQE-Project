import unittest
students = ["Ali", "Ahmed"]
# Test Class
class TestStudentManagement(unittest.TestCase):
    # Test Search
    def test_search_student(self):
        self.assertIn("Ali", students)
    # Test Delete
    def test_delete_student(self):
        students.remove("Ahmed")
        self.assertNotIn("Ahmed", students)
    # Test Add
    def test_add_student(self):

        students.append("Usama")

        self.assertIn("Usama", students)

# Run Tests
if __name__ == "__main__":
    unittest.main()