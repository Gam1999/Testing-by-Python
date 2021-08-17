
import unittest
import equation
from unittest import mock

class TestEquation(unittest.TestCase):
    # test_square_root
    def test_square_root(self):
        data = 8
        expected = 2.8284271247461903
        result = equation.square_root(data)
        self.assertEqual(expected, result)

# test_Equivalent_Diameter
    @mock.patch('equation.coutour_area')
    def test_Equivalent_Diameter(self, Equivalent_DiameterMock):
        c = 8
        expected = 1.7320508075688772
        Equivalent_DiameterMock.return_value = 3
        result = equation.Equivalent_Diameter(c)
        self.assertEqual(expected, result)

    def test_coutour_area(self):
        c = 4
        expected = 20.38216560509554
        result = equation.coutour_area(c)
        self.assertEqual(expected, result)