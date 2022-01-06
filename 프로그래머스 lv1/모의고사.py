def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p1_idx = 0
    p2_idx = 0
    p3_idx = 0
    p1_score = 0
    p2_score = 0
    p3_score = 0
    for ans in answers:
        if p1[p1_idx] == ans:
            p1_score += 1
        p1_idx += 1
        p1_idx = p1_idx % len(p1)

    for ans in answers:
        if p2[p2_idx] == ans:
            p2_score += 1
        p2_idx += 1
        p2_idx = p2_idx % len(p2)

    for ans in answers:
        if p3[p3_idx] == ans:
            p3_score += 1
        p3_idx += 1
        p3_idx = p3_idx % len(p3)

    answer.append(p1_score)
    answer.append(p2_score)
    answer.append(p3_score)
    arr = []

    most_answer = max(answer)
    for i in range(len(answer)):
        if most_answer == answer[i]:
            arr.append(i + 1)
    arr.sort()

    return arr