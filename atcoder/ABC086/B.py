"""
B - 1 21
"""
import math

a,b = map(int, input().split())
a = int(str(a) + str(b))
root = math.sqrt(a)
if root.is_integer():
    print("Yes")
else:
    print("No")