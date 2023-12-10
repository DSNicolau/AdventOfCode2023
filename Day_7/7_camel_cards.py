"""
Day 7: Camel Cards
Author: dnicolauit
Date: 2023-12-10
Answer 1: 247815719
Answer 2: 
""" 
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
    d = {}
    if len(set(play[i])) == 1: # All cards are the same
        play_strength.append(6) # The highest strenght
    elif len(set(play[i])) == 4: # There's only one pair
        play_strength.append(1) # One of the lowest strenght
    elif len(set(play[i])) == 5: # All cards are different
        play_strength.append(0) # The lowest strenght
    else:
        for c in play[i]: # Creating an efficient method (without external packages, such as Collections) to find the pairs
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        if max(d.values())==4: # Getting four of a kind
            play_strength.append(5) 
        elif len(set(play[i])) == 2: # Gettiing 3 of a kind + a pair
            play_strength.append(4)
        elif max(d.values())==3: # Getting 3 of a kind
            play_strength.append(3)
        else:
            play_strength.append(2) # Getting two pairs

# Part 1

# Sort the strenghts/type
ranks = sorted(set(play_strength))
sorted_bid=[]
for rank in ranks:
    # Get all the indexes for the same strenght/type
    idx = [index for index, value in enumerate(play_strength) if value == rank]
    play_current = []
    # If there's only one play of this type, just append it
    if len(idx)==1:
        sorted_bid.append(bid[idx[0]])
    else:
        # Get all the plays of this type
        for i in idx:
            play_current.append(play_int[i])
        # Sort the plays by value (card in hand)
        sorted_play_idx = sorted(range(len(play_current)), key=lambda x: play_current[x])
        # Then append by order
        for i in sorted_play_idx:
            sorted_bid.append(bid[idx[i]])

solution = 0        
# Finally, calculate the solution
for i in range(len(sorted_bid)):
    solution += sorted_bid[i]*(i+1)
    

print('Part 1 solution:',solution)

# Part 2