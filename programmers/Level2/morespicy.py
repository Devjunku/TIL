# 내가 짠 코드
def solution(scoville, K):
    scov_list = sorted(scoville)
    count = 0
    
    while True:
        count1 = 0
    
        for scov in scov_list:
            if scov < K:
                count1 += 1
    
        if count1 == 0:
            break

        scov_list = [scov_list.pop(0) + (scov_list.pop(0) * 2)] + scov_list
        count += 1
    
    return count

print(solution([1, 2, 3, 9, 10, 12], 7)) # 확인

# 다른 풀이
def solution(scoville, K):
    mix_cnt = 0

    while min(scoville) < K:
        scoville.sort()

        try:
            scoville.append(scoville.pop(0) + scoville.pop(0) * 2)
        except IndexError:
            return -1

        mix_cnt += 1

    return mix_cnt



# 정답
import heapq

def solution(scoville, K):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    
    mix_cnt = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappush(heap, num) + heapq.heappush(heap, num) * 2)
        except IndexError:
            return -1
        mix_cnt += 1

    return mix_cnt

