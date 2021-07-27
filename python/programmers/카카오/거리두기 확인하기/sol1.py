from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(s, d, place_list):
    
    queue = deque([s])
    mapping = [[0 for _ in range(5)] for _ in range(5)]
    mapping[s[0]][s[1]] = 1
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if (0 <= nx < 5 and 0 <= ny < 5) and manhaton(s, (nx, ny)) < 2 and mapping[nx][ny] != 1:
                if place_list[nx][ny] == 'P':
                    return 0
                if place_list[nx][ny] == 'X':
                    continue
                mapping[nx][ny] = 1
                queue.append((nx, ny))
    
    return 1
                
    
def manhaton(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])


def solution(places):
    answer = []
    for place in places:
        place_list = [list(p) for p in place]
        
        people_position = []
        for i in range(5):
            for j in range(5):
                if place_list[i][j] == 'P':
                    people_position.append((i, j))
        
        N = len(people_position)
        n = 1
        for i in range(N):
            for j in range(i+1, N):
                if manhaton(people_position[i], people_position[j]) <= 2:
                    n = bfs(people_position[i], people_position[j], place_list)
                    if n == 0:
                        break
                    
            if n == 0:
                break
        
        answer.append(n)
    return answer

if __name__ == '__main__':
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))