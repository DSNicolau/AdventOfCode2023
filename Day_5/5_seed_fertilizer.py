"""
Day 5: If You Give A Seed A Fertilizer
Author: dnicolauit
Answer 1: 388071289
Answer 2: 
""" 

from utils import Almanac
almanac = Almanac('Day_5/5_example.txt')
almanac.compute()
solution = almanac.get_min_location()

print('Part 1 solution:',solution)




