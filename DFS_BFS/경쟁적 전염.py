# import time
# n, k = map(int, input().split())
# start = time.time()
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
# s, x, y = map(int, input().split())
#
# x = x-1
# y = y-1
#
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# virous_index = []
#
# def dfs(virous_index, virous):
#     for row, column in virous_index:
#         for i in range(4):
#             nx = row + dx[i]
#             ny = column + dy[i]
#             #상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
#             if nx >= 0 and nx < n and ny >= 0 and ny < n:
#                 if graph[nx][ny] == 0:
#                     graph[nx][ny] = virous
#
# for _ in range(s):
#     for virous in range(1, k+1):
#         for i in range(n):
#             for j in range(n):
#                 if graph[i][j] == virous:
#                     virous_index.append([i, j])
#         dfs(virous_index, virous)
#     if graph[x][y] != 0:
#         break
#
# print(graph[x][y])
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

import time
from collections import deque

n,k = map(int, input().split())
start = time.time()  # 시작 시간 저장

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y, = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))
print(graph[target_x-1][target_y-1])
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
