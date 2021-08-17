import unittest
import shape
from unittest import mock

class TestShape(unittest.TestCase):
# test_Aspect_Ratio
    def test_Aspect_Ratio_positive(self):
        data1 = 12
        data2 = 20
        expected = 0.6
        result = shape.Aspect_Ratio(data1, data2)
        self.assertEqual(expected, result)
    
    def test_Aspect_Ratio_negative(self):
        data1 = -40
        data2 = 20
        expected = -2.0
        result = shape.Aspect_Ratio(data1, data2)
        self.assertEqual(expected, result)

# test_triangle
    @mock.patch('shape.WLForTriangle')
    def test_triangle(self, trianglemock):
        w = 8
        h = 8
        expected = 32.0
        trianglemock.return_value = 64
        result = shape.triangle(w, h)
        self.assertEqual(expected, result)

    def test_WLForTriangle(self):
        w = 5
        h = 5
        expected = 25
        result = shape.WLForTriangle(w, h)
        self.assertEqual(expected, result)
# test_Trapezoidaltri
    @mock.patch('shape.WLTrapezoidalTriangle')
    def test_Trapezoidaltri(self, TrapezoidaltrileMock):
        w = 8
        l = 8
        h = 4
        expected = 32
        TrapezoidaltrileMock.return_value = 16
        result = shape.TrapezoidalTriangle(w, l, h)
        self.assertEqual(expected, result)

    def test_WLTrapezoidalTriangle(self):
        w = 5
        h = 5
        expected = 10
        result = shape.WLTrapezoidalTriangle(w, h)
        self.assertEqual(expected, result)
# test_rhombic_area
    @mock.patch('shape.sum_area_wl')
    def test_rhombic_area(self, rhombic_area_mock):
        w = 4
        h = 2
        expected = 4
        rhombic_area_mock.return_value = 8
        result = shape.rhombic_area(w, h)
        self.assertEqual(expected, result)

    def test_sum_area_wl(self):
        w = 4
        h = 2
        expected = 8
        result = shape.sum_area_wl(w, h)
        self.assertEqual(expected, result)
