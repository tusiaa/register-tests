import unittest
import os.path
from parameterized import parameterized_class
from assertpy import assert_that
from src.register import *

@parameterized_class(('value', 'error'), [
    (1, ValueError),
    (1.5, ValueError),
    (True, ValueError),
    (None, ValueError),
    ("", ValueError),
    ([1,2,3], ValueError),
    ({'name': 2, 'grades': 4}, ValueError),
])
class RegisterParamerizedTest1(unittest.TestCase):
    def setUp(self):
        self.temp = register()

    def test_register_add_student_wrong_name(self):
        assert_that(self.temp.add_student).raises(self.error).when_called_with(self.value, "Kowalski", "96032687885")

    def test_register_add_student_wrong_surname(self):
        assert_that(self.temp.add_student).raises(self.error).when_called_with("Jan", self.value, "96032687885")

    def test_register_find_students_by_name_wrong(self):
        assert_that(self.temp.find_by_name).raises(self.error).when_called_with(self.value)

    def test_register_find_students_by_surname_wrong(self):
        assert_that(self.temp.find_by_surname).raises(self.error).when_called_with(self.value)

    def test_register_find_students_by_name_and_surname_wrong_name(self):
        assert_that(self.temp.find_by_name_and_surname).raises(self.error).when_called_with(self.value, "Kowalski")

    def test_register_find_students_by_name_and_surname_wrong_surname(self):
        assert_that(self.temp.find_by_name_and_surname).raises(self.error).when_called_with("Jan", self.value)

    def test_register_change_student_name_wrong_name(self):
        assert_that(self.temp.change_student_name).raises(self.error).when_called_with("96032687885", self.value)

    def test_register_change_student_surname_wrong_surname(self):
        assert_that(self.temp.change_student_surname).raises(self.error).when_called_with("96032687885", self.value)

    def test_register_import_students_wrong_file(self):
        assert_that(self.temp.import_students).raises(self.error).when_called_with(self.value)

    def test_register_export_students_wrong_file(self):
        assert_that(self.temp.export_students).raises(self.error).when_called_with(self.value)

    def test_register_import_remarks_wrong_file(self):
        assert_that(self.temp.import_remarks).raises(self.error).when_called_with(self.value)

    def test_register_export_remarks_wrong_file(self):
        assert_that(self.temp.export_remarks).raises(self.error).when_called_with(self.value)

    def test_register_import_from_json_wrong_file(self):
        assert_that(self.temp.import_from_json).raises(self.error).when_called_with(self.value)

    def test_register_export_to_json_wrong_file(self):
        assert_that(self.temp.export_to_json).raises(self.error).when_called_with(self.value)

    def test_register_send_confirmation_email_wrong_email(self):
        assert_that(self.temp.send_confirmation_email).raises(self.error).when_called_with(self.value, "Action")

    def test_register_send_confirmation_email_wrong_action(self):
        assert_that(self.temp.send_confirmation_email).raises(ValueError).when_called_with("python.test.email146@gmail.com", self.value)

    def tearDown(self):
        del self.temp
    
