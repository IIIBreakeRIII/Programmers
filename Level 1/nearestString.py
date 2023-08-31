# 가장 가까운 같은 글자

def solution(s):

    answer = []
    temp_list = []

    for i in range(len(s)):

        if s[i] not in temp_list:
            temp_list.append(s[i])
            answer.append(-1)
        else:
            answer.append(i - temp_list.index(s[i]))
            temp_list[temp_list.index(s[i])] = 0
            temp_list.append(s[i])

    return answer

print(solution("banana"))
print(solution("foobar"))
