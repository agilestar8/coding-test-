def solution(sizes):
    max_x = 0
    max_y = 0
    for w,h in sizes:
        if w<h:
            w,h = h,w
        max_x = max(max_x,w)
        max_y = max(max_y,h)
        
    return max_x*max_y