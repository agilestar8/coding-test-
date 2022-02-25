def shap_to_lower(s): # 샾 붙은거 2글자이므로, 1글자로 줄이기
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m,musicinfos):
    answer=[0, '(None)']   # time_len, title
    m = shap_to_lower(m)   # '#'제거
    
    for info in musicinfos:
        music = info.split(',') # 4등분(시작시간, 끝난시간, 곡 제목, 가사)
        start = music[0] # "12:00"
        end = music[1] # "12:20"
        hour = (int(end[:2])-int(start[:2])) *60 
        min = int(end[3:])-int(start[3:])
        time = hour + min        
        
        title = music[2] # 제목
        gasa = shap_to_lower(music[3]) # 가사
        # 가사 길이보다 시간이 길면, 가사를 몫*회수+나머지 만큼 반복해야함
        a,b = divmod(len(time),gasa)
        melody = gasa*a + gasa[:b]        
                
        if m in melody and time > answer[0]:
            answer= [time,title]
    
    return answer[-1]

