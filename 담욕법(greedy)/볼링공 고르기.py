# from itertools import combinations
#
# num, weight = map(int,input().split())
# wList = list(map(int,input().split()))
# sumList = list(combinations(wList, 2))
#
# for i in sumList:
#     if i[0]==i[1]:
#         sumList.remove(i)
# print(len(sumList))

n, m = map(int,input().split())
data = list(map(int,input().split()))
array=[0]*11

for x in data:
    array[x]+=1
result=0
for i in range(1, m+1):
    n -= array[i]
    result+= array[i]*n
print(result)