n = int(input())
for i in range(n):
    ex_res = input()
    if ex_res[0] == 'O':
        score = [1]
        cnt = 1
    else:
        score = [0]
        cnt = 0
    for j in range(1, len(ex_res)):
        if ex_res[j] == 'O':
            if ex_res[j] == ex_res[j-1]:
                cnt += 1
                score.append(cnt)
            else:
                cnt = 1
                score.append(cnt)
        else:
            cnt = 0
            score.append(cnt)
    print(sum(score))


n = int(input())

for i in range(n):
    case = str(input())
    score = 0
    cnt = 0
    for ca in case:
        if ca == 'O':
            cnt += 1
            score += count
        else:
            cnt = 0
    print(score)




