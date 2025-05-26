N,X = map(int, input().split())
A = list(map(int, input().split()))

l,r = 0,N-1
while l <= r:
    m = (l + r) // 2
    if A[m] == X:
        print(m+1)
        break
    elif A[m] < X:
        l = m + 1
    else:
        r = m - 1