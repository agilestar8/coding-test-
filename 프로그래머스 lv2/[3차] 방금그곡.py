def shap_to_lower(s): # 샾 붙은거 2글자이므로, 1글자로 줄이기
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m,musicinfos):
    answer=[0, '(None)']   # time_len, title
    m = shap_to_lower(m)   # '#'제거
    
    for info in musicinfos:
        split_info = info.split(',') # 4등분
        time_length = (int(split_info[1][:2]) - int(split_info[0][:2])) * 60 + int(split_info[1][3:]) - int(split_info[0][3:])
        
        title = split_info[2]
        part_notes = shap_to_lower(split_info[3])
        full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
        
        if m in full_notes and time_length>answer[0]:
            answer= [time_length,title]
    
    return answer[-1]