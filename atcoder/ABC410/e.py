from functools import lru_cache

n, h, m = map(int, input().split())
monsters = []
for _ in range(n):
    a, b = map(int, input().split())
    monsters.append((a, b))


@lru_cache(maxsize=None)
def dfs(monster_idx, current_h, current_m):
    if monster_idx == n:
        return 0

    a, b = monsters[monster_idx]
    max_defeated = 0

    if current_h >= a:
        defeated = 1 + dfs(monster_idx + 1, current_h - a, current_m)
        max_defeated = max(max_defeated, defeated)

    if current_m >= b:
        defeated = 1 + dfs(monster_idx + 1, current_h, current_m - b)
        max_defeated = max(max_defeated, defeated)

    return max_defeated


result = dfs(0, h, m)
print(result)
