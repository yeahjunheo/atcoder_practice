N = int(input())
d = [int(input()) for _ in range(N)]
d.sort(reverse=True)
count = 1
for i in range(1,N):
    if d[i] < d[i-1]:
        count += 1
print(count)