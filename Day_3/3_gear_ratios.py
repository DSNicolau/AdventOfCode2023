"""
Day 3: Gear Ratios
Author: dnicolauit
Date: 2023-12-03
Answer 1: 
Answer 2: 
""" 

import re
from utils import see_if_adjacent


data_matrix = []
not_symbols = '0123456789.'

#Get data
data = open("Day_3/Examples/example8.txt").read().splitlines()
data_dict={key: [] for key in range(0,len(data))}
for i in range(len(data)):
    # Put our data in a matrix
    data_matrix.append([*data[i]])
    # Put the found numbers in a dictionary with the respective indexes of the first digit
    data_dict[i].append({int(m.group(0)):m.start(0) for m in re.finditer("\d+", data[i])})

solution = 0
for i in range(len(data)):
    for number in data_dict[i][0].keys():
        number_len = len(str(number))
        index = data_dict[i][0][number]
        use_number = see_if_adjacent(matrix=data_matrix, number_len=number_len, index_horizontal=index, index_vertical=i, restrictions=not_symbols)
        if use_number:
            solution += number

print('Part 1 solution:',solution)

        

