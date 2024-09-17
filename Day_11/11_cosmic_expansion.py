"""
Day 11: Cosmic Expansion
Author: dnicolauit
Answer 1: 9974721
Answer 2: 
""" 
import copy
data = open("Day_11/11_cosmic_expansion_data.txt").read().splitlines()
# data = open("Day_11/11_example1.txt").read().splitlines()

data = [[j for j in i] for i in data]

# def n_pairs(n):
#     return int((n*(n-1))/2)

def expand_data(data):
    temp_data=copy.deepcopy(data)
    n=0
    for i in range(len(data)):
        if all(item == '.' for item in data[i]):
            temp_data.insert(i+n+1,temp_data[i+n].copy())
            n+=1
    n=0
    for i in range(len(data[0])):
        if all(item[i] == '.' for item in data):
            for j in range(len(temp_data)):
                temp_data[j].insert(i+n,'.')
            n+=1
    return temp_data

def get_pos(data):
    pos_dic = {}
    n=0
    for i in range(len(data)):
        for j in [i for i, x in enumerate(data[i]) if x == "#"]:
            pos_dic[n]=[i,j]
            n+=1
    return pos_dic

def sum_lens(positions):
    sum_len = 0
    for i in range(len(positions)):
        for j in range(i+1,len(positions)):
            sum_len+=abs(positions[i][0]-positions[j][0])+abs(positions[i][1]-positions[j][1])
    return sum_len


expanded_data = expand_data(data)
positions = get_pos(expanded_data)
solution = sum_lens(positions)
print('Part 1 solution:',solution)

def check_empty(data, pos1, pos2):
    n_rows = 0
    n_columns = 0
    max_row = max(pos1[0],pos2[0])
    min_row = min(pos1[0],pos2[0])
    max_col = max(pos1[1],pos2[1])
    min_col = min(pos1[1],pos2[1])
    # check rows
    for i in range(min_row,max_row):
        if all(item == '.' for item in data[i]):
            n_rows+=1
    for i in range(min_col,max_col):
        if all(item[i] == '.' for item in data):
            n_columns+=1
    return n_rows,n_columns

def sum_lens_n_empty(positions,data,n):
    sum_len = 0
    for i in range(len(positions)):
        for j in range(i+1,len(positions)):
            n_rows, n_columns = check_empty(data,positions[i],positions[j])
            sum_len+=abs(positions[i][0]-positions[j][0])+n_rows*n+abs(positions[i][1]-positions[j][1])+n_columns*n
    return sum_len

n = 1000000
positions_init = get_pos(data)
print(sum_lens_n_empty(positions_init,data,n-1))