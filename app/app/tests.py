from django.test import TestCase
from app.calc import addNumbers, subtractNumbers


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Testing function for Adding numbers fnctions"""
        self.assertEqual(addNumbers(3, 8), 11)
        
    def test_subtract_num(self):
        """"testing subtraction"""
        self.assertEqual(subtractNumbers(4, 2), 2)
