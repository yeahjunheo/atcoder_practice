N = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 0
isA = True
for i in range(N-1, -1, -1):
    if isA:
        res += arr[i]
    else:
        res -= arr[i]
    isA = not isA
print(res)