import sys
input = sys.stdin.readline

people = set()

N, game = map(str, input().split())
N = int(N)
for _ in range(N):
    person = input().strip()
    people.add(person)

real_number = len(people)
if game == "Y":
    print(real_number)
elif game == "F":
    print(real_number//2)
else:
    print(real_number//3)