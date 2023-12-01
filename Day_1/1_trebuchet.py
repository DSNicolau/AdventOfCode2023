"""
Day 1: Trebuchet?!
Author: dnicolauit
Date: 2023-12-01
Answer: 53921

"""

data = open("Day_1/1_trebuchet_data.txt").read().splitlines()
solution = 0
for i in data:
    numbers = [int(j) for j in [*i] if j.isdigit()]
    solution += 10*numbers[0]+numbers[-1]

print(solution)