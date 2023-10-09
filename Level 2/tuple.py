# 튜플

def solution(s):

    answer = []

    # slicing s
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)

    # repeat all attribute
    for i in s:
        temp = i.split(",")
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
