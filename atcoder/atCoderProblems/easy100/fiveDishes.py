foods = [int(input()) for _ in range(5)]
min_mod = 10
total = 0
for food in foods:
    if food % 10 != 0:
        min_mod = min(min_mod, food % 10)
    total += (food + 9) // 10 * 10
print(total - (10 - min_mod) if min_mod != 10 else total)