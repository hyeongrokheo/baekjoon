"""
problem tier : Gold 2 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

while T:
    T -= 1

    total = set()
    networks = []
    F = int(sys.stdin.readline())
    for i in range(F):
        f1, f2 = sys.stdin.readline().strip().split()
        if f1 not in total and f2 not in total:
            print(2)
            total.add(f1)
            total.add(f2)
            networks.append(set([f1, f2]))
        elif f1 in total and f2 not in total:
            for n in networks:
                if f1 in n:
                    n.add(f2)
                    print(len(n))
                    break
            total.add(f2)
        elif f1 not in total and f2 in total:
            for n in networks:
                if f2 in n:
                    n.add(f1)
                    print(len(n))
                    break
            total.add(f1)
        else:
            for i in range(len(networks)):
                if f1 in networks[i]:
                    for j in range(len(networks)):
                        if f2 in networks[j]:
                            if i == j:
                                print(len(networks[i]))
                            else:
                                # print(networks[i], networks[j])
                                # print(networks[i].union(networks[j]))
                                networks[i] = networks[i].union(networks[j])
                                # print(n, m)
                                print(len(networks[i]))
                                networks.remove(networks[j])
                            break
                    break
        # print(networks)


