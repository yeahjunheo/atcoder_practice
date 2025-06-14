n = int(input())
A = list(map(int, input().split()))
k = int(input())
count = 0
for a in A:
    if k <= a:
        count += 1
print(count)