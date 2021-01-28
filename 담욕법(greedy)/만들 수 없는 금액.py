# from itertools import combinations
#
# amount = int(input())
# coinList = list(map(int, input().split()))
# sumList = []
# comList = []
# answer = 1
# s=0
#
# for i in range(amount):
#     comList += list(combinations(coinList, i+1))
#
# for j in range(len(comList)):
#     for z in comList[j]:
#         s += z
#     if s not in sumList:
#         sumList.append(s)
#     s=0
#
# while answer in sumList:
#     answer+=1
#
# print(answer)

n = int(input())
data = list(map(int, input().split()))
data.sort()
target=1
for x in data:
    if target<x:
        break
    target+=x
print(target)