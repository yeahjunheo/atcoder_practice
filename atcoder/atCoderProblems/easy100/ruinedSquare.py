x1, y1, x2, y2 = map(int, input().split())
delta = [x2 - x1, y2 - y1]
x3, y3 = x2 - delta[1], y2 + delta[0]
x4, y4 = x3 - delta[0], y3 - delta[1]
print(x3, y3, x4, y4)