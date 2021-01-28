# numList=input()
# countZero=0
# countOne=0
#
# for i in range(len(numList)):
#     if numList[i]=='0':
#         if i>0 and numList[i-1]=='0':
#             countZero-=1
#         countZero+=1
#     else:
#         if i>0 and numList[i-1]=='1':
#             countOne-=1
#         countOne+=1
#
# if countZero>countOne:
#     result=countOne
# else:
#     result=countZero
#
# print(min(countZero, countOne))

data=input()
count0=0
count1=0
if data[0]=='1':
    count0+=1
else:
    count1+=1

for i in range(len(data)-1):
    if data[i]!=data[i+1]:
        if data[i+1]=='1':
            count0+=1
        else:
            count1+=1
print(min(count0, count1))