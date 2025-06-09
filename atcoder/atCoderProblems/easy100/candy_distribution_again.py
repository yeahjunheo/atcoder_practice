n,x = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
count = 0
while x > 0 and A:
    a = A.pop()
    count += 1 if a <= x else 0
    x -= a
if x > 0:
    count -= 1
print(count)