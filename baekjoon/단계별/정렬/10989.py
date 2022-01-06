import sys
input = sys.stdin.readline

n = int(input())
memo = [0]*10001

for i in range(n):
    memo[int(input())]+= 1

for i in range(10001):
    if memo[i] != 0:
        for j in range(memo[i]):
            print(i)

