# 괄호 회전하기

def check_bracket(bracket_list):
    stack = []
    for i in bracket_list:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        return True

def solution(s):
    s_list = list(s)
    count = 0

    for _ in range(len(s_list)):
        temp = s_list.pop(0)
        s_list.append(temp)

        if check_bracket(s_list) == True:
            count += 1

    return count

print(solution("[](){}"))
print(solution("[)(]"))
