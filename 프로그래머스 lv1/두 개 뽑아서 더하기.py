def solution(numbers):
    answer = []

    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            addsum = numbers[i] + numbers[j]
            answer.append(addsum)

    return sorted(set(answer))