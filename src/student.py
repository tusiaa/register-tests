from src.subject import *
from src.Pesel_matcher import pesel

class student:
    def __init__(self, name: str, surname: str, Pesel: str):
        if type(Pesel) is int:
            Pesel = str(Pesel)
        if not pesel(Pesel):
            raise ValueError("Pesel must be valid")
        if not name or type(name) != str:
            raise ValueError("Name must be string")
        if not surname or type(surname) != str:
            raise ValueError("Surname must be string")

        self.name = name
        self.surname = surname
        self.pesel = Pesel
        self.subjects = []
        self.remarks = []

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_pesel(self):
        return self.pesel

    def get_subjects(self):
        return self.subjects

    def get_remarks(self):
        return self.remarks

    def set_name(self, name: str):
        if not name or type(name) is not str:
            raise ValueError("Name must be string")
        self.name = name

    def set_surname(self, surname: str):
        if not surname or type(surname) is not str:
            raise ValueError("Surname must be string")
        self.surname = surname
    
    def set_pesel(self, Pesel: str):
        if type(Pesel) is int:
            Pesel = str(Pesel)
        if not pesel(Pesel):
            raise ValueError("Pesel must be valid")
        self.pesel = Pesel

    def add_remark(self, remark: str):
        if not remark or type(remark) is not str:
            raise ValueError("Remark must be string")
        self.remarks.append(remark)

    def delete_remark(self, remark: str):
        if not remark or type(remark) is not str:
            raise ValueError("Remark must be string")
        if remark in self.remarks:
            self.remarks.remove(remark)

    def change_remark(self, old_remark: str, new_remark: str):
        if not old_remark or type(old_remark) is not str:
            raise ValueError("Remark must be string")
        if not new_remark or type(new_remark) is not str:
            raise ValueError("Remark must be string")
        if old_remark in self.remarks:
            self.remarks[self.remarks.index(old_remark)] = new_remark

    def add_subject(self, Subject: subject):
        if type(Subject) is not subject and not (type(Subject) is str and Subject):
            raise ValueError("Subject must be a subject or string")

        if type(Subject) is str:
            Subject = Subject.capitalize()
            if self.find_subject(Subject):
                raise ValueError("Subject already exists")
            self.subjects.append(subject(Subject))

        if type(Subject) is subject:
            Subject.set_name(Subject.get_name().capitalize())
            if self.find_subject(Subject.get_name()):
                raise ValueError("Subject already exists")
            self.subjects.append(Subject)

    def delete_subject(self, Subject: subject):
        if type(Subject) is not subject and not (type(Subject) is str and Subject):
            raise ValueError("Subject must be a subject or string")

        if type(Subject) is str:
            Subject = Subject.capitalize()
            if self.find_subject(Subject):
                self.subjects.remove(self.find_subject(Subject))

        if type(Subject) is subject:
            Subject.set_name(Subject.get_name().capitalize())
            if self.find_subject(Subject.get_name()):
                self.subjects.remove(self.find_subject(Subject.get_name()))

    def find_subject(self, Subject: str):
        if not Subject or type(Subject) is not str:
            raise ValueError("Subject must be string")
        Subject = Subject.capitalize()
        for sub in self.subjects:
            if sub.get_name() == Subject:
                return sub
        return None

    def mean(self):
        sum = 0
        subjects = 0
        for sub in self.subjects:
            if sub.mean() != 0:
                sum += sub.mean()
                subjects += 1
        if subjects != 0:
            return sum / subjects
        return 0

        