class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self): # 트리의 size는 모든 자식노드의 수 + 자기자신(=1)
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):  # depth는 자식 중 depth가 큰 것+1
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        if l > r:
            return l + 1
        else:
            return r + 1

# DFS - 중위,전위,후위 탐색 
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        arr = []
        arr.append(self.data)
        if self.left:
            arr += self.left.preorder()
        if self.right:
            arr += self.right.preorder()
        return arr

    def postorder(self):
        arr = []
        if self.left:
            arr += self.left.postorder()
        if self.right:
            arr += self.right.postorder()
        arr.append(self.data)

        return arr

class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

def solution(x):
    return 0