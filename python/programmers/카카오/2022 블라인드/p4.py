score = 0

def lion_winner(lion, info):
    lion_score = 0
    Apeach_score = 0
    for i in range(len(info)):
        if lion[i] == 0 and info[i] == 0:
            continue
        if lion[i] > info[i]:
            lion_score += 10-i
        else:
            Apeach_score += 10-i
    return [lion_score > Apeach_score, lion_score - Apeach_score]

def dfs(s, n, lion, info):
    global res, score

    if n <= 0:
        game_res = lion_winner(lion, info)
        if game_res[0]:
            if score < game_res[1]:
                score = game_res[1]
                res = set()
                res.add(tuple(lion))
            elif score == game_res[1]:
                res.add(tuple(lion))
        return
    
    for i in range(s, len(lion)):
        if lion[i] <= info[i]:
            lion[i] += 1
            dfs(i, n-1, lion, info)
            lion[i] -= 1

def solution(n, info):
    global res
    lion = [0 for _ in range(11)]
    res = set()
    dfs(0, n, lion, info)
    res = list(res)
    
    if len(res) == 0:
        return [-1]

    res.sort(key=lambda x: (-x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], x[0]))

    answer = []
    for i in res[0]:
        answer.append(i)
    return answer



if __name__ == "__main__":
    print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
    print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
    print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
    print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))