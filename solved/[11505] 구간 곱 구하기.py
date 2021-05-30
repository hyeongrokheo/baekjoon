"""
problem tier : Gold 1 (solved.ac)
"""

import sys


class SegmentTree:
    def __init__(self, size):
        base = 1
        exp = 0
        while base < size:
            base *= 2
            exp += 1

        self.size = 2 ** exp
        self.init = 1
        self.tree = [self.init for i in range(self.size * 2)]

    def update(self, index, value):
        return self._update(index, value, 1, 1, self.size)

    def _update(self, index, value, tree_index, section_left, section_right):
        if section_left == section_right:
            # prev_value = self.tree[tree_index]
            self.tree[tree_index] = value
            return self.tree[tree_index]
        else:
            mid = (section_left + section_right) // 2
            if index <= mid:
                result = self._update(index, value, tree_index * 2, section_left, mid)
                self.tree[tree_index] = (result * self.tree[tree_index * 2 + 1]) % 1000000007
            else:
                result = self._update(index, value, tree_index * 2 + 1, mid + 1, section_right)
                self.tree[tree_index] = (result * self.tree[tree_index * 2]) % 1000000007
        return self.tree[tree_index]

    def query(self, start, end):
        return self._query(start, end, 1, 1, self.size)

    def _query(self, start, end, tree_index, section_left, section_right):
        if section_right < start or section_left > end:
            return self.init
        elif start <= section_left and section_right <= end:
            return self.tree[tree_index]
        else:
            mid = (section_left + section_right) // 2
            left_query = self._query(start, end, tree_index * 2, section_left, mid)
            right_query = self._query(start, end, tree_index * 2 + 1, mid + 1, section_right)
            return (left_query * right_query) % 1000000007


N, M, K = map(int, input().split())

tree = SegmentTree(size=N)

for i in range(N):
    tree.update(i+1, int(sys.stdin.readline()))

for i in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        tree.update(b, c)
    else:
        print(tree.query(b, c))
