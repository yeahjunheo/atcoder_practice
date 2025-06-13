n = int(input())
s = input()
maxX, x = 0, 0

for char in s:
    if char == 'I':
        x += 1
    elif char == 'D':
        x -= 1
    maxX = max(maxX, x)
print(maxX)