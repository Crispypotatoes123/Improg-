"""
File: Interior Grid-points.py
Author: Aimee Meeajaun (a.z.meeajaun@student.rug.nl)

Description: this program will calculate the number of interior points in a triangle based on input coordinates
"""
from math import gcd

def triangle_area (x1, y1, x2, y2, x3, y3):
    # deriving the area of the triangle using the shoelace formula
    area  =  (abs((x1*y2) - (x3*y2) + (x3*y1) - (x1*y3) + (x2*y3) - (x2*y1))/2.0)
    return area

def boundary_points (x1, y1, x2, y2, x3, y3):
    # finding the boundary points of the triangle using method of greatest common denominator [3]
    boundray =   gcd(abs(x1 - x2), abs(y1 - y2)) + gcd(abs(x2 - x3), abs(y2 - y3)) + gcd(abs(x3 - x1), abs(y3 - y1))
    return boundray

def interior_points (x1, y1, x2, y2, x3, y3 ):
    # calling area function to calculate the triangle area for the input points
    area = triangle_area(x1, y1, x2, y2, x3, y3)

    # assessing whether the area == 0 (collinear, then there is no area)
    if area ==0:
        return 0

    # calling boundary function to calculate the boundary points from the input
    boundary = boundary_points(x1, y1, x2, y2, x3, y3)

    # using Picks theorem to calculate the interior points [2]
    interior_points  = int(area - boundary/2 + 1)
    return interior_points

# getting the user input and putting it into a list [4]
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

final_interior = interior_points(x1, y1, x2, y2, x3, y3)
print(final_interior)

#sources:
#(1) understanding the shoelace formula: https://brilliant.org/wiki/triangles-calculating-area/
#(2) understanding picks theorem: https://artofproblemsolving.com/wiki/index.php/Pick%27s_Theorem
    #(2b) https://www.geeksforgeeks.org/picks-theorem-for-competitive-programming/
    #(2c) https://steemit.com/mathematics/@team-leibniz/pick-s-theorem-the-elegant-universal-and-surprisingly-simple-method-to-finding-area
#(3) formula for determining the boundary points: https://stackoverflow.com/questions/1049409/how-many-integer-points-within-the-three-points-forming-a-triangle
#(4) how to use .split() and why: https://www.w3schools.com/python/ref_string_split.asp

