n, q = map(int, input().split())
X = list(map(int, input().split()))
boxes = [0] * n
res = []
for x in X:
    if x >= 1:
        boxes[x-1] += 1
        res.append(x)
    else:
        minV = min(boxes)
        minIdx = boxes.index(minV)
        boxes[minIdx] += 1
        res.append(minIdx + 1)
print(*res)