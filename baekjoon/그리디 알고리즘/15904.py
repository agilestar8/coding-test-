import sys
input = sys.stdin.readline

word = input()
target = "UCPC"

idx = 0
check = 0
for i in range(len(word)):
    if word[i] == target[idx]:
        idx += 1
        check += 1
        if check == 4:
            break
        
if check == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
        

        
                
        
    
        
        
    
    
    

           
 

    
    