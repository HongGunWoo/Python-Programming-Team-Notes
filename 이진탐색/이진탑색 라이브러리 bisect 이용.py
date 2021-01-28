from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
array = list(map(int, input().split()))
left = bisect_left(array, x)
right = bisect_right(array, x)

if right-left == 0:
    print(-1)
else:
    print(right-left)