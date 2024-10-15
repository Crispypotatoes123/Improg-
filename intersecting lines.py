# points of intersection

#getting the coordinates for the points in the line
a = int(input())
b = int(input())
c = int(input())
d = int(input())

e = int(input())
f = int(input())
g = int(input())
h = int(input())

#function for when there is the same gradient, as the x and y coordinates of each line are the same (the lines overlap)
def no_gradient(a, b, c, d, e, f, g, h):
    """
    line 1 coordinates:
    :param a: x1
    :param b: y1
    :param c: x2
    :param d: y2

    line2 coordinates:
    :param e: x1
    :param f: y1
    :param g: x2
    :param h: y2
    :return: whether line1 = line2 (all coordinates the same)
    """
    if a == e and b == f and c == g and d == h:
        return print('OVERLAP')


def gradient(a, b, c, d): # finding the gradient of the line using y = dy/dx(x) + b
    """
    :param a: x1 coordinate
    :param b: y1 coordinate
    :param c: x2 coordinate
    :param d: y2 coordinate
    :return: the gradient/slope of the function
    """
    if (d - b) == 0: # if the numerator is 0 then the gradient is 0 (horizontal line at y_intercept)
        return 0
    elif (c - a) == 0: #if the denominator is 0
        return None
    else:
        return (d - b) / (c - a) # all conditions are met to calculate gradient

def y_intercept(x, gradient, y):
    """
    :param x: x_1 coordinate
    :param gradient: the slope of the line
    :param y: y_1 coordinate
    :return: the y_intercept
    """
    if gradient is None:
        return x
    return y + -gradient * x

def line_intersection(a, b, c, d, e, f, g, h):
    if no_gradient(a, b, c, d, e, f, g, h): # calling the no_gradient function to see if the lines overlap
        return print('OVERLAP')

#calling the gradient functions
    gradient_1 = gradient(a, b, c, d)
    gradient_2 = gradient(e, f, g, h)

    # calling the y-intercept function for user inputs
    y_intercept_1 = y_intercept(a, gradient_1, b)
    y_intercept_2 = y_intercept(e, gradient_2, f)

# Lines are parallel and not overlapping
    if gradient_1 == gradient_2 and y_intercept_1 == y_intercept_2:
        print("OVERLAP")
        return

    if gradient_1 is None and gradient_2 is None: # if both lines are vertical
        return print("NONE")
    if gradient_1 is None:#if line 1 in vertical
        x_coordinate_intersection = a
        y_coordinate_intersection = gradient_2 * x_coordinate_intersection + y_intercept_2
    elif gradient_2 is None: #if line 2 is vertical
        x_coordinate_intersection = e
        y_coordinate_intersection = gradient_1 * x_coordinate_intersection + y_intercept_1
    else: # if neither line is vertical
        x_coordinate_intersection = (y_intercept_2 - y_intercept_1) / (gradient_1 - gradient_2)
        y_coordinate_intersection = gradient_1 * x_coordinate_intersection + y_intercept_1

#seeing if the intersection point is within the bounds given by the user input
    if (min(a, c) <= x_coordinate_intersection <= max(a, c) and min(b, d) <= y_coordinate_intersection <= max(b, d) and
        min(e, g) <= x_coordinate_intersection <= max(e, g) and min(f, h) <= y_coordinate_intersection <= max(f, h)):
        print(f"({x_coordinate_intersection:.1f}, {y_coordinate_intersection:.1f})")
    else:
        print("NONE")

line_intersection(a, b, c, d, e, f, g, h)