@parameterized_class(('value', 'error'), [
    ("", ValueError),
    ("123456789", ValueError),
    ("96032687886", ValueError),
    ("96033687884", ValueError),
    ("12345678910", ValueError),
    (96032687886, ValueError),
    (9603.2687885, ValueError),
    (True, ValueError),
    (None, ValueError),
    ([1,2,3], ValueError),
    ({'name': 2, 'grades': 4}, ValueError),
])
class RegisterParamerizedTest2(unittest.TestCase):
    def setUp(self):
        self.temp = register()

    def test_register_add_student_wrong_pesel(self):
        assert_that(self.temp.add_student).raises(self.error).when_called_with("Jan", "Kowalski", self.value)

    def test_register_add_student_wrong_object(self):
        assert_that(self.temp.add_student).raises(self.error).when_called_with(self.value)

    def test_register_find_student_by_pesel_wrong(self):
        assert_that(self.temp.find_by_pesel).raises(self.error).when_called_with(self.value)

    def test_register_delete_student_wrong(self):
        assert_that(self.temp.delete_student).raises(self.error).when_called_with(self.value)

    def test_register_change_student_name_wrong_pesel(self):
        assert_that(self.temp.change_student_name).raises(self.error).when_called_with(self.value, "Jan")

    def test_register_change_student_surname_wrong_pesel(self):
        assert_that(self.temp.change_student_surname).raises(self.error).when_called_with(self.value, "Kowalski")

    def test_register_change_student_pesel_wrong_old_pesel(self):
        assert_that(self.temp.change_student_pesel).raises(self.error).when_called_with(self.value, "96032687885")
    
    def test_register_change_student_pesel_wrong_new_pesel(self):
        assert_that(self.temp.change_student_pesel).raises(self.error).when_called_with("96032687885", self.value)

    def tearDown(self):
        del self.temp

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.temp = register()

    def test_register_init(self):
        assert_that(self.temp).is_not_none()

    def test_register_add_student_by_data(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        assert_that(self.temp.get_students()).is_length(1)

    def test_register_add_student_by_object(self):
        Student = student("Jan", "Kowalski", "96032687885")
        self.temp.add_student(Student)
        assert_that(self.temp.get_students()).contains(Student)

    def test_register_add_student_by_data_already_exists(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        assert_that(self.temp.add_student).raises(ValueError).when_called_with("Jan", "Kowalski", "96032687885")

    def test_register_add_student_by_object_already_exists(self):
        Student = student("Jan", "Kowalski", "96032687885")
        self.temp.add_student(Student)
        assert_that(self.temp.add_student).raises(ValueError).when_called_with(Student)

    def test_register_delete_student_by_pesel(self):
        self.temp.add_student("Jan", "Kowalski", "94071449639")
        self.temp.delete_student("94071449639")
        assert_that(self.temp.find_by_pesel("94071449639")).is_none()

    def test_register_delete_student_by_pesel_not_found(self):
        self.temp.delete_student("94071449639")
        assert_that(self.temp.find_by_pesel("94071449639")).is_none()

    def test_register_delete_student_by_object(self):
        Student = student("Jan", "Kowalski", "96032687885")
        self.temp.add_student(Student)
        self.temp.delete_student(Student)
        assert_that(self.temp.get_students()).is_empty()

    def test_register_delete_student_by_object_not_found(self):
        Student = student("Jan", "Kowalski", "96032687885")
        self.temp.delete_student(Student)
        assert_that(self.temp.get_students()).is_empty()

    def test_register_get_students(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.add_student("Jan", "Kowalski", "94071449639")
        assert_that(self.temp.get_students()).is_length(2)

    def test_register_find_student_by_pesel(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        assert_that(self.temp.find_by_pesel("96032687885")).is_instance_of(student)

    def test_register_find_student_by_pesel_not_found(self):
        assert_that(self.temp.find_by_pesel("94071449639")).is_none()

    def test_register_find_students_by_name(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.add_student("Jan", "Nowak", "03241311845")
        self.temp.add_student("Jan", "Konkol", "94071449639")
        assert_that(self.temp.find_by_name("Jan")).is_length(3)

    def test_register_find_students_by_name_not_found(self):
        assert_that(self.temp.find_by_name("Jan")).is_empty()

    def test_register_find_students_by_surname(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.add_student("Ania", "Kowalski", "03241311845")
        self.temp.add_student("Karol", "Kowalski", "94071449639")
        assert_that(self.temp.find_by_surname("Kowalski")).is_length(3)

    def test_register_find_students_by_surname_not_found(self):
        assert_that(self.temp.find_by_surname("Kowalski")).is_empty()

    def test_register_find_students_by_name_and_surname(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.add_student("Jan", "Kowalski", "03241311845")
        assert_that(self.temp.find_by_name_and_surname("Jan", "Kowalski")).is_length(2)

    def test_register_find_students_by_name_and_surname_not_found(self):
        assert_that(self.temp.find_by_name_and_surname("Jan", "Kowalski")).is_empty()

    def test_register_change_student_name(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.change_student_name("96032687885", "Karol")
        assert_that(self.temp.find_by_pesel("96032687885").get_name()).is_equal_to("Karol")

    def test_register_change_student_name_not_found(self):
        self.temp.change_student_name("96032687885", "Karol")
        assert_that(self.temp.find_by_pesel("96032687885")).is_none()

    def test_register_change_student_surname(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.change_student_surname("96032687885", "Nowak")
        assert_that(self.temp.find_by_pesel("96032687885").get_surname()).is_equal_to("Nowak")

    def test_register_change_student_surname_not_found(self):
        self.temp.change_student_surname("96032687885", "Nowak")
        assert_that(self.temp.find_by_pesel("96032687885")).is_none()

    def test_register_change_student_pesel(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.change_student_pesel("96032687885", "03241311845")
        assert_that(self.temp.find_by_pesel("03241311845")).is_not_none()

    def test_register_change_student_pesel_not_found(self):
        self.temp.change_student_pesel("96032687885", "03241311845")
        assert_that(self.temp.find_by_pesel("03241311845")).is_none()

    def test_register_change_student_pesel_already_exists(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.add_student("Jan", "Nowak", "03241311845")
        assert_that(self.temp.change_student_pesel).raises(ValueError).when_called_with("96032687885", "03241311845")

    def test_register_import_students_from_file(self):
        self.temp.import_students("data/Students_Import.csv")
        assert_that(self.temp.get_students()).is_length(3)

    def test_register_import_students_from_file_not_found(self):
        assert_that(self.temp.import_students).raises(FileNotFoundError).when_called_with("students.csv")

    def test_register_export_students_to_file(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.find_by_pesel("96032687885").add_subject("Matematyka")
        self.temp.find_by_pesel("96032687885").find_subject("Matematyka").add_grade(grade(5, 5))
        self.temp.find_by_pesel("96032687885").find_subject("Matematyka").add_grade(grade(1, 2))
        self.temp.find_by_pesel("96032687885").add_subject("Informatyka")
        self.temp.add_student("Jan", "Nowak", "03241311845")
        self.temp.export_students("data/Students_Export.csv")
        assert_that(os.path.isfile("data/Students_Export.csv")).is_true()

    def test_register_import_remarks_from_file(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.import_remarks("data/Remarks_Import.csv")
        assert_that(self.temp.find_by_pesel("96032687885").get_remarks()).is_length(3)

    def test_register_import_remarks_from_file_not_found(self):
        assert_that(self.temp.import_remarks).raises(FileNotFoundError).when_called_with("remarks.csv")

    def test_register_export_remarks_to_file(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.find_by_pesel("96032687885").add_remark("Zaliczenie")
        self.temp.export_remarks("data/Remarks_Export.csv")
        assert_that(os.path.isfile("data/Remarks_Export.csv")).is_true()

    def test_register_import_from_json(self):
        self.temp.import_from_json("data/Register_Import.json")
        assert_that(self.temp.get_students()).is_length(3)

    def test_register_import_from_json_not_found(self):
        assert_that(self.temp.import_from_json).raises(FileNotFoundError).when_called_with("students.json")

    def test_register_export_to_json(self):
        self.temp.add_student("Jan", "Kowalski", "96032687885")
        self.temp.find_by_pesel("96032687885").add_subject("Matematyka")
        self.temp.find_by_pesel("96032687885").find_subject("Matematyka").add_grade(grade(5, 5))
        self.temp.find_by_pesel("96032687885").find_subject("Matematyka").add_grade(grade(1, 2))
        self.temp.find_by_pesel("96032687885").add_subject("Informatyka")
        self.temp.add_student("Jan", "Nowak", "03241311845")
        self.temp.find_by_pesel("03241311845").add_remark("Nowy")
        self.temp.find_by_pesel("03241311845").add_remark("Zaliczenie")
        self.temp.export_to_json("data/Register_Export.json")
        assert_that(os.path.isfile("data/Register_Export.json")).is_true()

    def test_register_send_confirmation_email(self):
        assert_that(self.temp.send_confirmation_email("python.test.email146@gmail.com", "Added student")).contains("success")

    def tearDown(self):
        del self.temp