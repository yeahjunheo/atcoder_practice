n = int(input())
P = list(map(int, input().split()))
count = 1
minPrev = P[0]
for i in range(1,n):
    if P[i] < minPrev:
        count += 1
        minPrev = P[i]
print(count)