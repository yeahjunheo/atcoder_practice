n,s = map(int, input().split())
T = list(map(int, input().split()))
prev = 0
for t in T:
    if t - prev >= s+0.5:
        print("No")
        exit()
    prev = t
print("Yes")