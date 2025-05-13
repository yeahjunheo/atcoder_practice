'''
There are N balls labeled with the first N uppercase letters. The balls have pairwise distinct weights.

You are allowed to ask at most Q queries. In each query, you can compare the weights of two balls (see Input/Output section for details).

Sort the balls in the ascending order of their weights.
'''

N, Q = map(int, input().split())
res  = ''
for i in range(N):
    res += chr(ord('A') + i)
