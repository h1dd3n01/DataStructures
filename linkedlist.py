# class SingleNode:
#     def __init__(self, data=None, next_node=None):
#         self.data = data
#         self.next = next_node
#
#
# class SingleList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#
#     def append(self, data):
#         node = SingleNode(data=data)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#             print('First node added to beginning')
#
#         else:
#             current = self.tail
#             self.tail.next = node
#             self.tail = node
#             print('Last node added to end')
#         self.count += 1
#
#     def iter(self):
#         current = self.head
#         while current is not None:
#             # print(current.data)
#             yield current
#             current = current.next
#
#     def find(self, data):
#         current = self.head
#         while current is not None:
#             if current.data == data:
#                 return True
#             current = current.next
#         return False
#
#     def delete(self, data):
#         current = self.head
#         prev = self.head
#         while current is not None:
#             if current.data == data:
#                 prev.next = current.next
#                 self.count -= 1
#                 return True
#             prev = current
#             current = current.next
#         return False
#
#
# # Single LinkedList
# if __name__ == '__main__':
#     v = 'Hi'
#     z = 'Bye'
#     c = 'Bye bye'
#
#     l = SingleList()
#     l.append(v)
#     l.append(z)
#     l.append(c)
#     print(l.delete('Hi'))


class DoubleNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # If List is circular

    # def append(self, data):
    #     node = DoubleNode(data)
    #
    #     if self.count == 0:
    #         self.head = node
    #         self.tail = node
    #         self.count += 1
    #     else:
    #         node.next = self.head
    #         node.prev = self.tail
    #         self.head.next = node
    #         self.tail.prev = node
    #         self.tail = node
    #         self.count += 1

    # def delete(self, data):
    #     if self.head.data == data:
    #         self.head.prev.next = self.head.next
    #         self.head = self.head.prev
    #         self.tail.prev = self.head
    #         self.count -= 1
    #         return True
    #     elif self.tail.data == data:
    #         self.tail.next.prev = self.head
    #         self.head.next = self.tail.prev
    #         self.tail = self.tail.prev
    #         self.count -= 1
    #         return True
    #     else:
    #         node = self.head
    #         while node is not None:
    #             if node.data == data:
    #                 node.prev.next = node.next
    #                 node.next.prev = node.prev
    #                 self.count -= 1
    #                 return True
    #             node = node.next
    #     return False






    def append(self, data):
        node = DoubleNode(data)
        if self.count == 0:
            self.head = node
            self.tail = node
            self.count += 1
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.count += 1

    def iter(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def delete(self, data):
        node = self.head
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return True
        while node is not None:
            if node.data == data:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.count -= 1
                return True
            node = node.next
        return False

    def find(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False


if __name__ == '__main__':
    pass
