def see_if_adjacent(matrix, number_len, index_horizontal, index_vertical, restrictions):
    # Data matrix is our search grid
    # index_horizontal and index_vertical are the coordinates of the first digit (of our number) in the matrix
    max_vertical = len(matrix)
    max_horizontal = len(matrix[0])
    vertical = [-1, 0, 1]
    neighbors = []
    # Create the neighbors coordinates of our number
    for i in vertical:
        neighbors.append((index_vertical+i, index_horizontal-1))
        neighbors.append((index_vertical+i, index_horizontal+number_len))
    for i in range(number_len):
        neighbors.append((index_vertical-1, index_horizontal+i))
        neighbors.append((index_vertical+1, index_horizontal+i))

    for coord in neighbors:
        # Check if the coordinates are in the matrix
        if 0<=coord[0]<max_vertical and 0<=coord[1]<max_horizontal:
            # Check if the coordinates are not either a number or a symbol
            if  matrix[coord[0]][coord[1]] not in restrictions:
                return True
    return False