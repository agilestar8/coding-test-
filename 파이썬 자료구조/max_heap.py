class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        m = len(self.data) - 1  # 마지막 인덱스
        # 왼쪽자식 = 2m
        # 오른자식 = 2m+1
        # 부모번호 = m/2
        while m > 1:
            if self.data[m] > self.data[m // 2]:  # 삽입한게 현재 부모보다 더 크면
                self.data[m], self.data[m // 2] = self.data[m // 2], self.data[m]  # swap
                m = m // 2
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self, i):
        left = 2 * i
        right = 2 * i + 1
        greatest = i

        if left < len(self.data) and self.data[left] > self.data[greatest]:
        # 조건이 만족하는 경우, greatest 는 왼쪽 자식의 인덱스를 가집니다.
        greatest = left
        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if right < len(self.data) and self.data[right] > self.data[greatest]:
        # 조건이 만족하는 경우, greatest 는 오른쪽 자식의 인덱스를 가집니다.
        greatest = right
        if greatest != i:
        # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
        self.data[i], self.data[greatest] = self.data[greatest], self.data[i]
        # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
        self.maxHeapify(greatest)

def solution(x):
    return 0