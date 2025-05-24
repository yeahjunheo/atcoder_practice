"""
B - Bishop
"""

# A more mathematical approach to this would be
H,W = map(int, input().split())
moveCount = 0
oddCount = W//2 + W%2
evenCount = W//2
moveCount = (H//2) * (oddCount + evenCount)
if H%2 == 1:
    moveCount += oddCount
if H == 1 or W == 1:
    moveCount = 1
print(moveCount)

# H,W = map(int, input().split())
# if H == 1 or W == 1:
#     print(1)
#     exit()
# count = 0
# for i in range(H):
#     if W%2 == 0:
#         count += W//2
#     else:
#         if i%2 == 0:
#             count += (W+1)//2
#         else:
#             count += W//2
# print(count)