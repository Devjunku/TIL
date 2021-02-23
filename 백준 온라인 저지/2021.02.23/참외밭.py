from sys import stdin

N = int(stdin.readline().rstrip())

direction = []
distance = []

for n in range(6):
    direc, dist = map(int, stdin.readline().rstrip().split())
    direction.append(direc)
    distance.append(dist)
north = []
east = []
south = []
west = []
for way, dis in zip(direction, distance):
    if way == 4:
        north.append(dis)
    elif way == 1:
        east.append(dis)
    elif way == 2:
        west.append(dis)
    else:
        south.append(dis)

print(north, east, south, west)

