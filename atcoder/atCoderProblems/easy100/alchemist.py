'''
C - Alchemist
https://atcoder.jp/contests/abc138/tasks/abc138_c
'''

n = int(input())
V = list(map(float, input().split()))
V.sort(reverse=True)
while len(V) > 1:
    a = V.pop()
    V[-1] = (V[-1] + a) / 2
print(int(V[0]) if V[0].is_integer() else V[0])