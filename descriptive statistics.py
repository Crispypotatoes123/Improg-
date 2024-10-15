"""
File: descriptive statistics.py
Author: Aimee Meeajaun (a.z.meeajaun@student.rug.nl)

Description: takes a user input of a random numbers and calculates the mean and variance
"""
# input a random number of numbers
user_input = input()

# converting the input into an integer and into a list
list_input = list(map(int, user_input.split()))

# solving for the mean
mean  = sum(list_input) / len(list_input)

# solving for the variance
variance = sum((x - mean) **2 for x in list_input) / (len(list_input) - 1)

# printing the results
print(round(mean,3))
print(round(variance,3))




