n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

S = set()
for _a in a:
    for _b in b:
        S.add(k - (_a + _b))

for _c in c:
    for _d in d:
        if _c + _d in S:
            print("Yes")
            exit()
print("No")