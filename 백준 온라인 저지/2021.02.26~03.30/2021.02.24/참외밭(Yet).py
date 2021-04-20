from sys import stdin

N = int(stdin.readline().rstrip())

direction = []
distance = []
d_dict = {}
for n in range(6):
    direc, dist = map(int, stdin.readline().rstrip().split())
    direction.append(direc)
    distance.append(dist)
    if direc in d_dict.keys():
        d_dict[direc] += 1
    else:
        d_dict[direc] = 1


north = []
east = []
south = []
west = []
print(d_dict)
print(direction)
print(distance)
for way, dis in zip(direction, distance):
    if way == 4:
        north.append(dis)
    elif way == 1:
        east.append(dis)
    elif way == 2:
        west.append(dis)
    else:
        south.append(dis)
    print( east, west, south, north)




