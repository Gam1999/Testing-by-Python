import math

# square_root
def square_root(num):
    ans_square_root = num ** 0.5
    return ans_square_root

# Equivalent Diameter
def coutour_area(cout_area):
    coutour_area_mul_4 = cout_area * 4.0
    sum_coutour_area_pi = (coutour_area_mul_4 * 4.0)/3.14
    return sum_coutour_area_pi

def Equivalent_Diameter(cout_area):
    return math.sqrt(coutour_area(cout_area))





