# import itertools
#
# n, m = map(int, input().split())
# city = []
# home_index = []
# chicken_index = []
# save_chicken = []
# answer=[]
#
# for _ in range(n):
#     city.append(list(map(int, input().split())))
#
# for x in range(n):
#     for y in range(n):
#         if city[x][y] == 1:
#             home_index.append([x, y])
#         elif city[x][y] == 2:
#             chicken_index.append([x, y])
#
# save_chicken=list(itertools.combinations(chicken_index, m))
#
# for i in range(len(save_chicken)):
#     chicken_load=[]
#     for x, y in home_index:
#         length = n*2
#         for j in range(len(save_chicken[0])):
#                 length = min(length, abs(x-save_chicken[i][j][0])+abs(y-save_chicken[i][j][1]))
#         chicken_load.append(length)
#     answer.append(sum(chicken_load))
# answer.sort()
# print(answer[0])

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result+=temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
print(result)
