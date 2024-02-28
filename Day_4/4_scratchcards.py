"""
Day 4: Scratchcards
Author: dnicolauit
Answer 1: 21138
Answer 2: 7185540
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
    count = sum([j in winning_numbers[-1] for j in numbers[-1]])
    # Part 1
    solution += int(2**(count-1))
    # Part 2
    for j in range(1,count+1):
        number_cards[i+j] += number_cards[i]


print('Part 1 solution:',solution)

# Part 2
solution = sum(number_cards)
print('Part 2 solution:',solution)

