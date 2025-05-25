N,Q = map(int,input().split())
A = list(map(int,input().split()))
prefixSum = [0] * (N + 1)
for i in range(1,N+1):
    prefixSum[i] = prefixSum[i-1] + A[i-1]
for _ in range(Q):
    L,R = map(int,input().split())
    print(prefixSum[R] - prefixSum[L-1])
