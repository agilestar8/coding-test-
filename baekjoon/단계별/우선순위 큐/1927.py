import sys,heapq
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    num = int(input())

    if num == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, num)
