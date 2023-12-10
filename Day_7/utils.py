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