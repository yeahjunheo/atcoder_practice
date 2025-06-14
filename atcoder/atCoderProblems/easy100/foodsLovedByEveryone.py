n, m = map(int, input().split())
food = [0]*(m+1)
for _ in range(n):
    k, *a = map(int, input().split())
    for i in range(k):
        food[a[i]] += 1
print(food.count(n))