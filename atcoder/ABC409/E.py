import sys

sys.setrecursionlimit(1 << 25)

n = int(input())
X = list(map(int, input().split()))
edges = [[] for _ in range(n)]
Br = dict()
for _ in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, w))
    edges[v].append((u, w))

res = 0

def dfs(u, p):
    global res
    cur = X[u]
    for v, w in edges[u]:
        if v == p:
            continue
        sub = dfs(v, u)
        res += abs(sub) * w
        cur += sub
    return cur

dfs(0, -1)
print(res)