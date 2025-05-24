"""
B - Break Number
"""

N = int(input())
twos = [2**i for i in range(6,-1,-1) if 2**i <= N]

print(twos[0])