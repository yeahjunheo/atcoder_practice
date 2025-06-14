n = int(input())
A = []
maxV, nextMaxV = 0, 0
for i in range(n):
    a = int(input())
    if a > maxV:
        nextMaxV = maxV
        maxV = a
    elif a > nextMaxV:
        nextMaxV = a
    A.append(a)
for a in A:
    if a == maxV:
        print(nextMaxV)
    else:
        print(maxV)