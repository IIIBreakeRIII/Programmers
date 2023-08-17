# 숫자 짝꿍

# def solution(x, y):
#     answer = ''
# 
#     num_x_list = list(x)
#     num_y_list = list(y)
#     answer_list = []
# 
#     for i in range(len(num_x_list)):
#         for j in range(len(num_y_list)):
#             if num_x_list[i] == num_y_list[j]:
#                 answer_list.append(int(num_x_list[i]))
#                 num_y_list[j] = "-1"
# 
#     
#     answer_list.sort(reverse=True)
#     
#     if len(answer_list) == 0:
#         return "-1"
#     elif answer_list[0] == 0:
#         return "0"
#     else:
#         for i in range(len(answer_list)):
#             answer += str(answer_list[i])
# 
#     return answer
# X & Y 에서 각 자리 숫자들이 몇 번씩 나왔는지 체크해서 서로 비교

def solution(x, y):
    answer = ''
    
    x_count = [0 for _ in range(10)]
    y_count = [0 for _ in range(10)]

    for i in x:
        temp = int(i)
        x_count[temp] += 1

    for i in y:
        temp = int(i)
        y_count[temp] += 1

    for i in range(9, -1, -1):
        temp = str(i) * min(x_count[i], y_count[i])
        answer += temp

    if len(answer) == 0:
        return "-1"
    elif answer[0] == "0":
        return "0"
    else:
        return answer

print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))
