def get_strenghts(play, d):
    if len(set(play)) == 1: # All cards are the same
        return 6 # The highest strenght
    elif len(set(play)) == 4: # There's only one pair
        return 1 # One of the lowest strenght
    elif len(set(play)) == 5: # All cards are different
        return 0 # The lowest strenght
    elif max(d.values())==4: # Getting four of a kind
        return 5
    elif len(set(play)) == 2: # Gettiing 3 of a kind + a pair
        return 4
    elif max(d.values())==3: # Getting 3 of a kind
        return 3
    return 2 # Getting two pairs


def get_sorted_bids(ranks, play_strength, play_int, bid):
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
    return sorted_bid

def get_dict(play):
    d = {}
    for c in play:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def replaceJ(play):
    d = get_dict(play)
    if 'J' in play and d['J']<5:
        del d['J']
        new_play = play.replace('J',sorted(d.items(), key=lambda x:x[1])[-1][0])
        d = get_dict(new_play)
    else : 
        new_play = play
    return new_play,d

def get_solution(play_strength, play_int, bid):
    # Sort the strenghts/type
    ranks = sorted(set(play_strength))
    sorted_bid = get_sorted_bids(ranks, play_strength, play_int, bid)
    solution = 0        
    # Finally, calculate the solution
    for i in range(len(sorted_bid)):
        solution += sorted_bid[i]*(i+1)
    return solution