import unittest
from parameterized import parameterized_class
from assertpy import assert_that
from src.subject import *

@parameterized_class(('value', 'error'), [
    (1, ValueError),
    (1.5, ValueError),
    (True, ValueError),
    (None, ValueError),
    ("", ValueError),
    ([1,2,3], ValueError),
    ({'name': 2, 'grades': 4}, ValueError),
])

class SubjectParamerizedTest1(unittest.TestCase):
    def setUp(self):
        self.temp = subject("Matematyka")
    
    def test_subject_init_wrong_name(self):
        assert_that(self.temp.__init__).raises(self.error).when_called_with(self.value)

    def test_subject_set_name_wrong(self):
        assert_that(self.temp.set_name).raises(self.error).when_called_with(self.value)

    def tearDown(self):
        del self.temp

@parameterized_class(('value', 'error'), [
    ("grade", ValueError),
    ("", ValueError),
    (0, ValueError),
    (25, ValueError),
    (1.5, ValueError),
    (True, ValueError),
    (None, ValueError),
    ([1,2,3], ValueError),
    ({grade: 1}, ValueError),
])
class SubjectParamerizedTest2(unittest.TestCase):
    def setUp(self):
        self.temp = subject("Matematyka")

    def test_subject_add_grade_wrong(self):
        assert_that(self.temp.add_grade).raises(self.error).when_called_with(self.value)

    def test_subject_find_grade_wrong_grade(self):
        assert_that(self.temp.find_grade).raises(self.error).when_called_with(self.value, 10)    

    def test_subject_find_grade_wrong_scale(self):
        assert_that(self.temp.find_grade).raises(self.error).when_called_with(5, self.value)

    def test_subject_change_grade_wrong_grade(self):
        self.temp.add_grade(grade("1", "2"))
        assert_that(self.temp.change_grade).raises(self.error).when_called_with(1, 2, self.value, 4)

    def test_subject_change_grade_wrong_scale(self):
        self.temp.add_grade(grade("1", "2"))
        assert_that(self.temp.change_grade).raises(self.error).when_called_with(1, 2, 3, self.value)
    
    def test_subject_delete_grade_wrong_grade(self):
        assert_that(self.temp.delete_grade).raises(self.error).when_called_with(self.value, 5)

    def test_subject_delete_grade_wrong_scale(self):
        assert_that(self.temp.delete_grade).raises(self.error).when_called_with(1, self.value)

    def tearDown(self):
        del self.temp

class SubjectTest(unittest.TestCase):
    def setUp(self):
        self.temp = subject("Matematyka")

    def test_subject_init(self):
        assert_that(self.temp).is_not_none()

    def test_subject_set_name(self):
        self.temp.set_name("Informatyka")
        assert_that(self.temp.name).is_equal_to("Informatyka")

    def test_subject_get_name(self):
        assert_that(self.temp.get_name()).is_type_of(str)

    def test_subject_get_grades(self):
        self.temp.add_grade(grade("1", "2"))
        assert_that(self.temp.get_grades()).is_length(1)

    def test_subject_add_grade(self):
        AddedGrade = grade("1", "2")
        self.temp.add_grade(AddedGrade)
        assert_that(self.temp.grades).contains(AddedGrade)

    def test_subject_find_grade_true(self):
        self.temp.add_grade(grade("1", "2"))
        assert_that(self.temp.find_grade("1", "2")).is_instance_of(grade)

    def test_subject_find_grade_false(self):
        assert_that(self.temp.find_grade("1", "2")).is_none()

    def test_subject_change_grade(self):
        self.temp.add_grade(grade("1", "2"))
        self.temp.change_grade("1", "2", "3", "4")
        assert_that(self.temp.find_grade("3", "4")).is_not_none()

    def test_subject_change_grade_without_grade(self):
        self.temp.change_grade(1, 2, 3, 4)
        assert_that(self.temp.find_grade(3, 4)).is_none()

    def test_subject_mean_without_grades(self):
        assert_that(self.temp.mean()).is_zero()

    def test_subject_delete_grade(self):
        self.temp.add_grade(grade("1", "2"))
        self.temp.delete_grade("1", "2")
        assert_that(self.temp.find_grade("1", "2")).is_none()

    def test_subject_delete_grade_without_grade(self):
        self.temp.delete_grade(1, 2)
        assert_that(self.temp.find_grade(1, 2)).is_none()

    def test_subject_mean_with_grades(self):
        self.temp.add_grade(grade("1", "2"))
        self.temp.add_grade(grade("3", "1"))
        self.temp.add_grade(grade("5", "6"))
        assert_that(self.temp.mean()).is_close_to(3.9, 0.1)

    def test_subject_mean_from_file(self):
      fileTest = open("data/Grades_Sample")
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            if len(data) == 2:
                self.temp.add_grade(grade(data[0], data[1].strip("\n")))
            else:
                mean = data[0].strip("\n")
                assert_that(self.temp.mean()).is_close_to(float(mean), 0.1)
      fileTest.close()

    def tearDown(self):
        del self.temp