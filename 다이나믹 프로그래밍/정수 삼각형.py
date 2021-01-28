n = int(input())
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))
for j in range(1, n):
    for z in range(len(array[j])):
        if z == 0:
            array[j][z] = array[j][z] + array[j-1][z]
        elif z == len(array[j])-1:
            array[j][z] = array[j][z] + array[j-1][z-1]
        else:
            array[j][z] = array[j][z] + max(array[j-1][z], array[j-1][z-1])
print(max(array[n-1]))