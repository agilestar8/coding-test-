arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    # 3x2의 0행렬 만들기

    for i in range(len(arr1)):  # 0 1 2
        for j in range(len(arr1[0])):  # 0 1
            for k in range(len(arr2[0])):  # 0 1

                answer[i][k] += arr1[i][j] * arr2[j][k]

    return answer