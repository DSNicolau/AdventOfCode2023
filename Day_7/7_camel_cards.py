"""
Day 7: Camel Cards
Author: dnicolauit
Answer 1: 247815719
Answer 2: 248747492
""" 

import utils

cards = {'A':14, 
         'K':13, 
         'Q':12, 
         'J':11, 
         'T':10, 
         '9':9, 
         '8':8, 
         '7':7, 
         '6':6, 
         '5':5, 
         '4':4, 
         '3':3, 
         '2':2}

data = open("Day_7/7_camel_cards_data.txt").read().splitlines()

# Part 1

play, bid = zip(*(i.split() for i in data))
# Convert the plays to a list of ints
play_int = []
for i in range(len(play)):
    play_int.append([int(cards.get(j)) for j in play[i]])
# Convert bids to ints
bid = list(map(int, bid))

# Organize by type
play_strength = []
for i in range(len(play)):
    d = utils.get_dict(play[i])
    play_strength.append(utils.get_strenghts(play[i], d))


solution = utils.get_solution(play_strength, play_int, bid)

print('Part 1 solution:',solution)

# Part 2

cards = {'A':13, 
         'K':12, 
         'Q':11, 
         'T':10, 
         '9':9, 
         '8':8, 
         '7':7, 
         '6':6, 
         '5':5, 
         '4':4, 
         '3':3, 
         '2':2,
         'J':1}

# Convert the plays to a list of ints
play_int = []
for i in range(len(play)):
    play_int.append([int(cards.get(j)) for j in play[i]])

play_strength = []
for i in range(len(play)):
    new_play,d = utils.replaceJ(play[i])
    play_strength.append(utils.get_strenghts(new_play, d))

solution = utils.get_solution(play_strength, play_int, bid)
    

print('Part 2 solution:',solution)
