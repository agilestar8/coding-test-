def solution(new_id): 
    
    # 1
    new_id = new_id.lower()
    print(new_id)
    
    # 2
    for i in new_id:
        if not i.isalpha() and not i.isdigit() and i != "." and i != "_" and i != "-":
            new_id = new_id.replace(i,"")
    print(new_id)
    
    # 3
    for i in range(len(new_id)):
        new_id = new_id.replace("..",".")
    print(new_id)
    
    # 4
    if new_id[0] == ".":
        new_id = new_id[1:] 
        
    print(new_id)        

    # 5
    if new_id == "":
        new_id = 'a'
    
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15] # 0~14 = 15개
    if new_id[-1] == ".":
        new_id = new_id[:-1]
        
    # 7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id = new_id + new_id[-1]
        
    return new_id