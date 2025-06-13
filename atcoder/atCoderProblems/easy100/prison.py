n,m = map(int, input().split())
gates = [(l,r) for l,r in (map(int, input().split()) for _ in range(m))]
lowID, highID = 1, n
for l,r in gates:
    lowID = max(lowID, l)
    highID = min(highID, r)
if lowID <= highID:
    print(highID - lowID + 1)
else:
    print(0)