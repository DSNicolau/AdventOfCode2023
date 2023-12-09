"""
Day 5: If You Give A Seed A Fertilizer
Author: dnicolauit
Date: 2023-12-09
Answer 1: 388071289
Answer 2: 
""" 

from utils import Almanac
almanac = Almanac('Day_5/5_seed_fertilizer_data.txt')
almanac.compute()
solution = almanac.get_min_location()

print('Part 1 solution:',solution)