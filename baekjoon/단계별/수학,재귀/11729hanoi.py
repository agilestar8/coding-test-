#Solution

# 하노이의 탑을 직접 풀어보면 답은 금방 나온다. 
# n개의 원판 디스크를 옮길 때는 먼저 n-1개의 원판을 중간에 놓고, 제일 큰 원판을 3으로 옮긴다. 
# 이후 다시 n-1개의 원판을 2에서 3으로 옮긴다. 이를 식으로 써보면 다음과 같다.

def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, end, mid)
        print(start, end)
        hanoi(n-1, mid, start, end)

n = int(input())
total_mvmt = 0

for disk in range(n):
    total_mvmt = total_mvmt * 2
    total_mvmt += 1

print(total_mvmt)
hanoi(n, 1, 2, 3)