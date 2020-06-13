from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        current = self.root
        node = Node(data)
        if current is None:
            self.root = node
            return
        else:
            while True:
                if node.data < current.data:
                    if current.left is None:
                        current.left = node
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        return
                    current = current.right

    def bfs(self):
        visited = list()
        que = deque([self.root])
        while len(que) > 0:
            node = que.popleft()
            print('Popped root node {}'.format(node.data))
            if node not in visited:
                print('Node not in visited, appending {}'.format(node.data))
                visited.append(node)
            if node.left:
                print('Appending left node {}'.format(node.left.data))
                que.append(node.left)
            if node.right:
                print('Appending right node {}'.format(node.right.data))
                que.append(node.right)
        return visited

    def dfs(self):
        visited = list()
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            if node not in visited:
                print('Node {} not in visited, appending'.format(node.data))
                visited.append(node)
            if node.left:
                print('Appending node {} to left'.format(node.left.data))
                queue.appendleft(node.left)
            if node.right:
                print('Appending node {} to right'.format(node.right.data))
                queue.appendleft(node.right)
        return visited


if __name__ == '__main__':
    import random

    tree = Tree()
    for i in range(100):
        v = random.randrange(0, 9999)
        n = Node(v)
        tree.insert(n)

    d = tree.dfs()
