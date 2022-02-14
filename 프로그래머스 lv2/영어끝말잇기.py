words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

def solution(n, words):
    l = len(words)

    for i in range(1,l):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [i%n+1,i//n+1]
    else:
        return [0,0]    
