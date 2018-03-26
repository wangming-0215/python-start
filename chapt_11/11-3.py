import unittest


class Employee():
    def __init__(self, first, last, salary):
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    def get_raise(self, range=5000):
        self.salary += range


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('wang', 'ming', 5000)

    def test_get_default_raise(self):
        self.employee.get_raise()
        self.assertEqual(self.employee.salary, 5000 + 5000)

    def test_get_7000_raise(self):
        self.employee.get_raise(7000)
        self.assertEqual(self.employee.salary, 5000 + 7000)


unittest.main()
