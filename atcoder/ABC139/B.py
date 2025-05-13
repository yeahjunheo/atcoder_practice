A, B = map(int, input().split())
count = 0
if B == 1:
    print(0)
    exit()
while B > 0:
    B = B - A + 1 if count != 0 else B - A
    count += 1
print(count)
    