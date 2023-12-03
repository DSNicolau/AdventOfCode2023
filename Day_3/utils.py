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

def count_adjacent_to_gear(data_dict,index_horizontal,index_vertical,max_vertical,max_horizontal):
    v=[]
    data = []
    search_horizontal = []
    # Our search is limited to the line above, bellow and the same as the gear
    for i in range(-1,2):
        if 0<=index_vertical+i<=max_vertical-1:
            data.append(data_dict[index_vertical+i])
        if 0<=index_horizontal+i<=max_horizontal-1:
            search_horizontal.append(index_horizontal+i)


    for i in range(len(data)):
        # number is the numbers in line i
        for number in data[i].keys():
            # j is an array of indexes of the appearance of the first digit of number
            for j in data[i][number]:
                # Finally, k are the indexes that contain the number
                for k in range(j,j+len(number)):
                    if k in search_horizontal:
                        v.append(int(number))
                        if len(v)==2:
                            result = v[0]*v[1]
                            return result
                        break

    return 0