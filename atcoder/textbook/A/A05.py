N,K = map(int,input().split())
count = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        a = K - i - j
        if 1 <= a <= N:
            count += 1
print(count)