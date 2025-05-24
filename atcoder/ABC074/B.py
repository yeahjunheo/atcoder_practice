"""
B - Collecting Balls (Easy Version)

        K
O O O O X
O X O O O
X O O O O
O O O X O

"""

N = int(input())
K = int(input())
X = list(map(int, input().split()))
totDist = 0

for i in range(N):
    ballPos = X[i]
    ballBPos = abs(ballPos - K)
    if ballBPos < ballPos:
        ballPos = ballBPos
    totDist += 2*ballPos

print(totDist)