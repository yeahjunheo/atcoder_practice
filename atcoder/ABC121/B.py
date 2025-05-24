"""
B - Can you solve this?
"""

N,M,C = map(int, input().split())
B = list(map(int, input().split()))
count = 0
for _ in range(N):
    A = list(map(int,input().split()))
    S = sum([a*b for a,b in zip(A,B)])
    if S + C > 0:
        count += 1
print(count)