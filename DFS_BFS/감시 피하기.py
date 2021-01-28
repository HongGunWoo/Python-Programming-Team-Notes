from itertools import combinations
n = int(input())
graph = []
empty_list=[]
teacher_list=[]
for i in range(n):
    graph.append(list(input().split()))
    for j in range(len(graph[i])):
        if graph[i][j] == 'X':
            empty_list.append([i, j])
        if graph[i][j] == 'T':
            teacher_list.append([i, j])

empty_list = list(combinations(empty_list, 3))

def dfs(x, y):
    if up(x, y) and down(x, y) and left(x, y) and right(x, y):
        return True
    else:
        return False

def up(x, y):
    while y<n:
        if graph[x][y] == "S":
            return False
        if graph[x][y] == "O":
            return True
        y += 1
    return True

def down(x, y):
    while y >= 0:
        if graph[x][y] == "S":
            return False
        if graph[x][y] == "O":
            return True
        y -= 1
    return True

def left(x, y):
    while x >= 0:
        if graph[x][y] == "S":
            return False
        if graph[x][y] == "O":
            return True
        x -= 1
    return True
def right(x, y):
    while x < n:
        if graph[x][y] == "S":
            return False
        if graph[x][y] == "O":
            return True
        x += 1
    return True

for empty in empty_list:
    result = len(teacher_list)
    for x, y in empty:
        graph[x][y] = 'O'
    for x, y in teacher_list:
        if not dfs(x, y):
            result -= 1
    if result == len(teacher_list):
        print('YES')
        break
    for x, y in empty:
        graph[x][y] = 'X'
if result != len(teacher_list):
    print('NO')
