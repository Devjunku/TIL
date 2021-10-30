# 승리면 1 그렇지 않으면 0
# 일단 head2head를 행렬로 만들어야 함
# 본인보다 큰 사람을 이긴 횟수
# 몸무게를 함께 열을 추가해서 표를 만들자.

def solution(weights, head2head):

    n = len(head2head)
    table = [[] for _ in range(n)]
    need_info = []
    for i in range(n):
        none = 1
        wl = list(head2head[i])
        cnt = 0
        # 승리면 1 그렇지 않으면 0
        for j in range(n):
            if i == j:
                table[i].append(-1)
            else:
                if wl[j] == "W":
                    table[i].append(1)
                    if weights[i] < weights[j]:
                        cnt += 1
                elif wl[j] == "L":
                    table[i].append(0)
                else:
                    table[i].append(-1)
                    none += 1
        w_cnt = 0
        real_play = 0
        for t in table[i]:
            if t == 1:
                w_cnt += 1
                real_play += 1
            elif t == 0:
                real_play += 1
        need_info.append((i+1, 0 if not real_play else round(w_cnt/real_play, 2), cnt, weights[i]))
    need_info.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))
    answer = []
    for info in need_info:
        answer.append(info[0])
    return answer

if __name__ == "__main__":
    print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
    print(solution([145,92,86], ["NLW","WNL","LWN"]))
    print(solution([60,70,60], ["NNN","NNN","NNN"]))