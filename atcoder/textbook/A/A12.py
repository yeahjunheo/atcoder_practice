n,k = map(int, input().split())
a = list(map(int, input().split()))
ng = 0
ok = 10**9 + 1
while ok - ng > 1:
    mid = (ok + ng) // 2
    temp = 0
    for i in range(n):
        temp += mid // a[i]
    if temp < k:
        ng = mid
    else:
        ok = mid
print(ok)

# n,k = map(int, input().split())
# a = list(map(int, input().split()))
# time = 0
# while True:
#     temp = 0
#     for i in range(n):
#         temp += time // a[i]
#     if temp < k:
#         time += 1
#     else:
#         print(time)
#         break