"""
File: vector.py
Author: Aimee Meeajaun (a.z.meeajaun@student.rug.nl)

Description:
    The function will return the length of the vector
from (0,0) to (x,y)
"""
from math import sqrt

def get_vector_length (coordinate_x, coordinate_y):
    return sqrt(coordinate_x**2 + coordinate_y**2)




