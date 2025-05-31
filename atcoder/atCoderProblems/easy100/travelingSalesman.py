'''
C - Traveling Salesman around Lake
'''

k,n = map(int,input().split())
A = list(map(int,input().split()))
diffA = []
for i in range(n):
    diffA.append(A[i] - A[i-1])
diffA[0] += k