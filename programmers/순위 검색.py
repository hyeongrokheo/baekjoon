"""
코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 순위 검색
"""

# dictionary = {
#     'cpp': 1,
#     'java': 2,
#     'python': 3
# }

def solution(info, query):
    # print(info)
    new_info = []
    for inf in info:
        temp = inf.split(' ')

        temp[4] = int(temp[4])
        new_info.append(temp)

    new_info.sort(key=lambda x: x[4])

    data = {}
    for inf in new_info:
        key_list = ['', inf[0], inf[1], inf[2], inf[3], inf[0]+inf[1], inf[0]+inf[2], inf[0]+inf[3], inf[1]+inf[2], inf[1]+inf[3], inf[2]+inf[3], inf[0]+inf[1]+inf[2], inf[0]+inf[1]+inf[3], inf[0]+inf[2]+inf[3], inf[1]+inf[2]+inf[3], inf[0]+inf[1]+inf[2]+inf[3]]
        for key in key_list:
            try:
                data[key].append(inf[4])
            except:
                data[key] = [inf[4]]

    answer = []
    for q in query:
        q = q.split(' ')
        for i in range(len(q)):
            if q[i] == '-':
                q[i] = ''
        target_info = q[0]+q[2]+q[4]+q[6]
        target_score = int(q[7])

        if target_info not in data.keys():
            answer.append(0)
            continue
        score_list = data[target_info]
        # if len(score_list) == 0:
        #     answer.append(0)
        if len(score_list) == 1:
            if score_list[0] >= target_score:
                answer.append(1)
            else:
                answer.append(0)
        else:
            left = 0
            right = len(score_list)-1
            while left <= right:
                mid = (left+right)//2
                if score_list[mid] < target_score:
                    left = mid+1
                elif score_list[mid] >= target_score:
                    right = mid-1
            answer.append(len(score_list)-left)
    return answer


print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]
               ))

print(solution(['a b c d 120'], ['a and b and c and dd 121']))