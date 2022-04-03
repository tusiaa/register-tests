import unittest
from src.grade import *

class GradeTest(unittest.TestCase):

    def setUp(self):
        self.temp = grade(5, 5)

    def test_grade_init(self):
        self.assertNotEqual(self.temp, None)

    def test_grade_init_grade_to_big(self):
        with self.assertRaises(ValueError):
            grade(10, 5)

    def test_grade_init_grade_to_small(self):
        with self.assertRaises(ValueError):
            grade(-1, 5)

    def test_grade_init_scale_to_big(self):
        with self.assertRaises(ValueError):
            grade(5, 20)

    def test_grade_init_scale_to_small(self):
        with self.assertRaises(ValueError):
            grade(5, -1)

    def test_grade_init_grade_to_big_scale_to_big(self):
        with self.assertRaises(ValueError):
            grade(10, 20)

    def test_grade_init_grade_to_small_scale_to_small(self):
        with self.assertRaises(ValueError):
            grade(-1, -1)

    def test_grade_init_grade_to_big_scale_to_small(self):
        with self.assertRaises(ValueError):
            grade(10, -1)

    def test_grade_init_grade_to_small_scale_to_big(self):
        with self.assertRaises(ValueError):
            grade(-1, 20)

    def test_grade_init_grade_number_string(self):
        self.assertNotEqual(grade("5", 5), None)

    def test_grade_init_scale_number_string(self):
        self.assertNotEqual(grade(5, "5"), None)

    def test_grade_init_grade_number_string_scale_number_string(self):
        self.assertNotEqual(grade("5", "5"), None)

    def test_grade_init_grade_string(self):
        with self.assertRaises(ValueError):
            grade("grade", 5)

    def test_grade_init_scale_string(self):
        with self.assertRaises(ValueError):
            grade(5, "scale")

    def test_grade_init_grade_string_scale_string(self):
        with self.assertRaises(ValueError):
            grade("grade", "scale")

    def test_grade_init_grade_integer_float(self):
        self.assertNotEqual(grade(5.0, 5), None)

    def test_grade_init_scale_integer_float(self):
        self.assertNotEqual(grade(5, 5.0), None)

    def test_grade_init_grade_integer_float_scale_integer_float(self):
        self.assertNotEqual(grade(5.0, 5.0), None)

    def test_grade_init_grade_float(self):
        with self.assertRaises(ValueError):
            grade(5.5, 5)

    def test_grade_init_scale_float(self):
        with self.assertRaises(ValueError):
            grade(5, 5.5)

    def test_grade_init_grade_float_scale_float(self):
        with self.assertRaises(ValueError):
            grade(5.5, 5.5)

    def test_grade_init_grade_bool(self):
        with self.assertRaises(ValueError):
            grade(True, 5)
    
    def test_grade_init_scale_bool(self):
        with self.assertRaises(ValueError):
            grade(5, True)

    def test_grade_init_grade_bool_scale_bool(self):
        with self.assertRaises(ValueError):
            grade(True, True)

    def test_grade_init_grade_None(self):
        with self.assertRaises(ValueError):
            grade(None, 5)

    def test_grade_init_scale_None(self):
        with self.assertRaises(ValueError):
            grade(5, None)

    def test_grade_init_grade_None_scale_None(self):
        with self.assertRaises(ValueError):
            grade(None, None)

    def test_grade_init_grade_empty(self):
        with self.assertRaises(ValueError):
            grade("", 5)

    def test_grade_init_scale_empty(self):
        with self.assertRaises(ValueError):
            grade(5, "")

    def test_grade_init_grade_empty_scale_empty(self):
        with self.assertRaises(ValueError):
            grade("", "")

    def test_grade_init_grade_array(self):
        with self.assertRaises(ValueError):
            grade([1, 2, 3], 5)

    def test_grade_init_scale_array(self):
        with self.assertRaises(ValueError):
            grade(5, [1, 2, 3])

    def test_grade_init_grade_array_scale_array(self):
        with self.assertRaises(ValueError):
            grade([1, 2, 3], [1, 2, 3])

    def test_grade_init_grade_object(self):
        with self.assertRaises(ValueError):
            grade({"grade": 5}, 5)

    def test_grade_init_scale_object(self):
        with self.assertRaises(ValueError):
            grade(5, {"scale": 5})

    def test_grade_init_grade_object_scale_object(self):
        with self.assertRaises(ValueError):
            grade({"grade": 5}, {"scale": 5})

    def test_grade_get_grade(self):
        self.assertEqual(self.temp.get_grade(), 5)

    def test_grade_get_scale(self):
        self.assertEqual(self.temp.get_scale(), 5)

    def test_grade_set_grade(self):
        self.temp.set_grade(6)
        self.assertEqual(self.temp.get_grade(), 6)

    def test_grade_set_grade_to_big(self):
        with self.assertRaises(ValueError):
            self.temp.set_grade(10)

    def test_grade_set_grade_to_small(self):
        with self.assertRaises(ValueError):
            self.temp.set_grade(-1)

    def test_grade_set_grade_number_string(self):
        self.temp.set_grade("6")
        self.assertEqual(self.temp.get_grade(), 6)

    def test_grade_set_grade_string(self):
        with self.assertRaises(ValueError):
            self.temp.set_grade("grade")

    def test_grade_set_grade_integer_float(self):
        self.temp.set_grade(6.0)
        self.assertEqual(self.temp.get_grade(), 6)

    def test_grade_set_grade_float(self):
        with self.assertRaises(ValueError):
            self.temp.set_grade(5.5)

    def test_grade_set_grade_bool(self):
        with self.assertRaises(ValueError):
            self.temp.set_grade(True)

    def test_grade_set_grade_None(self):    
        with self.assertRaises(ValueError):
            self.temp.set_grade(None)

    def test_grade_set_grade_empty(self):
        with self.assertRaises(ValueError):
            self.temp.set_grade("")

    def test_grade_set_grade_array(self):
        with self.assertRaises(ValueError):
            self.temp.set_grade([1, 2, 3])

    def test_grade_set_grade_object(self):
        with self.assertRaises(ValueError):
            self.temp.set_grade({"grade": 5})

    def test_grade_set_scale(self):
        self.temp.set_scale(6)
        self.assertEqual(self.temp.get_scale(), 6)

    def test_grade_set_scale_to_big(self):
        with self.assertRaises(ValueError):
            self.temp.set_scale(20)

    def test_grade_set_scale_to_small(self):
        with self.assertRaises(ValueError):
            self.temp.set_scale(-1)

    def test_grade_set_scale_number_string(self):
        self.temp.set_scale("6")
        self.assertEqual(self.temp.get_scale(), 6)

    def test_grade_set_scale_string(self):
        with self.assertRaises(ValueError):
            self.temp.set_scale("scale")

    def test_grade_set_scale_integer_float(self):
        self.temp.set_scale(6.0)
        self.assertEqual(self.temp.get_scale(), 6)

    def test_grade_set_scale_float(self):
        with self.assertRaises(ValueError):
            self.temp.set_scale(5.5)

    def test_grade_set_scale_bool(self):
        with self.assertRaises(ValueError):
            self.temp.set_scale(True)

    def test_grade_set_scale_None(self):
        with self.assertRaises(ValueError):
            self.temp.set_scale(None)

    def test_grade_set_scale_empty(self):
        with self.assertRaises(ValueError):
            self.temp.set_scale("")

    def test_grade_set_scale_array(self):
        with self.assertRaises(ValueError):
            self.temp.set_scale([1, 2, 3])

    def test_grade_set_scale_object(self):
        with self.assertRaises(ValueError):
            self.temp.set_scale({"scale": 5})

    def tearDown(self):
        del self.temp

    