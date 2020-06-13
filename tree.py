from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    def __lt__(self, other):
        if type(other) is int:
            return self.data < other
        else:
            return self.data < other.data

    def __gt__(self, other):
        if type(other) is int:
            return self.data > other
        else:
            return self.data > other.data

    def __eq__(self, other):
        if type(other) is int:
            return self.data == other
        else:
            return self.data == other.data

    def __str__(self):
        return str(self.data)


class Tree:

    def __init__(self):
        self.root_node = None

    def bsf(self):
        list_of_nodes = []
        traversal_queue = deque([self.root_node])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            print('Added node to list {}'.format(node.data))
            list_of_nodes.append(node.data)
            if node.left_node:
                print('Adding left node to traversalQueue {}'.format(node.left_node.data))
                traversal_queue.append(node.left_node)
            if node.right_node:
                print('Adding right node to traversalQueue {}'.format(node.right_node.data))
                traversal_queue.append(node.right_node)
        return list_of_nodes

    def get_min(self):
        current = self.root_node
        if current is None:
            return False
        else:
            while True:
                tmp = current
                current = current.left_node
                if current is None:
                    print('Min value of tree is {}'.format(tmp.data))
                    return tmp

    def get_max(self):
        current = self.root_node
        if current is None:
            return False
        else:
            while True:
                tmp = current
                current = current.right_node
                if current is None:
                    print('Max value of tree is {}'.format(tmp.data))
                    return tmp

    def insert(self, data):
        node = Node(data)
        current = self.root_node
        if current is None:
            self.root_node = node
            # print('Inserted as root')
            return
        else:
            while True:
                parent = current
                if node.data < current.data:
                    # print('{} is less than {}'.format(node.data, current.data))
                    parent = current
                    current = current.left_node
                    if current is None:
                        # print('Appending node to parents {} left side {}'.format(parent.data, node.data))
                        parent.left_node = node
                        return
                else:
                    # print('{} is greater than {}'.format(node.data, current.data))
                    parent = current
                    current = current.right_node
                    if current is None:
                        # print('Appending node to parents {} right side {}'.format(parent.data, node.data))
                        parent.right_node = node
                        return

    def get_parent_and_child(self, data):
        current = self.root_node
        parent = None
        if current is None:
            return None
        while current is not None:
            if current.data == data:
                # print('Returning parent with value {} and node with value {}'.format(parent.data, current.data))
                return parent, current
            if current.data > data:
                # print('{} is higher than {}'.format(current.data, data))
                parent = current
                current = current.left_node
            else:
                # print('{} is less than {}'.format(current.data, data))
                parent = current
                current = current.right_node
        # print('No data found')
        return

    def remove(self, data):
        parent, node = self.get_parent_and_child(data)

        if node is None and parent is None:
            print('No data found')
            return

        child_count = 0
        if node.left_node and node.right_node:
            child_count = 2
        if (node.right_node is None) and (node.left_node is None):
            child_count = 0
        else:
            child_count = 1

        if child_count == 0:
            if parent:
                if parent.left_node is node:
                    print('Removed left node {} from parent {}'.format(node.data, parent.data))
                    parent.left_node = None
                else:
                    print('Removed right node {} from parent {}'.format(node.data, parent.data))
                    parent.right_node = None
            else:
                print('Removed root node {}'.format(self.root_node.data))
                self.root_node = None

        elif child_count == 1:
            next_node = None
            if node.left_node:
                next_node = node.left_node
            else:
                next_node = node.right_node
            if parent:
                if parent.left_node:
                    parent.left_node = next_node
                else:
                    parent.right_node = next_node
            else:
                self.root_node = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_node
            while leftmost_node.left_node:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_node
            node.data = leftmost_node.data

            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self, data):
        current = self.root_node
        if current is None:
            return
        while current:
            if current.data == data:
                print(current.data)
                return current
            if current.data > data:
                current = current.left_node
            else:
                current = current.right_node
        print('No nodes found with value of {}'.format(data))
        return

    def inorder(self, root_node):
        """
            In this mode of traversal, you would visit the left sub-tree,
            the parent node, and finally the right sub-tree.
        """
        current = root_node

        if current is None:
            return

        self.inorder(current.left_node)
        # print('Left node data {}'.format(current.data))
        print(current.data)
        # print('Right node data {}'.format(current.data))
        self.inorder(current.right_node)

    def preorder(self, root_node):

        """
            To traverse a tree in pre-order mode,
            you would visit the node, the left sub-tree, and the
            right sub-tree node, in that order.
        """

        current = root_node

        if current is None:
            return
        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)


if __name__ == '__main__':
    import random

    tree = Tree()
    for i in range(200):
        if i == 0:
            tree.insert(200)
        n = Node(random.randint(0, 1000))
        tree.insert(n)

    # current = tree.search(200)
    # tree.inorder(current)
    tree.bsf()