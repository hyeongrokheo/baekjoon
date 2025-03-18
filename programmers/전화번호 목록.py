"""
코딩테스트 연습 > 해시
"""


def solution_sort(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        p1 = phone_book[i]
        p2 = phone_book[i+1]

        if p2.startswith(p1):
            return False

    return True


def solution(phone_book):
    # hash 이용한 풀이
    dct = {}

    for phone in phone_book:
        dct[phone] = 1

    for phone in phone_book:
        temp = ""

        for char in phone[:-1]:
            temp += char

            if dct.get(temp) == 1:
                return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
