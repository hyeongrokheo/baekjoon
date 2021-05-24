"""
problem tier : Silver 1 (solved.ac)
"""

N = int(input())

tree = {}
for i in range(N):
    inp = input().split()
    tree[inp[0]] = inp[1:]

# print(tree)

def preorder(Node):
    print(Node, end='')
    left = tree[Node][0]
    right = tree[Node][1]
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)

def inorder(Node):
    left = tree[Node][0]
    right = tree[Node][1]
    if left != '.':
        inorder(left)
    print(Node, end='')
    if right != '.':
        inorder(right)

def postorder(Node):
    left = tree[Node][0]
    right = tree[Node][1]
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    print(Node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

