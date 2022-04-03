class grade:
    def __init__(self, grade: int, scale: int) -> None:
        if type(grade) is not int:
            if not (type(grade) is str and grade.isdigit() is True) and not (type(grade) is float and grade.is_integer() is True):
                raise ValueError("Grade must be an integer")
        if type(scale) is not int:
            if not (type(scale) is str and scale.isdigit() is True) and not (type(scale) is float and scale.is_integer() is True):
                raise ValueError("Scale must be an integer")
        grade = int(grade)
        scale = int(scale)
        if(grade > 6):
            raise ValueError("Grade cannot be greater than 6")
        if(grade < 1):
            raise ValueError("Grade cannot be less than 1")
        if(scale > 10):
            raise ValueError("Scale cannot be greater than 10")
        if(scale < 1):
            raise ValueError("Scale cannot be less than 1")
        self.grade = grade
        self.scale = scale

    def get_grade(self) -> int:
        return self.grade

    def get_scale(self) -> int:
        return self.scale

    def set_grade(self, grade: int) -> None:
        if type(grade) is not int:
            if not (type(grade) is str and grade.isdigit() is True) and not (type(grade) is float and grade.is_integer() is True):
                raise ValueError("Grade must be an integer")
        grade = int(grade)
        if(grade > 6):
            raise ValueError("Grade cannot be greater than 6")
        if(grade < 1):
            raise ValueError("Grade cannot be less than 1")
        self.grade = grade

    def set_scale(self, scale: int) -> None:
        if type(scale) is not int:
            if not (type(scale) is str and scale.isdigit() is True) and not (type(scale) is float and scale.is_integer() is True):
                raise ValueError("Scale must be an integer")
        scale = int(scale)
        if(scale > 10):
            raise ValueError("Scale cannot be greater than 10")
        if(scale < 1):
            raise ValueError("Scale cannot be less than 1")
        self.scale = scale