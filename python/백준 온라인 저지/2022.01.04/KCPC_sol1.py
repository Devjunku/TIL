import sys
from collections import defaultdict
input = sys.stdin.readline

class TeamScore:
    def __init__(self, pk):
        self.pk = pk
        self.score = defaultdict(int)
        self.tot = 0
        self.last = 0
        self.apply_num = 0
    
    def feed_score(self, p, score, ind):
        tmp = self.score[p]
        self.score[p] = max(self.score[p], score)
        self.tot += max(0, self.score[p]-tmp)
        self.last = ind
        self.apply_num += 1
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, P, ME, Q = map(int, input().rstrip().split())
        teams = []

        dummy_obj = TeamScore[0]
        dummy_obj.tot = int(1e9)
        teams.append(dummy_obj)
        for i in range(1, N+1):
            obj = TeamScore(i)
            teams.append(obj)

        for i in range(1, Q+1):
            pk, p, score = map(int, input().rstrip().split())
            teams[pk].feed_score(p, score, i)

        teams.sort(key=lambda obj: (-obj.tot, obj.apply_num, obj.last))

        for i, team in enumerate(teams):
            if team.pk == ME:
                print(i)
                break
