#StudentManagement

import pickle
import os
from tabulate import tabulate
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

class Student:
    def __init__(self):
        pass

    @staticmethod
    def addStudent():
        """Add a new student to the database."""
        while True:
            with open('Student_details.dat', 'ab+') as f:
                sid1 = []
                found = False
                try:
                    f.seek(0)
                    while True:
                        r = pickle.load(f)
                        try:
                            sid1.append(r[0])
                            found = True
                        except:
                            pass
                except EOFError:
                    pass
                if not found:
                    print('\nCreating Table - Student\n')
                    sid = '000001'
                elif found:
                    sid = int(max(sid1)) + 1
                    sid = str(sid)
                    n = len(sid)
                    while n < 6:
                        sid = '0' + sid
                        n += 1
                name = input('Enter name   :')
                grade = input('Enter grade  :')
                stat = 'AVAILABLE'
                l = [sid.upper(), name.upper(), grade, stat]
                pickle.dump(l, f)
                print('\nStudent', sid.upper(), 'was added successfully :)\n')
                ch = input('Do you want to add more student(s) [Y -> Yes, B -> Back, E -> Exit] :')
                if ch.upper() == 'B':
                    break
                elif ch.upper() == 'E':
                    exit()
                elif ch not in 'Yy':
                    break
                f.close()

    @staticmethod
    def updateStudent():
        """Update student details."""
        while True:
            with open('Student_details.dat', 'rb') as f1:
                with open('Student_details1.dat', 'wb') as f2:
                    found = False
                    update = False
                    sid = input('Enter student id   :')
                    try:
                        while True:
                            r = pickle.load(f1)
                            if r[0] == sid.upper() and r[3] == 'AVAILABLE':
                                found = True
                            if found:
                                ch = input('''\nWhat do you want to update?
    1. Name
    2. Grade                                      
            :''')
                                if ch == '1':
                                    u = 'name'
                                    cc = 1
                                elif ch == '2':
                                    u = 'grade'
                                    cc = 2
                                else:
                                    print('Please choose a valid option :(')
                                print(u)
                                old = r[cc]
                                print('Current', u, '   :', old)
                                new = input('Enter new ' + u + '   :')
                                if ch == '1':
                                    r[cc] = new.upper()
                                if cc == '2':
                                    r[cc] = new.upper()
                            pickle.dump(r, f2)
                            update = True
                            found1 = found
                            found = False
                    except EOFError:
                        pass
                    f1.close()
                    f2.close()
                    if update:
                        print()
                        print(u.upper(), 'was updated successfully :)\n')
                        os.remove('Student_details.dat')
                        os.rename('Student_details1.dat', 'Student_details.dat')
                    elif not found:
                        print('\n!!! Student ID not found !!!\n')
                    elif update == False and found == True:
                        os.remove('Student_details1.dat')
                        print('\nSorry, an unexpected error occurred :(\n')
                    c = input('\nDo you want to update again [Y -> Yes, B -> Back, E -> Exit]   :')
                    if c.upper() == 'B':
                        break
                    elif c.upper() == 'E':
                        exit()
                    elif c not in 'yY':
                        break

    @staticmethod
    def deleteStudent():
        """Delete a student from the database."""
        while True:
            with open('Student_details.dat', 'rb') as f1:
                with open('Student_details1.dat', 'wb') as f2:
                    found = False
                    update = False
                    sid = input('Enter student id   :')
                    try:
                        while True:
                            r = pickle.load(f1)
                            if r[0] == sid.upper() and r[3] == 'AVAILABLE':
                                found = True
                                if found:
                                    str = 'DELETED'
                                    r[1] = str
                                    r[2] = str
                                    r[3] = str
                                    update = True
                            pickle.dump(r, f2)
                    except EOFError:
                        pass
                    f1.close()
                    f2.close()
                    if update:
                        print()
                        print('Record was deleted successfully :)')
                        os.remove('Student_details.dat')
                        os.rename('Student_details1.dat', 'Student_details.dat')
                    elif found == False:
                        print('\n!!! Student ID not found !!!\n')
                    elif update == False and found == True:
                        print('Sorry, an unexpected error occurred :(')
                    c = input('Do you want to try again [Y -> Yes, B -> Back, E -> Exit]   :')
                    if c.upper() == 'B':
                        break
                    elif c.upper() == 'E':
                        exit()
                    elif c not in 'yY':
                        break

    @staticmethod
    def displayStudent():
        """Display all available students."""
        with open('Student_details.dat', 'rb') as f:
            l = [['SID', 'NAME', 'GRADE']]
            try:
                while True:
                    r = pickle.load(f)
                    if r[3] == 'AVAILABLE':
                        l1 = [r[0], r[1], r[2]]
                        l.append(l1)
            except EOFError:
                print(tabulate(l, headers='firstrow', tablefmt='fancy_grid'))
                print('End of Records')
            ch = input('Press B to go back or E to exit: ')
            if ch.upper() == 'B':
                return
            elif ch.upper() == 'E':
                exit()

