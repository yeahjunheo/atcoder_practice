H,W = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(H)]
Q = int(input())
cumX = [[0]*(W+1) for _ in range(H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        cumX[i][j] = matrix[i-1][j-1] + cumX[i-1][j] + cumX[i][j-1] - cumX[i-1][j-1]
for _ in range(Q):
    a,b,c,d = map(int,input().split())
    ans = cumX[c][d] - cumX[a-1][d] - cumX[c][b-1] + cumX[a-1][b-1]
    print(ans)
# H,W = map(int,input().split())
# mat = {i+1: [0]*(W+1) for i in range(H)}
# for i in range(H):
#     row = list(map(int, input().split()))
#     for j in range(W):
#         mat[i+1][j+1] += row[j] + mat[i+1][j]
# Q = int(input())
# for _ in range(Q):
#     a,b,c,d = map(int,input().split())
#     ans = 0
#     for i in range(a,c+1):
#         ans += mat[i][d] - mat[i][b-1]
#     print(ans)