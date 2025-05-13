A = int(input())
B = int(input())
C = int(input())
X = int(input())

res = 0

for i in range(A + 1):
    curr = X - 500 * i
    if curr >= 0:
        for j in range(B + 1):
            curr2 = curr - 100 * j
            if curr2 >= 0:
                if curr2 // 50 <= C:
                    res += 1
print(res)