import sys
import heapq

sys.stdin = open('input.txt', 'r')

max_heap = []
min_heap = []
result = 0

N = int(sys.stdin.readline())
for i in range(N):
    inp = int(sys.stdin.readline())
    if i == 0:  # 맨 처음 입력 result로 초기화
        result = inp
        print(result)  # 중간값 출력
    else:
        if result <= inp:  # result보다 입력이 크거나 같은 경우
            heapq.heappush(min_heap, inp)  # 입력을 오른쪽 min heap에 넣기
            heapq.heappush(max_heap, -result)  # result를 왼쪽 max heap에 넣기
        else:  # result보다 입력이 작은 경우
            heapq.heappush(max_heap, -inp)  # 입력을 왼쪽 max heap에 넣기
            heapq.heappush(min_heap, result)  # result를 오른쪽 min heap에 넣기

        if len(min_heap) == len(max_heap):  # 개수가 짝수 인 경우
            if min_heap[0] > -max_heap[0]:  # 왼쪽 max heap의 가장 큰수가 오른쪽 min heap 가장 작은 수 보다 작은 경우
                result = -heapq.heappop(max_heap)  # 왼쪽 max heap의 가장 큰수가 중간값
            else:  # 오른쪽 min heap의 가장 작은 수가 왼쪽 max heap 가장 큰수보다 작은 경우
                result = heapq.heappop(min_heap)  # 오른쪽 min heap의 가장 작은 수가 중간값
        elif len(min_heap) > len(max_heap):  # 왼쪽 min heap 배열의 수가 더 많은 경우
            result = heapq.heappop(min_heap)  # 왼쪽 min heap의 가장 작은 값이 중간 값
        else:  # 오른쪽 max heap 배열의 수가 더 많은 경우
            result = -heapq.heappop(max_heap)  # 오른쪽 max heap의 가장 큰 값이 중간 값

        print(result)  # 중간값 출력

