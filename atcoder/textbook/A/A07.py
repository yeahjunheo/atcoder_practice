'''
Instead of trying to make things a dictionary and filling
a data set within information, we can think of ways to
simplify the stroage of information.

In this case, we don't have to think about storing all the
number of participants for each day, but rather think of
how many participants enter or leave for attendance as the
days progress.
'''

D = int(input())
N = int(input())
A = [0]*(D+1)
for _ in range(N):
    L,R = map(int,input().split())
    A[L-1] += 1
    A[R] -= 1
res = 0
for i in range(D):
    res += A[i]
    print(res)