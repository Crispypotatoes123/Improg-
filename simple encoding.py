"""
File: simple encoding.py
Author: Aimee Meeajaun (a.z.meeajaun@student.rug.nl)

Description:
    this program will assign each letter in a message to the opposite letter in the alphabet and print the result
"""

#input from the user
user_input = str(input(''))

def backwards_alphabet (user_input):
    '''
    :param user_input: a word or sentence from the user
    :return: each letter in the sentence will have a reversed letter
    '''

    # defining the upper and lower case alphabet
    lower_case_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_case_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #the reversed alphabets
    backwards_lower_case = lower_case_alphabet[::-1]
    backwards_upper_case = upper_case_alphabet[::-1]

    #creating a mapping table for the replacement
    trans_table = str.maketrans(lower_case_alphabet + upper_case_alphabet,
                                backwards_lower_case + backwards_upper_case)
    translated_input = user_input.translate(trans_table)

    return translated_input

#calling the function back to the user input
final = backwards_alphabet(user_input)
print(final)


#sources I used to learn how to use the maketrans function:
#https://w3schools.com/Python/ref_string_maketrans.asp
#https://www.shiksha.com/online-courses/articles/maketrans-function-in-python/#:~:text=The%20Python%20maketrans()%20function,during%20the%20string%20translation%20procedure.




