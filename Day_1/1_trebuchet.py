"""
Day 1: Trebuchet?!
Author: dnicolauit
Date: 2023-12-01
Answer: 53921

"""

# Part 1

data = open("Day_1/1_trebuchet_data.txt").read().splitlines()
solution = 0
for i in data:
    numbers = [int(j) for j in [*i] if j.isdigit()]
    solution += 10*numbers[0]+numbers[-1]

print('Part 1 solution:',solution)

# Part 2

numbers_dict = {  'one':'1',
                    'two':'2',
                    'three':'3',
                    'four':'4',
                    'five':'5',
                    'six':'6',
                    'seven':'7',
                    'eight':'8',
                    'nine':'9'}

solution = 0
for i in data:
    new_string = i
    for key, value in numbers_dict.items():
        if key in new_string:
            # Note: 'sevenine' is considered as 79
            # Substituting 'seven' per '7' and 'nine' per '9', would result in '7ine', which is not correct
            # Instead, a nice hack we do here is to substitute each number string by their first character, their number, and their last character
            # This would result in 's7n9e' :D
            key_list = [*key]
            new_string = new_string.replace(key, key_list[0]+value+key_list[-1])
    numbers = [int(j) for j in [*new_string] if j.isdigit()]
    solution += 10*numbers[0]+numbers[-1]

print('Part 2 solution:',solution)

