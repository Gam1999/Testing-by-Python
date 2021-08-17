import unittest
import employee

class TestEmployee(unittest.TestCase):
    def Test_Bonus_50000(self):
        data = 2000
        expected = 200
        result = employee.Employee(data).get_bonus()
        self.assertEqual(expected, result)

    def Test_Tax_60000(self):
        data = 60000
        expected = 6000
        result = employee.Employee(data).get_tax()
        self.assertEquals(expected, result)

    def Test_Bonus_50000(self):
        data = 5000
        expected = 500
        result = employee.Employee(data).get_bonus()
        self.assertEqual(expected, result)

    def test_bonus_3000(self):
        data = 3000
        expected = 300
        result = employee.Employee(data).get_bonus()
        self.assertEqual(expected, result)

    def test_tax_3000(self):
        data = 3000
        expected = 231
        result = employee.Employee(data).get_tax()
        self.assertEqual(expected, result)

    def test_bonus_6000(self):
        data = 6000
        expected = 600
        result = employee.Employee(data).get_bonus()
        self.assertEqual(expected, result)