import math
# Aspect_Ratio
def Aspect_Ratio(a, b):
    ans_Aspect_Ratio = a / b
    return ans_Aspect_Ratio

# triangle
def WLForTriangle(wt, lt):
    ans_WidthAndLength = wt * lt
    return ans_WidthAndLength

def triangle(wt, lt):
    ans_triangle = (1/2) * WLForTriangle(wt, lt)
    return ans_triangle

# Trapezoidal triangle
def WLTrapezoidalTriangle(w, l):
    WL_TrapezoidalTriangle = w + l
    return WL_TrapezoidalTriangle

def TrapezoidalTriangle(w, l, h):
    ans_TrapezoidalTriangle = (1 / 2) * WLTrapezoidalTriangle(w, l) * h
    return ans_TrapezoidalTriangle

# rhombus area
def sum_area_wl(w, h):
    ans_sum_area_wl = w * h
    return ans_sum_area_wl

def rhombic_area(w, h):
    ans_Rhombic_area = (1 / 2) * sum_area_wl(w, h)
    return ans_Rhombic_area






