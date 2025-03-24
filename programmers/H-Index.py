"""
코딩테스트 연습 > 정렬
"""


def solution(citations):
    citations.sort()

    for i in range(len(citations)):
        h_index = len(citations) - i
        citation = citations[i]
        if citation >= h_index:
            return h_index
    return 0
