"""
File: playfair++.py
Author: Aimee Meeajaun (a.z.meeajaun@student.rug.nl)

Description: this code takes a code-phrase and creates a 7x7 table and a user input which is then encrypted using the table from the code phrase.
"""
# Converting both inputs to lowercase
user_input_code = input().lower()
user_input = input().lower()

# Creating a 7x7 table for the input code-phrase
def playfair_grid(user_input_code):

    # Concatenating the input string with the alphabet and removing duplicates
    cipher = "".join(dict.fromkeys(user_input_code + '0123456789abcdefghijklmnopqrstuvwxyz .,\'"!?:;()@&'))

    # Creating a 7x7 table
    table = [[cipher[i + j] for j in range(7)] for i in range(0, 49, 7)]
    return table

def pairs(user_input):

    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz .,\'"!?:;()@&'

    # taking out any invalid characters that are not in the provided alphabet
    user_input = "".join(i for i in user_input if i in alphabet)

    # If there is an odd number of characters a space is added
    if len(user_input) % 2 != 0:
        user_input += ' '

    # creating the pairs
    input_pairs = [user_input[i:i + 2] for i in range(0, len(user_input), 2)]
    return input_pairs


# Getting the coordinates of each letter in the pairs
def coordinates(table, letter):
    for x in range(7):
        for y in range(7):
            if table[x][y] == letter:
                return x, y

    #case where there are no coordinates/pairs
    return None

def encryption(table, input_pairs):
    encrypted_message = ''

    # for loop to handle different cases and types of pairs that could arise
    for pair in input_pairs:

        #if there is a pair of '&&'
        if pair == '&&':
            # pair is not encoded and added to the message as is
            encrypted_message += '&&'
            continue
        #repeating characters
        coordinate_1 = coordinates(table, pair[0])
        # if the characters are the same, the second is replaced with '&'
        coordinate_2 = coordinates(table, pair[1] if pair[0] != pair[1] else '&')

        # case were the rows are the same
        if coordinate_1[0] == coordinate_2[0]:
            encrypted_message += table[coordinate_1[0]][(coordinate_1[1] + 1) % 7]
            encrypted_message += table[coordinate_2[0]][(coordinate_2[1] + 1) % 7]

        # case where columns are the same
        elif coordinate_1[1] == coordinate_2[1]:
            encrypted_message += table[(coordinate_1[0] + 1) % 7][coordinate_1[1]]
            encrypted_message += table[(coordinate_2[0] + 1) % 7][coordinate_2[1]]

        #where both rows and columns are different (normal case)
        else:
            encrypted_message += table[coordinate_1[0]][coordinate_2[1]]
            encrypted_message += table[coordinate_2[0]][coordinate_1[1]]

    return encrypted_message

# Calling functions
table = playfair_grid(user_input_code)
input_pairs = pairs(user_input)
encrypted_message = encryption(table, input_pairs)

#printing the final results
print(encrypted_message)

#sources used:
#(1) https://www.geeksforgeeks.org/python-character-coordinates-in-matrix/ (finding the coordinates, used in coordinates function)
#(2) https://math.asu.edu/sites/default/files/playfair.pdf (understanding the playfair game)
#(3) https://www.geeksforgeeks.org/python-dictionary/
#(4) Gemini AI to help with debugging, not creating any code




