n,l = map(int, input().split())
D = list(map(int, input().split()))
if l%3 != 0:
    print(0)
    exit()

points = {0: 1}
curr = 0
for d in D:
    curr += d
    point = curr % l
    if point in points:
        points[point] += 1
    else:
        points[point] = 1

side = l // 3
res = 0

for i,v in points.items():
    if points.get((i + side) % l, 0) > 0 and points.get((i + 2 * side) % l, 0) > 0:
        res += v * points[(i + side) % l] * points[(i + 2 * side) % l]
        points[(i + side) % l] = 0
        points[(i + 2 * side) % l] = 0
print(res)