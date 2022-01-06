class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    # 특정 노드 참조
    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    # 선형순회
    def traverse(self):
        arr = []
        curr = self.head  # head에서 시작

        while curr != None:  # 마지막 노드가 아닐때까지
            arr.append(curr.data)  # 데이터를 추가하고
            curr = curr.next  # 다음 노드 가리키기
        return arr
    
    # 노드 삽입
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    # 노드 삭제
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        curr = self.getAt(pos)

        if pos == 1:
            if self.nodeCount == 1:  # 노드가 한개뿐인데 삭제할 경우
                self.head = None  # head/tail 다 끊음
                self.tail = None
            else:
                self.head = curr.next  # head는 삭제할 것의 다음으로 지정
                curr.next = None
        else:
            prev = self.getAt(pos - 1)
            curr = prev.next
            if pos == self.nodeCount:  # 맨 끝을 삭제할 경우
                prev.next = None  # 맨 끝 이전 노드는 None가리키고
                self.tail = prev  # tail이 됨
            else:
                prev.next = curr.next # 이전 노드는 다다음 노드를 가리킴
                curr.next = None

        self.nodeCount -= 1
        return curr.data
