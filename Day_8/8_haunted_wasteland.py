"""
Day 8: Haunted Wasteland
Author: dnicolauit
Answer 1: 19637
Answer 2: 8811050362409
""" 
import utils
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


# Part 2
current_node = []
final_node = []
for key, _ in nodes.items():
    if 'A' in key:
        current_node.append(key)
    elif 'Z' in key:
        final_node.append(key)

numbers = []
solution = 0
for node in current_node:
    i = 0
    number = 0
    while node not in final_node:
        node = nodes[node][directions[i]]
        if i == len(directions)-1:
            i = 0
        else: i += 1
        number += 1
    numbers.append(number)

num1 = numbers[0]
num2 = numbers[1]
solution = utils.find_lcm(num1, num2)

for i in range(2, len(numbers)):
    solution = utils.find_lcm(solution, numbers[i])

print('Part 2 solution:',solution)