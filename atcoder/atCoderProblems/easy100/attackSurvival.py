n,k,q = map(int, input().split())
ans = [0] * n
for _ in range(q):
    a = int(input()) - 1
    ans[a] += 1
for i in range(n):
    if ans[i] + k - q > 0:
        print("Yes")
    else:
        print("No")