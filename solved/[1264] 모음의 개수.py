"""
problem tier : Bronze 4 (solved.ac)
"""

VOWELS = ['a', 'e', 'i', 'o', 'u']


def solution():
    while (sentence := input().lower()) != '#':
        print(sum([sentence.count(vowel) for vowel in VOWELS]))


solution()
