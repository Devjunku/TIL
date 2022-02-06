# 막는 것으로 끝내는 것이 아니라
# 한번을 더 돌아야 됨.
# 어떻게 돌아야 되나...?
# 어차피 info의 경우 17개 밖에 안 되서 시간 복잡도의 문제는 없음
# 이미 방문한 경우는 체크를 해서 안세는 방향으로 진행하면 될거 같긴 한데,
# 방문 배열을 2개 만들어서 2개 모두 true이면 끝내는 것으로 해보자.

max_sheep_cnt = 0
childs = []

def solution(info, 	edges):
    global childs

    childs = [[] for _ in range(len(info))]

    for i in edges:
        childs[i[0]].append(i[1])

    nxt_nodes = []
    get_animal(0, 0, 0, nxt_nodes, info)

    return max_sheep_cnt


def get_animal(sheep_cnt, wolf_cnt, node, nxt_nodes, info):
    global max_sheep_cnt

    sheep_cnt += info[node]^1
    wolf_cnt += info[node]
    max_sheep_cnt = max(sheep_cnt, max_sheep_cnt)

    if (sheep_cnt <= wolf_cnt):
        return
    
    copied = []
    copied.append(nxt_nodes)

    if childs[node]:
        copied.append(childs[node])

    copied.remove(node)

    for nxt_node in copied:
        get_animal(sheep_cnt, wolf_cnt, nxt_node, copied, info)


if __name__ == "__main__":
    print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])) # 5
    print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])) # 5