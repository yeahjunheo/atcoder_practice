N, A, B = map(int, input().split())

res = 0

for num in range(1, N + 1):
    digit_sum = sum(map(int, str(num)))
    if A <= digit_sum <= B:
        res += num
print(res)