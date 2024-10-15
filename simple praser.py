"""
File: simple praser.py
Author: Aimee Meeajaun (a.z.meeajaun@student.rug.nl)

Description: this program will translate a user input with a user defined cipher and output a message
"""

def simple_praser(user_input, cipher):

    # Defining the valid characters that can be included in the input and the cipher
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_characters = '<>+-*'

    # Putting the user input into a list
    input_list = list(user_input)

    # Removing invalid characters that are not in the alphabet or predefined cipher characters
    user_input = "".join(i for i in user_input if i in alphabet)
    cipher = "".join(i for i in cipher if i in cipher_characters)

   # Setting the initial index to 0 (the first character in the input)
    translation = 0

    for i in cipher:
        # if there is a '<' then will go to one position backwards, and loop around the input
        if i == '<':
            translation = (translation - 1) % len(input_list)

        # if there is a '>' then will go to one position forwards and loop around the input
        elif i == '>':
            translation = (translation + 1) % len(input_list)

        # if there is a '+' then will go to one position forwards in the alphabet and loop around the alphabet
        elif i == '+':
            letter_index = alphabet.index(input_list[translation])
            input_list[translation] = alphabet[(letter_index + 1) % len(alphabet)]

        # if there is a '-' then will go to one position backwards in the alphabet and loop around the alphabet
        elif i == '-':
            letter_index = alphabet.index(input_list[translation])
            input_list[translation] = alphabet[(letter_index - 1) % len(alphabet)]

        # if there is a '*' then will take the position of the next letter (wrt the alphabet) and add it to the first letter, loop around the alphabet
        elif i == '*':
            pair_2 = (translation + 1) % len(input_list)
            pair_1 = alphabet.index(input_list[translation])
            pair_2_index = alphabet.index(input_list[pair_2])
            input_list[translation] = alphabet[(pair_1 + pair_2_index) % len(alphabet)]

    #appends the translation to the input_list
    return ''.join(input_list)

#getting the user inputs
user_input = input().lower()
cipher = input().lower()

#applying the function
final_translation = simple_praser(user_input, cipher)
print(final_translation)

