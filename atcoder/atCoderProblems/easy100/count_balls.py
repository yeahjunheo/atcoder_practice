n,a,b = map(int, input().split())
count = 0
rec = n // (a+b)
count += rec * a
count += min(n % (a + b), a)
print(count)