class Marks:
    @staticmethod
    def addOrUpdateMarks():
        """Add or update marks for a student."""
        while True:
            with open('Marks.dat', 'ab+') as f:
                with open('Student_details.dat', 'rb') as f1:
                    sid = input('Enter student ID   :')
                    with open('Marks.dat', 'rb') as f3:
                        try:
                            found = False
                            while True:
                                r = pickle.load(f3)
                                if r[0] == sid.upper():
                                    found = True
                                    math = r[1]
                                    phy = r[2]
                                    chem = r[3]
                                    cs = r[4]
                                    eng = r[5]
                        except EOFError:
                            print('Loading.....')
                        f3.close()
                    try:
                        found1 = False
                        while True:
                            r = pickle.load(f1)
                            if r[0] == sid.upper() and r[3] == 'AVAILABLE':
                                found1 = True
                                st_div = r[3]
                    except EOFError:
                        pass
                    if not found1:
                        print('\n!!! No student found with the given ID !!!\n')
                    f1.close()
                    if found1:
                        t_sub = input("Enter subject [MATHEMATICS, PHYSICS, CHEMISTRY, COMPUTER SCIENCE, ENGLISH]   : ")
                        if t_sub.upper() == 'MATHEMATICS':
                            sub = 1
                        elif t_sub.upper() == 'PHYSICS':
                            sub = 2
                        elif t_sub.upper() == 'CHEMISTRY':
                            sub = 3
                        elif t_sub.upper() == 'COMPUTER SCIENCE':
                            sub = 4
                        elif t_sub.upper() == 'ENGLISH':
                            sub = 5
                        else:
                            print('!!! Invalid subject !!!')
                        print('SUBJECT               : ', t_sub)
                        theory = input('Enter theory marks    [80]    : ')
                        if int(theory) > 80:
                            print('!!! Theory marks should be less than 80 !!! ')
                        pract = input('Enter practical marks [20]    : ')
                        if int(pract) > 20:
                            print('!!! Practical marks should be less than 20 !!! ')
                        if int(theory) < 81 and int(pract) < 21:
                            if not found:
                                if sub == 1:
                                    l = [sid.upper(), [theory, pract], ['0', '0'], ['0', '0'], ['0', '0'], ['0', '0']]
                                elif sub == 2:
                                    l = [sid.upper(), ['0', '0'], [theory, pract], ['0', '0'], ['0', '0'], ['0', '0']]
                                elif sub == 3:
                                    l = [sid.upper(), ['0', '0'], ['0', '0'], [theory, pract], ['0', '0'], ['0', '0']]
                                elif sub == 4:
                                    l = [sid.upper(), ['0', '0'], ['0', '0'], ['0', '0'], [theory, pract], ['0', '0']]
                                elif sub == 5:
                                    l = [sid.upper(), ['0', '0'], ['0', '0'], ['0', '0'], ['0', '0'], [theory, pract]]
                                pickle.dump(l, f)
                            if found:
                                if sub == 1:
                                    l = [sid.upper(), [theory, pract], phy, chem, cs, eng]
                                elif sub == 2:
                                    l = [sid.upper(), math, [theory, pract], chem, cs, eng]
                                elif sub == 3:
                                    l = [sid.upper(), math, phy, [theory, pract], cs, eng]
                                elif sub == 4:
                                    l = [sid.upper(), math, phy, chem, [theory, pract], eng]
                                elif sub == 5:
                                    l = [sid.upper(), math, phy, chem, cs, [theory, pract]]
                                with open('Marks.dat', 'rb') as f4:
                                    with open('Marks1.dat', 'wb+') as f5:
                                        try:
                                            update = False
                                            while True:
                                                r = pickle.load(f4)
                                                if r[0] == sid.upper():
                                                    update = True
                                                    r = l
                                                pickle.dump(r, f5)
                                        except EOFError:
                                            pass
                                        f4.close()
                                        f5.close()
                                        if update:
                                            f.close()
                                            os.remove('Marks.dat')
                                            os.rename('Marks1.dat', 'Marks.dat')
                                        elif not update:
                                            os.remove('Marks1.dat')
                    ch = input('Do you want to add or update more marks [Y -> Yes, B -> Back, E -> Exit] :')
                    if ch.upper() == 'B':
                        break
                    elif ch.upper() == 'E':
                        exit()
                    elif ch not in 'Yy':
                        break

    @staticmethod
    def displayMarks():
        """Display marks for all students."""
        with open('Marks.dat', 'rb') as f:
            l = [['SID', 'MATH THEORY', 'MATH PRACT', 'PHY THEORY', 'PHY PRACT', 'CHEM THEORY', 'CHEM PRACT', 'CS THEORY', 'CS PRACT', 'ENG THEORY', 'ENG PRACT']]
            try:
                while True:
                    r = pickle.load(f)
                    l1 = [r[0], r[1][0], r[1][1], r[2][0], r[2][1], r[3][0], r[3][1], r[4][0], r[4][1], r[5][0], r[5][1]]
                    l.append(l1)
            except EOFError:
                print(tabulate(l, headers='firstrow', tablefmt='fancy_grid'))
                print('-' * 20, 'End of Records', '-' * 20)
            ch = input('Press B to go back or E to exit: ')
            if ch.upper() == 'B':
                return
            elif ch.upper() == 'E':
                exit()

