N,K = map(int, input().split())
A = list(map(int, input().split()))

res = 1
for i in range(N):
    res *= A[i]
    if len(str(res)) > K:
        res = 1
print(res)