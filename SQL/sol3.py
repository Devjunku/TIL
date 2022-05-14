def solution(papers):

    entire_papers = [[0 for _ in range(15)] for _ in range(15)]

    for x1, y1, x2, y2 in papers:
        entire_papers[x1][y1] += 1
        entire_papers[x2][y2] += 1
        entire_papers[x1][y2] -= 1
        entire_papers[x2][y1] -= 1

    for i in range(15):
        for j in range(1, 15):
            entire_papers[i][j] += entire_papers[i][j-1]
    
    for i in range(15):
        for j in range(1, 15):
            entire_papers[j][i] += entire_papers[j-1][i]

    answer = 0
    for i in range(15):
        for j in range(15):
            answer = max(answer, entire_papers[i][j])

    return answer


if __name__ == "__main__":
    print(solution([[0, 0, 2, 2], [2, 2, 4, 4]] )) # 1