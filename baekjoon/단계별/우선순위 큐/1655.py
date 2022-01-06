import sys,heapq

input = sys.stdin.readline

n = int(input())
minheap = []    # min heap은 heapq 그대로 사용
maxheap = []    # max heap은 없으므로 min heap에서 -붙여서 사용

for i in range(n):
    num = int(input())
    
    if len(minheap) == len(maxheap):
        heapq.heappush(maxheap, (-num,num))
    else:
        heapq.heappush(minheap, (num, num))

    if minheap and maxheap[0][1] > minheap[0][1]:   # 조건에 안 맞을 시, 양쪽의 값 교체
        to_right = heapq.heappop(maxheap)[1]
        to_left = heapq.heappop(minheap)[1]

        heapq.heappush(maxheap, (-to_left,to_left))
        heapq.heappush(minheap, (to_right,to_right))
    
    print(maxheap[0][1])