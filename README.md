# Student Management System

## Overview

The **Student Management System** is a Python-based program designed to manage student records, marks, and generate report cards. It provides functionalities to add, update, delete, and display student details, as well as manage and display student marks. The program also generates a detailed report card for individual students.

This program is designed for educational institutions to efficiently manage student data and academic performance.

---

## Features

1. **Student Management**:
   - **Add Student**: Add new students with details such as name, grade, and status.
   - **Update Student**: Update student details like name or grade.
   - **Delete Student**: Mark a student as deleted (soft delete).
   - **Display Students**: View all available students in a tabular format.

2. **Marks Management**:
   - **Add or Update Marks**: Add or update marks for subjects like Mathematics, Physics, Chemistry, Computer Science, and English.
   - **Display Marks**: View marks for all students in a tabular format.

3. **Report Card Generation**:
   - Generate a detailed report card for a student, including marks, total scores, grades, and overall performance.
   - Export the report as a .pdf file.

4. **User-Friendly Menus**:
   - Intuitive menus with options to go back or exit the program at any point.

---

## How to Use

### Prerequisites
- Python 3.x installed on your system.
- The `tabulate` and `reportlab` library installed. You can install it using:

  ```bash
  pip install -r requirements.txt
  ```

### Running the Program
1. Clone or download the repository.
2. Navigate to the directory containing the `StudentManagement.py` file.
3. Run the program using the following command:
   ```bash
   python StudentManagement.py
   ```

### Program Workflow
1. **Main Menu**:
   - Choose between managing student marks, managing the student list, generating a report card, or exiting the program.

2. **Student Management**:
   - Add, update, delete, or display student details.

3. **Marks Management**:
   - Add or update marks for students and display marks in a tabular format.

4. **Report Card**:
   - Enter a student ID to generate a detailed report card.

5. **Exit**:
   - Exit the program at any time using the exit option in the menus.

---

## File Structure

- **Student_details.dat**: Stores student details (ID, name, grade, status).
- **Marks.dat**: Stores student marks for various subjects.
- **StudentManagement.py**: The main Python script containing the program logic.

---

## Code Structure

The program is divided into three main classes:

1. **Student**:
   - Handles student-related operations like adding, updating, deleting, and displaying students.

2. **Marks**:
   - Manages marks for students, including adding, updating, and displaying marks.

3. **Report**:
   - Generates and displays a report card for a student based on their marks.

---

## Example Workflow

1. **Add a Student**:
   - Go to **Manage Student List** → **Add Student**.
   - Enter the student's name and grade.

2. **Add Marks**:
   - Go to **Manage Student Marks** → **Add or Update Marks**.
   - Enter the student ID and subject marks.

3. **Generate Report Card**:
   - Go to **Generate Report Card**.
   - Enter the student ID to view their report card.

---

## Notes

- The program uses **pickle** to store data in binary files (`Student_details.dat` and `Marks.dat`). Ensure these files are not manually edited.
- The program supports soft deletion of students. Deleted students are marked as "DELETED" and are not displayed in the student list.
- The report card includes grades calculated based on the total marks obtained by the student.

---

## Future Enhancements

- Add a graphical user interface (GUI) for better user interaction.
- Implement data validation for inputs (e.g., valid grades, marks within range).

---

## Author

This program was developed as a Python project for educational purposes. Feel free to modify and extend the code as needed.

---

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.

---

Enjoy using the **Student Management System**! If you have any questions or suggestions, feel free to reach out. 😊
