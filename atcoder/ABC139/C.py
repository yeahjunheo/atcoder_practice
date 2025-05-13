N = int(input())
A = list(map(int, input().split()))
res = [0]*N
for i in range(N-2, -1, -1):
    if A[i] >= A[i+1]:
        res[i] = res[i+1] + 1
    else:
        res[i] = 0
print(max(res))