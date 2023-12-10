"""
Day 6: Wait For It
Author: dnicolauit
Date: 2023-12-09
Answer 1: 
Answer 2: 
""" 

import math
data = open("Day_6/6_wait_for_it_data.txt").read().splitlines()
time = [int(i) for i in (data[0].split(':')[1]).split()]
distance = [int(i) for i in (data[1].split(':')[1]).split()]


# This is basically a quadratic inequation, so we'll use the quadratic formula to solve it.
# tt = total_time
# ht = hold_time
# d = distance
# The distance can be determined as d = (tt-ht)*ht
# inequality: -ht² + tt*ht - d > 0
# We know both tt and d, so we can solve for ht
# (-tt+sqrt(tt²-4d))/(-2) > ht > (-tt-sqrt(tt²-4d))/(-2)
# However, a small characteristic needs to be added
# When the number is not integer (without the ceil and floor operation), we need to subtract one
# SO we introduce a conditional, if the sqrt is not an integer, we subtract one
solution = 1
for tt, d in zip(time, distance):
    solution *= math.floor((-tt-math.sqrt(tt**2-4*d))/(-2))-math.floor((-tt+math.sqrt(tt**2-4*d))/(-2))-1*(math.sqrt(tt**2-4*d) % 1 == 0)

print('Part 1 solution:',solution)