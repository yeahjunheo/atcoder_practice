a,b,m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
min_a = min(a_list)
min_b = min(b_list)
min_cost = min_a + min_b
for _ in range(m):
    x,y,c = map(int, input().split())
    curr_cost = a_list[x-1] + b_list[y-1] - c
    min_cost = min(min_cost, curr_cost)
print(min_cost)