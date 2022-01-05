T = int(input())

answer = []
for _ in range(T):
    n, k, t, m = map(int, input().split())

    team_problem_time = { 
        x : {
            # 점수, 시간
            y:[0, 1] for y in range(1, k+1)
        } for x in range(1, n+1)
    }

    # 총점, 제출횟수, 시간
    team_summary = [[0, 0, 0, i] for i in range(1, n+1)]

    time = 1
    for _ in range(m):
        i, j, s = map(int, input().split())
        if team_problem_time[i][j][0] < s:
            team_problem_time[i][j][0] = s
            team_summary[i-1][2] = time
        
        team_problem_time[i][j][1] += 1
        time += 1
    
    for i in range(1, n+1):
        for key, value in team_problem_time[i].items():
            team_summary[i-1][0] += value[0]
            team_summary[i-1][1] += value[1]

    team_summary = sorted(team_summary, key=lambda x: (-x[0], x[1], x[2]))
    
    for i in range(n):
        if team_summary[i][3] == t:
            print(i+1)
            break