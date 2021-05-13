"""
가장 작은 수를 기억하는 segment tree 만들어보자....
"""

import sys
sys.setrecursionlimit(10**9)


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = Node()

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, cursor):
        if cursor:
            self._print_tree(cursor.left)
            self._print_tree(cursor.right)
            if cursor.value:
                print(cursor.value)

    def insert(self, value):
        cursor = self.root
        while True:
            if cursor.value:
                if value < cursor.value:
                    if cursor.left:
                        cursor = cursor.left
                    else:
                        cursor.left = Node()
                        cursor = cursor.left
                elif value > cursor.value:
                    if cursor.right:
                        cursor = cursor.right
                    else:
                        cursor.right = Node()
                        cursor = cursor.right
            else:
                cursor.value = value
                break


tree = Tree()
while True:
    try:
        tree.insert(int(sys.stdin.readline()))
    except:
        break

tree.print_tree()
