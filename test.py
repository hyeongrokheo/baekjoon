
import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

nodes = {}

def solution():
    N, M, V = map(int, input().split())

    print(N, M, V)
    for i in range(M):
        S, E = map(int, input().split())
        if S not in nodes.keys():
            nodes[S] = []
        if E not in nodes.keys():
            nodes[E] = []
        nodes[S].append(E)
        nodes[E].append(S)

    print(nodes)




print(solution())
