import math
import numpy as np

# Sobel operator

def multiMat(A, B): 
    C = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

    dimension = len(A)

    for i in range(dimension):
        for j in range(dimension):
            for k in range(dimension):
                C[i][j] += A[i][k] * B[k][j]
    return C

def addMat(Gx, Gy):
    dimension = len(Gx)

    for i in range(dimension):
        for j in range(dimension):
            Gx[i][j] += Gy[i][j]
    return Gx

def sobel_op(A):
    tem_y = [[1, 2, 1],
             [0, 0, 0],
             [-1, -2, -1]]
    tem_x = [[-1, 0, 1],
             [-2, 0, 2],
             [-1, 0, 1]]
    Gx = multiMat(tem_x, A)
    Gy = multiMat(tem_y, A)

    Gx = multiMat(Gx,Gx)
    Gy = multiMat(Gy,Gy)

    G = np.sqrt(addMat(Gx, Gy))
    return G.tolist()

# averagingFillter
def averagingFillter(A):
    m = len(A)
    n = len(A[0])
    size = m * n

    for i in range(m):
        for j in range(n):
            A[i][j] /= size
    return A

# Convolution_Matrix
def Convolution_Matrix(A, B):
    con = 0
    dimension = len(A)
    for i in range(dimension):
        for j in range(dimension):
            con += A[i][j] * B[i][j]
    
    return con

# matrixA
def matrixA(x):
    A = [[x, x, x, x], 
         [x, x, x, x],
         [x, x, x, x]]
    return A 






            


























