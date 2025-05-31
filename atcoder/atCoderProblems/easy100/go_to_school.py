'''
C - Go To School
https://atcoder.jp/contests/abc142/tasks/abc142_c
'''

n = int(input())
A = list(map(int, input().split()))
order = [0]*(n+1)
for i,a in enumerate(A):
    order[a] = i+1
print(*order[1:])