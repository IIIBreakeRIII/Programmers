# 올바른 괄호

# first answer, timeout
def first_solution(s):
    
    list_s = list(s)
    stack = []

    for i in range(len(s)):
        if i == 0 or len(stack) == 0 or list_s[i] == stack[0]:
            stack.append(list_s[i])
            if stack[0] == ")":
                return False
        else:
            stack.remove(stack[len(stack) - 1])

    if len(stack) != 0:
        return False
    else:
        return True

def solution(s):
    stack = []

    for i in s:
        if i == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
print(solution("())()"))
