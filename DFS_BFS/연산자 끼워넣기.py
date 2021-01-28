# from itertools import permutations
#
# n = int(input())
# n_list = list(map(int, input().split()))
# # 덧셈 = 0, 뺄셈 = 1, 곱셈 = 2, 나눗셈 = 3
# operations = list(map(int, input().split()))
# operations_list = []
#
# def cal(i, result, op):
#     if op == 0:
#         return result + n_list[i+1]
#     elif op == 1:
#         return result - n_list[i+1]
#     elif op == 2:
#         return result * n_list[i+1]
#     elif op == 3:
#         if result < 0:
#             return -(-result // n_list[i+1])
#         else:
#             return result//n_list[i+1]
#
# for i in range(4):
#     for _ in range(operations[i]):
#         operations_list.append(i)
# operations_list = list(permutations(operations_list, len(operations_list)))
# max_num = -1000000000
# min_num = 1000000000
# for op in operations_list:
#     result = n_list[0]
#     for i in range(len(op)):
#         result = cal(i, result, op[i])
#     max_num = max(max_num, result)
#     min_num = min(min_num, result)
#
# print(max_num)
# print(min_num)

n = int(input())
data = list(map(int, input().split()))
# 덧셈 = 0, 뺄셈 = 1, 곱셈 = 2, 나눗셈 = 3
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)