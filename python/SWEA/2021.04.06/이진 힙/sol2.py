
# 출처: https://hongsj36.github.io/2020/01/27/IM_Tree/
# 대부분의 풀이가 class로 되어 있어서 도움이 되네용.
# 주석은 제가 달았습니다. 오늘 이 코드 보느라 시간 다 갔네용..
class Tree:
    def __init__(self):
        self.lst = [0]

    def sort(self, num): # sorting
        if num >= 2:
            if self.lst[num] < self.lst[num // 2]:
                # 자리 바꾸기
                self.lst[num], self.lst[num // 2] = self.lst[num // 2], self.lst[num]
                self.sort(num // 2)  # 재귀로 들어감.

    def append(self, data): # tree node 추가
        num = len(self.lst)
        self.lst.append(data) #재귀 아님..
        self.sort(num) # sort로 연결

    def my_sum(self, node):
        if node <= 1: # node가 1보다 작거나 같다는건.. 네 그렇습니다. 의미가 없는 것이지요.
            return self.lst[node]
        else:
            return self.lst[node] + self.my_sum(node // 2) # 그렇지 않는 노드들만 더할 수 있도록!

    def my_result(self):
        last = len(self.lst) - 1
        self.sum = 0
        if last >= 2: # 이 조건이 중요한 이유는 node의 개수가 2보다 작으면(실제로 1개이면)
            # 답을 구할 수 없기 때문입니다. 즉 0입니다.
            return self.my_sum(last // 2) # last // 2부터의 합을 알고싶기 때문에.
        else:
            return 0 # 0으로 출력!


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())  # 안씀
    tree = Tree() # 클래스 할당~
    for i in map(int, input().split()): #데이터 받고
        tree.append(i) # 클래스를 이용줍시다
    print('#{} {}'.format(test_case, tree.my_result()))
