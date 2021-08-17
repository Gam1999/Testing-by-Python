import unittest
import matrix
import numpy.testing as nptest
from unittest import mock


class TestMatrix(unittest.TestCase):

    def check_result_averagingFillter(self, data, expected):
        result = matrix.averagingFillter(data)
        self.assertEqual(expected, result)

    def check_result_sobel_op(self, data, expected):
        result = matrix.sobel_op(data)
        self.assertEqual(expected, result)

    def check_result_matrixA(self, data, expected):
        result = matrix.matrixA(data)
        self.assertEqual(expected, result)
 
# test_averagingFillter
    def test_averagingFillter_negative(self):
        img = [[-4, -4, -4], 
               [-4, -4, -4],
               [-4, -4, -4]]
        expected = [[-0.4444444444444444, -0.4444444444444444, -0.4444444444444444],
                      [-0.4444444444444444, -0.4444444444444444, -0.4444444444444444],
                      [-0.4444444444444444, -0.4444444444444444, -0.4444444444444444]]
        self.check_result_averagingFillter(img, expected)

    def test_averagingFillter_positive(self):
        img = [[9, 9, 9], 
               [9, 9, 9],
               [9, 9, 9]]
        expected = [[1, 1, 1],
                      [1, 1, 1],
                      [1, 1, 1]]
        self.check_result_averagingFillter(img, expected)

# test_sobel
    @mock.patch('matrix.multiMat')
    def test_sobel_op_sum_zero(self, randmock):
        # SpyAuthorize spy = new SpyAuthorize();
        img = [[9, 9, 9], 
               [9, 9, 9],
               [9, 9, 9]]
        expected = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        randmock.return_value = [[0, 0, 0],
                                 [0, 0, 0],
                                 [0, 0, 0]]
        
        self.check_result_sobel_op(img, expected)

    def test_sobel_op_positive(self):
        img = [[1, 1, 1], 
               [1, 1, 1],
               [2, 2, 2]]
        expected = [[2.0, 2.0, 2.0],
                    [2.8284271247461903, 2.8284271247461903, 2.8284271247461903],
                    [2.0, 2.0, 2.0]]
        self.check_result_sobel_op(img, expected)

    def test_sobel_op_negative(self):
        img = [[-6, -6, -6], 
               [-6, 1, 1],
               [2, 2, 2]]
        expected = [[21.908902300206645, 16.852299546352718, 16.852299546352718],
                      [22.627416997969522, 22.627416997969522, 22.627416997969522],
                      [5.656854249492381, 15.0996688705415, 15.0996688705415]]
        self.check_result_sobel_op(img, expected)

# test_multiMat
    def test_multiMat_negative(self):
        matrix1 = [[-6, -6, -6], 
                   [-6, -1, -1],
                   [-2, -2, -2]]
        matrix2 = [[6, 6, 6], 
                   [6, 1, 1],
                   [2, 2, 2]]
        
        expected = [[-84, -54, -54], 
                    [-44, -39, -39], 
                    [-28, -18, -18]]
        result = matrix.multiMat(matrix1, matrix2)
        self.assertEqual(expected, result)

    def test_multiMat_positive(self):
        matrix1 = [[2, 2, 2], 
                   [2, 4, 4],
                   [6, 6, 6]]
        matrix2 = [[6, 6, 6], 
                   [6, 1, 1],
                   [2, 2, 2]]
        
        expected = [[28, 18, 18], 
                    [44, 24, 24], 
                    [84, 54, 54]]
        result = matrix.multiMat(matrix1, matrix2)
        self.assertEqual(expected, result)

# test_Convolution_Matrix
    def test_Convolution_Matrix_negative(self):
        matrix1 = [[-6, -6, -6], 
                   [-6, -1, 1],
                   [-2, -2, -2]]
        matrix2 = [[6, 6, 6], 
                   [6, 1, 1],
                   [2, 2, 2]]
        
        expected = -156
        result = matrix.Convolution_Matrix(matrix1, matrix2)
        self.assertEqual(expected, result)

    def test_Convolution_Matrix_positive(self):
        matrix1 = [[40, 42, 46], 
                   [46, 50, 55],
                   [52, 56, 56]]
        matrix2 = [[0, 1, 0], 
                   [0, 0, 0],
                   [0, 0, 0]]
        
        expected = 42
        result = matrix.Convolution_Matrix(matrix1, matrix2)
        self.assertEqual(expected, result)

# test_matrixA
    def test_matrixA_positive(self):
        data = 4  
        expected = [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]]
        self.check_result_matrixA(data, expected)

    def test_matrixA_negative(self):
        data = -6
        expected = [[-6, -6, -6, -6], [-6, -6, -6, -6], [-6, -6, -6, -6]]
        self.check_result_matrixA(data, expected)

    
    





    