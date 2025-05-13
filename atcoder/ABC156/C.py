N = int(input())
X = list(map(int, input().split()))
avg = sum(X) // N + int(sum(X) % N > N//2)
total = 0
for i in range(N):
    total += (X[i] - avg) ** 2
print(total)