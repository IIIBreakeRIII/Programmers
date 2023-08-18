# 최댓값과 최솟값

def solution(s):
    answer = ""
    s_list = list(map(str, s.split(" ")))
    int_list = []

    for i in range(len(s_list)):
        int_list.append(int(s_list[i]))

    answer += str(min(int_list))
    answer += " "
    answer += str(max(int_list))

    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
