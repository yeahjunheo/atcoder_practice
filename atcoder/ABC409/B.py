n = int(input())
A = list(map(int, input().split()))
B = set(A)
res = -1
count = n
for num in range(10**9):
    if count >= num:
        res += 1
        count -= A.count(num)
    else:
        break
print(res)