class Report:
    @staticmethod
    def gradeCalc(l):
        """Calculate grade based on marks."""
        if l > 85 and l <= 100:
            grade = 'A1'
        elif l > 80 and l <= 85:
            grade = 'A2'
        elif l > 70 and l <= 80:
            grade = 'B1'
        elif l > 60 and l <= 70:
            grade = 'B2'
        elif l > 50 and l <= 60:
            grade = 'C1'
        elif l > 40 and l <= 50:
            grade = 'C2'
        elif l > 32 and l <= 40:
            grade = 'D'
        elif l <= 32:
            grade = 'F [FAILED]'
        return grade

    @staticmethod
    def displayReport():
        """Generate and display a report card for a student."""
        while True:
            with open('Student_details.dat', 'rb') as f:
                with open('Marks.dat', 'rb') as f1:
                    sid = input('Enter student ID   :')
                    try:
                        found = False
                        while True:
                            r = pickle.load(f)
                            if r[0] == sid.upper() and r[3] == 'AVAILABLE':
                                sid = r[0]
                                s_name = r[1]
                                s_grade = r[2]
                                found = True
                    except EOFError:
                        pass
                    found1 = False
                    if found:
                        try:
                            found1 = False
                            while True:
                                r = pickle.load(f1)
                                if r[0] == sid.upper():
                                    math = r[1]
                                    phy = r[2]
                                    chem = r[3]
                                    cs = r[4]
                                    eng = r[5]
                                    found1 = True
                        except EOFError:
                            pass
                    if not found:
                        print('\n!!! Student not found !!!\n')
                    if not found1:
                        print('\n!!! No marks were added for student', sid.upper(), '!!!\n')
                    if found and found1:
                        print('-' * 85)
                        print('MUHNIH SCHOOL'.center(85))
                        print('PO Box: XXXX GitHub HTTPS'.center(85))
                        print('Tel: XX XXX XXXX'.center(85))
                        print('mail@domain.com'.center(85))
                        print('Website: www.github.com'.center(85))
                        print()
                        print('FINAL REPORT CARD - 2020-21'.center(85))
                        print()
                        print('Name of Student   :', s_name)
                        print('Student ID        :', sid)
                        print('Grade             :', s_grade)
                        print()
                        str1 = 'GRADE ' + s_grade + ' YEARLY PERFORMANCE'
                        print(str1.center(85))
                        l = [['SUBJECT', 'THEORY (80)', 'PRACTICAL (20)', 'TOTAL (100)', 'GRADE']]
                        l1 = ['ENGLISH', eng[0], eng[1], int(eng[0]) + int(eng[1])]
                        grade1 = Report.gradeCalc(l1[3])
                        l1.append(grade1)
                        l2 = ['MATHEMATICS', math[0], math[1], int(math[0]) + int(math[1])]
                        grade2 = Report.gradeCalc(l2[3])
                        l2.append(grade2)
                        l3 = ['PHYSICS', phy[0], phy[1], int(phy[0]) + int(phy[1])]
                        grade3 = Report.gradeCalc(l3[3])
                        l3.append(grade3)
                        l4 = ['CHEMISTRY', chem[0], chem[1], int(chem[0]) + int(chem[1])]
                        grade4 = Report.gradeCalc(l4[3])
                        l4.append(grade4)
                        l5 = ['COMPUTER SCICENCE', cs[0], cs[1], int(cs[0]) + int(cs[1])]
                        grade5 = Report.gradeCalc(l5[3])
                        l5.append(grade5)
                        l.append(l1)
                        l.append(l2)
                        l.append(l3)
                        l.append(l4)
                        l.append(l5)
                        print(tabulate(l, headers='firstrow', tablefmt='fancy_grid'))
                        result = [['RESULT - GRADE ', s_grade]]
                        if grade1 == 'F [FAILED]' or grade2 == 'F [FAILED]' or grade3 == 'F [FAILED]' or grade4 == 'F [FAILED]' or grade5 == 'F [FAILED]':
                            rr = ['Detained In Grade ', s_grade]
                        else:
                            rr = ['Passed And Promoted From Grade ', s_grade]
                        result.append(rr)
                        print(tabulate(result, headers='firstrow', tablefmt='grid'))
                        print()
                        print('THANK YOU'.center(85))
                        datentime = str(datetime.now())
                        print('\nPricipal, GITHUB SCHOOL', '                           ', '   issued on:', datentime[0:19])
                        print('-' * 85)
                    
                        print()
                        inp = input("Do you want export report as PDF (Y -> Yes | N -> No): ")
                        if (inp.upper() == 'Y'):
                            Report.generatePDF(sid, s_name, s_grade, math, phy, chem, cs, eng)
                       
                    ch = input('\nPress B to go back or E to exit: ')
                    if ch.upper() == 'B':
                        break
                    elif ch.upper() == 'E':
                        exit()

    @staticmethod
    def generatePDF(sid, s_name, s_grade, math, phy, chem, cs, eng):
        pdf_filename = f"Report_Card_{sid}.pdf"
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        
        styles = getSampleStyleSheet()
        center_style = ParagraphStyle(
            'CenteredStyle',
            parent=styles['Heading1'],
            alignment=TA_CENTER,
        )
        
        story = []
        
        story.append(Paragraph("MUHNIH SCHOOL", center_style))
        story.append(Paragraph("PO Box: XXXX GitHub HTTPS", center_style))
        story.append(Paragraph("Tel: XX XXX XXXX", center_style))
        story.append(Paragraph("mail@domain.com", center_style))
        story.append(Paragraph("Website: www.github.com", center_style))
        story.append(Spacer(1, 12))
        
        story.append(Paragraph("FINAL REPORT CARD - 2020 - 21", center_style))
        story.append(Spacer(1, 12))
        
        student_data = [
            ["Name of Student:", s_name],
            ["Student ID:", sid],
            ["Grade:", s_grade]
        ]
        student_table = Table(student_data, colWidths=[100, 300])
        student_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(student_table)
        story.append(Spacer(1, 12))
        
        grade_perf = f"GRADE {s_grade} YEARLY PERFORMANCE"
        story.append(Paragraph(grade_perf, center_style))
        story.append(Spacer(1, 12))
        
        l1 = ['ENGLISH', eng[0], eng[1], int(eng[0]) + int(eng[1])]
        grade1 = Report.gradeCalc(l1[3])
        l1.append(grade1)
        
        l2 = ['MATHEMATICS', math[0], math[1], int(math[0]) + int(math[1])]
        grade2 = Report.gradeCalc(l2[3])
        l2.append(grade2)
        
        l3 = ['PHYSICS', phy[0], phy[1], int(phy[0]) + int(phy[1])]
        grade3 = Report.gradeCalc(l3[3])
        l3.append(grade3)
        
        l4 = ['CHEMISTRY', chem[0], chem[1], int(chem[0]) + int(chem[1])]
        grade4 = Report.gradeCalc(l4[3])
        l4.append(grade4)
        
        l5 = ['COMPUTER SCIENCE', cs[0], cs[1], int(cs[0]) + int(cs[1])]
        grade5 = Report.gradeCalc(l5[3])
        l5.append(grade5)
        
        marks_data = [
            ['SUBJECT', 'THEORY (80)', 'PRACTICAL (20)', 'TOTAL (100)', 'GRADE'],
            l1, l2, l3, l4, l5
        ]
        
        marks_table = Table(marks_data, colWidths=[120, 80, 100, 80, 80])
        marks_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(marks_table)
        story.append(Spacer(1, 12))
        
        result_data = [
            ['RESULT - GRADE ', s_grade]
        ]
        
        if grade1 == 'F [FAILED]' or grade2 == 'F [FAILED]' or grade3 == 'F [FAILED]' or grade4 == 'F [FAILED]' or grade5 == 'F [FAILED]':
            result_data.append(['Detained In Grade ', s_grade])
        else:
            result_data.append(['Passed And Promoted From Grade ', s_grade])
        
        result_table = Table(result_data, colWidths=[200, 100])
        result_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(result_table)
        story.append(Spacer(1, 24))
        
        story.append(Paragraph("THANK YOU", center_style))
        story.append(Spacer(1, 24))
        
        datentime = str(datetime.now())
        signature_data = [
            ["Principal, GITHUB SCHOOL", f"issued on: {datentime[0:19]}"]
        ]
        signature_table = Table(signature_data, colWidths=[300, 200])
        signature_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(signature_table)
        
        doc.build(story)
        print(f"\nReport card saved as {pdf_filename} successfully :)\n")
        

