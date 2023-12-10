"""
Day 8: Haunted Wasteland
Author: dnicolauit
Date: 2023-12-10
Answer 1: 19637
Answer 2: 
""" 

data = open("Day_8/8_haunted_wasteland_data.txt").read()

# Part 1
dict_dir = {'L':0, 'R':1}
directions = [dict_dir[i] for i in data.split('\n\n')[0]]

nodes_str = data.split('\n\n')[1].splitlines()

nodes = {}
for i in nodes_str:
    key = i.split(' =')[0]
    value = ((i.split('= ')[1]).split('(')[1]).split(')')[0]
    nodes[key] = [j.split()[0] for j in value.split(',')]

i = 0
current_node = 'AAA'
solution = 0
while current_node != 'ZZZ':
    current_node = nodes[current_node][directions[i]]
    if i == len(directions)-1:
        i = 0
    else: i += 1
    solution += 1
print('Part 1 solution:',solution)