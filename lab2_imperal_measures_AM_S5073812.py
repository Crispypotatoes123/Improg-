"""
File: imperial_measures_AM_S5073812.py
Author: Aimee Meeajaun (a.z.meeajaun@student.rug.nl)

Description:
    this program will covert measurements given by the user from meters to feet and inches
"""

#obtaining the user input in meters
user_input = input()

#removing 'm' if the user adds it to their inital input (i.e. 2,54m)
for letter in user_input:
    if letter == 'm':
        user_input = user_input.replace('m', '')
    else:
        pass

#converting the user input to a float and making sure it's not negative
user_input_flt = abs(float(user_input))

#converting the user input to mm (multiply by 1000) and to inches (divide 25.4)
user_inch = (user_input_flt *1000) / 25.4

# getting the feet and rounding to the closest whole number
feet_final = user_inch // 12

# getting the inches with the reminders
inches_final = user_inch % 12

print(f'''{feet_final:1.0f} ft {int(inches_final)} in''')









