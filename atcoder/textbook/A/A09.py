H,W,N = map(int,input().split())
snow = [[0]*(W+2) for _ in range(H+2)]
for _ in range(N):
    a,b,c,d = map(int,input().split())
    snow[a][b] += 1
    snow[a][d+1] -= 1
    snow[c+1][b] -= 1
    snow[c+1][d+1] += 1
for i in range(1,H+1):
    for j in range(1,W+1):
        snow[i][j] += snow[i-1][j] + snow[i][j-1] - snow[i-1][j-1]
for i in range(1,H+1):
    print(*snow[i][1:W+1])