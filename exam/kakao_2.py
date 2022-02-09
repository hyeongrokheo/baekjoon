

from collections import deque

current_J_card = 'X'
win_dict = {
    'R': 'P',
    'S': 'R',
    'P': 'S'
}
swap_count = 0

def fight(a, b):
    global current_J_card
    global swap_count
    if a == 'X':
        if current_J_card != win_dict[b]:
            current_J_card = win_dict[b]
            swap_count += 1
        return 0
    elif b == 'X':
        if current_J_card != win_dict[a]:
            current_J_card = win_dict[a]
            swap_count += 1
        return 1
    else:
        if [a,b] in [['R', 'S'], ['S', 'P'], ['P', 'R']]:
            return 0
        elif a == b:
            return -1
        else:
            return 1

def start_round(cards):
    new_cards = []
    free_win = None:


def solution(n, a, cards):
    cards = deque(list(cards))
    cards.insert(a, 'X')
    print(cards)

    count = 0
    new_cards = []
    while len(cards) >= 2:
        print(cards)
        cards = start_rount(cards)
    print(cards)







print(solution(4, 1, 'PRS'))
