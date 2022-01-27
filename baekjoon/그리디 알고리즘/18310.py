import sys
input = sys.stdin.readline

n = int(input())
home_location = list(map(int,input().split()))
home_location.sort()

print(home_location[(n//2)-1])
        
    




