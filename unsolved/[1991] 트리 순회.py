"""
problem tier : Silver 1 (solved_old.ac)
"""

N = int(input())

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None
        if left:
            self.left = Node(left)
        if right:
            self.right = Node(right)

    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, target, left, right):
        return self._insert(self.root, target, left, right)

    def _insert(self, node, target, left, right):
        if not node:
            return
        if node.value == target:
            return node
        else:
            if self._insert(node.left, target, left, right):

            if left:
                return left
            right = self._insert(node.right, target, left, right)
            if right:
                return right
            return None



binary_tree = BinaryTree()
# binary_tree.root = Node('A', 'B', 'C')
# print(binary_tree.find('A').value)
# print(binary_tree.find('B').value)
# print(binary_tree.find('C').value)
# print(binary_tree.find('D'))

for i in range(N):
    value, left, right = tuple(input().split())
    if left == '.':
        left = None
    if right == '.':
        right = None
    # new_node = Node(value, left=left, right=right)
    target_node = binary_tree.insert(value, left, right)
    if target_node:
        target_node = new_node
    else:
        binary_tree.root = new_node

binary_tree.root.preorder()


# class tree:
#     def __init__(self, value=None):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def find(self, target):
#         if self.value == target:
#             return self
#         else:
#             if self.left:
#                 if self.left.find(target):
#                     return self.left.find(target)
#             if self.right:
#                 if self.right.find(target):
#                     return self.right.find(target)
#             return None
#
#     def tprint(self):
#         if self.left:
#             self.left.tprint()
#         print(self.value)
#         if self.right:
#             self.right.tprint()

    # def insert_left(self, left):
    #     self.left = tree(left, None, None)

    # def insert_right(self, right):
    #     self.left = tree(right, None, None)

    # def find(self, target):
    #     if self.value == target:
    #         return self
    #     elif self.left:
    #         if self.left.find(target):
    #             return self.left
#
# Tree = tree()
# for i in range(N):
#     value, left, right = tuple(input().split())
#     if left == '.':
#         left = None
#     if right == '.':
#         right = None
#     node = tree(value)
#     if Tree.find(value):
#         print(Tree.find(value))
#         Tree.find(value).left = left
#         Tree.find(value).right = right
#     else:
#         Tree.value = value
#         Tree.left = left
#         Tree.right = right
#
# Tree.tprint()
