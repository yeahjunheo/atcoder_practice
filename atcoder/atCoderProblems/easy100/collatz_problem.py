s = int(input())
visited = set()
i = 1
visited.add(s)
while True:
    i += 1
    s = s // 2 if s%2==0 else 3*s + 1
    visited.add(s)
    if len(visited) < i:
        print(i)
        break