'''
A adds a 0 at the end of t
B increases the number of digits in t by 1, where 9 goes back to 0
'''

import collections

s = input()
n = len(s)
if not s:
    print(0)

q = collections.deque([("", 0)])
visited = {"": 0}

while q:
    current_t, steps = q.popleft()

    if current_t == s:
        print(steps)

    # Press button A (append 0)
    next_t_a = current_t + "0"
    if len(next_t_a) <= n and next_t_a not in visited:
        visited[next_t_a] = steps + 1
        q.append((next_t_a, steps + 1))

    # Press button B (replace each digit with the next digit)
    if current_t:
        next_t_b_list = []
        for char in current_t:
            digit = int(char)
            next_digit = (digit + 1) % 10
            next_t_b_list.append(str(next_digit))
        next_t_b = "".join(next_t_b_list)
    else:
        next_t_b = "1"

    if len(next_t_b) <= n + 1 and next_t_b not in visited: # slightly relaxed length check
        visited[next_t_b] = steps + 1
        q.append((next_t_b, steps + 1))