from src.grade import *

class subject:
    def __init__(self, name: str):
        if not name or type(name) != str:
            raise ValueError("Name must be a string")
        self.name = name
        self.grades = []

    def get_name(self):
        return self.name

    def get_grades(self):
        return self.grades

    def set_name(self, name: str):
        if not name or type(name) != str:
            raise ValueError("Name must be a string")
        self.name = name

    def add_grade(self, Grade: grade):
        if not isinstance(Grade, grade):
            raise ValueError("Grade must be a grade")
        self.grades.append(Grade)

    def find_grade(self, grade: int, scale: int):
        if type(grade) is not int:
            if not (type(grade) is str and grade.isdigit() is True) and not (type(grade) is float and grade.is_integer() is True):
                raise ValueError("Grade must be an integer")
        if type(scale) is not int:
            if not (type(scale) is str and scale.isdigit() is True) and not (type(scale) is float and scale.is_integer() is True):
                raise ValueError("Scale must be an integer")
        grade = int(grade)
        scale = int(scale)
        if grade > 6 or grade < 1:
            raise ValueError("Grade cannot be greater than 6 or less than 1")
        if scale > 10 or scale < 1:
            raise ValueError("Scale cannot be greater than 10 or less than 1")
        for i in self.grades:
            if i.get_grade() == grade and i.get_scale() == scale:
                return i

    def change_grade(self, grade: int, scale: int, new_grade: int, new_scale: int):
        Grade = self.find_grade(grade, scale)
        if Grade is not None:
            Grade.set_grade(new_grade)
            Grade.set_scale(new_scale)

    def delete_grade(self, grade: int, scale: int):
        Grade = self.find_grade(grade, scale)
        if Grade is not None:
            self.grades.remove(Grade)

    def mean(self):
        sum = 0
        scale = 0
        for i in self.grades:
            sum += i.get_grade()*i.get_scale()
            scale += i.get_scale()
        if scale == 0:
            return 0
        return sum / scale
    