# 피로도

def solution(k, dungeons):

    answer = 0

    dungeons.sort(key=lambda x:x[0], reverse=True)

    for i in dungeons:
        if i[0] <= k:
            print(i[0])
            k -= i[1]
            answer += 1

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
