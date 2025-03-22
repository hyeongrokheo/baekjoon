"""
코딩테스트 연습 > 힙
"""

import heapq


def solution(jobs):
    hq = []
    jobs = [(jobs[i][1], jobs[i][0], i) for i in range(len(jobs))]
    total_count = len(jobs)
    # jobs 0:소요시간, 1:들어온시간, 2:번호
    jobs.sort(key=lambda x: x[1])

    current_time = 0
    total_spend_time = 0

    while len(jobs) > 0 or len(hq) > 0:
        # print(current_time)
        while len(jobs) > 0 and jobs[0][1] <= current_time:
            heapq.heappush(hq, jobs[0])
            jobs = jobs[1:]

        if len(hq) != 0 and hq[0][1] <= current_time:
            job = heapq.heappop(hq)
            # print(job)
            current_time += job[0]
            total_spend_time += current_time - job[1]
        else:
            current_time = jobs[0][1]

    # print(total_spend_time)
    return total_spend_time // total_count

print(solution([[0, 3], [1, 9], [3, 5]]))
print(solution([[0, 1], [5, 1], [0, 1]]))
