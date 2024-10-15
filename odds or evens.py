"""
File: odds_evens_AM_S5073812.py
Author: Aimee Meeajaun (a.z.meeajaun@student.rug.nl)

Description:
    this program will play a game that will determine if the sum of the user inputs is even or odd
"""

#the user inputs
player_odds = input()
player_evens = input()

if player_odds.isdigit() and player_evens.isdigit():
    player_odds = int(player_odds)
    player_evens = int(player_evens)
    if player_odds <=0 or player_evens <=0: # if nay of the user inputs are less than 0 (-ve)
        print ('FORFEIT')
    else:
        game_sum =player_odds + player_evens #summation of the 2 user inputs
        if game_sum > 0:
            if game_sum % 2.0 == 0: #  if the sum divided by 2 is 0 (even)
                print('EVENS')
            elif game_sum % 2.0 != 0:# if the sum divided by 2 is NOT 0 (odd)
                print('ODDS')
else:
    print('FORFEIT')