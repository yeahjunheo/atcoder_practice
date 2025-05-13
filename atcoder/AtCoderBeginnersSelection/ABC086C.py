N = int(input())
prevTime, prevX, prevY = 0, 0, 0
for _ in range(N):
    goalTime, goalX, goalY = map(int, input().split())
    deltaT = goalTime - prevTime
    deltaP = abs(goalX - prevX) + abs(goalY - prevY)
    if deltaP > deltaT or (deltaT - deltaP) % 2 != 0:
        print('No')
        exit()
    prevTime, prevX, prevY = goalTime, goalX, goalY

print('Yes')