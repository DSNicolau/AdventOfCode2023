"""
Day 10: Pipe Maze
Author: dnicolauit
Answer 1: 6800
Answer 2: 
""" 

data = open("Day_10/10_pipe_maze_data.txt").read().splitlines()
# data = open("Day_10/10_example7.txt").read().splitlines()
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

travel_len = 0
finished = False


pos_str = ""
pre_pos = ""

# above
if data[cur_pos[0]-1][cur_pos[1]]=='|' or data[cur_pos[0]-1][cur_pos[1]]=='F' or data[cur_pos[0]-1][cur_pos[1]]=='7':
    pos_str = data[cur_pos[0]-1][cur_pos[1]]
    cur_pos = [cur_pos[0]-1,cur_pos[1]]
    travel_len+=1
    pre_pos = "b"
# below
elif data[cur_pos[0]+1][cur_pos[1]]=='|' or data[cur_pos[0]+1][cur_pos[1]]=='J' or data[cur_pos[0]+1][cur_pos[1]]=='L':
        pos_str = data[cur_pos[0]+1][cur_pos[1]]
        cur_pos = [cur_pos[0]+1,cur_pos[1]]
        travel_len+=1
        pre_pos = "a"
# right
elif data[cur_pos[0]][cur_pos[1]+1]=='-' or data[cur_pos[0]][cur_pos[1]+1]=='7' or data[cur_pos[0]][cur_pos[1]+1]=='J':
    pos_str = data[cur_pos[0]][cur_pos[1]+1]
    cur_pos = [cur_pos[0],cur_pos[1]+1]
    travel_len+=1
    pre_pos = "l"
# left
elif data[cur_pos[0]][cur_pos[1]-1]=='-' or data[cur_pos[0]][cur_pos[1]-1]=='F' or data[cur_pos[0]][cur_pos[1]-1]=='L':
    pos_str = data[cur_pos[0]][cur_pos[1]-1]
    cur_pos = [cur_pos[0],cur_pos[1]-1]
    travel_len+=1
    pre_pos = "r"
else: print("WTF")
    


while not finished:
    if pos_str == "S":
        finished = True
    elif pos_str=="|":
        if pre_pos == "b":
            pre_pos = "b"
            pos_str = data[cur_pos[0]-1][cur_pos[1]]
            cur_pos = [cur_pos[0]-1,cur_pos[1]]
            travel_len +=1
        else:
            pre_pos = "a"
            pos_str = data[cur_pos[0]+1][cur_pos[1]]
            cur_pos = [cur_pos[0]+1,cur_pos[1]]
            travel_len +=1

    elif pos_str == "-":
        if pre_pos == "r":
            pre_pos = "r"
            pos_str = data[cur_pos[0]][cur_pos[1]-1]
            cur_pos = [cur_pos[0],cur_pos[1]-1]
            travel_len +=1
        else:
            pre_pos = "l"
            pos_str = data[cur_pos[0]][cur_pos[1]+1]
            cur_pos = [cur_pos[0],cur_pos[1]+1]
            travel_len +=1

    elif pos_str == "L":
        if pre_pos == "a":
            pre_pos = "l"
            pos_str = data[cur_pos[0]][cur_pos[1]+1]
            cur_pos = [cur_pos[0],cur_pos[1]+1]
            travel_len +=1
        else:
            pre_pos = "b"
            pos_str = data[cur_pos[0]-1][cur_pos[1]]
            cur_pos = [cur_pos[0]-1,cur_pos[1]]
            travel_len +=1

    elif pos_str == "J":
        if pre_pos == "a":
            pre_pos = "r"
            pos_str = data[cur_pos[0]][cur_pos[1]-1]
            cur_pos = [cur_pos[0],cur_pos[1]-1]
            travel_len +=1
        else:
            pre_pos = "b"
            pos_str = data[cur_pos[0]-1][cur_pos[1]]
            cur_pos = [cur_pos[0]-1,cur_pos[1]]
            travel_len +=1

    elif pos_str == "7":
        if pre_pos == "b":
            pre_pos = "r"
            pos_str = data[cur_pos[0]][cur_pos[1]-1]
            cur_pos = [cur_pos[0],cur_pos[1]-1]
            travel_len +=1
        else:
            pre_pos = "a"
            pos_str = data[cur_pos[0]+1][cur_pos[1]]
            cur_pos = [cur_pos[0]+1,cur_pos[1]]
            travel_len +=1

    elif pos_str == "F":
        if pre_pos == "b":
            pre_pos = "l"
            pos_str = data[cur_pos[0]][cur_pos[1]+1]
            cur_pos = [cur_pos[0],cur_pos[1]+1]
            travel_len +=1
        else:
            pre_pos = "a"
            pos_str = data[cur_pos[0]+1][cur_pos[1]]
            cur_pos = [cur_pos[0]+1,cur_pos[1]]
            travel_len +=1

    else: print("WTF")

solution = int(travel_len/2)
print('Part 1 solution:',solution)

