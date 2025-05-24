A,B = map(int, input().split())

ab = A/B
left = A//B
right = left + 1
if ab - left < right - ab:
    print(left)
else:
    print(right)