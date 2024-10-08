"""
Day 25: Snowverload
Author: dnicolauit
Answer 1: 
Answer 2: 
""" 

# data = open("Day_25/25_snowverload_data.txt").read()
data = open("Day_25/25_example.txt").read().splitlines()
print('ah')

data_dic = {}

# Parsing

for line in data:
    line = line.split()
    line[0]= line[0][:-1]
    for i in line:
        if i not in data_dic:
            data_dic[i] = []
        data_dic[i].append([x for x in line if x != i])

for key in data_dic:
    data_dic[key] = [j for i in data_dic[key] for j in i]
    data_dic[key] = list(set(data_dic[key]))

def remove_node(data_dic, edge1, edge2):
    data_dic[edge1].remove(edge2)
    data_dic[edge2].remove(edge1)
    return data_dic