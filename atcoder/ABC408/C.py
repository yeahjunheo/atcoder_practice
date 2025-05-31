n,m = map(int, input().split())
protected = [0] * (n+1)
for _ in range(m):
    start,end = map(int, input().split())
    protected[start-1] += 1
    protected[end] -= 1
currProt = [0] * (n+2)
for i in range(len(protected)):
    currProt[i+1] = currProt[i] + protected[i]
print(min(currProt[1:n+1]))