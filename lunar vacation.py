"""
File: lunar_vacation_AM_S5073812.py
Author: Aimee Meeajaun (a.z.meeajaun@student.rug.nl)

Description:
    this program will take in instructions and determine whether a ship has landed successfully, unsuccessfully or crashed
"""

import math

def lunar_vacation(x_distanceinitial=None, y_distanceinitial=None):

    # initial x and y position of the ship
    x_distanceinitial = int(input())
    y_distanceinitial = int(input())

    # if the initial vertical distance  is negative the ship has already crashed
    if y_distanceinitial < 0:
        print('CRASHED')
        return

    #when the ship has not crashed
    while True:
        delay = int(input())  # time in seconds
        rotation = int(input())  # the theta value
        thrust = int(input())  # seconds (time)

        # constants and initial conditions
        g = 1.625
        a = 3.0
        v_x_inital = 0 #inital velocity in the x direction
        v_y_inital = 0 #inital velocity in the y direction

        #changing y parameters to account for the delay (note there is no horizontal components as there is no thrust)
        y_distanceinitial += v_y_inital*delay + (g/2)* delay**2
        v_y = v_y_inital + g * delay

        # converting the rotation to radians
        rotation_radians = math.radians(rotation)

        #acceleration in x and y  with the thrust and rotation
        acceleration_x = v_x_inital * thrust + math.cos(rotation_radians) * thrust
        acceleration_y = v_y * thrust + math.sin(rotation_radians) * thrust

        #the final position of the ship for the x and y coordinates
        final_x_position = x_distanceinitial + v_x_inital * thrust + acceleration_x  / 2 * thrust ** 2
        final_y_position = y_distanceinitial + v_y * thrust + acceleration_y - g / 2 * thrust ** 2

        #if the final position is negative
        if final_y_position <0:
            print('CRASHED')
            return

        #conditions for successful
        if rotation == 0 and final_y_position <= 1 and final_x_position <= 5 and v_y <= 1:
            print('SUCCESSFUL')
            return

        #resetting the initial values for when the program loops for many instructions
        x_distanceinitial = final_x_position
        y_distanceinitial = final_y_position
        v_x_inital += acceleration_x * thrust
        v_y_inital += acceleration_y * thrust

        print('UNSUCCESSFUL')

lunar_vacation()