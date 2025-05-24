N = int(input())
P = list(map(int, input().split()))

tildeB = []
tildeS = []
isTilde = False

for i in range(1,N-1):
    if P[i-1] < P[i] > P[i+1] and isTilde:
        tildeB.append(i)
    elif P[i-1] > P[i] < P[i+1] and isTilde:
        tildeS.append(i)
    else:
        if P[i-1] < P[i]:
            isTilde = True
        else:
            isTilde = False
print(tildeB, tildeS)