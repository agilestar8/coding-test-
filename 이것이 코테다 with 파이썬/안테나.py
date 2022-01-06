n = int(input())
location = list(map(int,input().split()))

location.sort()
print(location[n//2-1])
