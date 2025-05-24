H,W,N = map(int, input().split())
G = dict(i+1 for i in range(H + W))

for _ in range(N):
    x,y = map(int, input().split())


Q = int(input())
for _ in range(Q):
    a,b = map(int, input().split())
    if a == 1:
        print(xrow[b-1])
        xrow[b-1] = 0
    else:
        print(ycol[b-1])
        ycol[b-1] = 0

    # if a == 1:
    #     print(G[b-1].count(1))
    #     G[b-1] = [0] * W
    # else:
    #     count = 0
    #     for i in range(H):
    #         if G[i][b-1] == 1:
    #             count += 1
    #             G[i][b-1] = 0
    #     print(count)