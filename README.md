# Student Management System

## Project Description
This project is developed in Python.

The system allows:
- Add Students
- View Students
- Search Students
- Delete Students

## Technologies Used
- Python
- unittest
- GitHub
- SonarQube
- Snyk

## Functionalities
1. Add Student
2. View Students
3. Search Student
4. Delete Student
## Testing Strategy

The project uses Python’s built-in unittest framework.

Test Coverage:
Adding a student
Preventing duplicate entries
Searching students
Deleting students
Handling invalid operations
Example Test Cases:
Test Case ID	Description	Expected Result
TC01	Add new student	Student added successfully
TC02	Add duplicate student	Warning message
TC03	Search existing student	Student found
TC04	Search non-existing student	NOT FOUND
TC05	Delete student	Student removed
## Bug Reporting

During testing, the following types of issues are considered:

Duplicate handling errors
Case sensitivity mismatches
Deletion of non-existing records
Empty input validation issues
## Security Analysis (Snyk)

The project was analyzed using Snyk Security Scanner.

Identified Security Concerns:
Lack of persistent data storage security
No authentication system
No role-based access control
Input validation limitations
In-memory data exposure risk
Suggested Fixes:
Use database instead of in-memory list
Implement user authentication
Add input sanitization layer
Encrypt stored data if persisted
Implement access control policies
## Code Quality Analysis (SonarQube)

The following improvements were made to maintain code quality:

✔ Removed global variables
✔ Reduced code duplication
✔ Improved function modularity
✔ Used OOP principles
✔ Improved readability and maintainability
## Developed By
Sameer Ahmed (Fa23-bse-011)
Talha Ahmed (Fa23-bse-025)
Alishba Waseem (Fa23-bse-028)
Aima Jahangir (Fa23-bse-043)
Esha Zia (Fa23-bse-045)
Usama Saleem  (Fa23-bse-053)
