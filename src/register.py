from src.student import *
import csv
import json

class register:
    def __init__(self):
        self.students = []

    def get_students(self):
        return self.students

    def add_student(self, name: str, surname: str = None, pesel: str = None):
        if surname is None and type(name) is student:
            if self.find_by_pesel(name.pesel) is not None:
                raise ValueError("Student already exists")
            self.students.append(name)
        else:
            if self.find_by_pesel(pesel) is not None:
                raise ValueError("Student already exists")
            self.students.append(student(name, surname, pesel))

    def delete_student(self, Pesel: str):
        if type(Pesel) is student:
            for Student in self.students:
                if Student.pesel == Pesel.pesel and Student.name == Pesel.name and Student.surname == Pesel.surname:
                    self.students.remove(Student)
        else:
            if not pesel(Pesel):
                raise ValueError("Invalid pesel")
            for Student in self.students:
                if Student.pesel == Pesel:
                    self.students.remove(Student)

    def find_by_pesel(self, Pesel: str):
        if not pesel(Pesel):
            raise ValueError("Invalid pesel")
        for student in self.students:
            if student.pesel == Pesel:
                return student
    
    def find_by_name(self, name: str):
        if not name or type(name) is not str:
            raise ValueError("Invalid name")
        students = []
        for student in self.students:
            if student.name == name:
                students.append(student)
        return students

    def find_by_surname(self, surname: str):
        if not surname or type(surname) is not str:
            raise ValueError("Invalid surname")
        students = []
        for student in self.students:
            if student.surname == surname:
                students.append(student)
        return students

    def find_by_name_and_surname(self, name: str, surname: str):
        if not name or type(name) is not str:
            raise ValueError("Invalid name")
        if not surname or type(surname) is not str:
            raise ValueError("Invalid surname")
        students = []
        for student in self.students:
            if student.name == name and student.surname == surname:
                students.append(student)
        return students

    def change_student_name(self, Pesel: str, name: str):
        if not pesel(Pesel):
            raise ValueError("Invalid pesel")
        if not name or type(name) is not str:
            raise ValueError("Invalid name")
        if self.find_by_pesel(Pesel):
            self.find_by_pesel(Pesel).set_name(name) 

    def change_student_surname(self, Pesel: str, surname: str):
        if not pesel(Pesel):
            raise ValueError("Invalid pesel")
        if not surname or type(surname) is not str:
            raise ValueError("Invalid surname")
        if self.find_by_pesel(Pesel):
            self.find_by_pesel(Pesel).set_surname(surname)

    def change_student_pesel(self, old_pesel: str, new_pesel: str):
        if not pesel(old_pesel) or not pesel(new_pesel):
            raise ValueError("Invalid pesel")
        if self.find_by_pesel(new_pesel):
            raise ValueError("Student already exists")
        if self.find_by_pesel(old_pesel):
            self.find_by_pesel(old_pesel).set_pesel(new_pesel)

    def import_students(self, file: str):
        if not file or type(file) is not str:
            raise ValueError("Invalid file path")
        try:
            with open(file, "r") as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                headers = next(reader)
                for row in reader:
                    for i in range(0, len(row)):
                        row[i] = row[i].strip(" ")
                    if not self.find_by_pesel(row[0]):
                        self.add_student(row[1], row[2], row[0])
                    if len(row) > 3:
                        if not self.find_by_pesel(row[0]).find_subject(row[3]):
                            self.find_by_pesel(row[0]).add_subject(row[3])
                    if len(row) > 4:
                        self.find_by_pesel(row[0]).find_subject(row[3]).add_grade(grade(row[4], row[5]))
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

    def export_students(self, file: str):
        if not file or type(file) is not str:
            raise ValueError("Invalid file path")
        with open(file, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(["Pesel", "Name", "Surname", "Subject", "Grade", "Scale"])
            for student in self.students:
                if student.get_subjects():
                    for subject in student.get_subjects():
                        if subject.get_grades():
                            for grade in subject.get_grades():
                                writer.writerow([student.pesel, student.name, student.surname, subject.name, grade.grade, grade.scale])
                        else:
                            writer.writerow([student.pesel, student.name, student.surname, subject.name])
                else:
                    writer.writerow([student.pesel, student.name, student.surname])


    def import_remarks(self, file):
        if not file or type(file) is not str:
            raise ValueError("Invalid file path")
        try:
            with open(file, "r") as csv_file:
                reader = csv.reader(csv_file, delimiter=";")
                headers = next(reader)
                for row in reader:
                    if not self.find_by_pesel(row[0]):
                        raise ValueError("Student not found")
                    self.find_by_pesel(row[0]).add_remark(row[1])
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

    def export_remarks(self, file):
        if not file or type(file) is not str:
            raise ValueError("Invalid file path")
        with open(file, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=";")
            writer.writerow(["Pesel", "Remark"])
            for student in self.students:
                if student.get_remarks():
                    for remark in student.get_remarks():
                        writer.writerow([student.pesel, remark])
        
    def import_from_json(self, file):
        if not file or type(file) is not str:
            raise ValueError("Invalid file path")
        try:
            with open(file, "r") as json_file:
                data = json.load(json_file)
                for student in data["students"]:
                    self.add_student(student["name"], student["surname"], student["pesel"])
                    for subject in student["subjects"]:
                        self.find_by_pesel(student["pesel"]).add_subject(subject["name"])
                        for Grade in subject["grades"]:
                            self.find_by_pesel(student["pesel"]).find_subject(subject["name"]).add_grade(grade(Grade["grade"], Grade["scale"]))
                    for remark in student["remarks"]:
                        self.find_by_pesel(student["pesel"]).add_remark(remark)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

    def export_to_json(self, file): 
        if not file or type(file) is not str:
            raise ValueError("Invalid file path")
        with open(file, "w") as json_file:
            data = json.dumps(self, indent=4, default=vars)
            json_file.write(data)

    def send_confirmation_email(self, email: str, action: str):
        import smtplib
        from email.message import EmailMessage

        if not email or type(email) is not str:
            raise ValueError("Invalid email")
        if not action or type(action) is not str:
            raise ValueError("Invalid action")

        sender = 'python.test.email146@gmail.com'
        msg = EmailMessage()
        msg.set_content("Hello,\nThis is a confirmation email for \"%s\" action." % action)

        msg['Subject'] = 'Confirmation email'
        msg['From'] = sender
        msg['To'] = email

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.login(sender, "NoweHaslo")
            smtp_server.send_message(msg)
            smtp_server.close()
            return "Email sent successfully!"
        except Exception as ex:
            raise Exception("Something went wrong: \"%s\"" % ex)
