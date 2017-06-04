import math
instructions = [i.strip() for i in open('Day1.txt','r').read().split(',')]

x,y = 0,0
facing = 0
directions = ['n','e','s','w']
print instructions
for inst in instructions:
    if len(inst) <= 1:
        continue

    direction = inst[0]
    num = int(inst[1:])
    if direction == 'L':
        if facing:
            facing = (facing - 1)
        else:
            facing = 3
    else:
        facing = (facing + 1) % 4

    if (facing == 0):
        y += num
    elif (facing == 1):
        x += num
    elif (facing == 2):
        y -= num
    else:
        x -= num

print abs(x) + abs(y)