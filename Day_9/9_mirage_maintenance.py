"""
Day 9: Mirage Maintenance
Author: dnicolauit
Answer 1: 1782868781
Answer 2: 1057
""" 

import copy
data = open("Day_9/9_mirage_maintenance_data.txt").read().splitlines()
# data = open("Day_9/9_example.txt").read().splitlines()
data = [[int(j) for j in i.split()] for i in data]
# Part 1

solution = 0
for dat in data:
    last = []
    while sum(dat)!=0:
        dat_temp = dat[:-1]
        last.append(dat[-1])
        for i in range(1,len(dat)):
            dat_temp[i-1] = dat[i]-dat[i-1]
        dat = copy.copy(dat_temp)
    solution += sum(last)

print('Part 1 solution:',solution)



# Part 2

solution = 0
for dat in data:
    first = []
    while sum(dat)!=0:
        dat_temp = dat[:-1]
        first.append(dat[0])
        for i in range(1,len(dat)):
            dat_temp[i-1] = dat[i]-dat[i-1]
        dat = copy.copy(dat_temp)
    temp_sol = 0
    for j in first[::-1]:
        temp_sol = j-temp_sol
    solution += temp_sol

print('Part 2 solution:',solution)