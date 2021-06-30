ans_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

scores = list(map(int, input().split()))

def confirm(ans_score, scores):
    total = 0
    for a, s in zip(ans_score, scores):

        if a < s:
            return 'hacker'
        
        total += s

    if total >= 100: return 'draw'
    else: return 'none'

print(confirm(ans_score, scores))