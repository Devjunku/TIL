from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    t = 0
    truck_weights = deque(truck_weights)
    
    bridge_gone = []
    bridge_going = [0]
    going_t = deque()   
    while truck_weights:
        t += 1
        if weight > sum(bridge_going) + truck_weights[0]:
            truck = truck_weights.popleft()
            bridge_going.append(truck)
            going_t.append(1)
        
        if going_t[0] == bridge_length:
            going_t.popleft()
        
        for i in range(len(going_t)):
            going_t[i] += 1

    print(t)



if __name__ == '__main__':
    print(solution(2, 10, [7,4,5,6]))
