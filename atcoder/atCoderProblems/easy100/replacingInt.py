'''
Replacing Integers

7, 4 -> 3, 4 -> 1, 4 -> 3, 4 -> ...

2, 6 -> 4, 6 -> 2, 6 -> ...
'''

n, k = map(int, input().split())
remainder = n % k
print(min(remainder, k-remainder))