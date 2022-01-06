def solution(array, commands):
    answer = []
    for a in range(0, len(commands)):
        sub = []
        i = commands[a][0]
        j = commands[a][1]
        k = commands[a][2]
        for b in range(i-1, j):
            sub.append(array[b])
        sub.sort()
        answer.append(sub[k-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))