def main():
    """Main function to run the program."""
    print('MUHNIH SCHOOL'.center(85))
    print('PO Box: XXXX GitHub HTTPS'.center(85))
    print('Tel: XX XXX XXXX'.center(85))
    print('mail@domain.com'.center(85))
    print('Website: www.github.com'.center(85))
    print()
    print('Welcome to MUHNIH SCHOOL'.center(85))
    while True:
        print('''Choose an option:
              1. Manage Student Marks
              2. Manage Student List
              3. Generate Report Card
              4. Exit''')
        ch = int(input("Enter your choice: "))
        if ch == 1:
            while True:
                print('''Choose an option:
                      1. Add or Update Marks
                      2. Display Marks
                      3. Back
                      4. Exit''')
                ch1 = int(input("Enter your choice: "))
                if ch1 == 1:
                    Marks.addOrUpdateMarks()
                elif ch1 == 2:
                    Marks.displayMarks()
                elif ch1 == 3:
                    break
                elif ch1 == 4:
                    exit()
                else:
                    print('Please choose a valid option :(')

        elif ch == 2:
            while True:
                print('''Choose an option:
                      1. Add Student
                      2. Update Student
                      3. Delete Student
                      4. Display Student
                      5. Back
                      6. Exit''')
                ch2 = int(input("Enter your choice: "))
                if ch2 == 1:
                    Student.addStudent()
                elif ch2 == 2:
                    Student.updateStudent()
                elif ch2 == 3:
                    Student.deleteStudent()
                elif ch2 == 4:
                    Student.displayStudent()
                elif ch2 == 5:
                    break
                elif ch2 == 6:
                    exit()
                else:
                    print('Please choose a valid option :(')

        elif ch == 3:
            Report.displayReport()
            
        elif ch == 4:
            print('Thank you for using MUHNIH SCHOOL')
            break
        else:
            print('Please choose a valid option :(')

if __name__ == '__main__':
    main()
