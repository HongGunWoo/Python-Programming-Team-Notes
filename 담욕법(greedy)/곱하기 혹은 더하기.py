# s='567'
# result=0
# for i in s:
#     i=int(i)
#     if i==0 or i==1 or result==0:
#         result+=i
#     else:
#         result*=i
# print(result)

data=input()
result=int(data[0])
for i in range(1, len(data)):
    num=int(data[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num
print(result)