"""
Day 11: Cosmic Expansion
Author: dnicolauit
Answer 1: 
Answer 2: 
""" 
import copy
# data = open("Day_11/11_cosmic_expansion_data.txt").read().splitlines()
data = open("Day_11/11_example1.txt").read().splitlines()

data = [[j for j in i] for i in data]

def n_pairs(n):
    return int((n*(n-1))/2)

def expand_data(data):
    temp_data=copy.copy(data)
    n=0
    for i in range(len(data)):
        if all(item == '.' for item in data[i]):
            temp_data.insert(i+n,temp_data[i+n].copy())
            n+=1
    n=0
    for i in range(len(data[0])):
        if all(item[i] == '.' for item in data):
            for j in range(len(temp_data)):
                temp_data[j].insert(i+n,'.')
            n+=1
            print('a')
    return temp_data

for i in data:
    print(i)
print('---------------------------------------')
for i in expand_data(data):
    print(i)
