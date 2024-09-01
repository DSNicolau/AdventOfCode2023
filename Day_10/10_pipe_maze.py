"""
Day 10: Pipe Maze
Author: dnicolauit
Answer 1: 
Answer 2: 
""" 

# data = open("Day_10/10_pipe_maze_data.txt").read().splitlines()
data = open("Day_10/10_example1.txt").read().splitlines()
data = [[j for j in i] for i in data]

i = 0
found = False
prev_mov=[0,0]
while not found:
    if 'S' in data[i]:
        for j in range(len(data[i])):
            if data[i][j]=='S':
                cur_pos=[i,j]
                found = True
                break
    i+=1
max_x = len(data[0])
max_y = len(data)
print(cur_pos)
print(max_x)
print(max_y)

travel_len = 0
finished = False
cur_finished = False


while not finished:
    # above
    if prev_mov[1]!=-1 and cur_pos[1]!=0 and not cur_finished:
        if data[cur_pos[0],cur_pos[1]-1]=='|' or data[cur_pos[0],cur_pos[1]-1]=='F':
            cur_finished = True
            prev_mov=[0,1]
            cur_pos[1]-=1
            travel_len+=1
        elif data[cur_pos[0],cur_pos[1]-1]=='S':
            travel_len+=1
            cur_finished=True
            finished=True
    # below
    if prev_mov[1]!=1 and cur_pos[1]!=max_y and not cur_finished:
        if data[cur_pos[0],cur_pos[1]+1]=='|' or data[cur_pos[0],cur_pos[1]+1]=='J':
            cur_finished = True
            prev_mov=[0,-1]
            cur_pos[1]+=1
            travel_len+=1
        elif data[cur_pos[0],cur_pos[1]-1]=='S':
            travel_len+=1
            cur_finished=True
            finished=True
    # right
    if prev_mov[0]!=-1 and cur_pos[0]!=max_x and not cur_finished:
        if data[cur_pos[0]+1,cur_pos[1]]=='-' or data[cur_pos[0],cur_pos[1]-1]=='7':
            cur_finished = True
            prev_mov=[1,0]
            cur_pos[0]+=1
            travel_len+=1
        elif data[cur_pos[0],cur_pos[1]-1]=='S':
            travel_len+=1
            cur_finished=True
            finished=True
    # left
    if prev_mov[0]!=1 and cur_pos[0]!=0 and not cur_finished:
        if data[cur_pos[0],cur_pos[1]-1]=='|' or data[cur_pos[0],cur_pos[1]-1]=='F':
            cur_finished = True
            prev_mov=[-1,0]
            cur_pos[0]-=1
            travel_len+=1
        elif data[cur_pos[0],cur_pos[1]-1]=='S':
            travel_len+=1
            cur_finished=True
            finished=True
    
print(travel_len)
print(travel_len/2)