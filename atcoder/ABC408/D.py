t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    count = [0] * (n + 1)
    for i in range(n):
        count[i + 1] = count[i] + (1 if s[i] == "0" else -1)
    totOnes = s.count("1")
    ma = 0
    res = 0
    for i in range(n + 1):
        res = min(res, count[i] - ma)
        ma = max(ma, count[i])

    print(totOnes + res)
