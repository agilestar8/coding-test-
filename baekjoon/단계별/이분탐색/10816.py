n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int,input().split()))

dic = {}
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# print(dic)
for i in arr2:
    if i in dic:
        print(dic[i], end = " ")
    else:
        print(0, end = " ")

# for i in range(m):
#     start = 0
#     end = n-1   
#     find = False
#     while start <= end:
#         mid = (start+end)//2
#         if arr2[i] == arr[mid]:
#             print(arr.count(arr2[i]), end = " ")
#             find = True
#             break
            
#         elif arr2[i] > arr[mid]:
#             start = mid+1

#         elif arr2[i] < arr[mid]:
#             end = mid-1

#     if not find:
#         print(0, end = " ")




