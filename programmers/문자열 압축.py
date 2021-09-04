"""
코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 문자열 압축
"""

def solution(s):
    result = len(s)

    for length in range(1, len(s)+1):
        total_length = len(s)
        new_list = [s[j:j+length] for j in range(0, len(s), length)]
        flag = 0
        count_list = []
        for i in range(len(new_list)):
            if i == 0:
                continue
            if new_list[i] == new_list[i-1]:
                flag += 1
            else:
                count_list.append(flag)
                flag = 0
        if flag != 0:
            count_list.append(flag)
        for c in count_list:
            if c == 0:
                continue
            else:
                total_length = total_length - (c * length) + len(str(c+1))
        if result > total_length:
            result = total_length
    return result


# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
print(solution("aaaaaaaaaa"))