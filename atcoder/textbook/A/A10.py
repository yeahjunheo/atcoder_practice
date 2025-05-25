N = int(input())
A = list(map(int, input().split()))
D = int(input())

lmax = [0] * (N + 1)
rmax = [0] * (N + 1)
for i in range(N):
    lmax[i+1] = max(lmax[i], A[i])
for i in range(N-1, -1, -1):
    rmax[i] = max(rmax[i+1], A[i])
for _ in range(D):
    l,r = map(int, input().split())
    print(max(lmax[l-1], rmax[r]))