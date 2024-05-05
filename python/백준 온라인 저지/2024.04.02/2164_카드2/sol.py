
from collections import deque
number = int(input())
data = deque([i for i in range(1, number+1)])

while number != 1:

    data.popleft()
    number -= 1

    if number == 1:
        break
    
    element = data.popleft()
    data.append(element)

print(data[0])



