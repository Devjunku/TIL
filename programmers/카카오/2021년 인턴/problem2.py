from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def manhattan(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])


def partition(point1, point2, pl):

    x_range = [point1[0], point2[0]]
    x_range.sort()
    y_range = [point1[1], point2[1]]
    y_range.sort()

    pl[point1[0]][point1[1]] = 1

    q = deque([point1])

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if x_range[0] <= nx <= x_range[1] and y_range[0] <= ny <= y_range[1] and pl[nx][ny] != 1:
                if pl[nx][ny] == 'X':
                    continue
                elif pl[nx][ny] == 'O':
                    pl[nx][ny] = 1
                    q.append((nx, ny))
                elif pl[nx][ny] == 'P':
                    return True
    return False


def toList(place):
    pl = [list(ele) for ele in place]
    person = []
    for i in range(len(pl)):
        for j in range(len(pl)):
            if pl[i][j] == 'P':
                person.append((i, j))
    return pl, person


def solution(places):
    answer = []
    num = 1
    for place in places:
        pl, person = toList(place)
        for i in range(len(person)):
            for j in range(i+1, len(person)):
                if manhattan(person[i], person[j]) <= 2 and len(answer) != num:
                    if partition(person[i],  person[j], pl):
                        answer.append(0)
        if len(answer) != num:
            answer.append(1)
        num += 1
    return answer


if __name__ == "__main__":
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
