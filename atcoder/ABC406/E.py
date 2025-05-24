T = int(input())

def popCount(n):
    return bin(n).count('1')

for _ in range(T):
    N, K = map(int, input().split())
    res = 0
    x = (1 << K) - 1
    while x <= N:
        res += x
        c = x & -x
        r = x + c
        x = (((r ^ x) >> 2) // c) | r
    print(res%998244353)