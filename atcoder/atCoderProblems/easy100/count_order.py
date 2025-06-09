from itertools import permutations

n = int(input())
p_list = tuple(map(int, input().split()))
q_list = tuple(map(int, input().split()))
perm_order = tuple(permutations(range(1, n + 1)))
a = perm_order.index(p_list)
b = perm_order.index(q_list)
print(abs(a - b))