# human=int(input())
# hlist=list(map(int, input().split()))
# hlist.sort()
# group=0
#
# while True:
#     n = hlist[-1]
#     if hlist[-1]>len(hlist):
#         break
#     hlist = hlist[:-n]
#     group += 1
#     if len(hlist)==0:
#         break
# print(group)

n=int(input())
data=list(map(int, input().split()))
data.sort()
result=0
count=0

for i in data:
    count+=1
    if count>=i:
        result+=1
        count=0
print(result)