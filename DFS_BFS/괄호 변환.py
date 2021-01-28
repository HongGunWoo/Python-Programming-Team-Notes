# def solution(p):
#     if p == "":
#         return ""
#     u, v = share(p)
#     if u[0] == "(" and u[-1] == ")":
#         return u + solution(v)
#     else:
#         emp = '('
#         emp += solution(v) + ')'
#         for i in range(1, len(u)-1):
#             if u[i] == '(':
#                 emp += ')'
#             else:
#                 emp += '('
#         return emp
#
# def share(p):
#     u = ''
#     v = ''
#     left = 0
#     right = 0
#     for i in range(len(p)):
#         if p[i] == "(":
#             left += 1
#             u += p[i]
#         elif p[i] == ")":
#             right += 1
#             u += p[i]
#         if left == right:
#             v += p[i+1:]
#             break
#     return u, v
#
# print(solution("(()())()"))

def balance_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balance_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

print(solution("()))((()"))