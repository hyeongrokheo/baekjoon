
def solution(startHeight, descentRate):
    fallenTime = []
    for i in range(len(startHeight)):
        time = startHeight[i] // descentRate[i]
        if startHeight[i] % descentRate[i] != 0:
            time += 1
        fallenTime.append(time)
    print(fallenTime)
    fallenTime.sort()
    count = 0
    for i in range(len(fallenTime)):
        if i+1<=fallenTime[i]:
            count += 1
            # break
        else:
            break
    return count

# print(solution([1,3,5,4,8], [1,2,2,1,2]))
print(solution([4,15,15,12,18,3,8], [2,5,3,2,3,3,2]))