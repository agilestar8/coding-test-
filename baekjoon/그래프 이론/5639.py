import sys
sys.setrecursionlimit(10 ** 9)
input =sys.stdin.readline

def postorder(left,right):
    # 
    if left > right:
        return
    else:
        mid = right + 1
        for i in range(left+1, right+1):
            if arr[left] < arr[i]:
                mid = i
                break
        
        postorder(left+1, mid-1)
        postorder(mid,right)
        print(arr[left])
                    
arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

postorder(0,len(arr)-1)
