Case = input()

x_to_y = [list(map(int, input().split(' '))) for _ in range(int(Case))]

def work(sp, ep):
    dist = ep - sp
    
    if(dist == 1):
        return 1
    elif(dist == 2):
        return 2
    
    n = 1
    
    while(True):
        if((dist >= (n ** 2 - n + 1)) & (dist <= n ** 2)):
            return n * 2 - 1
        elif((dist > n**2) & (dist <= (n ** 2 + n))):
            return n * 2
        
        n += 1
        
for a, b in x_to_y:
    print(work(a, b))

