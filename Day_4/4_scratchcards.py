"""
Day 4: Scratchcards
Author: dnicolauit
Date: 2023-12-04
Answer 1: 
Answer 2: 
""" 

data = open("Day_4/4_scratchcards_data.txt").read().splitlines()

winning_numbers = []
numbers = []
solution = 0
number_cards = [1 for i in range(len(data))]
for i, d in enumerate(data): 
    winning_numbers_single, numbers_single = (d.split(':')[1]).split('|')
    winning_numbers.append([int(j) for j in winning_numbers_single.split()])
    numbers.append([int(j) for j in numbers_single.split()])
    count = int(sum([j in winning_numbers[-1] for j in numbers[-1]]))
    solution += int(2**(sum([j in winning_numbers[-1] for j in numbers[-1]])-1))
    for j in range(1,count+1):
        number_cards[i+j] += number_cards[i]

print('Part 1 solution:',solution)
print(sum(number_cards))

