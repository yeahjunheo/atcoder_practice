'''
C - Divide the Problems
https://atcoder.jp/contests/abc132/tasks/abc132_c
'''

n = int(input())
D = list(map(int, input().split()))
D.sort()
left, right = D[n//2-1], D[n//2]
print(right-left)