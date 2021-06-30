arr = [[0 for _ in range(1001)] for _ in range(1001)]

T = int(input())

color_page = []

for t in range(T):
    color_page.append(list(map(int, input().split())))

set_area = []
for t in range(T-1, -1, -1):
    area = 0
    x, y, w, h = color_page[t][0], color_page[t][1], color_page[t][2], color_page[t][3]
    for i in range(x, x+w):
        for j in range(y, y+h):
            arr[i][j] += 1
            if arr[i][j] == 1:
                area += 1
    set_area.append(area)

for i in range(len(set_area)-1, -1, -1):
    print(set_area[i])


    

