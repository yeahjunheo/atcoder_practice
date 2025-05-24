N = int(input())

for i in range(N, 0, -1):
    num = [int(x) for x in str(i)]
    if num.count(3) > 0:
        continue
    if sum(num) % 3 == 0:
        continue
    print(i)
    break